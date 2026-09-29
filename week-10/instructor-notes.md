# Week 10 Instructor Notes — Multiple Inheritance & Mixins

## Teaching goal

Week 9 used one general parent with several descendants.

Week 10 introduces:

```text
one child
   ↓
multiple parents
```

The central idea is not "multiple inheritance is powerful."

It is:

> Multiple inheritance is available, but it introduces method-resolution and design complexity that students should be able to recognize.

## Source alignment

### Inggriani Liem

Use the Diktat directly for:

- definition of multiple inheritance;
- conflicts caused by same-name or conflicting inherited features;
- repeated inheritance where multiple parents share a common ancestor;
- inheritance-design caution.

The Diktat also lists Mixin Class / Mixin Inheritance terminology, but it does not provide a detailed Python mixin tutorial.

### OpenStax

Use **13.5 Multiple Inheritance and Mixin Classes** for the Python-facing treatment:

- Python multiple-inheritance syntax;
- method resolution order;
- mixin classes.

Keep this distinction explicit for students.

## Recommended 200-minute flow

| Time | Activity |
|---|---|
| 08:30–08:45 | Review Week 9 inheritance structures |
| 08:45–09:10 | Basic multiple inheritance |
| 09:10–09:35 | Conflicting inherited methods |
| 09:35–10:00 | Python MRO |
| 10:00–10:10 | Break |
| 10:10–10:35 | Repeated/diamond inheritance |
| 10:35–11:00 | Mixin concept |
| 11:00–11:30 | Employee + capabilities lab |
| 11:30–11:40 | Diamond challenge |
| 11:40–11:50 | Quiz / Week 11 bridge |

## Opening example

Use:

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

Ask:

> What capabilities does Lecturer inherit?

Then immediately introduce the more important question:

> What happens if both parents define the same method?

## Conflict example

Use:

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

Have students predict before running.

Then inspect:

```python
C.__mro__
```

Do not begin with the full MRO theory. Let the runtime observation motivate the concept.

## MRO explanation

Use:

> MRO is Python's method-search order across the inheritance hierarchy.

For Week 10, that is enough.

Avoid:

- formal C3 linearization proof;
- metaclass internals;
- advanced `super()` chains.

## Repeated inheritance

Map the Diktat's repeated inheritance concept to a Python diamond:

```text
       Person
       /    \
 Employee  Student
       \    /
    TeachingAssistant
```

Explain that the same ancestor is reached through more than one parent path.

Then inspect Python's MRO.

Do not imply that Python behaves exactly like Eiffel's rename/select mechanisms. Those mechanisms are part of the Diktat's language-specific discussion.

## Mixin

Introduce mixin after students understand multiple inheritance.

Use this distinction:

```text
Person
→ domain identity

LoggingMixin
→ capability
```

Good introductory mixins are:

- LoggingMixin
- ExportMixin
- PrintableMixin

Avoid business-domain hierarchies that make the mixin concept harder to see.

## Important source nuance

Do not say:

> Liem teaches Python mixins.

The Diktat lists mixin terminology, but the detailed Python mixin material is supplied by OpenStax/course implementation.

## Common misconceptions

### 1. Multiple inheritance is always better reuse

No. It introduces resolution/conflict complexity.

### 2. MRO randomly chooses a parent

No. Python uses a deterministic lookup order.

### 3. Mixin should be the main identity of an object

Usually not in these examples. It represents a focused capability.

### 4. Diamond inheritance is automatically an error

No. It is a structure that requires careful method resolution and design reasoning.

### 5. Multiple inheritance replaces composition

No. Has-a/uses relationships may still be clearer with composition.

## Quiz administration

The quiz answer key is intentionally not stored in the public repository. Keep the instructor key in a private lecturer-controlled location.

## Assignment grading notes

Reward students who can explain why the mixin is a capability and why MRO matters.

Do not reward extra complexity such as:

- many unnecessary parents;
- custom metaclasses;
- manual MRO emulation;
- clever `super()` chains that obscure the learning goal.

## What not to teach yet

Avoid deep treatment of:

- C3 algorithm internals;
- cooperative multiple-inheritance constructor edge cases;
- metaclasses;
- protocols/structural typing;
- advanced framework mixin architectures.

## Closing question

End with:

> We have spent several weeks reasoning about class hierarchies. At runtime, however, variables do not contain classes—they refer to objects. What exactly happens when two variables refer to the same object?

That leads directly to:

**Week 11 — Object Lifecycle, References & Object Identity.**
