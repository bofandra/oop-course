# Publication Checklist

This document captures the remaining GitHub-level publication steps for the open course.

The course content itself is already validated by the repository's automated checks. These items improve discoverability and release presentation rather than changing the curriculum.

## Recommended repository metadata

### Description

Use:

> Self-paced Object-Oriented Programming open course using Python and Google Colab, from object modelling to OOA/OOD/OOP/OOT and a complete capstone project.

### Suggested topics

```text
object-oriented-programming
python
oop
open-course
education
google-colab
jupyter-notebook
self-paced-learning
computer-science
programming-course
```

Keep topics descriptive rather than promotional.

## First stable release

Recommended tag:

```text
v1.0.0
```

Recommended release title:

```text
Object Oriented Programming Open Course — v1.0.0
```

Use [RELEASE_NOTES.md](RELEASE_NOTES.md) as the release body.

The release should point to the audited baseline on `main` after all validation checks are green.

## Pre-release checks

Before creating the release:

- [ ] GitHub Actions validation on `main` is green.
- [ ] README first-visit path is readable without cloning the repository.
- [ ] Module 0–16 navigation is intact.
- [ ] All Colab launch links are covered by validation.
- [ ] No public assessment answer keys are present.
- [ ] `CITATION.cff`, `LICENSE.md`, and `ACCESSIBILITY.md` are present.
- [ ] `LEARNER_PROGRESS.md` and `READING_GUIDE.md` are linked from the learner path.
- [ ] Repository description and topics are set.
- [ ] Release notes match the actual state of `main`.

## After release

After publishing `v1.0.0`:

- keep new course-level changes under the `Unreleased` section of [CHANGELOG.md](CHANGELOG.md);
- avoid changing learning outcomes silently in wording-only commits;
- continue requiring the course validator to pass before merging material changes;
- use a new release only when there is a meaningful learner-facing or course-level baseline change.

## Scope of versioning

Versioning applies to the **course package as a published artifact**, not to individual learner progress.

A patch release can cover corrections that preserve learning outcomes.

A minor release can cover backwards-compatible additions or meaningful learner-experience improvements.

A major release should be considered when the course learning outcomes, required module progression, formal reference policy, or assessment model changes substantially.
