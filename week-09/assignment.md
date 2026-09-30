# Module 9 Assignment — Abstract Payment Hierarchy

## Objective

Model a general concept that should not be instantiated directly, while requiring concrete subclasses to implement specific behavior.

## Task

Implement:

```text
Payment
├── CashPayment
├── CardPayment
└── EWalletPayment
```

## Payment

Use Python `ABC` and `@abstractmethod`.

Shared state:

- `reference_id`

Shared concrete behavior:

- `display_reference()`

Required abstract behavior:

```python
pay(amount)
```

## CashPayment

Implement `pay(amount)` with a simple message or return value indicating a cash payment.

## CardPayment

Additional state:

- `card_last_four`

Implement `pay(amount)`.

## EWalletPayment

Additional state:

- `provider`

Implement `pay(amount)`.

## Required demonstration

Create at least:

- one CashPayment;
- one CardPayment;
- one EWalletPayment.

Place them in one list and call:

```python
for payment in payments:
    payment.pay(100_000)
```

Also demonstrate inherited shared behavior.

## Written explanation

Answer:

1. Why is Payment abstract in your model?
2. Which feature is abstract/deferred?
3. Which features are concrete/shared?
4. What happens if a subclass does not implement `pay()`?
5. Why can an abstract class still contain shared state and concrete methods?
6. How does the design reuse inheritance and polymorphism from previous modules?
7. Would every superclass in every system need to be abstract? Why not?

## Rubric

| Criterion | Weight |
|---|---:|
| Appropriate abstract superclass | 20% |
| Correct abstract method | 15% |
| Correct concrete subclasses | 20% |
| Shared state/concrete behavior | 15% |
| Polymorphic demonstration | 15% |
| Explanation / reasoning | 15% |
| **Total** | **100%** |

## Scope

Do not use multiple inheritance or mixins.

Those are Module 10 topics.

The use of Python `ABC` is an implementation technique for the abstract/deferred-class concept taught from the Diktat.
