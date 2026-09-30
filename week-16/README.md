# Module 16 — Final Project / Final Test

> **Run the notebook:** [Open Module 16 planning notebook in Google Colab](https://colab.research.google.com/github/bofandra/oop-course/blob/main/week-16/16_final_project_planning.ipynb)

## Learning outcome

Design, implement, test, demonstrate, and defend a complete object-oriented solution by integrating the full course.

## Course integration

The final project integrates:

```text
Module 1   Thinking in Objects
Module 2   Classes, Objects & Instances
Module 3   State & Behavior
Module 4   Encapsulation & Abstraction
Module 5   Object Relationships
Module 6   Inheritance
Module 7   Overriding, Polymorphism & Dynamic Binding
Module 9   Abstract Classes
Module 10  Multiple Inheritance / Mixins when justified
Module 11  References & Object Identity
Module 12  Operator Overloading / Modules when useful
Module 13  Exceptions, Assertions & Contracts
Module 14  OOA → OOD → OOP → OOT
Module 15  Reusability & Design Patterns when useful
```

Not every optional technique must appear. Learners should use an abstraction only when it improves the model.

## Final workflow

```text
Requirement
  ↓
OOA
  ↓
OOD
  ↓
Class Diagram
  ↓
OOP
  ↓
OOT
  ↓
Demo / Viva
```

## Capstone case

The final assessment uses a **University Learning Management System**.

Learners must analyse the requirement themselves rather than being given a ready-made class list.

The system must support, at minimum:

- university learners and teaching staff;
- courses with capacity;
- enrollment into courses;
- assignments created for courses;
- submissions made for assignments;
- submission status and grading;
- at least two assignment/scoring variants that require meaningful polymorphic behavior;
- invalid operations that must be rejected without corrupting object state.

## Expected evidence

A strong submission should make this trace visible:

```text
Requirement
  ↓
OOA decision
  ↓
OOD decision
  ↓
Python implementation
  ↓
Test evidence
  ↓
Demo explanation
```

Evidence should include:

- candidate classes with clear responsibilities;
- meaningful object relationships, distinguishing general references/associations from whole–part relationships where relevant;
- appropriate state and behavior;
- encapsulation and valid object state;
- inheritance and polymorphism where justified;
- invariants, state-transition/precondition rules, and exception handling;
- executable Python implementation;
- tests for independent and collaborating classes;
- at least one end-to-end scenario;
- ability to explain design decisions.

## Learner materials

- [Final Project brief](../assessments/final-project/README.md)
- [Detailed rubric](../assessments/final-project/final_project_rubric.md)
- [Demo / viva guide](../assessments/final-project/demo-viva-guide.md)
- [Planning notebook](16_final_project_planning.ipynb)
- [Submission checklist](final-project-checklist.md)
- [Mastery checks / project defense prompts](../MASTERY_CHECKS.md)

## Scope

The final project is an **OOP assessment**, not an application-stack assessment.

Not required:

- web UI;
- database;
- REST API;
- GUI;
- authentication system;
- deployment;
- external framework.

An in-memory Python solution is enough.

## Final message

The target is not the largest program.

The target is a solution whose object model, responsibilities, relationships, runtime behavior, contracts, tests, and design decisions can all be explained coherently.

## Course navigation

[← Module 15](../week-15/) · [Course Map](../COURSE_MAP.md) · [Course Home](../README.md)
