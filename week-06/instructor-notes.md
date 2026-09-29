# Week 6 Instructor Notes — Inheritance

## Teaching goal

Week 5 taught:

```text
Car has an Engine
Order has OrderItems
Appointment refers to Patient and Doctor
```

Week 6 introduces a different relationship:

```text
Doctor is a Person
Developer is an Employee
```

The key learning goal is not Python syntax. It is deciding whether inheritance is **semantically appropriate**.

## Source alignment

### Inggriani Liem

Use the Diktat framing that:

- a child/descendant class inherits attributes and methods from an ancestor/parent class;
- inheritance is a fundamental OO concept;
- inheritance should be designed carefully rather than added arbitrarily;
- **is-a** is the conceptual relationship between a general class and a more specific subclass;
- a subclass object must still be an object of the superclass concept;
- has-a should not be confused with inheritance.

The Diktat also discusses many advanced inheritance consequences such as multiple inheritance, renaming, subcontracting, and typing effects. Do **not** teach those in detail in Week 6; later weeks cover selected advanced topics.

### OpenStax

Use:

- **13.1 Inheritance Basics**
- **13.2 Attribute Access**

Use only the relevant `super()` material from 13.3 as a Python implementation bridge for superclass initialization.

Overriding and polymorphism remain Week 7 topics.

## Recommended 200-minute flow

| Time | Activity |
|---|---|
| 08:30–08:45 | Review Week 5: has-a vs is-a |
| 08:45–09:10 | Inheritance concept and terminology |
| 09:10–09:35 | Python subclass syntax |
| 09:35–10:00 | Inherited attributes and methods |
| 10:00–10:10 | Break |
| 10:10–10:35 | Subclass-specific state/behavior |
| 10:35–10:55 | `super().__init__()` |
| 10:55–11:25 | Employee lab |
| 11:25–11:40 | Inheritance vs composition challenge |
| 11:40–11:50 | Quiz / bridge to overriding |

## Opening question

Write:

```text
Car ______ Engine
Doctor ______ Person
```

Ask students to fill the blanks.

Expected:

```text
Car has an Engine
Doctor is a Person
```

Then say:

> Week 5 handled "has-a". Week 6 handles "is-a".

## Basic inheritance example

Start with:

```python
class Person:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(self.name)


class Doctor(Person):
    pass
```

Then:

```python
doctor = Doctor("Dr. Andi")
doctor.display_name()
```

Ask:

- Where was `display_name()` defined?
- Why can Doctor use it?
- Is Doctor still conceptually a Person?

## Subclass specialization

Then add:

```python
class Doctor(Person):
    def __init__(self, name, specialty):
        super().__init__(name)
        self.specialty = specialty

    def diagnose(self):
        print("Diagnosing")
```

Draw:

```text
Person
- name
- display_name()

Doctor
- inherited name
- inherited display_name()
- specialty
- diagnose()
```

## Teaching super()

Use a deliberately narrow explanation:

> `super().__init__(...)` lets the subclass reuse the superclass initialization before adding subclass-specific state.

Do not explain:

- MRO internals;
- cooperative multiple inheritance;
- zero-argument `super()` implementation details.

Those would distract from the Week 6 goal.

## Important caution

The Diktat explicitly warns that inheritance should be designed carefully.

Use this bad example:

```python
class Engine:
    def start(self):
        print("start")


class Car(Engine):
    pass
```

Ask:

> Is a Car an Engine?

No.

Then redesign:

```python
class Car:
    def __init__(self, engine):
        self.engine = engine
```

This links Week 5 and Week 6.

## isinstance()

Use lightly:

```python
isinstance(doctor, Doctor)
isinstance(doctor, Person)
```

The teaching point is conceptual:

```text
Doctor is a Person.
```

Do not expand into Python's full type system.

## Common misconceptions

### 1. Inheritance is just code reuse

Correct with the is-a test.

### 2. A subclass gets only methods

Clarify that inherited features include state/attributes and behavior in the conceptual model.

### 3. Every related class should share a parent

No. Use inheritance only when the specialized/general relationship makes sense.

### 4. super() means "the parent class"

For this week, phrase it operationally as a way to reuse superclass initialization. Avoid oversimplified claims about all runtime behavior.

## Quiz answer key

1. **B**
2. **C**
3. **B**
4. **B**
5. **C**
6. Superclass = more general class; subclass = more specialized class that inherits from it.
7. Because inheritance communicates an is-a semantic relationship; code similarity alone does not make one concept a specialized form of another.
8. Example: Doctor inherits `name`; Doctor adds `specialty`.
9. It gains inherited superclass features and can add more specialized features.
10. Because Week 6 focuses first on inheritance itself; Week 7 studies replacing inherited behavior and the polymorphic consequences.

## Assignment grading notes

Reward meaningful modelling more than clever code.

A simple correct hierarchy is better than unnecessary extra inheritance levels.

If a student duplicates Employee initialization instead of using `super().__init__()`, deduct only against the relevant criterion; the deeper purpose remains understanding the inheritance relationship.

## What not to teach yet

Avoid detailed coverage of:

- method overriding;
- polymorphism;
- dynamic binding;
- abstract classes;
- multiple inheritance;
- MRO;
- mixins.

## Closing question

End with:

> A Doctor can inherit `display_name()` from Person. But what if Doctor needs a different implementation of a behavior that already exists in Person?

That leads directly to:

**Week 7 — Overriding, Polymorphism & Dynamic Binding.**
