# Course Material Release Plan

This plan distinguishes **public repository visibility** from **official pedagogical release**.

Because the repository is public, files on `main` are visible immediately. The release plan therefore controls when material is **announced, assigned, and due**, not whether a student can technically browse it earlier.

## Weekly release rhythm

Recommended default:

```text
Monday 08:00
→ announce weekly README + reading focus

Thursday
→ reminder / prerequisite check

Saturday 08:30–11:50
→ synchronous class + notebook/lab

Saturday after class
→ assignment/lab officially opens

Following Thursday or Friday
→ assignment/lab due

Before next Saturday
→ quiz feedback / common-error notes
```

Avoid deadlines immediately before class when students are also preparing for a major assessment.

## What to announce each week

### Before class

Officially point students to:

- weekly README;
- reading section;
- notebook;
- any preparation question.

Do **not** ask students to complete the full lab before the concept is taught.

### During class

Use:

- notebook examples;
- TODO cells;
- exercises;
- short quiz/reflection.

### After class

Assign:

- the weekly coding-lab / assignment evidence;
- only the exercises needed for reinforcement.

The repository may contain more practice than needs to be graded.

## Suggested grading/release policy

| Material | Purpose | Default treatment |
|---|---|---|
| README | concepts / preparation | required reading |
| notebook examples | guided learning | in class |
| TODO cells | practice | formative / lab evidence |
| exercises.md | practice bank | selective, mostly formative |
| quiz.md | concept check | small graded component |
| assignment.md | coding application | weekly coding-lab component |
| instructor-notes.md | lecturer guidance | public teaching notes without answer key |
| major assessment | summative | separately scheduled |

## Special release rules

### Week 7 → Week 8

Do not create a heavy Week 7 deadline on the night before the Mid Test.

Recommended:

- Week 7 lab completed mostly in class;
- any submission due by **Thursday before the Mid Test**;
- Friday reserved for review.

### Final Project

Officially announce the Final Project after Week 12.

Do not wait until Week 16 to reveal the project.

Recommended progression:

```text
after Week 12
→ brief + rubric + planning notebook

Week 13
→ students identify contract/exception rules

Week 14
→ OOA/OOD/class-diagram milestone

Week 15
→ implementation/test milestone

Week 16
→ demo/viva

23 January
→ final corrected submission / closure
```

## Week 14–15 workload guardrail

The Week 14 University Registration and Week 15 Food Ordering materials are pedagogically valuable, but both are full mini-system exercises.

When the Final Project is active:

- use them primarily as in-class labs;
- grade selected evidence rather than demanding two complete take-home mini-projects;
- allow the same Week 14 OOA/OOD skills to feed directly into Final Project Milestone A;
- allow Week 15 reuse/testing discussion to feed directly into Final Project Milestone B.

This keeps the weekly coding-lab component active without creating unnecessary project stacking.

## Version / release management on GitHub

For a public repository, recommended lightweight practice:

```text
main
→ always contains the current approved course material

Git tag after major checkpoints
→ semester-start
→ pre-midterm
→ post-midterm
→ final-project-release
→ semester-complete
```

Tags are useful for reproducibility, but they are not access controls.

If future cohorts require hidden future material, use a private instructor repository as the source and publish selected material to the public course repository when released.

## Student communication template

Weekly announcement can stay short:

> Week N material is now officially assigned. Read the Week N README before class, bring/open the notebook in Colab, and review the listed source section. The coding lab opens after Saturday's session; only the stated submission items are graded.

This keeps the repository rich while making workload expectations explicit.
