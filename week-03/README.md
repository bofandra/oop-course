# Module 3 — Attributes, Methods, State & Behavior

## Learning outcomes

By the end of this module, learners should be able to:

1. explain that object **state** is represented by attribute values at runtime;
2. define instance methods that read object state;
3. define instance methods that change object state;
4. distinguish state from behavior;
5. place simple behavior on the object that owns the related state;
6. explain how method calls can produce state transitions.

## Source alignment

Inggriani Liem states that a class has attributes and methods/services. Attribute values at runtime represent the **state** of an object, while methods are executable services associated with the object. The Diktat also frames method execution as something requested through interaction/messages between objects.

OpenStax 11.3 provides the Python implementation basis for this module: defining and calling instance methods that work with instance attributes.

This module stays focused on **state and behavior**. Access control, protected internal state, and invariants are introduced in Module 4.

## From Module 2 to Module 3

Module 2:

```text
Class
  ↓
Instance
  ↓
Attributes
  ↓
State
```

Module 3 adds:

```text
State
  +
Methods
  ↓
Behavior
  ↓
State can change over time
```

## 1. Object state

Consider:

```python
class Appointment:
    def __init__(self, patient_name, doctor_name, status):
        self.patient_name = patient_name
        self.doctor_name = doctor_name
        self.status = status
```

Create an object:

```python
appointment = Appointment(
    "Budi",
    "Dr. Andi",
    "waiting"
)
```

The current values of the attributes describe the object's state:

```text
Appointment
- patient_name = Budi
- doctor_name  = Dr. Andi
- status       = waiting
```

## 2. A method can read state

```python
class Appointment:
    def __init__(self, patient_name, doctor_name, status):
        self.patient_name = patient_name
        self.doctor_name = doctor_name
        self.status = status

    def display_info(self):
        print(
            self.patient_name,
            self.doctor_name,
            self.status
        )
```

`display_info()` reads the object's current state but does not change it.

## 3. A method can change state

```python
class Appointment:
    def __init__(self, patient_name, doctor_name):
        self.patient_name = patient_name
        self.doctor_name = doctor_name
        self.status = "waiting"

    def confirm(self):
        self.status = "confirmed"
```

Usage:

```python
appointment = Appointment(
    "Budi",
    "Dr. Andi"
)

print(appointment.status)

appointment.confirm()

print(appointment.status)
```

Conceptually:

```text
waiting
   │
   │ confirm()
   ▼
confirmed
```

## 4. Direct assignment vs meaningful behavior

Python allows:

```python
appointment.status = "confirmed"
```

But compare it with:

```python
appointment.confirm()
```

The second form communicates **what the object is doing**, not merely which attribute happens to change.

At this stage, the key question is:

> What behavior naturally belongs to the object that owns this state?

Module 4 will discuss how an object can also control and protect its internal state.

## 5. State-changing vs read-only behavior

Example:

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def resize(self, width, height):
        self.width = width
        self.height = height
```

Here:

```text
area()
→ reads state

resize()
→ changes state
```

Both are behaviors, but they have different effects.

## 6. Parameters vs object attributes

Consider:

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
```

`amount` is a parameter for one method call.

`self.balance` is part of the object's state.

```text
amount
→ temporary input to deposit()

self.balance
→ state stored by the object
```

## 7. Responsibility

Suppose an Order owns its total and items.

Ask:

> Who should calculate the order total?

A natural candidate is the `Order` object because the behavior depends directly on state that belongs to the order.

This is only a heuristic, not a mechanical rule:

> Behavior closely related to an object's state is a candidate responsibility of that object.

## Live coding — Appointment lifecycle

Build:

```python
class Appointment:
    def __init__(self, patient_name, doctor_name):
        self.patient_name = patient_name
        self.doctor_name = doctor_name
        self.status = "waiting"

    def confirm(self):
        self.status = "confirmed"

    def cancel(self):
        self.status = "cancelled"

    def display_status(self):
        print(self.status)
```

Then trace:

```text
waiting
  ↓ confirm()
confirmed

waiting
  ↓ cancel()
cancelled
```

Do not add validation rules yet. That becomes the bridge to Module 4.

## Main exercise — Book

Create a `Book` class with:

State:

- `title`
- `author`
- `is_available`

Behavior:

- `display_info()`
- `borrow()`
- `return_book()`

Expected state changes:

```text
available
   │ borrow()
   ▼
not available

not available
   │ return_book()
   ▼
available
```

## Challenge

After implementing `borrow()`, try borrowing the same Book object twice.

Ask:

> What prevents the second borrow?

At this stage, probably nothing.

Do not solve it with a large validation framework yet. Keep the question for Module 4:

> Should outside code and object methods be allowed to create any state they want?

## Design exercise — Online Order

Requirement:

> An order contains a customer name, total, and status. It can be confirmed and cancelled. It can also display a summary.

Identify:

- state;
- read-only behavior;
- state-changing behavior.

Then sketch the class interface before coding.

## Reflection

Answer:

> Why is `appointment.confirm()` often more expressive than directly writing `appointment.status = "confirmed"`?

## Reading

### Inggriani Liem

Focus on:

- attributes as runtime object state;
- methods/services associated with a class/object;
- method signature and body at a conceptual level;
- objects performing services through interaction.

### OpenStax

Read **11.3 Instance methods**.

## Module 3 package

- [Colab notebook](03_state_and_behavior.ipynb)
- [Exercises](exercises.md)
- [Quiz](quiz.md)
- [Assignment](assignment.md)
- [Instructor notes](instructor-notes.md)
- [Mastery checks with worked feedback](../MASTERY_CHECKS.md)

## Next module

Module 3 asks:

> What can an object do with its state?

Module 4 asks:

> Who should be allowed to change that state, and how do we keep the object valid?

```text
State + Behavior
      ↓
Encapsulation
      ↓
Abstraction
```
