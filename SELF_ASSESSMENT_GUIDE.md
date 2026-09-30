# Self-Assessment Guide

This guide helps independent learners decide whether they understand a module well enough to continue.

## Evidence ladder

For each module, aim to reach all four levels:

1. **Recognize** — identify the concept when you see it.
2. **Explain** — describe it in your own words.
3. **Apply** — use it in a new example without step-by-step copying.
4. **Defend** — explain why your design choice is appropriate and what alternative you rejected.

## Module mastery checkpoints

| Module | You are ready to move on when you can... |
|---:|---|
| 0 | write small Python functions, conditions, loops, and collection operations without step-by-step help |
| 1 | identify meaningful objects and explain identity, state, behavior, and collaboration |
| 2 | define classes, create instances, and explain `__init__`, `self`, and instance state |
| 3 | assign responsibilities and implement behavior that changes valid object state |
| 4 | explain and demonstrate why state should be protected behind meaningful operations |
| 5 | distinguish is-a from has-a/reference relationships and model collaborating objects |
| 6 | use inheritance only when the subtype relationship is meaningful |
| 7 | demonstrate overriding, polymorphism, and runtime method selection without type-based branching |
| 8 | integrate Modules 1–7 in one coherent solution and explain your design |
| 9 | use abstract/deferred behavior to express a meaningful common contract |
| 10 | explain multiple inheritance, method resolution, and when a focused mixin is justified |
| 11 | predict aliasing, mutation, reassignment, identity, and object-lifecycle behavior |
| 12 | implement useful special methods and organize related classes into modules |
| 13 | protect object rules using exceptions, assertions, preconditions, postconditions, and invariants |
| 14 | move from requirement → OOA → OOD → implementation → tests and explain the trace |
| 15 | identify a real variation/reuse problem and apply a small reusable design without overengineering |
| 16 | build, test, demonstrate, and defend a complete object-oriented solution |

## Worked self-check feedback

Use [Mastery Checks](MASTERY_CHECKS.md) after you have attempted a module's examples/exercises. The prompts are intentionally different from the public quizzes and include collapsible worked feedback so independent learners can verify reasoning without exposing facilitator assessment keys.

Recommended order:

```text
module study
→ exercises
→ quiz attempt
→ mastery check
→ open worked feedback
→ rerun/modify an example if needed
→ retry uncertain ideas
```

## Quiz review protocol

After attempting a module quiz:

1. label each answer **certain**, **uncertain**, or **guess**;
2. revisit the module section connected to every uncertain/guess answer;
3. verify code-related ideas by running or modifying an executable example;
4. write a one- or two-sentence explanation in your own words;
5. reattempt those items later without looking at your notes.

Do not count a lucky guess as mastery.

## Coding review protocol

Ask whether each class has a clear responsibility, objects own the state they should protect, relationships are explicit, inheritance represents a real is-a relationship, polymorphism replaces inappropriate type branching, invalid operations preserve valid state, and important behavior is testable.

## Reflection prompt

```text
I can now...
I was confused about...
The design decision I can now explain is...
```

## Assessment integrity

The repository does not publish direct keys for assessment material that may also be reused in facilitated cohorts. For self-paced learning, feedback comes from executable examples, module outcomes, exercises, rubrics, [Mastery Checks](MASTERY_CHECKS.md), mastery checkpoints, and repeated attempts.
