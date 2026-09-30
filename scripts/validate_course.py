#!/usr/bin/env python3

"""Validate the public OOP course repository using only the Python standard library."""

from __future__ import annotations

import contextlib
import csv
import io
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def required_structure(errors: list[str]) -> None:
    required = [
        "README.md",
        "CHANGELOG.md",
        "CITATION.cff",
        "ACCESSIBILITY.md",
        "LOCAL_SETUP.md",
        "COURSE_MAP.md",
        "OPEN_COURSE_GUIDE.md",
        "SELF_PACED_GUIDE.md",
        "SELF_ASSESSMENT_GUIDE.md",
        "MASTERY_CHECKS.md",
        "ASSESSMENT_ALIGNMENT.md",
        "INSTRUCTOR_GUIDE.md",
        "EXECUTION_AUDIT.md",
        "GRADING_SYSTEM.md",
        "GRADEBOOK_GUIDE.md",
        "COLAB.md",
        "REFERENCE_MAP.md",
        "CONTRIBUTING.md",
        ".github/ISSUE_TEMPLATE/content.yml",
        ".github/ISSUE_TEMPLATE/technical.yml",
        "grading_config.json",
        "templates/assessment_registry.csv",
        "templates/gradebook_scores.csv",
        "assessments/demo-participation-rubric.md",
        "scripts/calculate_grades.py",
        "templates/colab_template.ipynb",
        "00-python-primer/README.md",
        "00-python-primer/00_python_primer.ipynb",
        "00-python-primer/readiness-check.md",
        "week-08/README.md",
        "assessments/midterm/README.md",
        "assessments/midterm/midterm_exam.ipynb",
        "assessments/midterm/midterm_rubric.md",
        "week-16/README.md",
        "week-16/16_final_project_planning.ipynb",
        "week-16/final-project-checklist.md",
        "assessments/final-project/README.md",
        "assessments/final-project/final_project_rubric.md",
        "assessments/final-project/demo-viva-guide.md",
    ]

    for week in list(range(1, 8)) + list(range(9, 16)):
        folder = f"week-{week:02d}"
        required.extend(
            [
                f"{folder}/README.md",
                f"{folder}/exercises.md",
                f"{folder}/quiz.md",
                f"{folder}/assignment.md",
                f"{folder}/instructor-notes.md",
            ]
        )
        if not list((ROOT / folder).glob("*.ipynb")):
            fail(errors, f"{folder}: teaching notebook is missing")

    for rel in required:
        if not (ROOT / rel).exists():
            fail(errors, f"Missing required file: {rel}")


def validate_notebooks(errors: list[str]) -> None:
    notebooks = sorted(ROOT.rglob("*.ipynb"))

    for path in notebooks:
        rel = path.relative_to(ROOT)
        try:
            notebook = json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            fail(errors, f"{rel}: invalid notebook JSON: {exc}")
            continue

        if notebook.get("nbformat") != 4:
            fail(errors, f"{rel}: expected nbformat 4")

        cells = notebook.get("cells")
        if not isinstance(cells, list) or not cells:
            fail(errors, f"{rel}: notebook has no cells")
            continue

        code_cells = [
            cell for cell in cells
            if cell.get("cell_type") == "code"
        ]

        # Published notebooks should start clean so learners do not inherit
        # stale execution state or saved output from a prior run.
        for index, cell in enumerate(code_cells):
            execution_count = cell.get("execution_count")
            outputs = cell.get("outputs", [])
            if execution_count is not None:
                fail(
                    errors,
                    f"{rel}: code cell {index} has saved execution_count={execution_count!r}",
                )
            if outputs:
                fail(
                    errors,
                    f"{rel}: code cell {index} has {len(outputs)} saved output(s)",
                )

        # First compile every code cell.
        for index, cell in enumerate(code_cells):
            source = cell.get("source", "")
            if isinstance(source, list):
                source = "".join(source)
            try:
                compile(source, f"{rel}:cell-{index}", "exec")
            except Exception as exc:
                fail(errors, f"{rel}: cell {index} does not compile: {exc}")

        # Then execute the cells sequentially in an isolated temporary directory.
        # The notebooks are intentionally self-contained. TODO-only cells are valid no-ops.
        namespace: dict[str, object] = {"__name__": "__main__"}
        with tempfile.TemporaryDirectory() as temp_dir:
            old_cwd = Path.cwd()
            old_path = list(sys.path)
            try:
                os.chdir(temp_dir)
                sys.path.insert(0, temp_dir)
                # Avoid a module written by a previous notebook execution.
                sys.modules.pop("models", None)

                with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                    for index, cell in enumerate(code_cells):
                        source = cell.get("source", "")
                        if isinstance(source, list):
                            source = "".join(source)
                        try:
                            exec(
                                compile(source, f"{rel}:cell-{index}", "exec"),
                                namespace,
                                namespace,
                            )
                        except Exception as exc:
                            fail(
                                errors,
                                f"{rel}: runtime error in cell {index}: "
                                f"{type(exc).__name__}: {exc}",
                            )
                            break
            finally:
                os.chdir(old_cwd)
                sys.path[:] = old_path
                sys.modules.pop("models", None)


