#!/usr/bin/env python3

"""Calculate OOP course progress/final grades from a long-form CSV ledger."""

from __future__ import annotations

import argparse
import csv
import json
from collections import defaultdict
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_REGISTRY = ROOT / "templates" / "assessment_registry.csv"
DEFAULT_CONFIG = ROOT / "grading_config.json"

VALID_STATUSES = {"SUBMITTED", "LATE", "MISSING", "EXC", "PENDING"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Calculate OOP course grades.")
    parser.add_argument("--scores", required=True, help="Path to long-form score CSV.")
    parser.add_argument(
        "--registry",
        default=str(DEFAULT_REGISTRY),
        help="Assessment registry CSV.",
    )
    parser.add_argument(
        "--config",
        default=str(DEFAULT_CONFIG),
        help="Grading configuration JSON.",
    )
    parser.add_argument(
        "--mode",
        choices=("progress", "final"),
        default="progress",
        help="Progress excludes unresolved future work; final requires all included work resolved.",
    )
    parser.add_argument("--output", help="Optional output CSV path. Defaults to stdout.")
    return parser.parse_args()


def load_config(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def load_registry(path: Path) -> dict[str, dict]:
    registry: dict[str, dict] = {}
    with path.open(newline="", encoding="utf-8-sig") as handle:
        for row in csv.DictReader(handle):
            assessment_id = row["assessment_id"].strip()
            if not assessment_id:
                continue
            included = row.get("included", "true").strip().lower() in {"true", "1", "yes"}
            registry[assessment_id] = {
                "assessment_id": assessment_id,
                "component": row["component"].strip(),
                "week": row.get("week", "").strip(),
                "title": row.get("title", "").strip(),
                "included": included,
                "max_score": float(row.get("max_score", "100") or 100),
            }
    return registry


def parse_float(value: str, field: str, context: str) -> float:
    try:
        return float(value)
    except ValueError as exc:
        raise ValueError(f"{context}: invalid {field}={value!r}") from exc


def load_scores(path: Path, registry: dict[str, dict]) -> tuple[dict, list[str]]:
    students: dict[str, dict] = {}
    warnings: list[str] = []
    seen: set[tuple[str, str]] = set()

    with path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        required = {
            "student_id",
            "student_name",
            "assessment_id",
            "raw_score",
            "status",
            "penalty_percent",
            "notes",
        }
        missing_cols = required - set(reader.fieldnames or [])
        if missing_cols:
            raise ValueError(
                "Score CSV is missing columns: " + ", ".join(sorted(missing_cols))
            )

        for line_no, row in enumerate(reader, start=2):
            student_id = row["student_id"].strip()
            student_name = row["student_name"].strip()
            assessment_id = row["assessment_id"].strip()
            status = row["status"].strip().upper()

            if not student_id and not student_name and not assessment_id:
                continue
            if not student_id:
                raise ValueError(f"line {line_no}: student_id is required")
            if not student_name:
                raise ValueError(f"line {line_no}: student_name is required")
            if assessment_id not in registry:
                raise ValueError(
                    f"line {line_no}: unknown assessment_id {assessment_id!r}"
                )
            if status not in VALID_STATUSES:
                raise ValueError(
                    f"line {line_no}: invalid status {status!r}; "
                    f"expected one of {sorted(VALID_STATUSES)}"
                )

            key = (student_id, assessment_id)
            if key in seen:
                raise ValueError(
                    f"line {line_no}: duplicate score row for "
                    f"{student_id}/{assessment_id}"
                )
            seen.add(key)

            raw_text = row["raw_score"].strip()
            penalty_text = row["penalty_percent"].strip() or "0"

            if status in {"SUBMITTED", "LATE"}:
                if not raw_text:
                    raise ValueError(
                        f"line {line_no}: {status} requires raw_score"
                    )
                raw_score = parse_float(
                    raw_text, "raw_score", f"line {line_no}"
                )
                max_score = registry[assessment_id]["max_score"]
                if not 0 <= raw_score <= max_score:
                    raise ValueError(
                        f"line {line_no}: raw_score must be between 0 and {max_score}"
                    )
                penalty = parse_float(
                    penalty_text, "penalty_percent", f"line {line_no}"
                )
                if not 0 <= penalty <= 100:
                    raise ValueError(
                        f"line {line_no}: penalty_percent must be 0–100"
                    )
                normalized = raw_score / max_score * 100
                adjusted = normalized * (1 - penalty / 100)
            elif status == "MISSING":
                raw_score = 0.0
                penalty = 0.0
                adjusted = 0.0
            else:
                raw_score = None
                penalty = 0.0
                adjusted = None

            student = students.setdefault(
                student_id,
                {
                    "student_id": student_id,
                    "student_name": student_name,
                    "scores": {},
                },
            )
            if student["student_name"] != student_name:
                warnings.append(
                    f"{student_id}: inconsistent student_name values; "
                    f"using {student['student_name']!r}"
                )

            student["scores"][assessment_id] = {
                "status": status,
                "raw_score": raw_score,
                "penalty_percent": penalty,
                "adjusted_score": adjusted,
                "notes": row.get("notes", "").strip(),
            }

    return students, warnings


def letter_grade(score: float, scale: list[dict]) -> str:
    ordered = sorted(scale, key=lambda item: float(item["minimum"]), reverse=True)
    for item in ordered:
        if score >= float(item["minimum"]):
            return str(item["grade"])
    return ""


def component_expected(
    registry: dict[str, dict], component: str
) -> list[str]:
    return [
        assessment_id
        for assessment_id, item in registry.items()
        if item["included"] and item["component"] == component
    ]


def evaluate_student(
    student: dict,
    registry: dict[str, dict],
    config: dict,
    mode: str,
) -> dict:
    weights = config["component_weights"]
    component_scores: dict[str, float | None] = {}
    completion: dict[str, str] = {}
    unresolved: list[str] = []

    for component in weights:
        expected = component_expected(registry, component)
        counted: list[float] = []
        resolved_count = 0
        denominator_count = 0

        for assessment_id in expected:
            record = student["scores"].get(assessment_id)

            if record is None:
                if mode == "final":
                    unresolved.append(assessment_id)
                continue

            status = record["status"]

            if status == "EXC":
                resolved_count += 1
                continue

            if status == "PENDING":
                if mode == "final":
                    unresolved.append(assessment_id)
                continue

            denominator_count += 1
            resolved_count += 1
            counted.append(float(record["adjusted_score"]))

        if mode == "final":
            effective_expected = sum(
                1
                for assessment_id in expected
                if student["scores"].get(assessment_id, {}).get("status") != "EXC"
            )
            if effective_expected == 0:
                component_scores[component] = None
                completion[component] = "0/0"
            elif len(counted) == effective_expected:
                component_scores[component] = sum(counted) / len(counted)
                completion[component] = f"{len(counted)}/{effective_expected}"
            else:
                component_scores[component] = None
                completion[component] = f"{len(counted)}/{effective_expected}"
        else:
            component_scores[component] = (
                sum(counted) / len(counted) if counted else None
            )
            non_exc_records = [
                assessment_id
                for assessment_id in expected
                if student["scores"].get(assessment_id, {}).get("status") != "EXC"
            ]
            completion[component] = f"{len(counted)}/{len(non_exc_records)}"

    if mode == "final":
        finalizable = not unresolved and all(
            component_scores.get(component) is not None for component in weights
        )
        if finalizable:
            final_numeric = sum(
                float(component_scores[component]) * float(weight)
                for component, weight in weights.items()
            )
            completed_weight = 1.0
            progress_percent = final_numeric
            grade = letter_grade(final_numeric, config["letter_scale"])
        else:
            final_numeric = None
            completed_weight = sum(
                float(weight)
                for component, weight in weights.items()
                if component_scores.get(component) is not None
            )
            weighted_points = sum(
                float(component_scores[component]) * float(weight)
                for component, weight in weights.items()
                if component_scores.get(component) is not None
            )
            progress_percent = (
                weighted_points / completed_weight if completed_weight else None
            )
            grade = ""
    else:
        finalizable = False
        completed_weight = sum(
            float(weight)
            for component, weight in weights.items()
            if component_scores.get(component) is not None
        )
        weighted_points = sum(
            float(component_scores[component]) * float(weight)
            for component, weight in weights.items()
            if component_scores.get(component) is not None
        )
        progress_percent = (
            weighted_points / completed_weight if completed_weight else None
        )
        final_numeric = None
        grade = ""

    return {
        "student_id": student["student_id"],
        "student_name": student["student_name"],
        "component_scores": component_scores,
        "completion": completion,
        "completed_weight": completed_weight,
        "progress_percent": progress_percent,
        "finalizable": finalizable,
        "final_numeric": final_numeric,
        "letter_grade": grade,
        "unresolved": sorted(set(unresolved)),
    }


def format_num(value: float | None) -> str:
    return "" if value is None else f"{value:.2f}"


def write_summary(
    rows: list[dict],
    weights: dict,
    output_path: str | None,
    mode: str,
) -> None:
    fieldnames = ["student_id", "student_name"]
    for component in weights:
        fieldnames.extend([f"{component}_score", f"{component}_completion"])
    fieldnames.extend(
        [
            "completed_weight_percent",
            "progress_percent",
            "finalizable",
            "final_numeric",
            "letter_grade",
            "unresolved_assessments",
        ]
    )

    handle = (
        Path(output_path).open("w", newline="", encoding="utf-8")
        if output_path
        else sys.stdout
    )
    try:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for item in rows:
            row = {
                "student_id": item["student_id"],
                "student_name": item["student_name"],
            }
            for component in weights:
                row[f"{component}_score"] = format_num(
                    item["component_scores"][component]
                )
                row[f"{component}_completion"] = item["completion"][component]
            row.update(
                {
                    "completed_weight_percent": f"{item['completed_weight'] * 100:.2f}",
                    "progress_percent": format_num(item["progress_percent"]),
                    "finalizable": "YES" if item["finalizable"] else "NO",
                    "final_numeric": format_num(item["final_numeric"]),
                    "letter_grade": item["letter_grade"],
                    "unresolved_assessments": ";".join(item["unresolved"]),
                }
            )
            writer.writerow(row)
    finally:
        if output_path:
            handle.close()


def main() -> int:
    args = parse_args()

    config = load_config(Path(args.config))
    registry = load_registry(Path(args.registry))

    configured_components = set(config["component_weights"])
    registry_components = {
        item["component"] for item in registry.values() if item["included"]
    }
    unknown_components = registry_components - configured_components
    if unknown_components:
        raise ValueError(
            "Registry contains components missing from grading config: "
            + ", ".join(sorted(unknown_components))
        )

    total_weight = sum(float(value) for value in config["component_weights"].values())
    if abs(total_weight - 1.0) > 1e-9:
        raise ValueError(
            f"Component weights must sum to 1.0; found {total_weight}"
        )

    students, warnings = load_scores(Path(args.scores), registry)
    for warning in warnings:
        print(f"WARNING: {warning}", file=sys.stderr)

    rows = [
        evaluate_student(student, registry, config, args.mode)
        for _, student in sorted(students.items())
    ]
    write_summary(rows, config["component_weights"], args.output, args.mode)

    if args.mode == "final":
        not_finalizable = [row for row in rows if not row["finalizable"]]
        if not_finalizable:
            print(
                f"WARNING: {len(not_finalizable)} student(s) are NOT FINALIZABLE.",
                file=sys.stderr,
            )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
