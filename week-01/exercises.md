# Week 1 Exercises — Thinking in Objects

These exercises focus on **object-oriented thinking**, not detailed Python syntax.

## Exercise 1 — Identify Identity, State, and Behavior

Consider a university student registration system.

A student has a student ID, name, and email address. A student can register for a course and cancel a registration.

For the `Student` concept, identify:

1. possible identity;
2. possible state;
3. possible behavior.

Write your answer in this form:

```text
Object:
Identity:
State:
Behavior:
```

---

## Exercise 2 — Candidate Objects

Requirement:

> A restaurant receives customer orders. An order contains menu items. A customer can place an order. The kitchen prepares the order, and the order has a status.

Identify candidate objects.

For each candidate object, write:

- why it deserves to be modelled as an object;
- possible state;
- possible behavior.

Then identify nouns that **do not necessarily need to become classes**.

---

## Exercise 3 — Class or Object?

For each item below, decide whether it is best interpreted as a **class**, an **object/instance**, or neither in the given context.

1. `Patient`
2. `patient_budi`
3. `Doctor`
4. `doctor_andi`
5. `"waiting"`
6. `Appointment`
7. one appointment scheduled for Budi with Dr. Andi at 10:00

Explain your reasoning.

---

## Exercise 4 — State or Behavior?

For a `Book` object, classify each item as likely **state** or **behavior**:

- title
- author
- ISBN
- availability
- borrow
- return
- display information

Then propose one additional state and one additional behavior.

---

## Exercise 5 — Object Collaboration

Requirement:

> A member borrows a book from a library.

Draw a simple text diagram showing collaboration among the objects you identify.

Example style:

```text
Object A
   │ action
   ▼
Object B
```

Then answer:

1. Which object initiates the interaction?
2. Which object owns the book's availability state?
3. Which object should change that availability state?

There may be more than one reasonable model. Explain your choice.

---

## Exercise 6 — Do Not Turn Every Noun into a Class

Requirement:

> An appointment has a patient, doctor, time, and status.

For each of the following, decide whether you would model it as a separate class **in a simple first version**:

- Patient
- Doctor
- Appointment
- Time
- Status

Explain why.

The goal is not to find one universal answer. The goal is to justify modelling decisions.

---

## Exercise 7 — Procedural vs Object-Oriented Organization

Suppose a program stores:

```python
patient_names = []
patient_phones = []
patient_birth_years = []
```

and uses several functions that receive indexes into those lists.

Discuss:

1. What risks appear as the system grows?
2. What information belongs together?
3. How might an object-oriented model organize the same concept?

Do **not** rewrite the whole program yet.

---

## Challenge — University Course Registration

Requirement:

> Students enroll in courses. A course has a code, name, and capacity. A lecturer teaches a course. An enrollment records the relationship between a student and a course.

Identify at least **five candidate objects or concepts**.

For each candidate, write:

```text
Name:
Identity:
State:
Behavior:
Relationships:
```

Finally answer:

> Why might `Enrollment` deserve to become an object instead of simply storing courses in a list inside `Student`?
