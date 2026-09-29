# Week 6 Assignment — Employee Inheritance Hierarchy

## Objective

Use inheritance to model a genuine **is-a** relationship between a general class and more specialized classes.

## Task

Implement this hierarchy:

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

Use:

```python
super().__init__(employee_id, name)
```

## Designer

Designer **is an Employee**.

Additional state:

- `design_tool`

Additional behavior:

- `create_design()`

Use superclass initialization for shared Employee state.

## Required demonstration

Create at least:

- one Employee;
- two Developer objects;
- two Designer objects.

Demonstrate:

1. inherited attributes;
2. inherited `display_info()`;
3. subclass-specific attributes;
4. subclass-specific methods;
5. `isinstance()` checks that reinforce the is-a relationship.

## Written explanation

Answer:

1. Why is Developer a reasonable subclass of Employee?
2. Why is Designer a reasonable subclass of Employee?
3. Which state is shared conceptually across all employees?
4. Which behavior is inherited?
5. Which behavior is specialized by adding new methods?
6. Why would `Employee(Car)` or `Car(Employee)` be a poor inheritance decision?
7. What is the role of `super().__init__()` in your implementation?

## Rubric

| Criterion | Weight |
|---|---:|
| Correct superclass design | 20% |
| Correct subclass definitions | 20% |
| Correct use of inherited features | 20% |
| Correct use of `super().__init__()` | 15% |
| Meaningful is-a reasoning | 15% |
| Written explanation | 10% |
| **Total** | **100%** |

## Scope

Do not override inherited methods yet.

Do not implement polymorphism, abstract classes, or multiple inheritance.

Those topics appear in later weeks.
