# Module 5 — Object Relationships

> **Run the notebook:** [Open Module 5 in Google Colab](https://colab.research.google.com/github/bofandra/oop-course/blob/main/week-05/05_object_relationships.ipynb)

## Learning outcomes

By the end of this module, learners should be able to:

1. explain why useful OO systems are built from **collaborating objects**;
2. explain a **Client–Supplier** relationship;
3. model one object holding a reference to another object;
4. distinguish a general object-reference/association relationship from a whole–part **has-a** relationship;
5. distinguish **has-a** from **is-a** at a conceptual level;
6. use composition-style modelling when one object is meaningfully built from or contains component objects;
7. assign collaboration responsibilities to appropriate objects.

## Source alignment

Inggriani Liem states that relationships among classes include **Client–Supplier** and inheritance. In a Client–Supplier relationship, the Client uses services provided by the Supplier. The Diktat defines a class A as a Client of class B when A contains an entity of type B; that entity may appear as an attribute, a formal routine argument, or a function result.

The Diktat also distinguishes **has-a** from **is-a**. A has-a relationship reflects a whole/component relationship; its example is a Car having an Engine and Wheels. It warns that beginners often incorrectly implement has-a using inheritance.

This module concentrates on Client–Supplier, object references/associations, has-a, composition-style modelling, and collaboration. A stored reference does not automatically imply whole–part composition. Inheritance is introduced formally in Module 6.

## From Module 4 to Module 5

Module 4 focused on one object protecting its own state:

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

Module 5 asks:

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

This is a **reference/association relationship**. Do not automatically call every stored object reference composition: Patient and Doctor have their own identities and lifecycles outside this Appointment.

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

## 4. Reference/association vs has-a whole–part relationship

A class may refer to another object without the second object being one of its components.

For example:

```text
Appointment → Patient
Rental → Customer
```

These are useful object references/associations.

By contrast, the Diktat's classic whole–part example is:

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

The formal inheritance treatment comes next module.

## 5. Composition-style modelling

A practical whole–part example:

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
  │ contains / whole–part
  ▼
OrderItem
  │ refers to / association
  ▼
Product
```

Here, the Order–OrderItem relationship is composition-style whole–part modelling. The OrderItem–Product relationship is a reference to an independently meaningful Product.

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
Appointment refers to Patient
→ reference / association

Car has-a Engine
Order contains OrderItem
→ whole–part / composition-style relationship

Doctor is-a Person
→ inheritance
```

Do not implement inheritance deeply this module. That is Module 6.

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

Then explain which object is the Client, which objects act as Suppliers, and which links are general references/associations rather than whole–part composition.

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

Preview **13.1 Inheritance Basics** only to reinforce the distinction between a general/specialized **is-a** relationship and the object relationships studied this module.

## Module 5 package

- [Colab notebook](05_object_relationships.ipynb)
- [Exercises](exercises.md)
- [Quiz](quiz.md)
- [Assignment](assignment.md)
- [Instructor notes](instructor-notes.md)
- [Mastery checks with worked feedback](../MASTERY_CHECKS.md)

## Next module

Module 5:

```text
Order has OrderItem
Car has Engine
Appointment uses Patient/Doctor
```

Module 6 asks:

> What if one class really is a more specialized kind of another class?

That leads directly to:

**Module 6 — Inheritance.**
