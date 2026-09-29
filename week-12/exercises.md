# Week 12 Exercises — Operator Overloading, Genericity & Modules

## Exercise 1 — Readable Objects

Create a `Book` class with `title` and `author`.

Implement `__str__()` so `print(book)` produces a useful human-readable representation.

Explain why this is better than relying on the default object representation.

---

## Exercise 2 — Identity vs Equality Revisited

Create:

```python
p1 = Point(2, 3)
p2 = Point(2, 3)
```

Implement `__eq__()`.

Then explain:

```python
p1 is p2
p1 == p2
```

using concepts from Week 11.

---

## Exercise 3 — Point Addition

Implement:

```python
p3 = p1 + p2
```

using `__add__()`.

If `p1 = (2, 3)` and `p2 = (4, 5)`, the result should represent `(6, 8)`.

Explain what method call Python conceptually maps `p1 + p2` to.

---

## Exercise 4 — Meaningful or Arbitrary?

For each pair, decide whether defining `+` is likely to have a clear meaning:

1. Point + Point
2. Money + Money
3. Student + Student
4. Vector + Vector
5. Order + Order

There may be context-dependent answers. Explain your assumptions.

---

## Exercise 5 — Overriding vs Overloading

Compare `overriding` and `overloading` by explaining:

- definition;
- whether inheritance is required;
- one example from this course.

Do not confuse Week 7 method overriding with Week 12 operator overloading.

---

## Exercise 6 — Genericity Concept

The Diktat uses examples such as:

```text
LIST[BOOK]
LIST[PERSON]
LIST[POINT]
```

Explain:

1. What is the general/generic structure?
2. What is the type parameter?
3. What changes between the examples?
4. How is this concept different from inheritance?

No Python `TypeVar` implementation is required.

---

## Exercise 7 — Split Code into Modules

Create:

```text
models.py
main.py
```

Place `Point` in `models.py`.

Import it in `main.py`:

```python
from models import Point
```

Create objects and demonstrate `__str__()`, `__eq__()`, and `__add__()`.

---

## Challenge — Money

Create a simple `Money` class with `amount`, `currency`, `__str__()`, `__eq__()`, and `__add__()`.

For this exercise, only add objects with the same currency.

Explain why `Money(100_000, "IDR") + Money(50_000, "IDR")` has a reasonable domain meaning.