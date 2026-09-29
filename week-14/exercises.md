# Week 14 Exercises — OOA, OOD, OOP & OOT

## Exercise 1 — Requirement to Candidate Objects

Requirement:

> A library has members and books. Members borrow books through loans. Each loan has a borrow date and return status.

Identify candidate classes.

For each candidate, write:

- identity/state;
- behavior;
- responsibility.

---

## Exercise 2 — Candidate or Just an Attribute?

For the library requirement, decide whether each concept should probably be a class or merely an attribute/value:

1. Member
2. Book
3. Loan
4. borrow date
5. member name
6. return status

Explain the reasoning. Do not use a mechanical rule such as 'every noun becomes a class'.

---

## Exercise 3 — Minimal Class Diagram

Draw a simple class diagram for:

```text
Student
Course
Enrollment
```

Show:

- main attributes;
- main methods;
- which objects reference which other objects.

Formal UML multiplicity notation is optional.

---

## Exercise 4 — OOA vs OOD

Classify each decision as primarily **analysis** or **design**:

1. discovering that Enrollment is an important domain concept;
2. deciding that Enrollment stores `_status` internally;
3. identifying Student and Course from the requirement;
4. deciding the constructor parameters;
5. identifying that Enrollment connects Student and Course;
6. deciding to expose a read-only `status` property.

Explain each answer.

---

## Exercise 5 — Contract Design

For a Course with capacity, write:

- one invariant;
- one precondition for enrollment;
- one postcondition after successful enrollment.

Keep the contract language simple.

---

## Exercise 6 — Test Independent Classes

For `Student` and `Course`, write plain Python `assert` statements that test their independent state.

Do not test collaboration yet.

---

## Exercise 7 — Test Collaboration

Create one Student, one Course, and one Enrollment.

Test that:

- Enrollment refers to the correct Student;
- Enrollment refers to the correct Course;
- the initial Enrollment status is correct.

---

## Exercise 8 — End-to-End Scenario

Write one complete scenario:

```text
create Student
→ create Course
→ enroll
→ verify Course/Enrollment state
→ cancel Enrollment
→ verify final state
```

Use plain `assert` statements.

---

## Challenge — Find the Missing Responsibility

Suppose all registration logic is written in a single `main()` function.

Explain which responsibilities should probably move into Student, Course, or Enrollment classes and why.