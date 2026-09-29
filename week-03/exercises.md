# Week 3 Exercises — Attributes, Methods, State & Behavior

## Exercise 1 — Identify State and Behavior

For a `BankAccount`, classify each item:

- owner
- balance
- display_balance()
- deposit()
- withdraw()

Which are state? Which are behavior?

---

## Exercise 2 — Read-only vs State-changing Methods

Consider:

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def resize(self, width, height):
        self.width = width
        self.height = height
```

Answer:

1. Which method only reads state?
2. Which method changes state?
3. What state changes after `resize(10, 20)`?

---

## Exercise 3 — Appointment State Transition

Implement:

```text
waiting
  ↓ confirm()
confirmed
```

and:

```text
waiting
  ↓ cancel()
cancelled
```

Use an `Appointment` class with:

- `patient_name`
- `doctor_name`
- `status`
- `confirm()`
- `cancel()`
- `display_status()`

Create two separate Appointment objects and demonstrate that changing one does not change the other.

---

## Exercise 4 — Parameters vs Attributes

Given:

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
```

Explain the difference between:

- `amount`
- `self.balance`

Then call `deposit()` three times with different values.

---

## Exercise 5 — Move Behavior to the Object

Suppose code outside a Book object does this:

```python
book.is_available = False
```

Rewrite the design so the caller can express the action as:

```python
book.borrow()
```

Explain why the second form communicates domain intent more clearly.

---

## Exercise 6 — Responsibility

For each behavior, choose the object that most naturally owns it in a simple model:

1. `calculate_subtotal()` — Product or OrderItem?
2. `confirm()` — Patient or Appointment?
3. `display_balance()` — BankAccount or Customer?
4. `area()` — Rectangle or Screen?

There may be context-dependent answers. Explain your reasoning using the state each behavior needs.

---

## Exercise 7 — Book Lifecycle

Create:

```text
Book
State:
- title
- author
- is_available

Behavior:
- display_info()
- borrow()
- return_book()
```

Trace the state after this sequence:

```python
book.borrow()
book.return_book()
book.borrow()
```

Write the state after every method call.

---

## Challenge — What Rule Is Missing?

Run:

```python
book.borrow()
book.borrow()
```

If the second call still "works", explain why the class currently allows it.

Do not jump ahead to a complex solution. Write one sentence describing the rule the class should eventually enforce.

This becomes the bridge to Week 4.