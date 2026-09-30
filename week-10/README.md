# Module 10 — Multiple Inheritance & Mixins

> **Run the notebook:** [Open Module 10 in Google Colab](https://colab.research.google.com/github/bofandra/oop-course/blob/main/week-10/10_multiple_inheritance_mixins.ipynb)

## Learning outcomes

By the end of this module, learners should be able to:

1. explain **multiple inheritance** as one class inheriting from more than one parent class;
2. identify method-name conflicts that can arise from multiple inheritance;
3. explain **repeated inheritance / diamond-shaped inheritance** conceptually;
4. inspect Python's method lookup order using `__mro__`;
5. explain why parent ordering matters when multiple parents provide the same method;
6. use a **mixin** as a focused reusable capability;
7. distinguish a primary domain superclass from small capability-oriented mixins;
8. avoid unnecessary multiple inheritance when composition or single inheritance is clearer.

## Source alignment

Inggriani Liem explicitly defines **multiple inheritance** as a descendant class inheriting from more than one parent. The Diktat also warns that multiple inheritance can create conflicts when ancestor classes contain features with the same name or conflicting method bodies.

The Diktat separately discusses **repeated inheritance**: a multiple-inheritance structure in which parent classes share a common ancestor. It notes that this can introduce additional conflicts and discusses language-specific mechanisms such as renaming and selection.

The Diktat lists **Mixin Class / Mixin Inheritance** terminology, but it does not provide the detailed Python mixin teaching used here.

OpenStax 13.5 is the Python-facing source for **multiple inheritance and mixin classes**, including method resolution order concepts.

Therefore:

```text
Multiple / repeated inheritance concepts
→ Inggriani Liem

Python multiple inheritance,
MRO demonstration, mixin examples
→ OpenStax + course implementation
```

## From Module 9 to Module 10

Module 9 used a single inheritance hierarchy:

```text
Payment
├── CashPayment
├── CardPayment
└── EWalletPayment
```

Module 10 asks:

> What happens if one class legitimately needs behavior from more than one parent?

## 1. Basic multiple inheritance

```python
class Teacher:
    def teach(self):
        print("Teaching")


class Researcher:
    def research(self):
        print("Researching")


class Lecturer(Teacher, Researcher):
    pass
```

Usage:

```python
lecturer = Lecturer()

lecturer.teach()
lecturer.research()
```

Conceptually:

```text
Teacher      Researcher
     \       /
      \     /
      Lecturer
```

Lecturer inherits behavior from two parents.

## 2. Conflict: same method name

Suppose both parents define:

```python
class A:
    def display(self):
        print("A")


class B:
    def display(self):
        print("B")


class C(A, B):
    pass
```

What does this call do?

```python
C().display()
```

Python needs a deterministic lookup order.

## 3. Method Resolution Order (MRO)

Inspect:

```python
print(C.__mro__)
```

A useful introductory interpretation:

> MRO is the order Python uses when searching for an inherited method or attribute.

For Module 10, learners only need to understand the observable lookup order.

Do not teach the full C3 linearization algorithm.

## 4. Parent order matters

Compare:

```python
class C(A, B):
    pass
```

with:

```python
class C(B, A):
    pass
```

If both parents provide `display()`, the lookup order changes.

This makes multiple inheritance more powerful—but also easier to misuse.

## 5. Repeated inheritance / diamond shape

Consider:

```text
       Person
       /    \
 Employee  Student
       \    /
    TeachingAssistant
```

TeachingAssistant inherits through two paths that share Person as an ancestor.

This corresponds to the Diktat's **repeated inheritance** concept.

In Python, inspect:

```python
TeachingAssistant.__mro__
```

The goal is to recognize the structure and method lookup issue, not to master all implementation edge cases.

## 6. Mixin as a focused capability

A mixin should usually represent a small reusable capability rather than the primary domain identity.

Example:

```python
class LoggingMixin:
    def log(self, message):
        print("[LOG]", message)


class Person:
    def __init__(self, name):
        self.name = name


class Doctor(Person, LoggingMixin):
    def diagnose(self):
        self.log("Starting diagnosis")
        print(self.name, "is diagnosing")
```

Here:

```text
Person
→ primary domain superclass

LoggingMixin
→ focused reusable capability
```

## 7. Another mixin example

```python
class ExportMixin:
    def export_text(self):
        return str(self.__dict__)


class Report(ExportMixin):
    def __init__(self, title):
        self.title = title
```

The idea is reuse of a small capability.

Do not treat every helper class as a mixin.

## 8. Multiple inheritance is not automatically better

Ask first:

```text
Does this class truly need behavior
from multiple parent abstractions?
```

If the relationship is really:

```text
has-a
uses
contains
```

composition may be clearer.

This continues the design caution from Module 5–6.

## Main exercise — Employee with capabilities

Model:

```text
Employee
   ▲
   │
Manager
  + LoggingMixin
  + ExportMixin
```

Requirements:

- Employee has `employee_id` and `name`;
- LoggingMixin provides `log(message)`;
- ExportMixin provides `export_text()`;
- Manager inherits Employee plus the two mixin capabilities.

Demonstrate all behaviors.

## Challenge — Teaching Assistant diamond

Model:

```text
       Person
       /    \
 Employee  Student
       \    /
    TeachingAssistant
```

Give Person a method:

```python
describe()
```

Optionally redefine `describe()` in Employee and Student.

Then inspect:

```python
TeachingAssistant.__mro__
```

and predict which `describe()` executes.

## Reflection

Answer:

> When is multiple inheritance useful, and when might composition or single inheritance produce a clearer design?

## Reading

### Inggriani Liem

Focus on:

- multiple inheritance;
- conflicts among inherited features;
- repeated inheritance;
- common-ancestor inheritance structure;
- the warning that inheritance needs careful design.

### OpenStax

Read **13.5 Multiple Inheritance and Mixin Classes**.

## Module 10 package

- [Colab notebook](10_multiple_inheritance_mixins.ipynb)
- [Exercises](exercises.md)
- [Quiz](quiz.md)
- [Assignment](assignment.md)
- [Instructor notes](instructor-notes.md)
- [Mastery checks with worked feedback](../MASTERY_CHECKS.md)

## Next module

Module 10 focuses on inheritance structure.

Module 11 moves from class structure back to runtime objects:

> When two variables refer to objects, what exactly are they referring to?

That leads to:

**Module 11 — Object Lifecycle, References & Object Identity.**
