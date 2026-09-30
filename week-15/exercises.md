# Module 15 Exercises — Reusability, Patterns & Case Study

## Exercise 1 — Code Reuse or Design Reuse?

Classify each example:

1. importing a class from `models.py`;
2. inheriting `display_info()` from a superclass;
3. reusing a Strategy-style structure for another varying algorithm;
4. using a class library;
5. reusing a Factory Method-style creation structure.

Choose **code reuse**, **design reuse**, or **both** and explain.

---

## Exercise 2 — Find the Variation

Given:

```python
def calculate_shipping(mode, subtotal):
    if mode == 'pickup':
        return 0
    elif mode == 'standard':
        return 15000
    elif mode == 'express':
        return 30000
```

Answer:

1. What varies?
2. What stays stable?
3. Which responsibility could move into separate objects?

---

## Exercise 3 — Strategy-style Refactor

Create:

```text
DeliveryStrategy-style objects
├── PickupDelivery
├── StandardDelivery
└── ExpressDelivery
```

Each must provide:

```python
fee(subtotal)
```

Refactor Order so it calls the selected object's `fee()` without mode-based branching.

---

## Exercise 4 — Pattern or Overengineering?

For each case, decide whether a Strategy-style abstraction is probably useful:

1. one fixed delivery rule that will never vary;
2. three interchangeable tax calculations selected at runtime;
3. one two-line helper used once;
4. several discount policies expected to grow.

Explain every answer.

---

## Exercise 5 — Creation Responsibility

Given caller code that repeatedly chooses between `EmailNotification()` and `SMSNotification()`, explain what responsibility could move into a creator abstraction.

Then implement the small Factory Method-style example from the module material.

---

## Exercise 6 — Food Ordering Responsibilities

For `Customer`, `MenuItem`, `OrderItem`, and `Order`, assign:

- state;
- behavior;
- responsibility.

Explain why `OrderItem.subtotal()` belongs on OrderItem rather than Order.

---

## Exercise 7 — Test the Reusable Design

Write plain `assert` tests showing that the same Order works with at least three delivery strategies.

Do not inspect the strategy type in Order.

---

## Challenge — Remove the Pattern

Take one of your Module 15 pattern-based solutions and rewrite it in the simplest possible form without the pattern.

Compare both versions:

- number of classes;
- ease of adding one new variation;
- readability;
- coupling.

Conclude which version is more appropriate for the stated requirement and why.