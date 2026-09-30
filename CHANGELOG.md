# Changelog

This file records meaningful course-level changes. Small wording fixes may be omitted unless they change learning outcomes, assessment expectations, navigation, or validation behavior.

## 2026-10-01 — Audited Open-Course Baseline

This baseline marks the first fully audited public version of the self-paced Object Oriented Programming course.

### Course-content audit

Reviewed the course end-to-end from Module 0 through Module 16, including notebooks, exercises, quizzes, assignments, instructor notes, the Mid-Course Assessment, and the Final Project.

Key conceptual clarifications:

- class invariant vs state-transition rule;
- general object reference/association vs whole–part has-a/composition-style relationship;
- inheritance as a semantic is-a relationship rather than code reuse alone;
- explicit evidence of overriding, polymorphism, and dynamic binding;
- state-transition rules expressed as state-dependent preconditions where appropriate;
- exceptions for required runtime validation vs `assert` for internal correctness assumptions;
- plain `assert` in OOT examples treated as lightweight test checks, not business-rule enforcement;
- Strategy-style examples use an explicit abstract common contract already taught earlier in the course.

### Assessment alignment

The Mid-Course Assessment was tightened so it directly evidences:

- object modelling and relationships;
- encapsulation and lifecycle rules;
- inheritance;
- overriding;
- polymorphism;
- dynamic binding.

The Final Project package was aligned across:

- brief;
- planning notebook;
- checklist;
- rubric;
- demo/viva guide.

Optional techniques remain optional when they do not improve the model.

### Learner experience

Improved first-visit navigation with:

- a short readiness path;
- direct Module 0 / Module 1 entry points;
- clearer self-paced checkpoints;
- stronger distinction between learner guidance and optional instructor timing suggestions.

The repository remains independent of fixed institutional schedules.

### Automated validation

The course validator now checks:

- required Module 0–16 structure;
- notebook JSON and code compilation;
- sequential notebook execution;
- Python examples;
- gradebook self-test;
- relative Markdown links;
- Colab launch coverage;
- module-to-Colab navigation;
- reference-map coverage;
- public onboarding navigation;
- assessment structure;
- public answer-key guard;
- open-course neutrality.

The GitHub Actions validation workflow passed on `main` after the audit and learner-experience updates.

### Baseline environment

- Primary language: Python
- CI Python version: 3.12
- Primary zero-setup lab environment: Google Colab
- Instructional license: CC BY 4.0
- Code/software license: MIT

## Unreleased

### Reference discipline

- added `SOURCE_BOUNDARY.md` to distinguish formal concepts, minimal Python implementation bridges, and out-of-scope additions;
- clarified that implementation bridges must not create hidden learning outcomes or assessment requirements;
- added CI validation so the two-reference source-boundary policy remains part of the published course baseline.

### Publication polish

- added `CITATION.cff` so the repository has machine-readable citation metadata;
- added `ACCESSIBILITY.md` with learner and contributor accessibility guidance;
- added validation guards for citation/accessibility publication assets;
- added `LOCAL_SETUP.md` documenting the Python 3.12 reference environment, optional local workflow, and repository validation command;
- added a notebook publication-hygiene guard requiring published notebooks to have no saved execution counts or cell outputs;
- added consistent Previous / Course Map / Next navigation to Module 0–16 and a validator guard for the learning path.

Future changes should preserve the course progression, assessment guardrails, reference alignment, accessibility guidance, and self-paced/open-course neutrality described in the repository documentation.
