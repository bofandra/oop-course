# Module 5 Instructor Notes — Object Relationships

## Teaching goal

Students can now design one object reasonably well. Module 5 changes the scale:

```text
one object
   ↓
multiple collaborating objects
```

The most important distinction is:

```text
has-a / uses
≠
is-a
```

## Source alignment

### Inggriani Liem

Use the Diktat directly:

- relationships among classes include Client–Supplier and inheritance;
- in Client–Supplier, the Client uses services of the Supplier;
- a Supplier entity may appear as an attribute, formal routine argument, or function result;
- has-a represents a whole/component relationship;
- the Diktat explicitly uses Car–Engine/Wheel and warns against treating has-a as inheritance;
- is-a is the inheritance relationship and is only previewed this module.

### OpenStax

Use 13.1 only as a preview of inheritance terminology so students can contrast `is-a` with the object relationships being studied.

## Suggested session flow

| Approx. duration | Activity |
|---|---|
| 15 min | Review: one object owns state/behavior |
| 30 min | Objects referencing other objects |
| 25 min | Client–Supplier |
| 20 min | has-a vs is-a |
| 10 min | Break |
| 25 min | Car–Engine and whole/component modelling |
| 25 min | Order / OrderItem / Product composition |
| 35 min | Library Loan lab |
| 10 min | Enrollment challenge |
| 5 min | Bridge to inheritance |

## Opening demonstration

First show duplicated text:

```python
class Appointment:
    def __init__(self, patient_name, doctor_name):
        self.patient_name = patient_name
        self.doctor_name = doctor_name
```

Then replace it with object references:

```python
class Appointment:
    def __init__(self, patient, doctor):
        self.patient = patient
        self.doctor = doctor
```

Ask:

> Are Patient and Doctor now copied into Appointment?

Expected answer: no. Appointment holds references to those objects.

Do not go deep into reference identity or aliasing; Module 11 covers runtime reference semantics in depth.

## Client–Supplier

Use a simple supplier such as NotificationService.

Keep the terminology faithful to the Diktat:

```text
Client
requests/uses a service
        ↓
Supplier
provides that service
```

Do not relabel the topic as dependency injection or architecture patterns.

## Has-a vs is-a

Use the Diktat's Car–Engine example.

Ask students to complete:

```text
A Car ______ an Engine.
A Doctor ______ a Person.
```

Expected:

```text
Car has an Engine.
Doctor is a Person.
```

Then state:

> If the natural sentence is "has a", inheritance is probably not the relationship you are looking for.

Treat this as a useful heuristic, not a formal proof.

## Composition example

Use Product → OrderItem → Order.

The teaching value is responsibility:

- Product knows its own product data;
- OrderItem knows Product + quantity and can calculate subtotal;
- Order knows its items and can calculate the whole total.

This revisits Module 3 responsibility in a multi-object setting.

## Common misconceptions

### 1. Every relationship should use inheritance

Counterexample: Car–Engine.

### 2. Storing an object means copying it

Clarify that the attribute refers to the object.

### 3. One giant class is easier

Show how Product, OrderItem, and Order have different responsibilities.

### 4. Any association is automatically composition

For this course, use composition mainly as a practical whole/part modelling idea. Do not teach full UML aggregation/composition lifecycle semantics because the source material does not provide that level of detail.

## Quiz administration

The quiz answer key is intentionally not stored in the public repository. Keep the instructor key in a private instructor-controlled location.

## Assignment grading notes

Reward clear relationships and object responsibilities.

Do not require inheritance, UML multiplicity, repositories, dependency injection, or domain-driven design terminology.

## What not to teach yet

Avoid:

- inheritance implementation;
- `super()`;
- overriding;
- polymorphism;
- formal UML association/composition notation;
- Repository pattern;
- dependency injection terminology.

## Closing question

End with:

> We now know that Car **has an** Engine. But what if Doctor really **is a** Person?

That leads directly to:

**Module 6 — Inheritance.**
