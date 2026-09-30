# Module 13 — Exception Handling & Assertions

> **Run the notebook:** [Open Module 13 in Google Colab](https://colab.research.google.com/github/bofandra/oop-course/blob/main/week-13/13_exceptions_assertions.ipynb)

## Learning outcomes

By the end of this module, learners should be able to:

1. explain why runtime failures require an exception-handling mechanism;
2. raise a Python exception when an operation cannot satisfy its required conditions;
3. handle expected exceptions using `try` / `except`;
4. prefer specific exception types over a broad catch-all handler;
5. explain exception propagation at a high level;
6. distinguish **precondition**, **postcondition**, and **class invariant**;
7. use Python `assert` for internal correctness assumptions;
8. distinguish **invalid external input → exception** from **internal program assumption → assertion**.

## Source alignment

Inggriani Liem explains exception handling as a mechanism for unexpected conditions that occur during execution. The Diktat links failure to a routine that cannot fulfill its contract and discusses exceptions, assertions, preconditions, postconditions, and class invariants.

The Diktat also frames preconditions and postconditions as part of a **Client–Supplier contract**:

```text
Client
must satisfy precondition
        ↓
Supplier operation executes
        ↓
Supplier should satisfy postcondition

Class invariant
must remain valid for valid objects
```

The Diktat's exception syntax and some statements are language-specific to Eiffel. Python implementation this module follows OpenStax 14.4–14.5 using:

- `try`
- `except`
- `raise`
- built-in exception types

Python `assert` is used as an implementation bridge for checking internal assumptions.

## From Module 12 to Module 13

Module 12 gave classes richer behavior.

Module 13 asks:

> What should happen when an operation cannot fulfill what the caller asked?

Example:

```python
account.withdraw(1_000_000)
```

when the account only contains:

```text
100,000
```

Silently producing an invalid balance is a poor result.

## 1. Runtime failure

Suppose:

```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        self.balance -= amount
```

Then:

```python
account = BankAccount(100_000)
account.withdraw(500_000)
```

produces:

```text
balance = -400000
```

If our domain rule is:

```text
balance >= 0
```

the object has become invalid.

## 2. Raise an exception

Python lets the method signal that it cannot complete the requested operation:

```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        if amount > self._balance:
            raise ValueError("Insufficient balance")

        self._balance -= amount
```

Now the method either:

```text
completes successfully
or
signals failure explicitly
```

## 3. Handle an exception

Caller code can decide what to do:

```python
try:
    account.withdraw(500_000)
except ValueError as error:
    print("Withdrawal failed:", error)
```

This separates:

```text
normal operation
from
error-handling path
```

## 4. Catch specific exceptions

Prefer:

```python
except ValueError:
    ...
```

when `ValueError` is the expected problem.

Avoid teaching:

```python
except:
    ...
```

as the default solution.

A broad catch can hide unrelated programming errors.

## 5. Exception propagation

Consider:

```python
def pay_bill(account, amount):
    account.withdraw(amount)
```

If `withdraw()` raises an exception and `pay_bill()` does not handle it, the exception propagates to the caller.

Conceptually:

```text
withdraw()
   raises
     ↓
pay_bill()
   does not handle
     ↓
caller receives exception
```

The important idea is that an error can be handled at an appropriate level rather than necessarily at the exact line where it occurs.

## 6. Preconditions

A precondition states what must be true **before** an operation is called successfully.

For:

```python
withdraw(amount)
```

possible preconditions are:

```text
amount > 0
amount <= balance
```

These describe what the operation expects.

## 7. Postconditions

A postcondition states what should be true **after** a successful operation.

If:

```text
old balance = 100000
amount      = 30000
```

then after a successful withdrawal:

```text
new balance = 70000
```

A conceptual postcondition:

```text
new_balance == old_balance - amount
```

## 8. Class invariant

A class invariant is a condition expected to remain true for valid instances.

For BankAccount:

```text
balance >= 0
```

For Product:

```text
stock >= 0
```

We introduced this idea informally in Module 4. Module 13 now connects it explicitly to contracts and assertions.

## 9. Python assert

For an internal correctness assumption:

```python
class Product:
    def __init__(self, stock):
        if stock < 0:
            raise ValueError("Initial stock cannot be negative")

        self._stock = stock

    def remove_stock(self, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be positive")

        if quantity > self._stock:
            raise ValueError("Insufficient stock")

        self._stock -= quantity

        assert self._stock >= 0
```

The exception handles an invalid request.

The assertion checks an internal condition that should be true if the method logic is correct.

## 10. Exception or assertion?

Use this working distinction:

```text
Invalid caller/input condition
→ raise an exception

Internal programmer assumption
that should always hold
→ assert
```

Example:

```python
if amount <= 0:
    raise ValueError("Amount must be positive")
```

versus:

```python
assert self._balance >= 0
```

Do not use `assert` as the main mechanism for validating normal user input.

## 11. Contract thinking

For:

```python
account.withdraw(amount)
```

think:

```text
PRECONDITION
amount > 0
amount <= balance

OPERATION
withdraw(amount)

POSTCONDITION
new balance = old balance - amount

INVARIANT
balance >= 0
```

This is the Client–Supplier contract view emphasized in the Diktat.

## Main exercise — Product Inventory

Implement a Product with:

- `name`
- internal `_stock`
- read-only `stock`
- `add_stock(quantity)`
- `remove_stock(quantity)`

Rules:

```text
quantity > 0
stock >= 0
```

Use:

- `ValueError` for invalid quantity;
- `ValueError` for removing more stock than available;
- `assert` after a successful state-changing operation to check the invariant.

Then handle one expected error using `try` / `except`.

## Challenge — BankAccount

Implement:

```text
BankAccount
- owner
- balance

deposit(amount)
withdraw(amount)
```

Contracts:

```text
deposit precondition:
amount > 0

withdraw preconditions:
amount > 0
amount <= balance

class invariant:
balance >= 0
```

Write a demonstration with both successful and failing operations.

## Reflection

Answer:

> Why is raising an exception often clearer than returning a magic value such as `-1` when an operation fails?

## Reading

### Inggriani Liem

Focus on:

- Exception handling;
- runtime failure;
- assertions;
- preconditions;
- postconditions;
- class invariants;
- Client–Supplier contract thinking.

### OpenStax

Read:

- **14.4 Handling Exceptions**
- **14.5 Raising Exceptions**

## Module 13 package

- [Colab notebook](13_exceptions_assertions.ipynb)
- [Exercises](exercises.md)
- [Quiz](quiz.md)
- [Assignment](assignment.md)
- [Instructor notes](instructor-notes.md)
- [Mastery checks with worked feedback](../MASTERY_CHECKS.md)

## Next module

Module 13 makes individual class operations more robust.

Module 14 asks:

> How do we systematically move from a requirement to object analysis, class design, implementation, and testing?

That leads to:

**Module 14 — OOP Analysis, Design, Class Diagram & Testing.**
