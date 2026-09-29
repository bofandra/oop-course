# Week 12 — Operator Overloading, Genericity & Organizing Classes into Modules

## Learning outcomes

By the end of this session, students should be able to:

1. distinguish **overloading** from **overriding**;
2. explain operator overloading as giving familiar operators meaningful behavior for user-defined objects;
3. implement selected Python special methods: `__str__()`, `__eq__()`, and `__add__()`;
4. choose operator behavior that matches the meaning of the modeled object;
5. explain **genericity** conceptually as type parametrization;
6. distinguish genericity from inheritance at a high level;
7. organize related classes into a Python module;
8. import and use classes from another module.

## Source alignment

Inggriani Liem defines **overloading** broadly as the ability for one name to be associated with more than one meaning in a program. The Diktat gives language examples such as routines with the same name but different parameters and multiple constructor forms.

Python **operator overloading** in this week is the implementation-facing topic from OpenStax 11.4. We use selected special methods to define what operators mean for our own objects.

Inggriani Liem also discusses **genericity** as an important OOP concept and contrasts it with inheritance:

```text
genericity
→ horizontal / type parametrization

inheritance
→ vertical / descendant inherits ancestor features
```

The Diktat illustrates genericity with examples such as:

```text
LINKED_LIST[BOOK]
SET[BOOK]
LIST[PERSON]
LIST[POINT]
```

This course keeps genericity **conceptual**. We do not introduce advanced Python `typing.Generic` or `TypeVar` machinery.

Organizing classes into Python modules is based on OpenStax 11.5.

## From Week 11 to Week 12

Week 11 asked:

> What object does a variable refer to at runtime?

Week 12 asks:

> How can our objects participate naturally in Python expressions, and how do we organize growing class definitions into modules?

## 1. A readable object representation

Without a custom string representation:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

point = Point(2, 3)
print(point)
```

The default output is usually not very meaningful to a user.

Define:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"
```

Now:

```python
print(Point(2, 3))
```

can display:

```text
(2, 3)
```

## 2. Equality with __eq__()

From Week 11:

```text
is
→ same object identity

==
→ value equality according to the object's equality behavior
```

We can define value equality:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return (
            self.x == other.x
            and self.y == other.y
        )
```

Then two different objects can be equal in value:

```python
p1 = Point(2, 3)
p2 = Point(2, 3)

print(p1 is p2)
print(p1 == p2)
```

## 3. Addition with __add__()

For points/vectors, addition can have a natural meaning:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(
            self.x + other.x,
            self.y + other.y
        )
```

Usage:

```python
p1 = Point(2, 3)
p2 = Point(4, 5)

p3 = p1 + p2
```

Conceptually:

```text
p1 + p2
   ↓
p1.__add__(p2)
```

The operator should reflect a meaningful domain operation.

## 4. Do not overload operators arbitrarily

Possible does not mean good design.

For example:

> Should adding two Student objects produce a third Student?

Usually not.

Ask:

> Does this operator have a clear and unsurprising meaning for the object?

Good candidates include:

- Point + Point;
- Vector + Vector;
- Money + Money under a simple same-currency assumption.

## 5. Overriding vs overloading

Keep the distinction clear:

```text
Overriding
→ subclass replaces inherited behavior

Overloading
→ same name/operator can represent different behavior/forms
```

Week 7 focused on overriding.

Week 12 focuses on selected operator overloading in Python.

## 6. Genericity concept

Genericity is about defining a structure or concept that can be parameterized by a type.

From the Diktat's style of examples:

```text
LIST[PERSON]
LIST[BOOK]
LIST[POINT]
```

The general LIST idea remains the same, while the element type changes.

Conceptually:

```text
Generic structure
      +
type parameter
      ↓
specialized use
```

## 7. Genericity vs inheritance

A useful high-level contrast from the Diktat:

```text
Genericity
horizontal variation
same generic structure, different type parameter

Inheritance
vertical specialization
subclass inherits/generalizes from ancestor
```

Do not treat one as a replacement for the other.

## 8. Organizing classes into modules

As the course grows, putting every class into one notebook or file becomes difficult.

Create:

```text
models.py
main.py
```

In `models.py`:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Point(
            self.x + other.x,
            self.y + other.y
        )
```

In `main.py`:

```python
from models import Point

p1 = Point(2, 3)
p2 = Point(4, 5)

print(p1 + p2)
```

## 9. Import aliases

Python also allows:

```python
import models as m

p = m.Point(2, 3)
```

For this course, understand the basic purpose:

> Modules help organize related code and make class definitions reusable across files.

Do not turn Week 12 into package management or deployment.

## Main exercise — Point

Implement a `Point` class with:

- `x`;
- `y`;
- `__str__()`;
- `__eq__()`;
- `__add__()`.

Demonstrate:

```python
p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = Point(1, 2)

print(p1)
print(p1 == p3)
print(p1 is p3)
print(p1 + p2)
```

Explain every result.

## Module exercise

Move `Point` into `models.py`.

Import it from `main.py` and repeat the demonstration.

## Challenge — Money

Create a simple `Money` class with:

- `amount`;
- `currency`;
- `__str__()`;
- `__eq__()`;
- `__add__()`.

For this week's simple model, only demonstrate addition between Money objects with the same currency.

Do not build currency conversion or exception architecture.

## Reflection

Answer:

> Why should operator overloading follow the meaning of the modeled object rather than merely demonstrate clever Python syntax?

## Reading

### Inggriani Liem

Focus on:

- Overloading;
- Genericity;
- genericity as type parametrization;
- genericity contrasted with inheritance.

### OpenStax

Read:

- **11.4 Overloading Operators**
- **11.5 Using Modules with Classes**

## Week 12 package

- [Colab notebook](12_operator_overloading_genericity_modules.ipynb)
- [Exercises](exercises.md)
- [Quiz](quiz.md)
- [Assignment](assignment.md)
- [Instructor notes](instructor-notes.md)
- [Example module](models.py)
- [Example runner](main.py)

## Next week

Week 12 gives our classes richer language-level behavior and organization.

Week 13 asks:

> What should happen when an operation cannot satisfy its expected conditions?

That leads to:

**Week 13 — Exception Handling & Assertions.**
