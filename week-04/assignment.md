# Module 4 Assignment — Encapsulated Inventory Item

## Objective

Redesign a stateful class so callers use a clear public interface and normal operations preserve a valid state.

## Task

Implement an `InventoryItem` class.

### State

- `sku`
- `name`
- internal `_quantity`, initialized to `0`

### Public interface

Implement:

```python
quantity
add(quantity)
remove(quantity)
display_info()
```

Use a read-only `quantity` property.

### Rule / invariant

```text
quantity >= 0
```

A newly created item must already satisfy the invariant. For this module, invalid add/remove requests may simply leave the object unchanged. Exception handling is studied later.

## Required demonstration

Create at least **three InventoryItem objects** and show:

1. reading quantity through the public property;
2. adding a valid quantity;
3. removing a valid quantity;
4. attempting to remove more than available;
5. each object maintaining independent state.

## Written explanation

Answer:

1. Which state is intended for internal use?
2. What is the public interface?
3. Why does the leading underscore not create strict privacy in Python?
4. What invariant does the class try to preserve?
5. Which part of your design demonstrates encapsulation?
6. Which part demonstrates abstraction?
7. What could go wrong if callers directly manipulate `_quantity`?

## Rubric

| Criterion | Weight |
|---|---:|
| Clear internal/public distinction | 20% |
| Public methods | 20% |
| Read-only quantity access | 15% |
| Invariant preserved in normal operations | 20% |
| Multiple independent instances | 10% |
| Explanation / reasoning | 15% |
| **Total** | **100%** |

## Scope

Do not add inheritance, custom exceptions, advanced descriptors, or metaprogramming.

The assignment is about **encapsulation, abstraction, and valid state**, not advanced Python.
