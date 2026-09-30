# Module 11 Assignment — Shared References in a Course Model

## Objective

Demonstrate identity, aliasing, mutation, reassignment, and shared references using custom objects.

## Task

Implement:

```text
Student
Course
Enrollment
```

### Student

State:

- `student_id`
- `name`

### Course

State:

- `course_code`
- `title`

Behavior:

- `rename(new_title)`

### Enrollment

State:

- reference to one Student
- reference to one Course

Behavior:

- `display_info()`

## Required demonstration

Create:

- two Student objects;
- one Course object;
- two Enrollment objects that refer to the same Course.

Demonstrate:

1. both Enrollment objects observe the original Course title;
2. rename the Course through one reference;
3. both Enrollment objects observe the changed title;
4. show that both Enrollment objects refer to the same Course with `is`;
5. create a second independent Course object with the same title;
6. show that equal-looking state does not imply object identity;
7. reassign one Course variable and explain which references still point to the original Course object.

## Written explanation

Answer:

1. Where does aliasing occur?
2. Which operation mutates an existing object?
3. Which operation reassigns a reference?
4. Why do both Enrollment objects see the Course rename?
5. What is the difference between Course identity and Course state?
6. Why does `b = a` not automatically create a copy?
7. When may an object become unreachable in this model?

## Rubric

| Criterion | Weight |
|---|---:|
| Correct object/reference model | 20% |
| Aliasing demonstration | 20% |
| Mutation vs reassignment | 20% |
| Identity checks | 15% |
| Shared-state reasoning | 15% |
| Lifecycle explanation | 10% |
| **Total** | **100%** |

## Scope

Do not implement custom copy/deepcopy behavior.

Do not depend on garbage-collection timing.

The focus is the conceptual runtime model of references and objects.
