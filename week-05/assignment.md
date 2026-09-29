# Week 5 Assignment — Enrollment Relationships

## Objective

Build a small model in which multiple objects collaborate through references.

## Task

Implement:

- `Student`
- `Course`
- `Enrollment`

### Student state

- `student_id`
- `name`

### Course state

- `course_code`
- `name`

### Enrollment state

- reference to one Student
- reference to one Course
- `status`

Initial Enrollment status:

```text
active
```

Add a simple `display_info()` method to Enrollment.

## Required demonstration

Create at least:

- 3 Student objects;
- 2 Course objects;
- 4 Enrollment objects.

Show that the same Student can appear in more than one Enrollment and that multiple Students can refer to the same Course.

## Written explanation

Answer:

1. Which objects does Enrollment refer to?
2. Why is Enrollment not a subclass of Student?
3. Why is Enrollment not a subclass of Course?
4. Which relationships are has-a/reference relationships?
5. In what sense is Enrollment a Client of Student/Course in this model?
6. What information would be duplicated if Enrollment stored only names instead of object references?

## Rubric

| Criterion | Weight |
|---|---:|
| Correct classes and instances | 20% |
| Correct object references | 25% |
| Clear relationship model | 20% |
| Multiple collaborating objects | 15% |
| Working display behavior | 5% |
| Explanation / reasoning | 15% |
| **Total** | **100%** |

## Scope

Do not use inheritance.

Week 6 is where `is-a` and inheritance are implemented formally.
