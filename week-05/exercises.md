# Module 5 Exercises — Object Relationships

## Exercise 1 — Reference Another Object

Create Patient, Doctor, and Appointment classes. Appointment must store references to one Patient and one Doctor.

Create two Patient objects, two Doctor objects, and two Appointment objects. Print each appointment's patient and doctor names by navigating through the object references.

## Exercise 2 — Avoid Duplicated Data

Compare:

```python
class Appointment:
    def __init__(self, patient_name):
        self.patient_name = patient_name
```

with:

```python
class Appointment:
    def __init__(self, patient):
        self.patient = patient
```

Explain one advantage and one trade-off of storing the Patient object rather than copying only the name.

## Exercise 3 — Identify Client and Supplier

Given:

```python
class Printer:
    def print_text(self, text):
        print(text)

class Report:
    def print_report(self, printer):
        printer.print_text("Monthly Report")
```

Answer:

1. Which class acts as Client?
2. Which class acts as Supplier?
3. What service is supplied?
4. Where does the Supplier appear: attribute, formal argument, or function result?

## Exercise 4 — Has-a or Is-a?

Classify each pair as **has-a** or **is-a** and explain why:

- Car / Engine
- Doctor / Person
- Order / OrderItem
- Laptop / Battery
- Student / Person
- Library / Book

Do not implement inheritance yet.

## Exercise 5 — Composition

Implement:

```text
Product
  ▲
  │ referred to by
OrderItem
  ▲
  │ contained in
Order
```

Requirements:

- Product has name and price.
- OrderItem has Product and quantity.
- OrderItem calculates subtotal.
- Order contains multiple OrderItems.
- Order calculates total.

## Exercise 6 — Responsibility

For the Order model, explain:

1. why `subtotal()` belongs naturally to OrderItem;
2. why `total()` belongs naturally to Order;
3. why Product should not calculate the entire Order total.

## Exercise 7 — Library Loan

Model Member, Book, and Loan. Loan should store references to Member and Book.

Add `display_info()` that shows:

```text
<member name> borrowed <book title>
```

Explain the relationships.

## Challenge — Enrollment as a Relationship Object

Requirement:

> A Student enrolls in a Course. The enrollment itself has a status.

Model Student, Course, and Enrollment. Enrollment must refer to Student and Course and store its own status.

Explain why Enrollment deserves to be an object rather than merely storing Course names inside Student.
