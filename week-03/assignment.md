# Week 3 Assignment — Model State Transitions

## Objective

Create objects whose methods express meaningful behavior and change state over time.

## Task — Simple Order

Implement an `Order` class.

### State

Each Order must have:

- `order_id`
- `customer_name`
- `total`
- `status`

Initial status:

```text
created
```

### Behavior

Implement:

```python
display_summary()
confirm()
cancel()
```

For this week's assignment, `confirm()` and `cancel()` may simply change the status. Validation rules are intentionally postponed to Week 4.

## Required demonstration

Create at least **three Order objects**.

Show:

1. their initial state;
2. one order being confirmed;
3. one order being cancelled;
4. one order remaining unchanged;
5. a summary for each order.

## Written explanation

Answer:

1. Which attributes represent Order state?
2. Which methods only read state?
3. Which methods change state?
4. What is the difference between the parameter `total` received by `__init__()` and `self.total` stored by the object?
5. Why is `order.confirm()` more meaningful than setting the status directly from outside?
6. What invalid transition can your current implementation still allow?

## Rubric

| Criterion | Weight |
|---|---:|
| Correct state model | 20% |
| Correct methods | 25% |
| State transitions demonstrated | 25% |
| Multiple independent objects | 15% |
| Explanation / reasoning | 15% |
| **Total** | **100%** |

## Scope

Do not add inheritance, property decorators, custom exceptions, or complex validation.

The missing state-protection rules are part of the learning objective for Week 4.