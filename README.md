# Object Oriented Programming

**TANRI ABENG UNIVERSITY — Faculty of Engineering and Technology**  
Semester: Odd 2026/2027  
Lecturer: Bofandra Muhammad  
Credits: 4  
Class: Saturday, 08:30–11:50  
Primary implementation language: **Python**  
Primary lab environment: **Google Colab**

## Course approach

This course is designed as **OOP thinking using Python**, not as a syntax-only Python course.

The semester storyline is:

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

## Course Learning Outcomes

By the end of the course, students should be able to:

1. Explain object-oriented concepts and model a problem using objects, classes, identity, state, and behavior.
2. Design collaborating objects using encapsulation, abstraction, responsibilities, and object relationships.
3. Apply inheritance, overriding, polymorphism, dynamic binding, abstract classes, multiple inheritance, and mixins appropriately.
4. Explain runtime object behavior including references, identity, lifecycle, operator overloading, genericity, modules, exceptions, assertions, and contracts.
5. Perform object-oriented analysis, design, implementation, and testing (OOA → OOD → OOP → OOT).
6. Build, test, demonstrate, and defend a complete object-oriented solution and recognize opportunities for code/design reuse.

See [Course Map](COURSE_MAP.md) for the detailed weekly learning-outcome, assessment, and source alignment.

Teaching operations:

- [Teaching Readiness Audit](TEACHING_READINESS_AUDIT.md)
- [Semester Teaching Calendar](TEACHING_CALENDAR.md)
- [Course Material Release Plan](RELEASE_PLAN.md)
- [Execution Audit](EXECUTION_AUDIT.md)

## Weekly Plan

| Week | Topic |
|---:|---|
| [0](00-python-primer/) | Python Primer / Prerequisite |
| [1](week-01/) | Introduction to OOP & Thinking in Objects |
| [2](week-02/) | Classes, Objects & Instances |
| [3](week-03/) | Attributes, Methods, State & Behavior |
| [4](week-04/) | Encapsulation & Abstraction |
| [5](week-05/) | Object Relationships |
| [6](week-06/) | Inheritance |
| [7](week-07/) | Overriding, Polymorphism & Dynamic Binding |
| [8](week-08/) | Mid Test |
| [9](week-09/) | Abstract Classes & Inheritance Structures |
| [10](week-10/) | Multiple Inheritance & Mixins |
| [11](week-11/) | Object Lifecycle, References & Object Identity |
| [12](week-12/) | Operator Overloading, Genericity & Organizing Classes into Modules |
| [13](week-13/) | Exception Handling & Assertions |
| [14](week-14/) | OOP Analysis, Design, Class Diagram & Testing |
| [15](week-15/) | Reusability, Design Patterns & OOP Case Study |
| [16](week-16/) | Final Project / Final Test |

## Assessment

| Component | Weight | Main repository evidence |
|---|---:|---|
| Quiz / Concept Exercises | 15% | weekly `quiz.md` / `exercises.md` |
| Weekly Coding Labs | 20% | weekly notebooks and `assignment.md` |
| Mid Test | 20% | [Mid Test package](assessments/midterm/) |
| Final Project | 35% | [Final Project package](assessments/final-project/) |
| Demo / Code Explanation / Participation | 10% | weekly discussion + final demo/viva |
| **Total** | **100%** | |

## Primary References

1. Inggriani Liem. *Diktat Kuliah Pemrograman Berorientasi Objek*. Departemen Teknik Informatika ITB, 2003.
2. OpenStax. *Introduction to Python Programming*. 2024.

The formal course scope is intentionally aligned to these two references.

The Diktat is used primarily for OOP concepts and terminology. OpenStax is used primarily for Python-facing implementation.

## Repository Structure

```text
oop-course/
├── 00-python-primer/
│   ├── README.md
│   ├── 00_python_primer.ipynb
│   └── readiness-check.md
├── week-01/
├── week-02/
├── ...
├── week-16/
├── assessments/
│   ├── midterm/
│   └── final-project/
├── templates/
│   └── colab_template.ipynb
├── COURSE_MAP.md
├── TEACHING_READINESS_AUDIT.md
├── TEACHING_CALENDAR.md
├── RELEASE_PLAN.md
└── EXECUTION_AUDIT.md
```

### Standard teaching-week package

Most instructional weeks contain:

```text
README.md
<week notebook>.ipynb
exercises.md
quiz.md
assignment.md
instructor-notes.md
```

Assessment weeks use dedicated material under `assessments/`.

Week 12 also contains small Python module files to demonstrate multi-file organization.

## Student workflow

A recommended weekly workflow is:

```text
Read weekly README
      ↓
Run Colab examples
      ↓
Complete TODO cells
      ↓
Do exercises
      ↓
Take concept quiz
      ↓
Complete assignment/lab
      ↓
Write reflection
```

## Using the notebooks

Open the notebook in Google Colab, save a personal copy, run the examples, complete the TODO cells, and submit the requested notebook/file according to the weekly instructions.

## Scope discipline

This repository intentionally avoids turning the OOP course into a framework-development course.

Topics such as databases, REST APIs, GUIs, deployment, advanced testing frameworks, dependency-injection frameworks, and large architecture patterns are not required unless explicitly introduced as optional context.

---

> The goal of this course is not merely to write classes. The goal is to learn how to model a problem as a set of meaningful objects that own state, perform behavior, collaborate, preserve their rules, and can be explained and tested.
