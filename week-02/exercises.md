# Module 2 Exercises — Classes, Objects & Instances

## Exercise 1 — Count Classes and Instances

Consider:

```python
class Book:
    pass

book_1 = Book()
book_2 = Book()
book_3 = Book()
```

Answer:

1. How many class definitions are there?
2. How many `Book` instances are there?
3. Are `book_1` and `book_2` two separate instances created from the same class? Explain without using Python identity operators yet.
4. What is the conceptual relationship between `Book` and `book_1`?

> Python's `is` identity operator is introduced formally in Module 11. Module 2 only requires the concept that separate constructor calls create separate instances.

---

## Exercise 2 — Build a Class with `__init__()`

Create:

```python
class Course:
    ...
```

Each instance must have:

- `code`
- `name`
- `credits`

Create:

```text
OOP101 — Object Oriented Programming — 4 credits
DB101  — Database Systems — 3 credits
```

Print the state of both objects.

---

## Exercise 3 — Trace `self`

Given:

```python
class Student:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)

student_1 = Student("Alya")
student_2 = Student("Bima")
```

Explain what `self` refers to when executing:

```python
student_1.display()
```

Then explain it again for:

```python
student_2.display()
```

---

## Exercise 4 — Instance Attributes

Create two `Product` objects:

```text
P001 — Keyboard — 500000
P002 — Mouse    — 200000
```

Use instance attributes:

- `sku`
- `name`
- `price`

Explain why `price` should be an instance attribute in this example.

---

## Exercise 5 — Class Attributes

Create:

```python
class Employee:
    company = "Example Corp"
```

with instance attributes:

- `employee_id`
- `name`

Create two employees and print their company through:

1. `Employee.company`
2. each employee instance.

Explain what information is shared and what is unique.

---

## Exercise 6 — Choose the Right Attribute Type

For a `Student` class in a simple university system, classify each item as more suitable for an **instance attribute** or a **class attribute**:

- student ID
- name
- email
- university name
- current GPA
- country of campus, assuming every student in this class belongs to the same campus

Explain every answer.

---

## Exercise 7 — Find the Problem

What is wrong with this design if different students should have different names?

```python
class Student:
    name = "Unknown"
    university = "Example University"
```

Rewrite the class so that the student's name belongs to each instance.

---

## Challenge — Flight Ticket

Create a `FlightTicket` class with:

Instance attributes:

- `flight_num`
- `airport`
- `gate`
- `time`
- `seat`
- `passenger`

Class attributes:

- `airline`
- `airline_code`

Create at least two ticket instances with different state.

Add a simple `print_info()` method that displays the ticket data.

Then answer:

> Which values are shared across ticket instances, and which values represent the state of one particular ticket?
