# Week 12 Instructor Notes — Operator Overloading, Genericity & Modules

## Teaching goal

Week 11 distinguished object identity from value equality. Week 12 lets students define selected object semantics explicitly and then organize classes into reusable modules.

```text
object semantics
      ↓
special methods
      ↓
operator overloading
      ↓
genericity concept
      ↓
module organization
```

## Source alignment

### Inggriani Liem — Overloading

The Diktat defines overloading broadly as one name being associated with more than one meaning. Its examples include routines with the same name but different parameters and multiple constructor forms.

Do not claim that the Diktat's overloading section specifically teaches Python `__add__()`, `__eq__()`, or `__str__()`.

### OpenStax — Python operator overloading

Use **11.4 Overloading Operators** for the Python implementation with selected special methods.

### Inggriani Liem — Genericity

Use the Diktat for genericity as type parametrization, examples such as `LIST[PERSON]`, `LIST[BOOK]`, and `LIST[POINT]`, and its high-level contrast of genericity as horizontal and inheritance as vertical.

Keep this conceptual. Do not introduce `TypeVar`, `Generic[T]`, covariance, contravariance, or static type-checking theory.

### OpenStax — Modules

Use **11.5 Using Modules with Classes** for moving class definitions into modules, importing classes, and using aliases.

## Recommended 200-minute flow

| Time | Activity |
|---|---|
| 08:30–08:45 | Review Week 11 identity vs equality |
| 08:45–09:10 | Overloading concept vs overriding |
| 09:10–09:35 | `__str__()` and `__eq__()` |
| 09:35–10:00 | `__add__()` |
| 10:00–10:10 | Break |
| 10:10–10:35 | Meaningful operator semantics |
| 10:35–10:55 | Genericity concept |
| 10:55–11:20 | Modules with classes |
| 11:20–11:40 | Point / Money lab |
| 11:40–11:50 | Quiz / Week 13 bridge |

## Opening bridge from Week 11

Use:

```python
p1 = Point(1, 2)
p2 = Point(1, 2)

print(p1 is p2)
print(p1 == p2)
```

Before defining `__eq__()`, ask:

> What should equal mean for Point objects?

This naturally motivates object-defined value equality.

## `__str__()`

Ask:

> If an object is printed, what representation would be useful to a human?

Keep the goal semantic, not memorization of dunder names.

## `__eq__()`

Connect to Week 11:

```text
is
→ identity

==
→ value equality
```

Explain that `__eq__()` lets the class define the second concept.

Do not introduce hashing rules this week.

## `__add__()`

Use Point first because coordinate-wise addition is easy to reason about.

Then ask:

> Does + make sense for every class?

Use Student as a counterexample. This prevents students from treating special methods as a checklist.

## Overloading vs overriding

Write side by side:

```text
Overriding
Week 7
subclass changes inherited method behavior

Overloading
Week 12
same operation/name can have different meaning/forms
```

Students often confuse these terms.

## Genericity

Use the Diktat examples directly:

```text
LIST[BOOK]
LIST[PERSON]
LIST[POINT]
```

Ask what stays the same and what changes.

Expected:

- general list structure/operations stay conceptually the same;
- the element type is parameterized.

Then contrast this with inheritance without implementing a generic Python type.

## Modules

Start with one file containing everything. Then split:

```text
models.py
main.py
```

Explain:

> A module is primarily an organization and reuse boundary here.

Do not expand into package publishing or environment management.

## Common misconceptions

### 1. Overloading and overriding are synonyms

False.

### 2. `is` uses `__eq__()`

False. `is` concerns identity.

### 3. Every operator should be overloaded

False. Operator meaning should be clear for the domain object.

### 4. Genericity means inheritance

False. The Diktat explicitly distinguishes the two concepts.

### 5. A module must contain exactly one class

False. A module may contain one or more related definitions.

## Quiz administration

The quiz answer key is intentionally not stored in the public repository. Keep the instructor key in a private lecturer-controlled location.

## Assignment grading notes

Reward semantic choices.

For Money, same-currency addition is enough.

If students attempt cross-currency conversion, do not award bonus points; it adds unrelated complexity.

If students use `typing.Generic` or `TypeVar`, do not reward the advanced syntax. Grade the required conceptual explanation.

## What not to teach yet

Avoid:

- `__hash__()`;
- ordering methods;
- advanced numeric protocol;
- `NotImplemented` edge cases as a major topic;
- `Generic[T]` / `TypeVar`;
- packaging / PyPI / pip;
- metaprogramming.

## Closing question

End with:

> What should our object do when an operation receives invalid input or cannot satisfy its expected conditions?

That leads directly to:

**Week 13 — Exception Handling & Assertions.**