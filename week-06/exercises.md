# Module 6 Exercises — Inheritance

## Exercise 1 — Identify the is-a Relationship

For each pair, decide whether inheritance is appropriate.

1. Doctor / Person
2. Car / Engine
3. Developer / Employee
4. Laptop / Battery
5. SavingsAccount / BankAccount
6. Order / Customer

Write your reasoning using one of these forms:

```text
X is a Y
```

or:

```text
X has a Y
```

---

## Exercise 2 — Basic Superclass and Subclass

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
    pass
```

Create one `Student` object and demonstrate that it can use `display_name()` inherited from `Person`.

---

## Exercise 3 — Add Subclass-specific State

Extend `Student` with:

- `student_id`

Use:

```python
super().__init__(name)
```

to initialize the Person part of the object.

Then print:

- inherited `name`
- subclass-specific `student_id`

---

## Exercise 4 — Add Subclass-specific Behavior

Create:

```text
Employee
  ↓
Developer
```

Employee:

- employee_id
- name
- display_info()

Developer adds:

- programming_language
- write_code()

Demonstrate that a Developer can use both inherited and subclass-specific behavior.

---

## Exercise 5 — Two Subclasses, One Superclass

Create:

```text
Person
├── Doctor
└── Patient
```

Doctor adds:

- specialty
- diagnose()

Patient adds:

- patient_id
- show_patient_id()

Create one object from each subclass and demonstrate inherited behavior.

---

## Exercise 6 — What Is Inherited?

Given:

```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def display_brand(self):
        print(self.brand)


class Car(Vehicle):
    def __init__(self, brand, seats):
        super().__init__(brand)
        self.seats = seats

    def display_seats(self):
        print(self.seats)
```

Answer:

1. Which attribute originates from Vehicle?
2. Which attribute is Car-specific?
3. Which method is inherited?
4. Which method exists only on Car?

---

## Exercise 7 — Inheritance Is Not Just Reuse

Suppose someone proposes:

```python
class Engine:
    def start(self):
        print("Engine started")


class Car(Engine):
    pass
```

Explain why this design is semantically weak even though it reuses `start()`.

Redesign it using a has-a relationship.

---

## Challenge — Employee Hierarchy

Model:

```text
Employee
├── Developer
├── Designer
└── Manager
```

All employees share:

- employee_id
- name

Each subclass adds one attribute and one behavior.

Use `super().__init__()` in every subclass.

Do not override superclass methods yet. That is the focus of Module 7.
