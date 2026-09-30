# Contributing

Contributions are welcome when they improve clarity, correctness, accessibility, or learning value without turning the repository into a broader Python/framework course.

## Before contributing

Read:

- [Course Map](COURSE_MAP.md)
- [Reference Map](REFERENCE_MAP.md)
- [Assessment Alignment](ASSESSMENT_ALIGNMENT.md)
- [Execution Audit](EXECUTION_AUDIT.md)

## Course design guardrails

Please preserve these principles:

1. Teach **object-oriented thinking using Python**, not Python syntax for its own sake.
2. Introduce concepts in the existing progression; do not assess a concept before it is taught.
3. Keep databases, web frameworks, REST APIs, GUIs, cloud deployment, advanced testing frameworks, and architecture frameworks outside required scope.
4. Prefer meaningful object responsibilities and collaboration over pattern count.
5. Keep learner-facing material self-paced and independent of institution-specific or fixed-calendar scheduling.
6. Do not publish answer keys for assessments that may be reused by facilitated cohorts.
7. Keep formal concepts aligned to the documented references.

## Module changes

Most instructional modules use:

```text
README.md
<module notebook>.ipynb
exercises.md
quiz.md
assignment.md
instructor-notes.md
```

When changing a module, check whether the same change also requires updates to:

- `COURSE_MAP.md`;
- `REFERENCE_MAP.md`;
- `ASSESSMENT_ALIGNMENT.md`;
- `MASTERY_CHECKS.md`;
- assessment rubrics.

## Notebook rules

- keep notebooks executable from top to bottom;
- avoid hidden runtime dependencies;
- keep examples small enough to understand;
- explain intentional weak/invalid designs before showing the corrected version;
- leave student TODO cells syntactically valid;
- do not require third-party packages unless the course scope is explicitly changed.

## Validation

Before opening a pull request, run:

```bash
python scripts/validate_course.py
```

The same validation also runs in GitHub Actions.

## Pull request checklist

Confirm that:

- learning outcomes still match the material;
- assessment requirements do not introduce untaught concepts;
- notebook examples execute sequentially;
- Markdown links are valid;
- Colab launch coverage remains complete;
- reference mapping remains accurate;
- learner-facing wording remains self-paced and institution-neutral;
- no assessment answer key has been published accidentally.
