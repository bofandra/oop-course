# Week 10 Assignment — Employee Capabilities with Mixins

## Objective

Use multiple inheritance in a controlled way and explain Python's method lookup behavior.

## Task

Implement:

```text
Employee
   ↑
Manager
 + LoggingMixin
 + ExportMixin
```

## Employee

State:

- `employee_id`
- `name`

Behavior:

- `display_info()`

## LoggingMixin

Behavior:

```python
log(message)
```

Output may be:

```text
[LOG] <message>
```

## ExportMixin

Behavior:

```python
export_text()
```

Return a simple textual representation of the object's state.

## Manager

Manager **is an Employee** and also gains the two focused mixin capabilities.

Additional state:

- `department`

Additional behavior:

- `manage()`

## Required demonstration

Create at least two Manager objects.

Demonstrate:

1. inherited Employee behavior;
2. Manager-specific behavior;
3. logging capability;
4. export capability;
5. `Manager.__mro__`.

## Conflict experiment

Add:

```python
class A:
    def describe(self):
        return "A"

class B:
    def describe(self):
        return "B"
```

Then create:

```python
class C(A, B):
    pass
```

Demonstrate which method is selected and explain the result using MRO.

Reverse parent order and repeat.

## Written explanation

Answer:

1. Why is Manager's relationship with Employee different from its relationship with LoggingMixin?
2. Why is LoggingMixin a capability rather than the primary domain identity?
3. What is MRO?
4. Why does parent order matter in the conflict experiment?
5. What is repeated/diamond inheritance?
6. Give one situation where composition would be clearer than multiple inheritance.
7. Why can multiple inheritance increase design complexity?

## Rubric

| Criterion | Weight |
|---|---:|
| Correct primary inheritance | 15% |
| Correct mixin implementation | 20% |
| Multiple capabilities demonstrated | 15% |
| MRO inspection/explanation | 20% |
| Conflict experiment | 15% |
| Design reasoning | 15% |
| **Total** | **100%** |

## Scope

Do not implement a custom MRO algorithm.

Do not use metaclasses or advanced cooperative-multiple-inheritance patterns.

The goal is to understand the structure and trade-offs.
