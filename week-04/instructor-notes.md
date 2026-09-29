# Week 4 Instructor Notes — Encapsulation & Abstraction

## Teaching goal

Week 3 deliberately exposed a weakness:

```python
book.borrow()
book.borrow()
```

or:

```python
appointment.status = "banana"
```

Week 4 should answer:

> How can an object expose useful behavior while keeping its state meaningful?

The key transition is:

```text
State + Behavior
      ↓
Encapsulation
      ↓
Controlled public interface
      ↓
Abstraction
```

## Source alignment

### Inggriani Liem

Use the Diktat points that:

- abstraction and encapsulation are characteristics of OO systems;
- access/visibility of features is part of class design;
- public/private visibility is discussed as a design concern;
- information hiding is relevant to encapsulation;
- a class invariant is a condition used to ensure instances remain consistent with the class definition.

Do not import language-specific access rules from C++/Java into Python as if they behaved identically.

### OpenStax

Use **11.1 Object-Oriented Programming Basics**.

OpenStax explicitly defines:

- encapsulation as grouping data and procedures and restricting direct modification;
- abstraction as hiding inner workings from users/units that do not need those details.

Review **11.3 Instance Methods** only for methods that access/modify instance state.

## Important Python distinction

Python does not provide the same strict feature visibility model described by languages with enforced `private` access.

For this course:

```python
self._balance
```

means:

> intended for internal use

not:

> impossible to access from outside.

This should be stated explicitly.

The `@property` examples are a practical Python bridge used in this course; do not imply that the Diktat itself teaches Python properties.

## Recommended 200-minute flow

| Time | Activity |
|---|---|
| 08:30–08:45 | Review Week 3 deliberate flaw |
| 08:45–09:10 | Encapsulation concept |
| 09:10–09:30 | Public interface vs internal state |
| 09:30–09:50 | Python underscore convention |
| 09:50–10:00 | Abstraction |
| 10:00–10:10 | Break |
| 10:10–10:30 | Read-only `@property` |
| 10:30–10:50 | Invariant concept |
| 10:50–11:30 | Product Inventory lab |
| 11:30–11:40 | Appointment challenge |
| 11:40–11:50 | Quiz / bridge to relationships |

## Opening demonstration

Start with:

```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance
```

Then deliberately do:

```python
account.balance = -1_000_000
```

Ask:

> The code runs. But is the object still valid for our domain?

This separates:

```text
syntactically possible
from
semantically valid
```

## Encapsulation explanation

Avoid reducing encapsulation to:

> Put underscores in front of variables.

Instead use:

> Keep state and behavior together and define how callers are supposed to interact with that state.

Then compare:

```python
account.balance -= 50_000
```

with:

```python
account.withdraw(50_000)
```

The second call gives the class a place to own the rule.

## Abstraction explanation

Use:

```text
PUBLIC VIEW
withdraw(amount)
balance

INTERNAL DETAIL
_balance
how validation is performed
how state is changed internally
```

The caller should know enough to use the object correctly, but should not need every implementation detail.

## Invariant

Introduce only lightly.

Example:

```text
Product invariant:
stock >= 0
```

Ask:

> Does every normal public operation leave the object in a state where this remains true?

Do not yet formalize preconditions/postconditions or Python `assert`; Week 13 covers that.

## Why `@property`?

Use it only to demonstrate:

```python
print(product.stock)
```

while storing:

```python
self._stock
```

The learning point is public read access with internal representation.

Do not teach descriptors, setters, computed properties, or advanced decorator mechanics.

## Double underscore

If students ask about:

```python
__balance
```

you may mention briefly that Python performs name mangling, but emphasize that this is not a security/privacy boundary.

The course standard for introductory examples remains:

```python
_balance
```

## Quiz answer key

1. **B**
2. **B**
3. **B**
4. **B**
5. **B**
6. Encapsulation concerns grouping state/behavior and controlling access/change; abstraction concerns exposing useful operations while hiding unnecessary internal workings.
7. Python's leading underscore is a convention, not enforced private access.
8. It lets callers read a value through the public interface without encouraging direct use of the internal attribute.
9. The caller need not know how status is represented, which checks run, or exactly how the state update is performed.
10. It defines a valid-state rule the object's operations should preserve.

## Assignment grading notes

Reward a clear interface and simple reasoning.

Do not require perfect protection from malicious callers. Python allows convention-breaking access.

The question is whether normal use of the class encourages valid interaction.

## What not to teach yet

Avoid deep treatment of:

- exceptions and custom error types;
- formal Design by Contract;
- inheritance visibility;
- friend classes;
- descriptors;
- metaclasses;
- advanced property setters;
- data classes.

## Closing question

End with:

> A Product can now protect its own stock. But an Order needs Product objects, and an Appointment needs Patient and Doctor objects. How should objects refer to and use each other?

That leads directly to:

**Week 5 — Object Relationships.**
