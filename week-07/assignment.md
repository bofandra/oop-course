# Week 7 Assignment — Polymorphic Payroll

> **Teaching schedule note:** Week 7 is immediately before the Mid Test. Prefer completing most of this work in class or set any submission deadline no later than Thursday before the Mid Test so the assignment does not compete with exam preparation.

## Objective

Demonstrate overriding, polymorphism, and runtime method selection using a meaningful inheritance hierarchy.

## Task

Implement:

```text
Employee
├── FullTimeEmployee
├── PartTimeEmployee
└── Freelancer
```

## Base class

`Employee` should contain:

- `employee_id`
- `name`
- `display_info()`

It may also define a basic `calculate_pay()` placeholder behavior for this week's exercise.

## FullTimeEmployee

Additional state:

- `monthly_salary`

Override:

```python
calculate_pay()
```

to return monthly salary.

## PartTimeEmployee

Additional state:

- `hourly_rate`
- `hours_worked`

Override `calculate_pay()`.

## Freelancer

Additional state:

- `project_fee`

Override `calculate_pay()`.

## Required demonstration

Create at least:

- 2 FullTimeEmployee objects;
- 2 PartTimeEmployee objects;
- 2 Freelancer objects.

Place all of them into one list:

```python
employees = [...]
```

Then use:

```python
for employee in employees:
    print(employee.calculate_pay())
```

Do not use type-based `if` / `elif` branching.

## Written explanation

Answer:

1. Which method is overridden?
2. Why is this an example of polymorphism?
3. What determines which `calculate_pay()` implementation runs?
4. Where would `super()` be useful in this hierarchy?
5. Why is this design preferable to one long `if employee_type == ...` chain?
6. How is overriding different from overloading?

## Rubric

| Criterion | Weight |
|---|---:|
| Correct inheritance hierarchy | 15% |
| Correct overriding | 25% |
| Polymorphic loop | 25% |
| Correct pay calculations | 15% |
| No unnecessary type branching | 10% |
| Explanation / reasoning | 10% |
| **Total** | **100%** |

## Scope

Do not use abstract base classes yet.

Do not use multiple inheritance.

Those concepts are covered after the Mid Test.
