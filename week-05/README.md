# Week 5 — Object Relationships

## Learning outcomes

By the end of this session, students should be able to:

1. explain why useful OO systems are built from **collaborating objects**;
2. explain a **Client–Supplier** relationship;
3. model one object holding a reference to another object;
4. recognize and implement a simple **has-a** relationship;
5. distinguish **has-a** from **is-a** at a conceptual level;
6. use composition when one object is built from or contains other objects;
7. assign collaboration responsibilities to appropriate objects.

## Source alignment

Inggriani Liem states that relationships among classes include **Client–Supplier** and inheritance. In a Client–Supplier relationship, the Client uses services provided by the Supplier. The Diktat defines a class A as a Client of class B when A contains an entity of type B; that entity may appear as an attribute, a formal routine argument, or a function result.

The Diktat also distinguishes **has-a** from **is-a**. A has-a relationship reflects a whole/component relationship; its example is a Car having an Engine and Wheels. It warns that beginners often incorrectly implement has-a using inheritance.

This week concentrates on Client–Supplier, has-a, composition, and collaboration. Inheritance is introduced formally in Week 6.

## From Week 4 to Week 5

Week 4 focused on one object protecting its own state:

```text
Product
- owns stock
- controls stock changes
```

But real systems need multiple objects:

```text
Patient
   │
   ▼
Appointment
   │
   ▼
Doctor
```

Week 5 asks:

> How should objects refer to and use each other?

## 1. Objects collaborate

```python
class Patient:
    def __init__(self, patient_id, name):
        self.patient_id = patient_id
        self.name = name


class Doctor:
    def __init__(self, doctor_id, name):
        self.doctor_id = doctor_id
        self.name = name
```

An Appointment can hold references to both objects:

```python
class Appointment:
    def __init__(self, patient, doctor, time):
        self.patient = patient
        self.doctor = doctor
        self.time = time
        self.status = "waiting"
```

Usage:

```python
patient = Patient("P001", "Budi")
doctor = Doctor("D001", "Dr. Andi")

appointment = Appointment(
    patient,
    doctor,
    "10:00"
)
```

Conceptually:

```text
Patient object
      ▲
      │ referenced by
      │
Appointment object
      │
      │ references
      ▼
Doctor object
```

## 2. Store objects, not duplicated text

Compare:

```python
class Appointment:
    def __init__(self, patient_name, doctor_name):
        self.patient_name = patient_name
        self.doctor_name = doctor_name
```

with:

```python
class Appointment:
    def __init__(self, patient, doctor):
        self.patient = patient
        self.doctor = doctor
```

The second model lets the Appointment refer to the Patient and Doctor objects rather than duplicate selected text values.

## 3. Client–Supplier

A simple teaching interpretation:

```text
Client
uses
Supplier
```

Example:

```python
class NotificationService:
    def send(self, message):
        print("Notification:", message)


class Appointment:
    def confirm(self, notification_service):
        self.status = "confirmed"
        notification_service.send(
            "Appointment confirmed"
        )
```

Here:

```text
Appointment
    │ uses service
    ▼
NotificationService
```

The focus is simply:

> One object can use a service supplied by another object.

## 4. Has-a

Use the Diktat's classic example:

```text
Car has an Engine
Car has Wheels
```

A simple Python model:

```python
class Engine:
    def __init__(self, model):
        self.model = model


class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine
```

Usage:

```python
engine = Engine("E-100")
car = Car("Example", engine)
```

This is not:

```python
class Car(Engine):
    pass
```

because Car **has an** Engine; a Car **is not an** Engine.

The formal inheritance treatment comes next week.

## 5. Composition

A practical composition example:

```text
Order
  contains
OrderItem
```

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class OrderItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def subtotal(self):
        return self.product.price * self.quantity
```

Then:

```python
class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def total(self):
        return sum(
            item.subtotal()
            for item in self.items
        )
```

The objects collaborate:

```text
Order
  │ contains
  ▼
OrderItem
  │ refers to
  ▼
Product
```

## 6. Collaboration and responsibility

Ask:

> Who should calculate an OrderItem subtotal?

A useful answer is OrderItem, because it knows the Product and quantity.

Then:

> Who should calculate the whole Order total?

A useful answer is Order, because it owns the collection of OrderItems.

## 7. Has-a vs is-a preview

Use only this distinction:

```text
has-a
→ whole/component or object relationship

is-a
→ general/specialized class relationship
```

Examples:

```text
Car has-a Engine
Order has-a OrderItem
Appointment has-a Patient reference

Doctor is-a Person
```

Do not implement inheritance deeply this week. That is Week 6.

## Main exercise — Library Loan

Model:

```text
Member
Book
Loan
```

A Loan should refer to one Member object and one Book object.

```python
class Loan:
    def __init__(self, member, book):
        self.member = member
        self.book = book
```

Add a simple `display_info()` method that reads information from the related objects.

Then explain which object is the Client, which objects act as Suppliers, and which relationships are has-a/reference relationships.

## Challenge — Student / Course / Enrollment

Requirement:

> A Student enrolls in a Course. Enrollment stores the relationship between one Student and one Course.

Model:

```text
Student
   ▲
   │
Enrollment
   │
   ▼
Course
```

Create two students, two courses, and multiple Enrollment objects.

Do not use inheritance.

## Reflection

Answer:

> Why is Car has Engine usually a better model than Car inherits Engine?

## Reading

### Inggriani Liem

Focus on:

- hubungan antar kelas;
- Client–Supplier;
- Client using Supplier services;
- has / is-a / is-implemented-using distinction;
- the Car–Engine/Wheel example.

### OpenStax

Preview **13.1 Inheritance Basics** only to reinforce the distinction between a general/specialized **is-a** relationship and the object relationships studied this week.

## Week 5 package

- [Colab notebook](05_object_relationships.ipynb)
- [Exercises](exercises.md)
- [Quiz](quiz.md)
- [Assignment](assignment.md)
- [Instructor notes](instructor-notes.md)

## Next week

Week 5:

```text
Order has OrderItem
Car has Engine
Appointment uses Patient/Doctor
```

Week 6 asks:

> What if one class really is a more specialized kind of another class?

That leads directly to:

**Week 6 — Inheritance.**
