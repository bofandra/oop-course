# Week 6 Assignment — Employee Inheritance Hierarchy

## Objective

Model a meaningful **is-a** relationship and implement it using Python inheritance.

## Task

Create these classes:

```text
Employee
├── Developer
└── Designer
```

## Employee

State:

- `employee_id`
- `name`

Behavior:

- `display_info()`

## Developer

Developer **is an Employee**.

Additional state:

- `programming_language`

Additional behavior:

- `write_code()`

## Designer

Designer **is an Employee**.

Additional state:

- `design_tool`

Additional behavior:

- `create_design()`

## Requirements

Use inheritance and `super().__init__()`.

Create at least:

- one Employee;
- two Developers;
- two Designers.

Demonstrate that Developer and Designer objects can use inherited Employee behavior.

Do **not** override `display_info()` yet. Overriding is the focus of Week 7.

## Written explanation

Answer:

1. Why are Developer and Designer valid subclasses of Employee?
2. Which features are inherited?
3. Which features are specific to Developer?
4. Which features are specific to Designer?
5. What does `super().__init__()` accomplish in your subclasses?
6. Why would `class Employee(Developer)` represent the relationship incorrectly?
7. Give one example from another domain where composition should be used instead of inheritance.

## Rubric

| Criterion | Weight |
|---|---:|
| Correct superclass design | 15% |
| Correct subclasses | 20% |
| Correct inherited access | 20% |
| Appropriate `super().__init__()` usage | 15% |
| Meaningful is-a modelling | 15% |
| Explanation / reasoning | 15% |
| **Total** | **100%** |

## Scope

Do not add method overriding, polymorphism, multiple inheritance, mixins, or abstract classes.

The assignment is specifically about **single inheritance and specialization**.
