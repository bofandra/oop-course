# Gradebook Quick Start

The repository uses a **long-form score ledger** rather than one very wide spreadsheet.

## Files

```text
grading_config.json
templates/assessment_registry.csv
templates/gradebook_scores.csv
scripts/calculate_grades.py
```

## 1. Copy the blank ledger privately

Do not enter real student data into the public repository.

Example local/private copy:

```bash
cp templates/gradebook_scores.csv ~/private-gradebook/oop-2026-scores.csv
```

## 2. Add one row per student per assessment

Example:

```csv
student_id,student_name,assessment_id,raw_score,status,penalty_percent,notes
S001,Student A,quiz_w01,80,SUBMITTED,0,
S001,Student A,lab_w01,90,SUBMITTED,0,
S001,Student A,quiz_w02,,PENDING,0,
S002,Student B,quiz_w01,0,MISSING,0,
```

## 3. Progress report

```bash
python scripts/calculate_grades.py \
  --scores ~/private-gradebook/oop-2026-scores.csv \
  --mode progress \
  --output ~/private-gradebook/oop-progress.csv
```

## 4. Finalization

Before final mode:

- future assessments should no longer be `PENDING`;
- missing work should be explicitly `MISSING`;
- excused work should be explicitly `EXC`;
- raw scores should be checked against rubrics.

Then:

```bash
python scripts/calculate_grades.py \
  --scores ~/private-gradebook/oop-2026-scores.csv \
  --mode final \
  --output ~/private-gradebook/oop-final.csv
```

If required assessments are unresolved, the output shows:

```text
finalizable = NO
```

and lists unresolved assessment IDs.

## Status rules

```text
SUBMITTED
→ score counts

LATE
→ score counts
→ only explicit penalty_percent is applied

MISSING
→ score 0

EXC
→ excluded from component average

PENDING
→ excluded from progress
→ blocks finalization
```

## Important

The numeric grade calculation is mechanical.

Before releasing final grades, separately verify any official:

- attendance requirement;
- exam-presence requirement;
- academic-integrity decision;
- institutional grade-scale rule.

These administrative eligibility rules are intentionally not silently embedded in the calculator.
