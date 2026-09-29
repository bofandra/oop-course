# Week 15 Instructor Notes — Reusability, Patterns & Case Study

## Teaching goal

Week 14 taught students to build a coherent OO solution.

Week 15 adds one question:

> Which parts of a proven design idea can be reused when a similar problem appears again?

The learning progression is:

```text
working OO design
      ↓
identify recurring problem
      ↓
reuse design idea
      ↓
pattern terminology
      ↓
evaluate trade-off
```

## Source alignment

### Inggriani Liem

Use the Diktat for these claims:

- class library and design pattern are mechanisms for reusability;
- OO reuse can happen beyond code, at the design level;
- patterns are larger building blocks than individual classes/objects;
- patterns are common solutions to problems in specific contexts;
- the pattern appendix lists names including Strategy and Factory Method.

Do not imply that the Diktat provides the exact Python implementations used this week.

### Python examples

The Strategy-style and Factory Method-style examples are course illustrations built from previously studied concepts:

- composition / Client–Supplier;
- inheritance;
- abstract classes;
- overriding;
- polymorphism;
- dynamic binding.

Do not introduce an external design-pattern catalogue as a third formal course reference.

## Recommended 200-minute flow

| Time | Activity |
|---|---|
| 08:30–08:45 | Review Week 14 complete-design flow |
| 08:45–09:05 | Code reuse vs design reuse |
| 09:05–09:25 | Pattern concept from Diktat |
| 09:25–10:00 | Strategy-style delivery refactor |
| 10:00–10:10 | Break |
| 10:10–10:35 | Factory Method-style creation example |
| 10:35–11:10 | Food Ordering case study |
| 11:10–11:30 | OOT / refactoring comparison |
| 11:30–11:40 | Pattern-or-overengineering discussion |
| 11:40–11:50 | Quiz / Final Project bridge |

## Opening question

Ask:

> We already know how to reuse a class. Can we also reuse a proven arrangement of responsibilities and collaborations?

Then show the Diktat distinction between class-library/code reuse and design-pattern/design reuse.

## Pattern definition

Use the course wording:

> A pattern is a named, reusable design idea for a recurring problem in a particular context.

Immediately add:

> A pattern is not automatically the best solution.

The problem comes first.

## Strategy-style example

Start with a working branch:

```python
if mode == 'pickup':
    ...
elif mode == 'standard':
    ...
elif mode == 'express':
    ...
```

Do not call it bad code immediately.

Ask:

> What changes when new delivery calculations are added?

Only after students identify the variation should you refactor to strategy objects.

Emphasize:

```text
stable responsibility:
Order asks for a fee

varying responsibility:
how fee is calculated
```

## Factory Method-style example

The course example intentionally stays small.

Use:

```text
NotificationCreator
├── EmailNotificationCreator
└── SMSNotificationCreator
```

with a creator method:

```python
create_notification()
```

The teaching point is the shift of object-creation responsibility.

Do not spend time on GoF taxonomy details, pattern participants terminology, or pattern variations.

## Important source nuance

Say explicitly:

> The Diktat gives us the reuse/pattern concept and pattern names. This Python implementation is our course illustration of those ideas.

This keeps the formal-source boundary clear.

## Case study

Use Food Ordering:

```text
Customer <──────────── Order
                       │
                       ├── contains ──> OrderItem ── references ──> MenuItem
                       ├── uses ──────> Delivery strategy
                       └── can use ───> Notification creator
```

Do not force both patterns into every student model if the student can explain a simpler coherent alternative under a different assumption.

## Pattern-or-overengineering discussion

Present two solutions:

```text
simple if/elif
vs
separate strategy objects
```

Ask which is more appropriate when:

- there is one fixed delivery rule;
- there are many changing delivery rules.

The correct lesson is contextual judgment, not 'patterns are always better'.

## Common misconceptions

### 1. Pattern = reusable code snippet

No. The emphasis is reusable design structure/idea.

### 2. More patterns means better design

No.

### 3. Strategy requires a long inheritance hierarchy

No. The essential idea here is interchangeable behavior objects with a common operation.

### 4. Factory Method means any function named factory

No. In this course example, creation is represented as a method whose concrete creator subclass determines the product object.

### 5. Patterns replace OOA/OOD

No. Analysis/design should reveal the problem before choosing a pattern.

## Quiz administration

The quiz answer key is intentionally not stored in the public repository. Keep the instructor key in a private lecturer-controlled location.

## Assignment grading notes

Reward reasoning before pattern syntax.

A student who builds many classes but cannot explain the variation/problem should not receive full pattern-design marks.

A simpler alternative can still earn strong modelling marks if it satisfies the requirement and the student accurately explains why a pattern was unnecessary under their assumptions.

## What not to teach

Avoid:

- all 23 GoF patterns;
- SOLID as a new framework;
- dependency inversion/injection theory;
- repository pattern;
- event bus architecture;
- extensive refactoring/code-smell catalogues;
- framework-specific factories.

## Closing question

End with:

> Can you now receive a new requirement, design an OO model, choose only the abstractions that help, implement it, test it, and explain every decision?

That leads directly to:

**Week 16 — Final Project / Final Test.**