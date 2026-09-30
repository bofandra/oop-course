# Week 9 Instructor Notes — Abstract Classes & Inheritance Structures

## Teaching goal

After the Mid Test, students already know:

```text
Inheritance
Overriding
Polymorphism
Dynamic Binding
```

Week 9 adds a design-level distinction:

```text
Concrete superclass
vs
Abstract/deferred superclass
```

The key question is:

> Should this superclass itself represent a complete object that we want to instantiate?

## Source alignment

### Inggriani Liem

This week is primarily grounded in the Diktat.

Use these source ideas:

- abstract/deferred classes support abstraction;
- a deferred class contains deferred features that are known during declaration/design but implemented by descendants;
- the Diktat describes the transition from deferred to effective implementation;
- abstract/deferred classes cannot be directly instantiated as meaningful objects;
- abstract classes are commonly used near the general/top level of inheritance structures, with more concrete classes lower in the hierarchy.

Preserve the Diktat terms **deferred**, **effecting**, and **concrete/effective implementation** when presenting the conceptual origin.

### OpenStax

Use OpenStax only for inheritance-structure reinforcement, especially hierarchical inheritance.

Do **not** claim that OpenStax provides a standalone abstract-class chapter or directly teaches Python `abc.ABC` as the source of this week's concept.

### Python bridge

This course translates the Diktat's abstract/deferred concept to Python using:

```python
from abc import ABC, abstractmethod
```

and:

```python
@abstractmethod
```

State explicitly:

> This is the Python implementation technique we are using. The conceptual basis comes from the Diktat.

## Suggested session flow

| Approx. duration | Activity |
|---|---|
| 15 min | Post-UTS review: superclass problems |
| 25 min | Concrete vs abstract/deferred class |
| 25 min | Deferred feature and effecting |
| 25 min | Python ABC implementation bridge |
| 10 min | Break |
| 25 min | Abstract class with shared concrete behavior |
| 25 min | Hierarchical inheritance |
| 30 min | Payment lab |
| 10 min | Abstract-or-concrete challenge |
| 10 min | Quiz / bridge to Week 10 |

## Opening example

Use:

```python
class Shape:
    def area(self):
        return 0
```

Ask:

> Is a generic Shape with area 0 a meaningful concrete object?

Then clarify:

> Sometimes a superclass should specify that an operation must exist without pretending to know its concrete implementation.

## Deferred → effective

Draw:

```text
Shape.area()
   deferred
      ↓
Rectangle.area()
   effective
      ↓
Circle.area()
   effective
```

Use the Diktat terminology first.

Then map it to Python:

```text
deferred feature
      ↓
@abstractmethod

concrete/effective descendant implementation
      ↓
normal overridden method
```

## Python ABC demonstration

Use:

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
```

Then show a complete Rectangle subclass.

Have students try instantiating:

```python
Shape()
```

and an incomplete subclass.

Let Python's error make the rule visible.

## Abstract class can contain concrete behavior

Important misconception to prevent:

> Abstract class = class containing only empty methods.

Counterexample:

```python
class Employee(ABC):
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name

    def display_name(self):
        return self.name

    @abstractmethod
    def calculate_pay(self):
        pass
```

The class can contain:

- shared state;
- shared concrete behavior;
- required deferred behavior.

## Not every superclass is abstract

Use Person:

```text
Person
├── Doctor
└── Patient
```

Ask:

> Is a plain Person object meaningful in our system?

If yes, Person may be concrete.

This keeps students from mechanically converting every parent class into an ABC.

## Common misconceptions

### 1. An abstract class is just a superclass with subclasses

False. The important point is incompleteness/non-instantiability in the model.

### 2. Every method in an abstract class must be abstract

False.

### 3. ABC is the source concept

No. ABC is the Python technique used to express the Diktat's abstract/deferred concept.

### 4. Abstract class and interface are always identical

Do not introduce a broad cross-language interface taxonomy here. Stay with the source material and Python example.

### 5. Abstract classes replace polymorphism

No. They work with inheritance/overriding/polymorphism and can make required polymorphic behavior explicit.

## Quiz administration

The quiz answer key is intentionally not stored in the public repository. Keep the instructor key in a private lecturer-controlled location.

## Assignment grading notes

Reward design reasoning.

A technically correct use of `ABC` is not enough if the student cannot explain why the superclass should be abstract.

Likewise, do not penalize a student who argues that a superclass should remain concrete when the stated domain assumptions make direct instances meaningful.

## What not to teach yet

Avoid:

- multiple inheritance;
- mixins;
- MRO;
- diamond problem;
- metaclasses;
- Protocol;
- structural subtyping;
- advanced typing.

## Closing question

End with:

> A class can now inherit one abstract/general parent. What changes when it inherits behavior from more than one parent?

That leads directly to:

**Week 10 — Multiple Inheritance & Mixins.**