def validate_python_files(errors: list[str]) -> None:
    python_files = sorted(
        path for path in ROOT.rglob("*.py")
        if ".git" not in path.parts and path.name != "validate_course.py"
    )

    for path in python_files:
        rel = path.relative_to(ROOT)
        source = path.read_text(encoding="utf-8")
        try:
            compile(source, str(rel), "exec")
        except Exception as exc:
            fail(errors, f"{rel}: Python syntax error: {exc}")

    main_file = ROOT / "week-12" / "main.py"
    if main_file.exists():
        process = subprocess.run(
            [sys.executable, "main.py"],
            cwd=main_file.parent,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=30,
        )
        if process.returncode != 0:
            fail(
                errors,
                "week-12/main.py failed: "
                + (process.stderr.strip() or f"exit {process.returncode}"),
            )


def validate_gradebook_tool(errors: list[str]) -> None:
    script = ROOT / "scripts" / "calculate_grades.py"
    registry = ROOT / "templates" / "assessment_registry.csv"
    config = ROOT / "grading_config.json"

    try:
        with registry.open(newline="", encoding="utf-8-sig") as handle:
            assessment_ids = [
                row["assessment_id"]
                for row in csv.DictReader(handle)
                if row.get("included", "true").strip().lower() in {"true", "1", "yes"}
            ]
    except Exception as exc:
        fail(errors, f"Could not read assessment registry: {exc}")
        return

    with tempfile.TemporaryDirectory() as temp_dir:
        score_path = Path(temp_dir) / "scores.csv"
        output_path = Path(temp_dir) / "summary.csv"

        with score_path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.writer(handle)
            writer.writerow(
                [
                    "student_id",
                    "student_name",
                    "assessment_id",
                    "raw_score",
                    "status",
                    "penalty_percent",
                    "notes",
                ]
            )
            for assessment_id in assessment_ids:
                writer.writerow(
                    [
                        "TEST001",
                        "Validation Student",
                        assessment_id,
                        "80",
                        "SUBMITTED",
                        "0",
                        "",
                    ]
                )

        process = subprocess.run(
            [
                sys.executable,
                str(script),
                "--scores",
                str(score_path),
                "--registry",
                str(registry),
                "--config",
                str(config),
                "--mode",
                "final",
                "--output",
                str(output_path),
            ],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=30,
        )

        if process.returncode != 0:
            fail(
                errors,
                "gradebook calculator self-test failed: "
                + (process.stderr.strip() or f"exit {process.returncode}"),
            )
            return

        try:
            with output_path.open(newline="", encoding="utf-8") as handle:
                rows = list(csv.DictReader(handle))
        except Exception as exc:
            fail(errors, f"Could not read gradebook self-test output: {exc}")
            return

        if len(rows) != 1:
            fail(errors, "gradebook calculator self-test produced unexpected row count")
            return

        row = rows[0]
        if row.get("finalizable") != "YES":
            fail(errors, "gradebook calculator self-test did not finalize complete data")
        if row.get("final_numeric") != "80.00":
            fail(
                errors,
                "gradebook calculator self-test expected final_numeric=80.00; "
                f"found {row.get('final_numeric')!r}",
            )


