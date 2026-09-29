# Week 15 Assignment — Food Ordering Reuse Case Study

## Objective

Refine a small OO system by identifying real variation points and applying reusable design ideas only where they help.

## Requirement

> A food-ordering system has Customers, MenuItems, OrderItems, and Orders. An Order contains multiple OrderItems. Different delivery methods calculate different delivery fees. After confirmation, an order may send a notification through a chosen channel.

## Part 1 — Core model

Implement:

- `Customer`;
- `MenuItem`;
- `OrderItem`;
- `Order`.

OrderItem must calculate its own subtotal.

Order must calculate the order subtotal from its OrderItems.

## Part 2 — Strategy-style delivery

Implement at least:

- `PickupDelivery`;
- `StandardDelivery`;
- `ExpressDelivery`.

Each must support:

```python
fee(subtotal)
```

Order must use the selected delivery object without a delivery-type `if/elif` chain.

## Part 3 — Factory Method-style notification

Implement a small creator hierarchy that can produce at least:

- `EmailNotification`;
- `SMSNotification`.

The caller should be able to ask a creator to send an order-confirmation message without constructing the concrete notification directly.

## Part 4 — OOT

Write plain `assert` tests for:

1. MenuItem state;
2. OrderItem subtotal;
3. Order subtotal;
4. three delivery strategies;
5. Order total with different delivery strategies;
6. at least one notification creator flow.

## Part 5 — Design explanation

Answer:

1. Which behavior varies in the delivery design?
2. What responsibility moved out of Order?
3. Why is the result Strategy-style?
4. What creation responsibility moved into the notification creator hierarchy?
5. Why is that Factory Method-style in this course example?
6. Which parts are code reuse?
7. Which parts are design reuse?
8. Name one place where adding another pattern would be unnecessary complexity.

## Rubric

| Criterion | Weight |
|---|---:|
| Core object model and responsibilities | 20% |
| Strategy-style delivery design | 25% |
| Factory Method-style creation design | 20% |
| Integration / end-to-end behavior | 15% |
| OOT tests | 10% |
| Design explanation / reuse reasoning | 10% |
| **Total** | **100%** |

## Scope

Do not add:

- database;
- REST API;
- GUI;
- payment gateway;
- repository pattern;
- dependency injection framework;
- full design-pattern catalogue.

The objective is to recognize **appropriate reuse**, not maximize abstraction.