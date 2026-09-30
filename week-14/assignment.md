# Module 14 Assignment — University Registration from Requirement to Test

## Objective

Produce a complete object-oriented solution using the Module 14 lifecycle:

```text
Requirement → OOA → OOD → OOP → OOT
```

## Requirement

> A university has Students and Courses. A Student can enroll in a Course through an Enrollment. Each Course has a maximum capacity. An Enrollment has an active or cancelled status. A new Enrollment may be created only while the Course has available capacity.

## Part 1 — OOA

Identify candidate classes.

For each candidate, document:

- state;
- behavior;
- responsibility.

Do not start with Python code.

## Part 2 — Class Diagram

Create a minimal class diagram showing:

- classes;
- important state;
- important behavior;
- relationships.

A clear text diagram is acceptable.

## Part 3 — OOD

For every class, define:

- constructor inputs;
- public interface;
- internal state, if any;
- object references;
- at least one relevant contract rule.

At minimum, include a capacity rule for Course/Enrollment.

## Part 4 — OOP

Implement the model in Python.

A reasonable solution is expected to include Student, Course, and Enrollment, but an alternative coherent model is acceptable.

Keep the implementation in memory only.

## Part 5 — OOT

Write plain Python `assert` tests for:

1. Student independently;
2. Course independently;
3. Enrollment references;
4. successful enrollment;
5. capacity limit;
6. cancellation;
7. one end-to-end registration scenario.

No pytest is required. The plain `assert` statements are test checks, not the application's business-rule enforcement. Run the tests without Python optimization (`-O`).

## Required explanation

Answer:

1. What did you discover during OOA?
2. Which decisions belong to OOD?
3. Which relationships appear in the class diagram?
4. What class invariant or precondition did you use?
5. Which tests are independent-class tests?
6. Which tests verify collaboration?
7. What does the end-to-end test prove that an isolated class test does not?

## Rubric

| Criterion | Weight |
|---|---:|
| OOA: candidate classes, state, behavior, responsibilities | 20% |
| Class diagram / relationships | 15% |
| OOD: interfaces, references, contracts | 20% |
| Python implementation | 20% |
| OOT: independent + collaboration + end-to-end tests | 20% |
| Explanation / reasoning | 5% |
| **Total** | **100%** |

## Scope

Do not add:

- database;
- web framework;
- GUI;
- REST API;
- pytest;
- repository pattern;
- sequence diagrams;
- advanced architecture patterns.

The goal is to practice the full object-oriented development lifecycle from the Diktat.