def normalize_relative_link(source: Path, link: str) -> Path | None:
    link = link.strip()
    if not link or link.startswith("#"):
        return None
    if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", link):
        return None

    target = link.split("#", 1)[0].split("?", 1)[0]
    if not target:
        return None

    resolved = (source.parent / target).resolve()
    try:
        resolved.relative_to(ROOT.resolve())
    except ValueError:
        return None

    if target.endswith("/"):
        resolved = resolved / "README.md"
    return resolved


def validate_markdown_links(errors: list[str]) -> None:
    link_pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")

    for path in sorted(ROOT.rglob("*.md")):
        rel = path.relative_to(ROOT)
        text = path.read_text(encoding="utf-8")
        for match in link_pattern.finditer(text):
            raw_link = match.group(1)
            target = normalize_relative_link(path, raw_link)
            if target is not None and not target.exists():
                fail(errors, f"{rel}: broken relative link: {raw_link}")


def validate_colab_index(errors: list[str]) -> None:
    index_path = ROOT / "COLAB.md"
    if not index_path.exists():
        return

    text = index_path.read_text(encoding="utf-8")
    notebooks = sorted(
        path.relative_to(ROOT)
        for path in ROOT.rglob("*.ipynb")
        if "templates" not in path.parts
    )

    for rel in notebooks:
        expected_url = (
            "https://colab.research.google.com/github/"
            "bofandra/oop-course/blob/main/"
            + rel.as_posix()
        )
        if expected_url not in text:
            fail(errors, f"COLAB.md: missing launch link for {rel}")


def validate_module_colab_navigation(errors: list[str]) -> None:
    module_targets = {}

    primer = ROOT / "00-python-primer" / "00_python_primer.ipynb"
    if primer.exists():
        module_targets[ROOT / "00-python-primer" / "README.md"] = primer

    for week in list(range(1, 8)) + list(range(9, 17)):
        folder = ROOT / f"week-{week:02d}"
        notebooks = sorted(folder.glob("*.ipynb"))
        if notebooks:
            module_targets[folder / "README.md"] = notebooks[0]

    midterm = ROOT / "assessments" / "midterm" / "midterm_exam.ipynb"
    if midterm.exists():
        module_targets[ROOT / "week-08" / "README.md"] = midterm
        module_targets[ROOT / "assessments" / "midterm" / "README.md"] = midterm

    for readme, notebook in module_targets.items():
        if not readme.exists():
            continue
        rel = notebook.relative_to(ROOT).as_posix()
        expected_url = (
            "https://colab.research.google.com/github/"
            "bofandra/oop-course/blob/main/"
            + rel
        )
        text = readme.read_text(encoding="utf-8")
        if expected_url not in text:
            fail(
                errors,
                f"{readme.relative_to(ROOT)}: missing direct Colab launch for {rel}",
            )


def validate_reference_map(errors: list[str]) -> None:
    path = ROOT / "REFERENCE_MAP.md"
    if not path.exists():
        return

    text = path.read_text(encoding="utf-8")
    for module in range(17):
        marker = f"| {module} |"
        if marker not in text:
            fail(errors, f"REFERENCE_MAP.md: missing Module {module} mapping")


def validate_publication_navigation(errors: list[str]) -> None:
    required_links = {
        ROOT / "README.md": [
            "START_HERE.md",
            "COLAB.md",
            "COURSE_MAP.md",
            "REFERENCE_MAP.md",
            "SELF_PACED_GUIDE.md",
            "SELF_ASSESSMENT_GUIDE.md",
            "ACCESSIBILITY.md",
            "LOCAL_SETUP.md",
            "CITATION.cff",
            "CHANGELOG.md",
            "00-python-primer/readiness-check.md",
            "week-01/",
            "CONTRIBUTING.md",
        ],
        ROOT / "START_HERE.md": [
            "00-python-primer/readiness-check.md",
            "00-python-primer/",
            "week-01/",
            "COLAB.md",
            "COURSE_MAP.md",
            "REFERENCE_MAP.md",
            "SELF_PACED_GUIDE.md",
            "SELF_ASSESSMENT_GUIDE.md",
        ],
    }

    for path, links in required_links.items():
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for link in links:
            if link not in text:
                fail(errors, f"{path.name}: missing public navigation link to {link}")


