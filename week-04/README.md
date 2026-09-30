# Module 4 — Encapsulation & Abstraction

## Learning outcomes

By the end of this session, students should be able to:

1. explain **encapsulation** as grouping state and behavior while controlling how state is accessed or changed;
2. explain **abstraction** as exposing what a caller needs while hiding unnecessary implementation detail;
3. distinguish a public interface from internal object state;
4. use Python naming conventions such as a leading underscore to communicate internal-use attributes;
5. use methods and a simple read-only `@property` to provide controlled access to state;
6. identify a simple class invariant such as `stock >= 0`;
7. redesign Module 3 classes so invalid state transitions are harder to create.

## Source alignment

Inggriani Liem identifies **abstraction** and **encapsulation** as core characteristics of object-oriented systems. The Diktat also discusses feature visibility—public, friend, and private—and explicitly says that deciding feature access is part of class design. It introduces a **class invariant** as an assertion that helps ensure class instances satisfy the class definition.

OpenStax 11.1 explicitly introduces both encapsulation and abstraction. It describes encapsulation as grouping data with procedures and restricting direct modification, and abstraction as hiding internal workings that a user of the unit does not need to know.

Python does not enforce visibility in the same way as languages with strict `private` access modifiers. In this course, a leading underscore (for example, `_balance`) is used as a **Python convention** to communicate that an attribute is intended for internal use. The `@property` examples below are a Python implementation technique used to create a simple public read interface.

## From Module 3 to Module 4

Module 3 gave objects meaningful behavior:

```text
state
  +
methods
  ↓
behavior
```

But this was still possible:

```python
account.balance = -10_000_000
appointment.status = "anything"
book.is_available = "maybe"
```

Module 4 asks:

> How should an object expose useful behavior while reducing accidental invalid state changes?

```text
Internal state
     ↓
controlled by
object behavior
     ↓
Public interface
```

## 1. Encapsulation is more than "private variables"

A useful working definition for this course:

> Encapsulation keeps related state and behavior together and controls how that state is used or changed.

Example without much control:

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
```

Outside code can write:

```python
account.balance = -1_000_000
```

A better object interface can make the intended operations explicit:

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
```

Now the normal interface is:

```python
account.deposit(100_000)
account.withdraw(50_000)
```

rather than asking callers to manipulate the internal balance directly.

## 2. Python underscore convention

In Python:

```python
self._balance
```

does **not** create strict privacy.

It communicates:

> This attribute is intended as an implementation detail. Callers should normally use the object's public interface instead.

So:

```python
account._balance = -1_000_000
```

is technically possible, but it violates the intended interface of this class.

Do not teach the underscore as a security boundary.

## 3. Public interface vs internal detail

Imagine:

```python
class Product:
    def __init__(self, name, stock):
        self.name = name
        self._stock = stock

    def add_stock(self, quantity):
        self._stock += quantity

    def remove_stock(self, quantity):
        if quantity <= self._stock:
            self._stock -= quantity
```

A caller needs to know:

```text
add_stock(quantity)
remove_stock(quantity)
stock
```

The caller does **not** need to know every detail of how stock is represented or updated internally.

That separation is the beginning of abstraction:

```text
WHAT can I ask the object to do?
        ↓
public interface

HOW does the object do it?
        ↓
implementation detail
```

## 4. Read access with `@property`

For a simple read-only public view:

```python
class Product:
    def __init__(self, name, stock):
        self.name = name
        self._stock = stock

    @property
    def stock(self):
        return self._stock
```

The caller can read:

```python
print(product.stock)
```

without directly using:

```python
product._stock
```

For Module 4, use `@property` only as a small implementation technique. Do not turn this module into an advanced lesson about descriptors.

## 5. Preserve a valid state

Suppose a Product should never have negative stock.

That rule can be expressed conceptually as:

```text
stock >= 0
```

This is an example of a **class invariant**: a condition that should remain true for valid instances.

A simple implementation:

```python
class Product:
    def __init__(self, name, stock):
        self.name = name
        self._stock = stock

    @property
    def stock(self):
        return self._stock

    def add_stock(self, quantity):
        if quantity > 0:
            self._stock += quantity

    def remove_stock(self, quantity):
        if 0 < quantity <= self._stock:
            self._stock -= quantity
```

At the conceptual level:

```text
Before operation:
stock >= 0

After valid operation:
stock >= 0
```

Formal assertion/contracts are studied later in Module 13. Here the point is simply to recognize and preserve a class rule.

## 6. Encapsulation vs abstraction

Use this distinction:

```text
ENCAPSULATION
How is state + behavior packaged
and access controlled?

ABSTRACTION
What useful interface is shown,
and what implementation detail is hidden?
```

They are related but not identical.

Example:

```python
account.withdraw(50_000)
```

The caller does not need to know every internal step used to update the balance.

That is useful abstraction.

The object also controls its own balance through its methods instead of encouraging arbitrary external mutation.

That is useful encapsulation.

## 7. Improve the Module 3 Appointment

Module 3:

```python
appointment.status = "cancelled"
appointment.status = "banana"
```

Module 4:

```python
class Appointment:
    def __init__(self, patient_name, doctor_name):
        self.patient_name = patient_name
        self.doctor_name = doctor_name
        self._status = "waiting"

    @property
    def status(self):
        return self._status

    def confirm(self):
        if self._status == "waiting":
            self._status = "confirmed"

    def cancel(self):
        if self._status != "cancelled":
            self._status = "cancelled"
```

Callers now have a clearer interface:

```python
appointment.confirm()
appointment.cancel()
print(appointment.status)
```

We are still keeping error handling simple. Raising and handling exceptions is studied in Module 13.

## Main exercise — Product Inventory

Create a `Product` class with:

State:

- `name`
- internal `_stock`

Public interface:

- read-only `stock` property;
- `add_stock(quantity)`;
- `remove_stock(quantity)`;
- `display_info()`.

Rule:

```text
stock >= 0
```

Demonstrate that normal use of the public methods preserves the rule.

## Challenge — Appointment

Improve the Module 3 Appointment so that:

- status starts as `waiting`;
- status is stored internally;
- callers can read status;
- `confirm()` changes `waiting → confirmed`;
- `cancel()` changes a non-cancelled appointment to `cancelled`;
- a cancelled appointment cannot later become confirmed.

Do not use inheritance or custom exception classes.

## Reflection

Answer:

> What is the difference between hiding unnecessary implementation detail and merely renaming an attribute with an underscore?

## Reading

### Inggriani Liem

Focus on:

- abstraction and encapsulation as characteristics of OO;
- visibility/access to features;
- information hiding;
- class invariant as a rule describing valid object state.

### OpenStax

Read **11.1 Object-Oriented Programming Basics**, especially the Encapsulation and Abstraction sections.

Review **11.3 Instance Methods** for methods that access and modify instance state.

## Module 4 package

- [Colab notebook](04_encapsulation_abstraction.ipynb)
- [Exercises](exercises.md)
- [Quiz](quiz.md)
- [Assignment](assignment.md)
- [Instructor notes](instructor-notes.md)

## Next module

Once one object controls its own state, the next question is:

> How do multiple objects work together without collapsing into one giant class?

That leads to:

**Module 5 — Object Relationships.**
