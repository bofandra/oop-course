# Execution Audit

Audit status: **validated against the current repository state**

## Scope

The audit checks the public course repository end-to-end:

- Module 0–16 required structure;
- all Jupyter notebooks;
- Python example files;
- notebook code-cell syntax;
- sequential execution of notebook code cells in isolated temporary directories;
- Module 12 multi-file module example;
- relative Markdown links;
- accidental publication of module quiz answer keys.

## Result

At the time of this audit:

```text
Required course structure    PASS
Notebook JSON / nbformat     PASS
Notebook code compilation    PASS
Notebook sequential runtime  PASS
Module 12 models.py/main.py    PASS
Relative Markdown links      PASS
Public quiz-key guard        PASS
```

No blocking syntax or runtime error was found in the executable teaching examples.

## Intentional teaching examples

Some cells deliberately demonstrate an invalid or weak design before the corrected design is introduced.

Examples include:

- Module 4: direct mutation can create invalid BankAccount state;
- Module 9: a concrete Shape returning a meaningless default area is shown before ABC;
- Module 13: an unprotected withdrawal demonstrates how invalid negative balance can occur;
- Module 15: a mode-based branch is shown before the Strategy-style refactor.

These cells are pedagogical demonstrations, not execution defects.

## Student TODO cells

TODO cells are intentionally incomplete student work areas. They are still syntax-checked but are valid no-op/comment cells until students implement them.

## Automated validation

The repository contains:

```text
scripts/validate_course.py
.github/workflows/course-validation.yml
```

The validator uses only the Python standard library.

It runs on:

- pushes to `main`;
- pull requests;
- manual workflow dispatch.

This turns the one-time execution audit into a regression check for future course edits.

## What this audit does not prove

A passing execution audit does not mean every possible student solution is correct, nor does it replace instructional review.

It verifies that the published course examples and repository structure are mechanically healthy and that the currently completed example cells execute successfully in sequence.
