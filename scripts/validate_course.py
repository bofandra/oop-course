#!/usr/bin/env python3

"""Validate the public OOP course repository using only the Python standard library."""

from __future__ import annotations

import contextlib
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
        "COURSE_MAP.md",
        "TEACHING_READINESS_AUDIT.md",
        "LECTURER_OPERATIONAL_KIT.md",
        "TEACHING_CALENDAR.md",
        "RELEASE_PLAN.md",
        "EXECUTION_AUDIT.md",
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
    validate_markdown_links(errors)
    validate_public_assessment_safety(errors)

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
    print("- required Week 0–16 structure: OK")
    print("- notebook compilation/execution: OK")
    print("- relative Markdown links: OK")
    print("- public assessment-key guard: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
