# Module 0 — Python Primer

This is prerequisite/self-study material so the main course can focus on object-oriented programming.

## Minimum Python prerequisites

Learners should be comfortable with:

- variables and expressions;
- `if` / `elif` / `else`;
- `for` and `while`;
- functions and parameters;
- lists, tuples, and dictionaries;
- basic imports/modules;
- reading Python errors.

## Materials

- [Python Primer notebook](00_python_primer.ipynb)
- [Readiness check](readiness-check.md)

## Reference

OpenStax, *Introduction to Python Programming*: use the relevant introductory chapters before Module 1.

Module 0 is intentionally Python prerequisite material. It does not introduce formal OOP concepts yet.

## Readiness example

Before Module 1, you should be able to read and explain code like:

```python
students = ["Aisyah", "Budi", "Siti"]

def greet(name):
    return f"Hello, {name}"

for student in students:
    print(greet(student))
```

You should also be able to modify a list/dictionary, write a short function, use a conditional, and interpret a basic Python error message.

If this is difficult, review the primer notebook and introductory Python material before continuing to Module 1.

## Next

Continue to [Module 1 — Introduction to OOP & Thinking in Objects](../week-01/).
