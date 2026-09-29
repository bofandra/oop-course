# Week 2 Assignment — Build a Small Object Model

## Objective

Demonstrate that one class definition can create multiple objects with independent instance state and shared class-level information.

## Task

Implement a small **Book Catalog** model.

Create a `Book` class with:

### Instance attributes

- `isbn`
- `title`
- `author`
- `year`

### Class attribute

- `publisher_group`

### Method

Add a simple:

```python
display_info()
```

that prints the current state of one book.

Do not implement borrowing, validation, availability rules, inheritance, or encapsulation yet.

## Required objects

Create at least **four Book instances** with different state.

Your program must demonstrate:

1. one class definition;
2. multiple instances;
3. `__init__()`;
4. `self`;
5. instance attributes;
6. a class attribute;
7. a simple instance method that displays state.

## Written explanation

Under your code, answer:

1. Which attributes belong to individual Book objects?
2. Which attribute belongs to the class?
3. What does `self` refer to when `book_3.display_info()` runs?
4. Why does changing the title of `book_1` not automatically change the title of `book_2`?
5. How many times is the `Book` class defined, and how many Book objects did you create?

## Suggested submission

Submit either:

- a Colab notebook; or
- one Python file plus a short Markdown/text explanation.

## Rubric

| Criterion | Weight |
|---|---:|
| Correct class definition | 15% |
| Correct `__init__()` and `self` usage | 20% |
| Correct instance attributes | 20% |
| Correct class attribute | 15% |
| Multiple independent instances | 15% |
| Explanation / reasoning | 15% |
| **Total** | **100%** |

## Reference focus

- Inggriani Liem — class as static definition, object instantiation, attributes as state, constructor/object creation.
- OpenStax — 11.2 Classes and instances; opening of 11.3 for instance methods.
