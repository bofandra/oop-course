# Teaching Readiness Audit

Audit date: **30 September 2026**

This audit evaluates whether the repository is realistically teachable as a 4-credit Saturday course, not merely whether the files compile.

## Overall status

```text
Curriculum progression          READY
200-minute lesson pacing        READY
Mid Test prerequisite alignment READY
Final Project alignment         READY
Weekly workload balance         READY WITH GUARDRAILS
Year-end calendar               NEEDS ACADEMIC-CALENDAR CONFIRMATION
Final demo capacity             NEEDS CLASS-SIZE CONFIRMATION
Public assessment safety        READY
Execution / CI                  READY
```

## 1. 200-minute session pacing

Weeks 1–7 and 9–15 each contain a 200-minute instructor flow from 08:30–11:50, including a 10-minute break.

The common rhythm is appropriate:

```text
15–25 min  review / motivation
50–75 min  core concepts
10 min     break
50–75 min  live coding / lab
10–20 min  quiz / reflection / next-week bridge
```

This balance is realistic for a 4-credit practical OOP class because students repeatedly move from concept → code → reasoning rather than receiving a continuous lecture.

## 2. Progression difficulty

### Weeks 1–3 — low to medium

Focus:

- objects;
- classes/instances;
- state/behavior.

Teaching-readiness finding:

Week 1 originally contained a Python `__init__` / `self` example even though the Week 1 README explicitly postpones those mechanics to Week 2.

**Resolved:** the Week 1 notebook now keeps the class example conceptual and leaves `__init__`, `self`, and instance-state mechanics for Week 2.

### Weeks 4–7 — medium

Focus:

- encapsulation;
- object relationships;
- inheritance;
- overriding/polymorphism.

The sequence is coherent:

```text
protect one object's state
→ connect objects
→ model is-a relationships
→ vary inherited behavior
```

Week 7 is the highest pre-midterm cognitive load. Keep its assignment as a review/lab if needed rather than stacking a large take-home deadline immediately before the Mid Test.

### Week 8 — assessment

The Mid Test is aligned to Weeks 1–7.

It does **not** require:

- abstract classes;
- multiple inheritance;
- exceptions;
- design patterns.

This prevents assessment of material that has not yet been formally taught.

### Weeks 9–11 — medium

Focus:

- abstract/deferred classes;
- multiple inheritance/mixins;
- runtime references/identity.

Week 10 is conceptually dense, but the course deliberately avoids C3 internals and advanced cooperative inheritance.

### Week 12 — medium-high density

Week 12 includes three related but distinct topics:

- operator overloading;
- genericity;
- modules.

The instructor flow already limits genericity to a conceptual treatment and keeps Python generic typing out of scope.

Recommendation:

> Do not expand Week 12 with `TypeVar`, package publishing, or additional special methods.

### Week 13 — medium-high

Exceptions + contracts are teachable in 200 minutes because the material reuses the invariant idea from Week 4.

The central distinction should remain:

```text
invalid external request → exception
internal correctness assumption → assertion
```

### Weeks 14–15 — high integration load

These weeks move from isolated concepts to whole-system design.

Main workload risk:

```text
Week 14 assignment
+ Week 15 assignment
+ Final Project preparation
```

can become three overlapping mini-projects.

Recommended operating policy:

- use Week 14 University Registration primarily as an **in-class integration lab / Final Project planning rehearsal**;
- use Week 15 Food Ordering primarily as an **in-class design-reuse lab**;
- do not require both as large independent take-home projects while the Final Project is active.

The assignment files remain useful as structured labs and can still be graded lightly as weekly-lab evidence.

### Week 16 — final integration

The final project correctly evaluates:

- OOA;
- OOD;
- OOP;
- OOT;
- relationships;
- inheritance/polymorphism;
- contracts/exceptions;
- executable tests;
- explanation/ownership.

Optional advanced techniques do not create bonus by themselves.

## 3. Assessment alignment

### Mid Test

Status: **aligned**

Evidence chain:

```text
Weeks 1–7
→ objects/classes/state
→ encapsulation
→ relationships
→ inheritance
→ polymorphism
→ Vehicle Rental assessment
```

### Final Project

Status: **aligned**

The University Learning Management System requires students to integrate previously taught material without being handed a fixed class list.

A particularly strong assessment choice is requiring two assignment/scoring variants to demonstrate real polymorphism.

## 4. Workload balance

Recommended outside-class workload target:

| Period | Suggested workload outside class |
|---|---:|
| Weeks 1–3 | 1.5–2 hours/week |
| Weeks 4–6 | 2–2.5 hours/week |
| Week 7 | 1.5–2 hours + Mid Test preparation |
| Week 8 | Mid Test only |
| Weeks 9–11 | 2–2.5 hours/week |
| Week 12 | 2–2.5 hours |
| Week 13 | 2–3 hours |
| Week 14 | 2 hours lab + Final Project milestone |
| Week 15 | 2 hours lab + Final Project implementation |
| Week 16 | Final integration/demo |

Avoid making every Markdown exercise, notebook TODO, quiz, and assignment separately graded.

A sustainable model is:

```text
notebook TODO + exercises
→ formative / in-class

quiz
→ small concept grade

assignment/lab
→ weekly coding-lab evidence

Mid Test / Final Project
→ major summative evidence
```

## 5. Year-end calendar risk

The nominal 16-class sequence places Week 13 and Week 14 on dates adjacent to the Christmas / New Year period.

This is an **operational risk**, not a curriculum defect.

Before publishing firm attendance or deadline expectations, confirm the official TANRI ABENG UNIVERSITY academic calendar for:

- 26 December 2026;
- 2 January 2027.

Do not assume campus operations on those dates from this repository alone.

The detailed nominal calendar is in [TEACHING_CALENDAR.md](TEACHING_CALENDAR.md).

## 6. Final demo capacity risk

The final demo/viva guide recommends **5–7 minutes per student**.

A 200-minute session has practical overhead for:

- setup;
- transitions;
- troubleshooting;
- breaks;
- score recording.

Approximate planning:

```text
20 students × 7 min = 140 min
25 students × 7 min = 175 min
30 students × 7 min = 210 min
```

Therefore:

- up to roughly 20–25 students: one Week 16 session is practical;
- above that: use shorter slots, parallel assessors, or the 23 January contingency/closure slot.

Confirm actual enrollment before fixing the demo schedule.

## 7. Public repository implications

Because `main` is public:

- future-week materials are visible even before their official teaching week;
- GitHub itself cannot function as a true staged-release gate;
- answer keys and executable reference solutions must remain outside public `main`.

The weekly **official release** should therefore mean:

> the date the lecturer announces/assigns the material through the course communication channel or LMS.

If strict access gating is ever required, use a private repository/branch/workspace rather than relying on public `main`.

## 8. Readiness decision

The course is ready to teach with three operating checks before the semester is locked:

1. confirm TAU year-end teaching dates;
2. confirm class size for the final viva;
3. decide which Week 14–15 work is formative versus separately graded.

No curriculum rewrite is required.
