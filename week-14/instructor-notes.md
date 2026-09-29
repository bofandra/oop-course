# Week 14 Instructor Notes — OOA, OOD, OOP & OOT

## Teaching goal

Weeks 1–13 mostly taught object-oriented concepts one topic at a time.

Week 14 integrates them into a development workflow:

```text
Requirement
   ↓
OOA
   ↓
OOD
   ↓
OOP
   ↓
OOT
```

The most important skill is resisting the urge to code immediately.

## Source alignment

### Inggriani Liem

This week is grounded primarily in the Diktat.

Use the source framing that:

- OOA analyses the problem using an object-oriented methodology;
- a central analysis product is the class diagram with class relationships/associations;
- OOD creates the detailed design / overall solution scheme;
- OOP implements the classes in a chosen language;
- OOT first tests independent classes, then classes with relationships, then the entire system.

The Diktat mentions additional diagrams for dynamics and user interaction. For this course, keep Week 14 to a minimal class diagram because formal sequence/dynamic-diagram teaching is outside the agreed scope.

### OpenStax

Use OpenStax only as implementation support for Python concepts already taught.

Do not present the OOA/OOD/OOP/OOT lifecycle as coming from OpenStax.

## Recommended 200-minute flow

| Time | Activity |
|---|---|
| 08:30–08:45 | Review Week 13 contracts |
| 08:45–09:10 | Requirement → OOA |
| 09:10–09:35 | Candidate classes / responsibilities |
| 09:35–10:00 | Minimal class diagram |
| 10:00–10:10 | Break |
| 10:10–10:35 | OOD: interfaces, references, contracts |
| 10:35–10:55 | OOP implementation |
| 10:55–11:20 | OOT: independent + collaboration tests |
| 11:20–11:40 | University Registration lab |
| 11:40–11:50 | Quiz / Week 15 bridge |

## Opening exercise

Show this requirement only:

> A clinic has patients and doctors. A patient can have an appointment with a doctor. An appointment has a scheduled time and status. An appointment can be confirmed or cancelled.

Ask students not to code.

First ask:

```text
What concepts have identity?
What state belongs to each?
What behavior belongs to each?
What relationships exist?
```

Then introduce OOA.

## Candidate objects

A reasonable Clinic analysis gives:

```text
Patient
Doctor
Appointment
```

But emphasize:

> Candidate identification is reasoning, not noun extraction.

Not every noun must become a class.

## Minimal class diagram

Use only enough notation to expose:

- class name;
- key attributes;
- key methods;
- relationship arrows/labels.

Do not spend the session teaching UML notation rules.

## OOA vs OOD

Use a comparison:

```text
OOA
What are the important domain concepts?
What responsibilities and relationships exist?

OOD
How exactly will the solution classes expose behavior?
What state is internal?
What constructor parameters and contracts are needed?
```

Avoid presenting a rigid universal boundary; the source describes lifecycle stages at a high level.

## OOP

Only after the model is visible should students write Python.

Reuse familiar techniques:

- `__init__()`;
- object references;
- encapsulation;
- exceptions;
- simple contracts.

No new Python feature is required.

## OOT

Follow the Diktat progression explicitly:

```text
1. test independent class
2. test related classes
3. test the system scenario
```

Use plain `assert` statements so testing does not turn into a pytest lesson.

### Independent

```python
student = Student('S001', 'Alya')
assert student.name == 'Alya'
```

### Collaboration

```python
enrollment = Enrollment(student, course)
assert enrollment.student is student
assert enrollment.course is course
```

### End-to-end

Test one complete registration journey.

## Contracts from Week 13

Bring forward the existing concepts:

```text
precondition
postcondition
invariant
```

Example:

```text
Course invariant:
0 <= active_enrollment_count <= capacity
```

Do not add a full formal Design-by-Contract framework.

## Common misconceptions

### 1. OOA means writing classes in Python

No. OOA is problem analysis.

### 2. A class diagram is the whole design

No. OOD includes interface, responsibility, state, and contract decisions.

### 3. Passing isolated tests proves the system works

No. Collaborations and an end-to-end scenario also need testing.

### 4. Every noun becomes a class

No. Candidate objects require modelling judgment.

### 5. Testing means pytest

No. Plain assertions are sufficient for this week's learning objective.

## Quiz administration

The quiz answer key is intentionally not stored in the public repository. Keep the instructor key in a private lecturer-controlled location.

## Assignment grading notes

Reward traceability:

```text
requirement
→ analysis decision
→ design decision
→ code
→ test
```

A simple coherent solution should score better than an elaborate system with unclear responsibilities.

Do not reward frameworks, databases, UML complexity, or testing libraries.

## What not to teach yet

Avoid:

- sequence diagrams;
- formal UML multiplicity rules;
- SOLID;
- repository pattern;
- dependency injection;
- pytest fixtures/mocking;
- advanced architecture;
- extensive refactoring theory.

## Closing question

End with:

> Once we have a working OO solution, can we reuse not only code but also proven design ideas?

That leads directly to:

**Week 15 — Reusability, Design Patterns & OOP Case Study.**