# Final Project / Final Test — University Learning Management System

## Goal

Design, implement, test, demonstrate, and defend a complete object-oriented solution.

The expected workflow is:

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
  ↓
Demo / Viva
```

## Scenario

A university needs a small in-memory learning-management system.

The system must support the following requirements.

### People and courses

The university has learners and teaching staff.

Teaching staff can create courses.

Each course has:

- a course code;
- a title;
- a maximum capacity.

Learners can enroll in a course only while capacity is available.

The system must prevent invalid duplicate/over-capacity enrollment according to the design you choose.

### Assignments

Teaching staff can create assignments for a course.

Each assignment has at least:

- an identifier;
- a title;
- a maximum score;
- a submission deadline or simple due marker.

The system must support at least **two assignment/scoring variants** whose grading behavior is meaningfully different.

The variation must be implemented using inheritance/overriding/polymorphism rather than one long type-based `if/elif` branch.

### Submissions

A learner enrolled in a course may submit work for an assignment in that course.

A submission must track at least:

- who submitted;
- which assignment it belongs to;
- submission status;
- score/grade state.

The system must reject invalid operations, such as grading outside allowed score rules or submitting when the relevant rule is not satisfied.

### Status and grading

The solution must demonstrate meaningful object state changes.

Examples include:

```text
enrollment:
active → cancelled

submission:
draft/submitted → graded
```

Exact status names may vary if the model remains coherent.

## Part A — OOA

Analyse the requirement before coding.

Document:

- candidate objects/classes;
- state;
- behavior;
- responsibilities;
- important relationships.

Do not begin from an instructor-provided class list.

Your analysis choices are part of the assessment.

## Part B — Class diagram

Create a minimal class diagram that makes visible:

- important classes;
- important state;
- important operations;
- inheritance relationships;
- object-reference relationships.

The diagram may be:

- PNG/PDF; or
- clear text/Markdown diagram.

Perfect UML notation is not required.

## Part C — OOD

Refine the analysis into an implementation design.

Document:

- constructor inputs;
- public interface;
- internal state where relevant;
- object references;
- inheritance/polymorphism decisions;
- preconditions;
- postconditions where useful;
- class invariants.

Every major design decision should have a reason.

## Part D — OOP implementation

Implement the system in Python.

The implementation must demonstrate:

- classes and instances;
- state and behavior;
- encapsulation;
- object collaboration;
- inheritance;
- overriding;
- polymorphism;
- exception handling;
- clear module organization where useful.

Use only abstractions that serve the requirement.

## Part E — OOT

Write executable tests using plain Python `assert`.

At minimum, test:

1. independent person-related object state;
2. independent course state;
3. enrollment collaboration;
4. capacity rule;
5. assignment creation;
6. polymorphic scoring behavior;
7. submission lifecycle;
8. invalid operation / exception behavior;
9. grading;
10. one complete end-to-end scenario.

No testing framework is required.

## Required end-to-end scenario

Your program must demonstrate one coherent journey such as:

```text
create teaching staff
      ↓
create course
      ↓
create learner
      ↓
enroll learner
      ↓
create assignment
      ↓
submit work
      ↓
grade submission
      ↓
verify final state
```

The exact design is yours.

## Required deliverables

Submit:

1. `README.md` — analysis and design explanation;
2. class diagram — PNG/PDF or Markdown/text;
3. Python source files;
4. `tests.py` or equivalent executable test file;
5. demo / viva evidence.

The **project artifact** is scored with the 100-point Final Project rubric and contributes **35%** of the course grade. The learner's **demo / code explanation / ownership evidence** is scored separately in the 10% Demo / Code Explanation / Participation component; do not double-count the same artifact quality in both components.

Suggested repository shape:

```text
final-project/
├── README.md
├── class-diagram.png
├── models.py
├── main.py
└── tests.py
```

You may split code differently if the structure is clearer.

## Demo / viva

Each learner should be ready for a **5–7 minute** demonstration and explanation.

You may be asked to:

- trace one object lifecycle;
- explain one relationship;
- explain why inheritance is or is not appropriate;
- show polymorphism at runtime;
- explain one exception/contract rule;
- run one test;
- modify a small part of the code live.

The goal is to show ownership of the design, not memorization.

## AI / external assistance

For self-paced study, document any AI or external assistance you use and make sure you can explain every submitted design decision and line of code. In a facilitated cohort, follow the facilitator's applicable rules for AI and external assistance.

If AI assistance is permitted, students remain responsible for understanding and defending every design decision and every submitted line of code.

## Scope

Do **not** add unrelated complexity.

Not required:

- web framework;
- database;
- REST API;
- GUI;
- authentication;
- cloud deployment;
- repository pattern;
- dependency-injection framework;
- external design-pattern catalogue.

An in-memory Python implementation is sufficient.

## Assessment

See:

- [Detailed rubric](final_project_rubric.md)
- [Demo / viva guide](demo-viva-guide.md)
- [Separate 10% Demo / Code Explanation / Participation rubric](../demo-participation-rubric.md)

The final project contributes **35%** of the course grade according to the course assessment plan.
