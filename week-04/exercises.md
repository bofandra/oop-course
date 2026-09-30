# Module 4 Exercises — Encapsulation & Abstraction

## Exercise 1 — Public Interface or Internal Detail?

Consider a `BankAccount` with:

- owner
- internal balance
- `deposit()`
- `withdraw()`
- public balance reading

Classify each item as something the caller should normally use directly or as an internal implementation detail.

Explain your reasoning.

---

## Exercise 2 — Improve Direct Mutation

Given:

```python
class Product:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock
```

Outside code can write:

```python
product.stock = -100
```

Redesign the class so a new Product starts with `_stock = 0`, then use:

- `add_stock(quantity)`
- `remove_stock(quantity)`
- a read-only `stock` property

The object should satisfy this rule immediately after creation and after every successful public operation:

```text
stock >= 0
```

---

## Exercise 3 — Encapsulation or Abstraction?

For each statement, decide whether it mainly illustrates **encapsulation**, **abstraction**, or both.

1. A BankAccount updates its own balance through `deposit()`.
2. A caller uses `withdraw(50000)` without knowing the internal steps.
3. A Product exposes its current stock but not the internal variable directly.
4. A driver sees a temperature indicator rather than raw internal engine details.

Explain every answer.

---

## Exercise 4 — Python Visibility Convention

Consider:

```python
class Example:
    def __init__(self):
        self._value = 10
```

Answer:

1. Does `_value` become strictly private in Python?
2. What does the leading underscore communicate?
3. Why is this still useful if Python technically allows external access?

---

## Exercise 5 — Appointment Invariant

For a simple Appointment:

```text
valid statuses:
waiting
confirmed
cancelled
```

Propose one invariant describing valid status.

Then redesign:

```python
appointment.status = ...
```

into an interface using:

- read-only status access;
- `confirm()`;
- `cancel()`.

A cancelled appointment must not later become confirmed.

---

## Exercise 6 — Product Invariant Trace

Initial state:

```text
stock = 10
```

Operations:

```text
add_stock(5)
remove_stock(3)
remove_stock(20)
```

For your Module 4 design:

1. What is stock after each operation?
2. Which operation should not be allowed to make stock negative?
3. What invariant is being preserved?

---

## Exercise 7 — What Does the Caller Need to Know?

For this interface:

```python
product.add_stock(5)
product.remove_stock(2)
print(product.stock)
```

Write two columns:

```text
Caller needs to know
Caller does not need to know
```

Include at least three items in each column.

---

## Challenge — Temperature Sensor

Design a `TemperatureSensor` class.

Internal state:

- `_celsius`

Public interface:

- read-only `celsius`
- `fahrenheit()`
- `update_celsius(value)`

Rule:

```text
celsius >= -273.15
```

Keep the implementation simple. Do not use custom exceptions yet.

Explain which parts demonstrate encapsulation and which parts demonstrate abstraction.
