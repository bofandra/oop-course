# Final Project Instructor Notes

## Assessment intent

The final project assesses integration, not feature count.

The student should demonstrate the complete reasoning chain:

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
Explanation / ownership
```

## Source alignment

The course lifecycle follows the Diktat framing:

- OOA analyses the problem and produces object-oriented models such as a class diagram;
- OOD develops the detailed solution design;
- OOP implements classes in a programming language;
- OOT tests independent classes, then related classes, then the full system.

The final project should therefore reward traceability from requirement to analysis, design, code, and tests.

## Do not publish a reference solution

The repository is public.

Do not commit a complete executable solution or answer key to the public `main` branch before assessment.

If a reference implementation is needed for grading consistency, keep it in a private lecturer-controlled location.

## Internal model possibilities

Do not give this list to students as the answer.

A reasonable internal model may include concepts similar to:

```text
person/learner/teaching-staff concepts
course
enrollment
assignment variants
submission
```

Equivalent designs are acceptable if responsibilities and relationships are coherent.

## Key evidence to look for

### Analysis

Can the student explain why each major class exists?

### Relationships

Can the student distinguish:

```text
is-a
from
has-a / references
```

### Polymorphism

The assignment/scoring variation should produce a real polymorphic call.

Prefer evidence like:

```python
assignment.calculate_score(...)
```

where different runtime assignment objects supply different implementations.

Do not reward:

```python
if assignment_type == ...:
    ...
elif assignment_type == ...:
    ...
```

as the required polymorphism evidence.

### Contracts

Look for meaningful rules such as:

- capacity cannot be exceeded;
- duplicate invalid enrollment is rejected;
- scoring remains within the assignment's allowed range;
- a submission cannot be graded in an impossible state.

Exact rules may vary with the student's model.

### Tests

Follow the Diktat-inspired progression:

```text
independent classes
→ collaborating classes
→ whole scenario
```

Plain asserts are sufficient.

## Final Project vs Demo component

The repository's detailed project rubric produces the score for the **Final Project (35%)** course component.

The **Demo / Code Explanation / Participation (10%)** course component is separate.

Use the viva to evaluate ownership, explanation, responsiveness to questions, and ability to make a small change.

## Optional concepts

Students may use:

- abstract classes;
- multiple inheritance/mixins;
- operator overloading;
- genericity concepts;
- simple design patterns.

Do not require all of them.

Optional techniques should improve the design. Do not award marks simply for inserting them.

## Common failure modes

### 1. Framework-heavy, OOP-light submission

A web/database layer does not compensate for weak object modelling.

### 2. Type branching instead of polymorphism

If all variation is handled through `if/elif`, the inheritance/polymorphism objective is not met.

### 3. Data-only classes

Classes containing only attributes with all behavior in one controller/main function demonstrate weak responsibility allocation.

### 4. Direct mutation of another object's internal state

Deduct encapsulation/responsibility marks where appropriate.

### 5. No invalid-state protection

If capacity, grading, or lifecycle rules can be violated silently, contract/exception marks should be reduced.

### 6. Tests only print output

Printing is not the same as verification. Require executable assertions.

### 7. Pattern inflation

Do not reward unnecessary pattern layers.

## Grading consistency

When two designs differ, grade against:

- requirement satisfaction;
- object responsibility;
- semantic relationships;
- valid state;
- polymorphic behavior;
- contract handling;
- executable tests;
- explanation.

Do not grade against one hidden reference class structure.

## Closing the course

The final course question is:

> Can the student think in objects, design collaborations, implement behavior, protect object validity, test the solution, and explain the reasoning?

That is the intended evidence of completing the course.