def validate_local_setup_guide(errors: list[str]) -> None:
    path = ROOT / "LOCAL_SETUP.md"
    if not path.exists():
        return

    text = path.read_text(encoding="utf-8")
    required_fragments = [
        "Python 3.12",
        "python scripts/validate_course.py",
        "COURSE VALIDATION PASSED",
        "Google Colab",
    ]
    for fragment in required_fragments:
        if fragment not in text:
            fail(errors, f"LOCAL_SETUP.md: missing required reproducibility guidance: {fragment}")


def validate_publication_metadata(errors: list[str]) -> None:
    citation_path = ROOT / "CITATION.cff"
    if citation_path.exists():
        text = citation_path.read_text(encoding="utf-8")
        required_fragments = [
            "cff-version: 1.2.0",
            'title: "Object Oriented Programming — Open Course"',
            "authors:",
            'family-names: "Muhammad"',
            'given-names: "Bofandra"',
            'repository-code: "https://github.com/bofandra/oop-course"',
        ]
        for fragment in required_fragments:
            if fragment not in text:
                fail(errors, f"CITATION.cff: missing required metadata fragment: {fragment}")

    accessibility_path = ROOT / "ACCESSIBILITY.md"
    if accessibility_path.exists():
        text = accessibility_path.read_text(encoding="utf-8")
        for heading in [
            "# Accessibility Guide",
            "## Learner guidance",
            "## Content authoring rules",
            "## Assessment accessibility",
        ]:
            if heading not in text:
                fail(errors, f"ACCESSIBILITY.md: missing required section: {heading}")


def validate_open_course_neutrality(errors: list[str]) -> None:
    forbidden_patterns = {
        "institution affiliation": re.compile(r"TANRI\s+ABENG", re.IGNORECASE),
        "institution abbreviation": re.compile(r"\bTAU\b"),
        "semester wording": re.compile(r"\bsemester\b", re.IGNORECASE),
        "fixed Saturday schedule": re.compile(r"\bSaturday\b", re.IGNORECASE),
        "old academic-year label": re.compile(r"2026\s*/\s*2027"),
        "old fixed class time": re.compile(r"08:30\s*[–-]\s*11:50"),
        "old UTS wording": re.compile(r"\bUTS\b", re.IGNORECASE),
        "old UAS wording": re.compile(r"\bUAS\b", re.IGNORECASE),
    }

    text_suffixes = {".md", ".py", ".json", ".csv", ".yml", ".yaml", ".ipynb"}
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path.suffix not in text_suffixes:
            continue
        if ".git" in path.parts:
            continue
        if path == ROOT / "scripts" / "validate_course.py":
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for label, pattern in forbidden_patterns.items():
            if pattern.search(text):
                fail(
                    errors,
                    f"{path.relative_to(ROOT)}: open-course neutrality check found {label}",
                )

    retired_paths = [
        ROOT / "TEACHING_CALENDAR.md",
        ROOT / "RELEASE_PLAN.md",
        ROOT / "LECTURER_OPERATIONAL_KIT.md",
        ROOT / "TEACHING_READINESS_AUDIT.md",
    ]
    for path in retired_paths:
        if path.exists():
            fail(
                errors,
                f"{path.relative_to(ROOT)}: schedule/cohort-specific document should not exist",
            )



