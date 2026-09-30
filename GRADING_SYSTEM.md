# Grading Operational System

This document operationalizes the course assessment plan already defined in the root README.

## 1. Final assessment grade formula

All major assessment artifacts use a **0–100 raw score**.

The course grade is calculated as:

```text
Quiz / Concept Exercises             15%
Module Coding Labs                   20%
Mid Test                             20%
Final Project                        35%
Demo / Code Explanation / Learning Evidence
                                      10%
-----------------------------------------
Total                               100%
```

Formula:

```text
Final Numeric
=
(Quiz Average × 0.15)
+
(Lab Average × 0.20)
+
(Mid Test × 0.20)
+
(Final Project × 0.35)
+
(Demo/Explanation/Learning Evidence × 0.10)
```

## 2. Module quiz aggregation

Graded quiz modules:

```text
1–7
9–15
```

Module 8 is the Mid Test and Module 16 is the Final Project / Final Test.

There are therefore **14 normal module quiz slots**.

Default rule:

> Every included module quiz has equal weight inside the 15% Quiz / Concept Exercises component.

If all 14 are included, one quiz contributes approximately:

```text
15% / 14 ≈ 1.0714 percentage points
```

to the final course grade.

The assessment registry can disable a module quiz if the instructor decides a particular module is formative only.

## 3. Module coding-lab aggregation

Graded lab slots use the same teaching modules:

```text
1–7
9–15
```

Default rule:

> Every included module coding lab has equal weight inside the 20% Module Coding Labs component.

If all 14 are included, one lab contributes approximately:

```text
20% / 14 ≈ 1.4286 percentage points
```

to the final course grade.

For Modules 14–15, the score may come from **selected assessment evidence** rather than requiring the entire Markdown assignment as a separate large take-home project.

## 4. Major assessments

### Mid Test — 20%

Use the raw score from:

[Mid Test rubric](assessments/midterm/midterm_rubric.md)

### Final Project — 35%

Use the raw score from:

[Final Project rubric](assessments/final-project/final_project_rubric.md)

### Demo / Code Explanation / Learning Evidence — 10%

Use:

[Demo / Code Explanation / Learning Evidence rubric](assessments/demo-participation-rubric.md)

This is intentionally separate from the 35% Final Project artifact score. Use [Assessment Alignment](ASSESSMENT_ALIGNMENT.md) to avoid double-counting artifact quality and ownership/explanation evidence.

## 5. Missing, late, excused, and pending work

The gradebook uses explicit statuses.

| Status | Meaning | Calculation behavior |
|---|---|---|
| `SUBMITTED` | on-time assessed work | raw score used |
| `LATE` | assessed after deadline | raw score used after any **explicit** penalty |
| `MISSING` | required work not submitted | score = 0 |
| `EXC` | officially excused/waived | excluded from that component denominator |
| `PENDING` | not yet assessed / future work | excluded from progress calculation; blocks finalization |

### Late penalties

The calculator does **not** invent an automatic late penalty.

If an approved course/institutional policy applies, enter the penalty explicitly in `penalty_percent`.

Example:

```text
raw score       = 80
penalty_percent = 10
adjusted score  = 72
```

If no penalty has been formally announced:

```text
penalty_percent = 0
```

### Excused work

Use `EXC` only when the instructor has formally waived that assessment for the student.

The remaining included assessments in the component determine the component average.

Do not use `EXC` merely because a score has not been entered yet.

### Pending work

Use `PENDING` for:

- future assessments;
- work awaiting grading;
- temporary administrative holds.

A final grade should not be released while required assessments remain `PENDING`.

## 6. Progress grade vs final grade

The calculator supports two modes.

### Progress mode

```bash
python scripts/calculate_grades.py \
  --scores path/to/gradebook_scores.csv \
  --mode progress
```

Purpose:

- show current component averages;
- ignore future/ungraded `PENDING` items;
- identify explicitly missing work.

A progress number is not a guaranteed final grade.

### Final mode

```bash
python scripts/calculate_grades.py \
  --scores path/to/gradebook_scores.csv \
  --mode final
```

Purpose:

- require all included assessments to be resolved as `SUBMITTED`, `LATE`, `MISSING`, or `EXC`;
- calculate the final weighted numeric score;
- assign the configured letter grade.

If required items are absent or `PENDING`, the student is marked **NOT FINALIZABLE**.

## 7. Letter-grade scale

The repository contains a configurable scale in:

`grading_config.json`

Current planned scale:

| Grade | Numeric range |
|---|---:|
| A | 85–100 |
| A- | 80–84.99 |
| B+ | 75–79.99 |
| B | 70–74.99 |
| B- | 65–69.99 |
| C+ | 60–64.99 |
| C | 56–59.99 |
| D | 45–55.99 |
| E | <45 |

**Operational warning:** confirm this scale against the grading scale you intend to use before publishing final grades. If the official scale changes, edit `grading_config.json`; do not hand-edit calculated totals.

## 8. Attendance / eligibility

Attendance eligibility is deliberately **not hard-coded** into the grade calculator.

Why:

- attendance policy is a facilitator-defined or organization-defined rule;
- exceptions may require administrative approval;
- attendance eligibility should not silently change a numeric grade formula.

Before final grade release, perform a separate eligibility check according to the applicable learning environment policy.

## 9. Gradebook files

Public templates:

```text
templates/
├── assessment_registry.csv
└── gradebook_scores.csv
```

Private working files should **not** be committed to this public repository.

Recommended local/private structure:

```text
private-gradebook/
├── gradebook_scores.csv
├── gradebook_summary_progress.csv
└── gradebook_summary_final.csv
```

Student names, IDs, attendance data, and final grades are private educational records.

## 10. Score-entry workflow

Recommended workflow:

```text
grade an assessment
      ↓
enter raw score + status
      ↓
enter explicit penalty only if policy applies
      ↓
run calculator
      ↓
review warnings / missing rows
      ↓
publish feedback
```

Before finalization:

```text
all required rows resolved
      ↓
run --mode final
      ↓
check NOT FINALIZABLE flags
      ↓
verify major rubric scores
      ↓
confirm institutional eligibility
      ↓
release final grade
```

## 11. Privacy rule

Never commit a real student gradebook to public `main`.

The repository should contain only:

- blank templates;
- rubrics;
- grading logic;
- documentation.

Keep real student records in a private location appropriate for your learning environment.
