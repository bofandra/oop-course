# Module 6 Instructor Notes — Inheritance

## Teaching goal

Module 5 taught:

```text
Car has an Engine
Order has OrderItems
Appointment refers to Patient and Doctor
```

Module 6 introduces a different relationship:

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

The Diktat also discusses many advanced inheritance consequences such as multiple inheritance, renaming, subcontracting, and typing effects. Do **not** teach those in detail in Module 6; later modules cover selected advanced topics.

### OpenStax

Use:

- **13.1 Inheritance Basics**
- **13.2 Attribute Access**

Use only the relevant `super()` material from 13.3 as a Python implementation bridge for superclass initialization.

Overriding and polymorphism remain Module 7 topics.

## Suggested session flow

| Approx. duration | Activity |
|---|---|
| 15 min | Review Module 5: has-a vs is-a |
| 25 min | Inheritance concept and terminology |
| 25 min | Python subclass syntax |
| 25 min | Inherited attributes and methods |
| 10 min | Break |
| 25 min | Subclass-specific state/behavior |
| 20 min | `super().__init__()` |
| 30 min | Employee lab |
| 15 min | Inheritance vs composition challenge |
| 10 min | Quiz / bridge to overriding |

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

> Module 5 handled "has-a". Module 6 handles "is-a".

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

> `super().__init__(...)` calls the superclass initializer so shared superclass-defined state is established in one place before the subclass adds its own state.

Do not explain:

- MRO internals;
- cooperative multiple inheritance;
- zero-argument `super()` implementation details.

Those would distract from the Module 6 goal.

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

This links Module 5 and Module 6.

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

For this module, phrase it operationally as a way to reuse superclass initialization. Avoid oversimplified claims about all runtime behavior.

## Quiz administration

The quiz answer key is intentionally not stored in the public repository. Keep the instructor key in a private instructor-controlled location.

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

**Module 7 — Overriding, Polymorphism & Dynamic Binding.**