def validate_assessment_structure(errors: list[str]) -> None:
    assignment_paths = sorted(ROOT.glob("week-*/assignment.md"))

    for path in assignment_paths:
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(ROOT)

        if re.search(r"\*\*Teaching (?:schedule|workload) note:\*\*", text, re.IGNORECASE):
            fail(
                errors,
                f"{rel}: facilitator-only teaching schedule/workload note belongs in instructor-notes.md",
            )

        rubric_lines = [
            line for line in text.splitlines()
            if line.strip().startswith("|")
            and re.search(r"\|\s*\d+(?:\.\d+)?%\s*\|\s*$", line)
            and "**Total**" not in line
        ]

        if not rubric_lines:
            fail(errors, f"{rel}: assignment rubric with percentage weights is missing")
            continue

        weights = []
        for line in rubric_lines:
            match = re.search(r"\|\s*(\d+(?:\.\d+)?)%\s*\|\s*$", line)
            if match:
                weights.append(float(match.group(1)))

        if abs(sum(weights) - 100.0) > 0.001:
            fail(
                errors,
                f"{rel}: rubric weights sum to {sum(weights):g}%, expected 100%",
            )

    for path in sorted(ROOT.glob("week-*/quiz.md")):
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(ROOT)
        if "## Part A" not in text or "## Part B" not in text:
            fail(errors, f"{rel}: quiz should contain both objective and explanation sections")

    registry_path = ROOT / "templates" / "assessment_registry.csv"
    with registry_path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        fields = set(reader.fieldnames or [])
        if "module" not in fields:
            fail(errors, "templates/assessment_registry.csv: canonical registry should use a module column")
        for row in reader:
            title = row.get("title", "")
            if re.search(r"\\bWeek\\s+\\d+\\b", title, re.IGNORECASE):
                fail(
                    errors,
                    "templates/assessment_registry.csv: assessment titles should use Module, not Week",
                )
                break

def validate_public_assessment_safety(errors: list[str]) -> None:
    for path in sorted(ROOT.glob("week-*/instructor-notes.md")):
        text = path.read_text(encoding="utf-8").lower()
        if "## quiz answer key" in text:
            fail(errors, f"{path.relative_to(ROOT)}: public quiz answer key detected")

    private_only = [
        ROOT / "assessments" / "midterm" / "answer-key.md",
        ROOT / "assessments" / "midterm" / "instructor-notes.md",
        ROOT / "assessments" / "final-project" / "answer-key.md",
        ROOT / "assessments" / "final-project" / "instructor-notes.md",
    ]
    for path in private_only:
        if path.exists():
            fail(errors, f"{path.relative_to(ROOT)}: public assessment answer key detected")


def main() -> int:
    errors: list[str] = []

    required_structure(errors)
    validate_notebooks(errors)
    validate_python_files(errors)
    validate_gradebook_tool(errors)
    validate_markdown_links(errors)
    validate_colab_index(errors)
    validate_module_colab_navigation(errors)
    validate_reference_map(errors)
    validate_publication_navigation(errors)
    validate_local_setup_guide(errors)
    validate_publication_metadata(errors)
    validate_assessment_structure(errors)
    validate_public_assessment_safety(errors)
    validate_open_course_neutrality(errors)

    if errors:
        print("COURSE VALIDATION FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    notebook_count = len(list(ROOT.rglob("*.ipynb")))
    markdown_count = len(list(ROOT.rglob("*.md")))
    python_count = len(
        [p for p in ROOT.rglob("*.py") if ".git" not in p.parts]
    )

    print("COURSE VALIDATION PASSED")
    print(f"- notebooks checked: {notebook_count}")
    print(f"- markdown files checked: {markdown_count}")
    print(f"- Python files checked: {python_count}")
    print("- required Module 0–16 structure: OK")
    print("- notebook compilation/execution: OK")
    print("- clean notebook publication state: OK")
    print("- relative Markdown links: OK")
    print("- Colab launch coverage: OK")
    print("- direct module Colab navigation: OK")
    print("- reference-map coverage: OK")
    print("- publication navigation: OK")
    print("- local reproducibility guide: OK")
    print("- citation/accessibility metadata: OK")
    print("- assignment rubric / quiz structure: OK")
    print("- learner-facing assessment neutrality: OK")
    print("- public assessment-key guard: OK")
    print("- gradebook calculator self-test: OK")
    print("- open-course neutrality: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
