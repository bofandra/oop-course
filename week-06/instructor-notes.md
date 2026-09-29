# Week 6 Instructor Notes — Inheritance

## Teaching goal

Students should understand inheritance first as a **model relationship**, not merely as a code-reuse trick.

The core mental model is:

```text
general class
    ↓
specialized class
```

or:

```text
Doctor is a Person
Developer is an Employee
```

## Source alignment

### Inggriani Liem

Use the Diktat directly:

- a descendant/child class inherits attributes and methods from an ancestor/parent class;
- inheritance is a fundamental OO concept;
- the **is-a** relationship connects a general class with a more specific subclass;
- a subclass instance must still be a valid instance of its superclass conceptually;
- inheritance should be designed carefully and not added arbitrarily;
- has-a and is-implemented-using relationships should not be confused with inheritance.

Do not expand into multiple inheritance yet. The Diktat discusses it, but it is reserved for Week 10.

### OpenStax

Use:

- **13.1 Inheritance Basics**
- **13.2 Attribute Access**

OpenStax 13.1 explicitly covers is-a vs has-a, superclass/subclass terminology, inheritance syntax, and inherited methods.

OpenStax 13.2 covers inherited instance attributes and adding subclass-specific state.

For `super().__init__()`, use only the relevant small portion of **13.3 Methods**. Do not teach overriding or polymorphism yet.

## Recommended 200-minute flow

| Time | Activity |
|---|---|
| 08:30–08:45 | Review Week 5: has-a vs is-a |
| 08:45–09:10 | Inheritance concept and terminology |
| 09:10–09:35 | Python subclass syntax |
| 09:35–10:00 | Inherited attributes and methods |
| 10:00–10:10 | Break |
| 10:10–10:30 | Subclass-specific state/behavior |
| 10:30–10:50 | `super().__init__()` |
| 10:50–11:25 | Employee hierarchy lab |
| 11:25–11:40 | Inheritance vs composition challenge |
| 11:40–11:50 | Quiz / bridge to overriding |

## Opening review

Write:

```text
Car has Engine
Doctor is Person
```

Ask:

> Which relationship belongs to Week 5, and which one suggests inheritance?

Expected:

- Car/Engine → has-a
- Doctor/Person → is-a

Then introduce inheritance only after that semantic distinction is clear.

## Terminology

Use both source terminologies:

```text
superclass / parent / ancestor
subclass / child / descendant
```

For the rest of teaching, prefer **superclass** and **subclass** because that matches OpenStax.

## Python syntax

Use the smallest possible example:

```python
class Person:
    def display_name(self):
        print("Person")

class Doctor(Person):
    pass
```

Ask:

> Which method did Doctor define itself?

None.

> Can a Doctor instance still call display_name()?

Yes, because it inherits the method.

## Subclass specialization

Then add:

```python
class Doctor(Person):
    def diagnose(self):
        print("Diagnosing")
```

Explain:

```text
inherit general features
+
add specific features
```

Avoid method overriding at this point.

## Using super().__init__()

Use:

```python
class Person:
    def __init__(self, name):
        self.name = name

class Doctor(Person):
    def __init__(self, name, specialty):
        super().__init__(name)
        self.specialty = specialty
```

Teaching wording:

> First initialize the inherited Person state, then initialize the Doctor-specific state.

Do not explain MRO, cooperative inheritance, or multiple inheritance behavior here.

## Inheritance is not just reuse

This is one of the most important Week 6 messages.

Use:

```text
Wrong question:
"Can I reuse code?"

Better question:
"Is this concept genuinely
a specialized kind of that concept?"
```

The Diktat explicitly warns that poorly designed inheritance can make implementation difficult.

## Useful is-a test

Ask students to say the sentence aloud:

```text
A Doctor is a Person.
A Manager is an Employee.
A Car is an Engine.
```

The sentence should make domain sense.

This is a heuristic, not a complete formal proof.

## Common misconceptions

### 1. Inheritance means "contains"

Correct with:

```text
Car has Engine
not
Car is Engine
```

### 2. Parent automatically gets child behavior

A Person instance does not automatically gain Doctor-only methods.

### 3. Inheritance exists only to avoid duplication

Code reuse can be a benefit, but the relationship should still model a meaningful is-a relationship.

### 4. Subclass should redefine everything

No. Inherited features are available precisely so the subclass does not have to duplicate them.

### 5. super() means "call any parent method automatically"

Keep the Week 6 use narrow: `super().__init__()` for superclass initialization.

## Live coding sequence

Recommended:

```text
Person
  ↓
Doctor(Person)
  ↓
inherit display_name()
  ↓
add specialty
  ↓
add diagnose()
  ↓
use super().__init__()
  ↓
add Patient(Person)
```

Then move to Employee / Developer / Designer.

## Quiz answer key

1. **B**
2. **B**
3. **C**
4. **C**
5. **B**
6. Superclass is the more general class; subclass is the more specialized class that inherits from it.
7. Because a Car is not a specialized kind of Engine; it has an Engine.
8. It may inherit shared Person state/behavior such as name and display_name().
9. Duplicated code does not prove an is-a relationship; inheritance should represent domain meaning.
10. Any syntactically correct `class Student(Person): ...` example is acceptable.

## Assignment grading notes

Reward:

- correct semantic is-a relationship;
- correct superclass/subclass direction;
- inherited feature use;
- simple subclass specialization;
- correct use of `super().__init__()`.

Do not reward unnecessary abstraction.

If students override methods, acknowledge that it works but tell them overriding is assessed next week.

## What not to teach yet

Avoid detailed treatment of:

- overriding;
- `super().method()` for extending overridden behavior;
- polymorphism;
- dynamic binding;
- abstract classes;
- multiple inheritance;
- MRO;
- mixins.

## Closing question

End with:

> Doctor inherits display_name() from Person. But what if Doctor needs a different version of a method that Person already defines?

That leads directly to:

**Week 7 — Overriding, Polymorphism & Dynamic Binding.**
