# Release Notes — v1.0.0 Candidate

## Object Oriented Programming — Open Course

This release candidate represents the first fully audited public baseline of the self-paced course.

## What is included

- Module 0 Python prerequisite/readiness path;
- Modules 1–16 covering object-oriented thinking using Python;
- executable Google Colab notebooks;
- exercises, concept quizzes, coding assignments, and mastery checks;
- Mid-Course Assessment integrating Modules 1–7;
- Final Project integrating OOA, OOD, OOP, OOT, contracts, polymorphism, and testing;
- self-paced learner guidance and progress tracking;
- instructor/facilitator guidance and optional grading tools;
- accessibility, citation, licensing, and reproducibility documentation;
- automated repository validation through GitHub Actions.

## Learning progression

```text
Python readiness
→ objects and classes
→ state and behavior
→ encapsulation
→ object relationships
→ inheritance
→ overriding / polymorphism
→ advanced object concepts
→ exceptions and contracts
→ OOA / OOD / OOP / OOT
→ reusability and patterns
→ complete final project
```

## Course design principles

The course is intentionally:

- self-paced and independent of a fixed institutional calendar;
- focused on object-oriented reasoning rather than framework development;
- executable in Google Colab without mandatory local setup;
- aligned to exactly two formal references;
- guarded against assessing concepts before they are taught;
- designed so optional advanced mechanisms do not become hidden final-project requirements.

## Formal references

1. Inggriani Liem, *Diktat Kuliah Pemrograman Berorientasi Objek*, 2003.
2. OpenStax, *Introduction to Python Programming*, 2024.

See [READING_GUIDE.md](READING_GUIDE.md), [REFERENCE_MAP.md](REFERENCE_MAP.md), and [SOURCE_BOUNDARY.md](SOURCE_BOUNDARY.md).

## Validation

The repository validator checks the public course package end-to-end, including:

- required Module 0–16 structure;
- notebook JSON, compilation, clean publication state, and sequential execution;
- Python examples;
- relative Markdown links;
- Colab launch coverage;
- learner onboarding and module navigation;
- reference/source-boundary coverage;
- assessment structure and concept progression;
- public answer-key guardrails;
- gradebook calculator self-test;
- open-course neutrality.

## Licensing

- Original instructional material: CC BY 4.0.
- Original code/software: MIT.

See [LICENSE.md](LICENSE.md).

## For learners

Begin with [START_HERE.md](START_HERE.md).

If basic Python is already comfortable, take the readiness check and continue to Module 1. Otherwise, complete Module 0 first.

Use [LEARNER_PROGRESS.md](LEARNER_PROGRESS.md) to track evidence and [MASTERY_CHECKS.md](MASTERY_CHECKS.md) for worked self-paced feedback.
