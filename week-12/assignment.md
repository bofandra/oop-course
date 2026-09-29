# Week 12 Assignment — Domain Value Object in Modules

## Objective

Use selected Python operator-overloading methods and organize the class into a reusable module.

## Task — Money

Create:

```text
money.py
main.py
```

## Money

State:

- `amount`
- `currency`

Implement:

```python
__str__()
__eq__()
__add__()
```

`__str__()` should return a useful readable representation.

`__eq__()` should consider two Money objects equal when both amount and currency are equal.

`__add__()` should return a **new Money object** representing the total.

For this week's assignment, only demonstrate addition between Money objects using the same currency. Do not build exchange-rate conversion.

## Required demonstration

Create at least four Money objects and demonstrate:

1. `print(money)`;
2. identity vs equality;
3. two equal-value but independent objects;
4. Money addition;
5. the result being a new Money object;
6. import from another module.

## Genericity explanation

Use the Diktat-style examples `LIST[BOOK]`, `LIST[PERSON]`, and `LIST[POINT]` to explain type parametrization conceptually.

No `typing.Generic` or `TypeVar` implementation is required.

## Written explanation

Answer:

1. What does `__str__()` add to the class?
2. What is the difference between `is` and `==` in your demonstration?
3. What does `__add__()` mean for Money?
4. Why should Money addition return a new object rather than secretly mutate one operand?
5. How is overloading different from overriding?
6. What is genericity/type parametrization?
7. How is genericity different from inheritance?
8. Why separate `Money` and runner code into different modules?

## Rubric

| Criterion | Weight |
|---|---:|
| Correct `__str__()` | 10% |
| Correct `__eq__()` | 15% |
| Correct `__add__()` | 20% |
| Meaningful operator semantics | 15% |
| Module organization/import | 15% |
| Genericity explanation | 10% |
| Written reasoning | 15% |
| **Total** | **100%** |

## Scope

Do not implement currency conversion, advanced error architecture, `typing.Generic`, `TypeVar`, packages, `pip`, or metaprogramming.

Exception handling is the topic of Week 13.