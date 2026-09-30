# Local Setup and Reproducibility

Google Colab is the recommended zero-setup environment for learners. Local setup is optional and is mainly useful for contributors, instructors, or learners who prefer their own editor.

## Reference environment

The automated repository validation currently runs with:

```text
Python 3.12
Ubuntu GitHub Actions runner
```

Python 3.12 is therefore the reference local version for reproducing the repository checks.

## Clone the repository

```bash
git clone https://github.com/bofandra/oop-course.git
cd oop-course
```

## Check Python

```bash
python --version
```

If your system uses `python3` instead:

```bash
python3 --version
```

## Optional virtual environment

The course examples themselves are intentionally lightweight and the repository validator uses only the Python standard library.

You may still create an isolated environment:

```bash
python -m venv .venv
```

Activate it using the normal command for your operating system.

A virtual environment is optional for the published course because there is no required third-party package installation for the automated course checks.

## Run the repository validation

From the repository root:

```bash
python scripts/validate_course.py
```

A healthy repository prints:

```text
COURSE VALIDATION PASSED
```

The validator checks, among other things:

- required course structure;
- notebook JSON and Python code syntax;
- sequential execution of teaching notebook code cells;
- Python example files;
- relative Markdown links;
- Colab navigation;
- assessment structure;
- citation/accessibility publication assets;
- gradebook calculator self-test;
- open-course neutrality.

## Run selected Python examples

Module 12 contains a multi-file example that can be run directly:

```bash
python week-12/main.py
```

Other executable examples are primarily provided inside the module notebooks.

## Working with notebooks locally

Local Jupyter tooling is **not required** by the course.

If you already use JupyterLab, Jupyter Notebook, VS Code, or another notebook-capable editor, you may open the `.ipynb` files locally. The repository does not require a particular notebook application.

For the lowest-friction learner experience, use [Google Colab](COLAB.md).

## No hidden setup step

Course notebooks are designed to execute from top to bottom without relying on state from another notebook.

The validator executes each notebook in an isolated temporary directory. This helps detect examples that accidentally depend on local files or prior notebook state.

## Generated and local-only files

The repository already ignores common local artifacts such as:

```text
.venv/
venv/
__pycache__/
.ipynb_checkpoints/
.env
.DS_Store
```

Private learner gradebooks and generated grade summaries should also remain outside version control.

## Before contributing

Run:

```bash
python scripts/validate_course.py
```

Then review [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.
