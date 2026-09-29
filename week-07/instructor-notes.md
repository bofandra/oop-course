# Week 7 Instructor Notes — Overriding, Polymorphism & Dynamic Binding

## Teaching goal

Week 6 established:

```text
Doctor is a Person
Developer is an Employee
```

Week 7 adds:

```text
same inherited operation name
        ↓
different subclass implementation
        ↓
runtime object decides behavior
```

The key conceptual chain is:

```text
Inheritance
   ↓
Redefinition / Overriding
   ↓
Polymorphism
   ↓
Dynamic Binding
```

## Source alignment

### Inggriani Liem

The Diktat uses the term **redefinition** for redefining inherited features.

It also explicitly treats:

- polymorphism;
- polymorphic attachment;
- dynamic binding.

Its dynamic-binding explanation is that the operation applied at runtime is based on the actual object type at runtime.

Preserve this terminology when explaining the conceptual source.

### OpenStax

Use **13.3 Methods**.

OpenStax explicitly covers:

- overriding inherited methods;
- `super()`;
- polymorphism;
- runtime class type determining which method runs.

The Python term **overriding** is the implementation term used throughout the student material.

## Recommended 200-minute flow

| Time | Activity |
|---|---|
| 08:30–08:45 | Review inheritance from Week 6 |
| 08:45–09:10 | Redefinition / overriding |
| 09:10–09:30 | Replace vs extend with `super()` |
| 09:30–10:00 | Polymorphism |
| 10:00–10:10 | Break |
| 10:10–10:35 | Dynamic binding |
| 10:35–11:05 | Notification live coding |
| 11:05–11:35 | Payroll lab |
| 11:35–11:45 | Shape challenge |
| 11:45–11:50 | UTS bridge |

## Opening example

Start with:

```python
class Person:
    def introduce(self):
        print("I am a person")


class Doctor(Person):
    pass
```

Then ask:

> What if Doctor needs a more specific introduction?

Change to:

```python
class Doctor(Person):
    def introduce(self):
        print("I am a doctor")
```

Explain:

```text
same method name
different inherited-class implementation
```

## Connect terminology carefully

Say:

> In the Diktat, this is discussed under **redefinition** of inherited features. In Python/OpenStax, we normally call this **method overriding**.

This avoids silently replacing the source terminology.

## super()

Show two cases.

Replace:

```python
def introduce(self):
    print("I am a doctor")
```

Extend:

```python
def introduce(self):
    super().introduce()
    print("My role is doctor")
```

Teaching question:

> Do we still want the superclass behavior, or do we want to replace it completely?

## Polymorphism

Use Notification:

```python
for notification in notifications:
    notification.send()
```

Ask:

- Is the call text different?
- Are the runtime objects different?
- Does the behavior differ?

Then define:

> Polymorphism lets one operation name work with multiple object forms.

Do not overcomplicate this with static/dynamic type theory.

## Dynamic binding

Use:

```python
people = [Person(), Doctor(), Patient()]

for person in people:
    person.role()
```

Ask students to predict output before execution.

Then connect to Diktat:

> Dynamic binding means the runtime object determines the implementation that is applied.

## Avoid type branching

Compare:

```python
if employee_type == "full_time":
    ...
elif employee_type == "part_time":
    ...
```

with:

```python
employee.calculate_pay()
```

The point is not that every `if` is bad.

The point is:

> If behavior varies naturally by subtype, polymorphism lets the variation live in the objects.

## Overriding vs overloading

Keep this short.

```text
Overriding
- inheritance context
- subclass changes inherited behavior

Overloading
- same operation name has multiple meanings/forms
```

Do not teach Python operator overloading in depth here. Week 12 covers that.

## Common misconceptions

### 1. Same method name always means overriding

No. The classes must be in an inheritance relationship for the Python/OpenStax overriding example.

### 2. Polymorphism requires an abstract class

No. Week 7 examples work without abstract classes.

### 3. super() is mandatory in every overridden method

No. Use it when superclass behavior should be reused/extended.

### 4. Dynamic binding means Python randomly chooses a method

No. The actual runtime object's class determines the applicable implementation.

## Quiz administration

The quiz answer key is intentionally not stored in the public repository. Keep the instructor key in a private lecturer-controlled location.

## Assignment grading notes

The central evidence is:

```python
for employee in employees:
    employee.calculate_pay()
```

with different subclass results.

Do not reward a solution that recreates polymorphism through a long type-checking chain.

Also do not penalize minor numerical choices if the subclass calculations are internally consistent and clearly explained.

## What not to teach yet

Avoid:

- abstract base classes;
- `ABC`;
- multiple inheritance;
- mixins;
- detailed MRO;
- operator overloading;
- design patterns.

## UTS preparation

Week 7 is the last new teaching week before the Mid Test.

Use the final minutes to remind students that UTS integrates:

```text
Week 1 — objects
Week 2 — classes/instances
Week 3 — state/behavior
Week 4 — encapsulation
Week 5 — relationships
Week 6 — inheritance
Week 7 — overriding/polymorphism
```

## Closing question

End with:

> Can you receive a new problem and decide which concepts from Weeks 1–7 actually belong in the solution?

That is the purpose of:

**Week 8 — Mid Test.**
