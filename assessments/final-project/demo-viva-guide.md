# Final Project Demo / Viva Guide

## Purpose

The demo/viva verifies that the student understands and owns the submitted design.

Recommended duration:

**5–7 minutes per student**

The demo/code-explanation component is evaluated separately according to the course assessment plan.

## Suggested 5–7 minute flow

### 1. Problem & model — about 1 minute

Student explains:

- the problem being solved;
- key responsibilities;
- one important relationship.

### 2. Design walkthrough — about 1–2 minutes

Student shows the class diagram and explains:

- one object-reference relationship;
- one inheritance relationship;
- why the inheritance relationship is semantically appropriate.

### 3. Runtime demonstration — about 2 minutes

Student runs one complete scenario:

```text
create
→ enroll
→ assignment
→ submission
→ grading
→ final state
```

The exact sequence may vary with the design.

### 4. Polymorphism & contract — about 1 minute

Student demonstrates:

- one polymorphic scoring call;
- one invalid operation;
- the resulting exception;
- why object state remains valid.

### 5. Test & question — about 1 minute

Student runs one test and answers one design question.

## Viva question bank

The instructor may ask questions such as:

1. Which class owns this responsibility, and why?
2. Is this relationship inheritance, a general reference/association, or a whole–part composition-style relationship, and why?
3. Why did you *not* use inheritance here?
4. Show where two runtime objects respond differently to the same operation.
5. What is the actual runtime object in this polymorphic call?
6. What is one precondition of this method?
7. What invariant are you protecting, and is there a separate lifecycle/transition precondition?
8. What happens when the operation fails?
9. Which test verifies collaboration rather than an isolated class?
10. If course capacity changes, which class should change?
11. If a new assignment/scoring variant is introduced, what code must change?
12. Which part of your design is reusable?
13. Which abstraction did you deliberately avoid because it was unnecessary?
14. Explain one reference/alias relationship in your runtime model.
15. Make a small change to one rule and update one test.

## Live modification

A small live modification can be used to confirm ownership.

Examples:

- change a capacity;
- add a new scoring variant;
- add one validation rule;
- rename one state;
- add one test assertion.

The modification should be small enough to assess understanding rather than typing speed.

## What not to assess

Do not turn the viva into trivia about:

- Python internals;
- C3 MRO algorithm;
- metaclasses;
- web frameworks;
- databases;
- package deployment;
- advanced testing frameworks.

Keep questions aligned with the course learning outcomes.

## AI-assisted submissions

If AI assistance is permitted by applicable rules, the viva becomes especially important.

The evaluation question remains:

> Can the student explain, modify, and defend the submitted object-oriented solution?

A student should not receive strong ownership/explanation marks merely because the submitted code runs.
