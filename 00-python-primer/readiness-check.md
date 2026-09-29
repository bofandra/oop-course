# Week 0 — Python Readiness Check

This is a **self-check**, not an OOP assessment.

You are ready for Week 1 if you can complete most tasks without needing step-by-step syntax help.

## Part A — Read the code

Explain what this code prints:

```python
students = [
    {"name": "Alya", "score": 80},
    {"name": "Budi", "score": 65},
    {"name": "Siti", "score": 90},
]

for student in students:
    if student["score"] >= 75:
        print(student["name"])
```

## Part B — Write a function

Write:

```python
def calculate_total(prices):
    ...
```

that returns the sum of all prices.

Example:

```python
calculate_total([10_000, 15_000, 5_000])
```

should return:

```text
30000
```

## Part C — Conditionals

Write:

```python
def grade(score):
    ...
```

using at least three score ranges.

## Part D — Collections

Given:

```python
student = {
    "id": "S001",
    "name": "Alya",
    "courses": ["OOP", "Database"]
}
```

Write code that prints:

1. the student's name;
2. the first course;
3. every course using a loop.

## Part E — Debugging

Find and fix the errors:

```python
def greet(name)
    return "Hello " + Name

print(greet("Alya"))
```

## Part F — Small challenge

Given:

```python
orders = [
    {"item": "Book", "price": 50_000, "quantity": 2},
    {"item": "Pen", "price": 10_000, "quantity": 3},
]
```

Calculate the total value of all orders.

## Readiness interpretation

If you can:

- read loops and conditionals;
- write a small function;
- work with lists/dictionaries;
- understand function parameters/return values;
- read a basic Python error;

you are ready to begin Week 1.

If not, revisit the Python Primer notebook and the relevant introductory OpenStax chapters before continuing.
