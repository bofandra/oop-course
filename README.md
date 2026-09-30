# Object Oriented Programming — Open Course

[![Validate course materials](https://github.com/bofandra/oop-course/actions/workflows/course-validation.yml/badge.svg)](https://github.com/bofandra/oop-course/actions/workflows/course-validation.yml)

A self-paced, open course for learning **object-oriented thinking using Python**.

This course is designed for anyone to use **at any time**, with a flexible self-paced learning path.

Primary implementation language: **Python**  
Primary lab environment: **Google Colab**

## Start learning

- New learner: [Start Here](START_HERE.md)
- Ready to run code: [Open notebooks in Google Colab](COLAB.md)
- Want the full pathway: [Course Map](COURSE_MAP.md)

No enrollment or fixed calendar is required.

### Start in 10 minutes

If this is your first visit:

1. Open the [Python Readiness Check](00-python-primer/readiness-check.md).
2. If the prerequisite feels comfortable, go directly to [Module 1](week-01/) and open its Colab notebook.
3. If the prerequisite is difficult, complete [Module 0 — Python Primer](00-python-primer/) first.
4. For each module, use this loop: **README → notebook → exercises → quiz → assignment → mastery check**.

You do not need to clone the repository to begin; Google Colab is the default zero-setup path.

## Course approach

This course is designed as **OOP thinking using Python**, not as a syntax-only Python course.

The learning storyline is:

```text
Problem
  ↓
Objects
  ↓
Classes, State & Behavior
  ↓
Encapsulation
  ↓
Object Relationships
  ↓
Inheritance
  ↓
Polymorphism
  ↓
Advanced Object Concepts
  ↓
Exceptions & Contracts
  ↓
OO Analysis & Design
  ↓
Reusability & Patterns
  ↓
Complete OOP Solution
```

## Learning outcomes

By the end of the course, learners should be able to:

1. Explain object-oriented concepts and model a problem using objects, classes, identity, state, and behavior.
2. Design collaborating objects using encapsulation, abstraction, responsibilities, and object relationships.
3. Apply inheritance, overriding, polymorphism, dynamic binding, abstract classes, multiple inheritance, and mixins appropriately.
4. Explain runtime object behavior including references, identity, lifecycle, operator overloading, genericity, modules, exceptions, assertions, and contracts.
5. Perform object-oriented analysis, design, implementation, and testing (OOA → OOD → OOP → OOT).
6. Build, test, demonstrate, and defend a complete object-oriented solution and recognize opportunities for code/design reuse.

See [Course Map](COURSE_MAP.md) for the detailed module, learning-outcome, assessment, and source alignment.

Open-course guidance:

- [Start Here](START_HERE.md)
- [Open in Google Colab](COLAB.md)
- [Open Course Guide](OPEN_COURSE_GUIDE.md)
- [Self-Paced Learning Guide](SELF_PACED_GUIDE.md)
- [Self-Assessment Guide](SELF_ASSESSMENT_GUIDE.md)
- [Mastery Checks with Worked Feedback](MASTERY_CHECKS.md)
- [Assessment Alignment](ASSESSMENT_ALIGNMENT.md)
- [Reference Map](REFERENCE_MAP.md)
- [Instructor Guide](INSTRUCTOR_GUIDE.md)
- [Execution Audit](EXECUTION_AUDIT.md)
- [Changelog](CHANGELOG.md)
- [Grading Operational System](GRADING_SYSTEM.md)
- [Gradebook Quick Start](GRADEBOOK_GUIDE.md)
- [Contributing](CONTRIBUTING.md)

## Suggested learning sequence

The numbered folders represent **modules in a recommended order**, not calendar weeks. Learners may move faster or slower as needed.

| Module | Topic |
|---:|---|
| [0](00-python-primer/) | Python Primer / Prerequisite |
| [1](week-01/) | Introduction to OOP & Thinking in Objects |
| [2](week-02/) | Classes, Objects & Instances |
| [3](week-03/) | Attributes, Methods, State & Behavior |
| [4](week-04/) | Encapsulation & Abstraction |
| [5](week-05/) | Object Relationships |
| [6](week-06/) | Inheritance |
| [7](week-07/) | Overriding, Polymorphism & Dynamic Binding |
| [8](week-08/) | Mid-Course Assessment |
| [9](week-09/) | Abstract Classes & Inheritance Structures |
| [10](week-10/) | Multiple Inheritance & Mixins |
| [11](week-11/) | Object Lifecycle, References & Object Identity |
| [12](week-12/) | Operator Overloading, Genericity & Organizing Classes into Modules |
| [13](week-13/) | Exception Handling & Assertions |
| [14](week-14/) | OOP Analysis, Design, Class Diagram & Testing |
| [15](week-15/) | Reusability, Design Patterns & OOP Case Study |
| [16](week-16/) | Final Project / Final Assessment |

## Optional assessment model

The repository includes a complete assessment model for learners or instructors who want structured evaluation.

| Component | Weight | Main repository evidence |
|---|---:|---|
| Quiz / Concept Exercises | 15% | module `quiz.md` / `exercises.md` |
| Coding Labs | 20% | notebooks and `assignment.md` |
| Mid-Course Assessment | 20% | [assessment package](assessments/midterm/) |
| Final Project | 35% | [Final Project package](assessments/final-project/) |
| Demo / Code Explanation / Learning Evidence | 10% | [rubric](assessments/demo-participation-rubric.md) |
| **Total** | **100%** | |

Self-paced learners may instead use the quizzes, labs, and rubrics purely for self-assessment.

## Primary references

1. Inggriani Liem. *Diktat Kuliah Pemrograman Berorientasi Objek*. Departemen Teknik Informatika ITB, 2003.
2. OpenStax. *Introduction to Python Programming*. 2024.

The formal course scope is intentionally aligned to these two references.

The Diktat is used primarily for OOP concepts and terminology. OpenStax is used primarily for Python-facing implementation.

See the [Reference Map](REFERENCE_MAP.md) for module-by-module source alignment.

## Repository structure

```text
oop-course/
├── 00-python-primer/
├── week-01/
├── week-02/
├── ...
├── week-16/
├── assessments/
│   ├── midterm/
│   └── final-project/
├── templates/
├── scripts/
├── COURSE_MAP.md
├── REFERENCE_MAP.md
├── COLAB.md
├── CONTRIBUTING.md
├── OPEN_COURSE_GUIDE.md
├── SELF_PACED_GUIDE.md
├── INSTRUCTOR_GUIDE.md
├── EXECUTION_AUDIT.md
├── GRADING_SYSTEM.md
└── GRADEBOOK_GUIDE.md
```

## Standard module package

Most instructional modules contain:

```text
README.md
<module notebook>.ipynb
exercises.md
quiz.md
assignment.md
instructor-notes.md
```

The folder names remain `week-01` through `week-16` for repository stability, but they should be read as a **recommended module sequence**, not as fixed dates.

## Self-paced learner workflow

A recommended workflow is:

```text
Read module README
      ↓
Run notebook examples
      ↓
Complete TODO cells
      ↓
Do selected exercises
      ↓
Take concept quiz
      ↓
Complete coding lab
      ↓
Attempt mastery checks
      ↓
Open worked feedback
      ↓
Write reflection
      ↓
Move to next module when ready
```

## Using the notebooks

Use the [Colab notebook index](COLAB.md) to launch the executable course notebooks directly in Google Colab. Save a personal copy, run the examples, complete the TODO cells, and compare your work against the stated requirements and rubrics.

## License

Instructional materials are licensed under **Creative Commons Attribution 4.0 International (CC BY 4.0)** and code/software portions are licensed under the **MIT License**, except where otherwise noted. See [LICENSE.md](LICENSE.md).

## Scope discipline

This repository intentionally avoids turning the OOP course into a framework-development course.

Topics such as databases, REST APIs, GUIs, deployment, advanced testing frameworks, dependency-injection frameworks, and large architecture patterns are not required unless explicitly introduced as optional context.

---

> The goal of this course is not merely to write classes. The goal is to learn how to model a problem as a set of meaningful objects that own state, perform behavior, collaborate, preserve their rules, and can be explained and tested.
