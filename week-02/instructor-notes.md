# Week 2 Instructor Notes — Classes, Objects & Instances

## Teaching goal

Week 1 established the mental model:

```text
Object
├── Identity
├── State
└── Behavior
```

Week 2 turns that model into Python.

The key learning transition is:

```text
Class = definition

Object / Instance = one runtime instance
created from that definition
```

Students should leave the session comfortable creating multiple instances with different state.

## Source alignment

### Inggriani Liem

The Diktat states that a class is a **static description** of the objects that may be created from it, while at runtime the program has objects that are instances of the class.

It also connects attributes with object state and describes constructor/creation procedures as the mechanism by which objects are created/initialized.

Use that framing as the conceptual basis.

### OpenStax

Use **11.2 Classes and instances** for the Python implementation:

- defining a class;
- creating instances;
- `__init__()`;
- `self`;
- instance attributes;
- class attributes.

Use only the beginning of **11.3 Instance methods** to show a simple method that reads/displays state. Save meaningful state-changing behavior and responsibility reasoning for Week 3.

## Recommended 200-minute flow

| Time | Activity |
|---|---|
| 08:30–08:45 | Review Week 1: class vs object concept |
| 08:45–09:10 | Python class definition and instantiation |
| 09:10–09:40 | `__init__()` and instance state |
| 09:40–10:00 | Understanding `self` |
| 10:00–10:10 | Break |
| 10:10–10:35 | Instance attributes vs class attributes |
| 10:35–11:10 | Live coding: Student |
| 11:10–11:35 | Colab exercise + Product challenge |
| 11:35–11:50 | Quiz / reflection / bridge to Week 3 |

## Opening review

Ask students:

> Yesterday we said Patient can be a class and Budi can be a particular patient object. How do we represent that distinction in Python?

Start with:

```python
class Patient:
    pass

patient_1 = Patient()
patient_2 = Patient()
```

Ask:

- How many class definitions?
- How many runtime objects?
- Are the two objects the same object?

Do not yet explain object references in depth; that belongs to Week 11.

## Teaching `__init__()`

Move from an empty instance to useful state:

```python
class Patient:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

Then:

```python
patient_1 = Patient("Budi", 30)
patient_2 = Patient("Siti", 25)
```

Draw:

```text
Patient class
   │
   ├── patient_1
   │     name = Budi
   │     age  = 30
   │
   └── patient_2
         name = Siti
         age  = 25
```

The important concept is **independent instance state**.

## Teaching `self`

Use one simple sentence:

> Inside an instance method, `self` refers to the particular instance involved in that method call.

Then:

```python
patient_1.display_info()
patient_2.display_info()
```

Ask students what `self.name` refers to in each call.

Avoid diving into method-binding internals.

## Instance vs class attributes

Use:

```python
class Student:
    university = "TANRI ABENG UNIVERSITY"

    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
```

Draw:

```text
Student class
- university = TAU

student_1
- student_id = S001
- name = Alya

student_2
- student_id = S002
- name = Bima
```

Ask:

> If every student can have a different name, where should `name` live?

> If this simplified model assumes every student belongs to the same university, where can `university` live?

Keep the model simple. Class attributes have subtleties in Python, but those subtleties are not the learning target.

## Common misconceptions

### Misconception 1: the class is the same as one object

Correct with:

```text
class definition
≠
one particular instance
```

### Misconception 2: `self` is the class

Use two instances and call the same method on both.

### Misconception 3: every attribute should be a class attribute

Ask whether changing one student's email should change every student's email.

### Misconception 4: `__init__()` should contain all program logic

Week 2 uses `__init__()` to establish initial state. Behavior design comes later.

## Live coding sequence

Recommended order:

```text
class Student: pass
        ↓
create two instances
        ↓
add __init__
        ↓
store student_id and name
        ↓
add class attribute university
        ↓
add display_info()
```

Do not jump directly to a fully finished class.

## Quiz administration

The quiz answer key is intentionally not stored in the public repository. Keep the instructor key in a private lecturer-controlled location.

## Assignment grading notes

Focus on whether students understand:

- one definition vs many instances;
- instance-specific state;
- class-level shared information;
- the role of `self`.

Do not reward extra complexity.

If a student introduces inheritance, property decorators, validation frameworks, dataclasses, or other advanced mechanisms, grade only what is relevant to Week 2 and encourage a simpler solution.

## What not to teach yet

Avoid detailed coverage of:

- encapsulation and private conventions;
- business-rule validation;
- object relationships;
- inheritance;
- overriding;
- polymorphism;
- object identity/reference internals;
- operator overloading.

## Closing question

End with:

> We can now create objects with state. But should outside code directly manipulate every attribute, or should the object provide meaningful behavior to manage its own state?

First answer the simpler part:

> What kinds of actions naturally belong to the object itself?

That leads directly to:

**Week 3 — Attributes, Methods, State & Behavior.**
