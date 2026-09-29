# Week 6 Exercises — Inheritance

## Exercise 1 — Identify Superclass and Subclass

For each pair, identify the superclass and subclass:

- Person / Doctor
- Employee / Developer
- Vehicle / Car
- Animal / Cat

Then write an **is-a** sentence for each.

---

## Exercise 2 — Simple Inheritance

Create:

```python
class Person:
    ...
```

with:

- `name`
- `display_name()`

Then create:

```python
class Student(Person):
    ...
```

Add:

- `student_id`
- `display_student_id()`

Demonstrate that a Student object can use both inherited and subclass-specific behavior.

---

## Exercise 3 — Inherited vs Specific Features

Given:

```text
Employee
- employee_id
- name
- display_info()

Developer is-a Employee
- programming_language
- write_code()
```

Classify each feature as:

- inherited from Employee; or
- specific to Developer.

---

## Exercise 4 — Use super().__init__()

Implement:

```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
```

and:

```python
class Car(Vehicle):
    ...
```

Car adds:

- `number_of_doors`

Use `super().__init__()` to initialize `brand`.

Create two Car objects.

---

## Exercise 5 — Is-a or Has-a?

Classify each relationship:

1. Car / Engine
2. Doctor / Person
3. Laptop / Battery
4. Cat / Animal
5. Order / OrderItem
6. Manager / Employee

For each, explain why inheritance is or is not appropriate.

---

## Exercise 6 — Invalid Inheritance

Consider:

```python
class Engine:
    pass

class Car(Engine):
    pass
```

Explain why this may be syntactically valid Python but conceptually poor modelling.

Rewrite it using an object relationship instead.

---

## Exercise 7 — One Superclass, Two Subclasses

Create:

```text
Person
├── Doctor
└── Patient
```

Requirements:

- Person: `name`, `display_name()`
- Doctor: `specialty`, `diagnose()`
- Patient: `patient_id`, `show_patient_id()`

Use `super().__init__()` in both subclasses.

---

## Challenge — Appropriate Generalization

You are given three classes with duplicated `name` and `email` state:

- Customer
- Employee
- Supplier

Would you create a Person superclass?

Write a short design argument. Consider whether all three concepts genuinely satisfy the intended **is-a Person** relationship in your domain.

There is no automatic answer based only on duplicated code.
