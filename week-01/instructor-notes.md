# Week 1 Instructor Notes — Introduction to OOP & Thinking in Objects

## Teaching goal

The central outcome is **not** that students can write a Python class.

The central outcome is that students can look at a small problem and reason in terms of:

```text
Object
├── Identity
├── State
└── Behavior
```

and recognize that objects collaborate with other objects.

## Source alignment

### Inggriani Liem

Use the introductory sections that frame an OO system as components that encapsulate data and functions, and that distinguish the static definition of a class from runtime objects. Also emphasize that objects have state/behavior and interact with other objects.

Do not introduce later concepts such as inheritance, genericity, assertions, or design patterns in detail during Week 1.

### OpenStax

Use **11.1 Object-Oriented Programming Basics** as the Python-facing introductory reading.

The Python syntax shown in class should remain minimal. Detailed `__init__`, `self`, and instance attributes belong to Week 2.

## Recommended 200-minute flow

| Time | Activity |
|---|---|
| 08:30–08:45 | Opening question: how would we represent a clinic appointment? |
| 08:45–09:10 | Procedural organization vs object-oriented organization |
| 09:10–09:40 | Object: identity, state, behavior |
| 09:40–10:00 | Class vs object/instance |
| 10:00–10:10 | Break |
| 10:10–10:35 | Candidate objects from requirements |
| 10:35–10:55 | Object collaboration |
| 10:55–11:25 | Library exercise |
| 11:25–11:40 | Challenge discussion |
| 11:40–11:50 | Reflection + bridge to Week 2 |

## Opening script

Start from data, not syntax:

```python
patient_name = "Budi"
doctor_name = "Andi"
appointment_time = "10:00"
```

Ask:

- What if we have 1,000 patients?
- What data belongs together?
- What concepts have their own state?
- What actions belong to those concepts?

Avoid saying procedural programming is inherently bad. The intended contrast is **organization as complexity grows**.

## Core explanation

A useful introductory sentence:

> An object represents something we want to keep track of during program execution. It has its own identity, state, and behavior.

Use:

```text
Appointment

Identity
- this specific appointment

State
- patient
- doctor
- time
- status

Behavior
- confirm
- cancel
- reschedule
```

Then ask students to produce equivalent examples for `Book`, `Student`, or `Order`.

## Class vs instance

Use only:

```python
class Patient:
    pass

patient_1 = Patient()
patient_2 = Patient()
```

Teaching interpretation:

```text
Patient   → class
patient_1 → object/instance
patient_2 → object/instance
```

Python nuance: classes themselves are also objects in Python, but this is **not necessary** for the Week 1 mental model.

## Important misconception: every noun becomes a class

Use the requirement:

> An appointment has a patient, doctor, time, and status.

Likely first model:

```text
Patient      → candidate class
Doctor       → candidate class
Appointment  → candidate class
time         → attribute/value
status       → attribute/value
```

Emphasize that this is a modelling decision, not a mechanical grammar rule.

## Object collaboration

Use:

```text
Patient
   │ books
   ▼
Appointment
   │ assigned to
   ▼
Doctor
```

Ask:

> Which object owns the appointment status?

This prepares students for responsibility and encapsulation later without formally teaching those topics yet.

## Notebook facilitation

For `01_thinking_in_objects.ipynb`:

1. run the procedural example;
2. ask students to identify what data belongs together;
3. run the minimal class example;
4. do not dwell on `__init__` and `self`;
5. spend most lab time on the Library exercise and Challenge;
6. require students to explain answers verbally or in comments.

## Quiz answer key

1. **B**
2. **B**
3. **C**
4. **D**
5. **B / False**
6. Expected: class = general definition; object/instance = a particular runtime instance of that class.
7. Accept any internally consistent example.
8. Typical candidates: Customer, Order, Product / OrderItem. Relationship explanation is more important than exact names.
9. Expected themes: grouping related state and behavior, clearer ownership/responsibility, easier reasoning as complexity grows, collaboration among objects.
10. **1 class, 2 Patient instances.**

## Assignment grading notes

Do not grade students down merely because their object model differs from the lecturer's model.

Grade the **reasoning**:

- Does the object have meaningful identity/state/behavior?
- Are attributes being unnecessarily promoted into classes?
- Are relationships understandable?
- Can the student explain the modelling decision?

A simpler well-justified model is preferable to a complicated model containing many artificial classes.

## What not to teach yet

Avoid detailed coverage of:

- `self` mechanics;
- constructor semantics;
- class vs instance attributes;
- visibility;
- encapsulation;
- inheritance;
- polymorphism;
- abstract classes;
- UML notation.

Those topics have dedicated weeks.

## Closing question

End with:

> If `Patient` is a class, how do we create many patient objects that each hold different state?

That question creates the transition to:

**Week 2 — Classes, Objects & Instances.**
