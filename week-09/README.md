# Week 9 — Abstract Classes & Inheritance Structures

## Learning outcomes

By the end of this session, students should be able to:

1. distinguish **concrete** classes from **abstract/deferred** classes;
2. explain why some superclass concepts are useful as specifications but should not be instantiated directly;
3. identify a behavior that subclasses are expected to implement;
4. design a general-to-specific inheritance hierarchy;
5. explain the difference between an abstract superclass and its concrete subclasses;
6. translate the abstract-class idea into Python using `ABC` and `@abstractmethod` as an implementation technique;
7. avoid making every superclass abstract without a clear modelling reason.

## Source alignment

Inggriani Liem explicitly discusses **deferred feature & class** as a mechanism needed for abstraction. A deferred class contains features that are known at declaration/design time but are implemented by descendant classes. The Diktat also distinguishes ordinary/concrete classes from abstract/deferred classes that are not intended to produce direct runtime objects.

The Diktat's hierarchy discussion also notes that abstract classes are often placed near the top of an inheritance hierarchy, while classes become more specific toward the bottom and can then be instantiated.

OpenStax is used this week for inheritance-structure context, especially hierarchical inheritance. OpenStax does **not** provide a standalone treatment of Python `abc.ABC` as the formal source for abstract classes in this course.

Therefore:

```text
Abstract/deferred class concept
→ sourced from Inggriani Liem

Python ABC / @abstractmethod
→ implementation translation used in this course
```

## From Week 7–8 to Week 9

Before UTS, students used concrete inheritance:

```text
Employee
├── FullTimeEmployee
├── PartTimeEmployee
└── Freelancer
```

But consider this question:

> Does it always make sense to create a plain Employee object?

Sometimes yes.

Sometimes the superclass is intended only to describe shared structure and required behavior for more specific subclasses.

That is where abstract/deferred classes become useful.

## 1. Concrete class

A concrete class has enough implementation to create meaningful objects directly.

```python
class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"My name is {self.name}"
```

A direct Person object can make sense:

```python
person = Person("Alya")
```

## 2. Abstract / deferred class

Suppose we model shapes:

```text
Shape
├── Rectangle
└── Circle
```

What should this mean?

```python
class Shape:
    def area(self):
        return 0
```

This technically runs, but semantically it is weak.

A generic Shape may not have enough information to calculate a meaningful area.

Instead, the superclass can specify:

> Every concrete Shape must provide an area operation.

That is the abstract/deferred idea.

## 3. Deferred feature → concrete implementation

Conceptually:

```text
Shape
└── area()   ← known/required, not yet concretely implemented

Rectangle
└── area()   ← concrete implementation

Circle
└── area()   ← concrete implementation
```

This closely matches the Diktat's distinction between **deferring** at design time and **effecting** in implementation.

## 4. Python implementation bridge: ABC

Python can represent the idea with:

```python
from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass
```

Then:

```python
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
```

Now Rectangle provides the required concrete implementation.

For this course, understand the Python syntax as a **translation of the abstract/deferred-class concept**, not as terminology directly sourced from the Diktat.

## 5. An abstract class can still have concrete features

Abstract does not mean "everything must be empty."

Example:

```python
from abc import ABC, abstractmethod


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

Here:

```text
Concrete/shared:
- employee_id
- name
- display_name()

Required from subclass:
- calculate_pay()
```

## 6. Concrete subclasses

```python
class FullTimeEmployee(Employee):
    def __init__(self, employee_id, name, salary):
        super().__init__(employee_id, name)
        self.salary = salary

    def calculate_pay(self):
        return self.salary
```

This combines concepts students already know:

- inheritance;
- `super()`;
- overriding;
- polymorphism.

Week 9 adds one design idea:

> The superclass may define behavior that must exist without providing its concrete implementation.

## 7. Hierarchical inheritance

A general superclass can have several specialized subclasses:

```text
Notification
├── EmailNotification
├── SMSNotification
└── PushNotification
```

or:

```text
Payment
├── CashPayment
├── CardPayment
└── EWalletPayment
```

The hierarchy expresses:

```text
general concept
      ↓
more specific concepts
```

## 8. Not every superclass should be abstract

Example:

```text
Person
├── Doctor
└── Patient
```

A direct Person object may still be meaningful in some systems.

So the right question is not:

> Does this class have subclasses?

Instead ask:

> Is this superclass itself a meaningful complete concept that should be instantiated directly?

If yes, it may remain concrete.

## Main exercise — Payment

Design:

```text
Payment
├── CashPayment
├── CardPayment
└── EWalletPayment
```

Payment should define a required:

```python
pay(amount)
```

Each concrete subclass provides its own implementation.

Use one list of Payment objects and call:

```python
for payment in payments:
    payment.pay(100_000)
```

## Challenge — Should the Superclass Be Abstract?

For each model, decide whether the top class should probably be abstract or concrete:

1. Shape → Rectangle / Circle
2. Person → Doctor / Patient
3. Payment → CashPayment / CardPayment
4. Vehicle → Car / Motorcycle
5. Document → Invoice / Report

There may be more than one defensible answer.

Explain your modelling assumption.

## Reflection

Answer:

> What problem does an abstract/deferred class solve that a normal concrete superclass does not?

## Reading

### Inggriani Liem

Focus on:

- deferred feature & class;
- deferring vs effecting;
- abstract class / deferred class;
- abstract classes near the general/top level of an inheritance hierarchy;
- descendants implementing deferred features.

### OpenStax

Review the inheritance hierarchy material, especially hierarchical inheritance.

Python `ABC` / `@abstractmethod` is used as a course implementation technique rather than as a formal OpenStax topic.

## Week 9 package

- [Colab notebook](09_abstract_classes.ipynb)
- [Exercises](exercises.md)
- [Quiz](quiz.md)
- [Assignment](assignment.md)
- [Instructor notes](instructor-notes.md)

## Next week

Week 9 asks:

> How can one general abstraction require concrete behavior from several descendants?

Week 10 asks:

> What happens when a class inherits from **more than one parent**?

That leads directly to:

**Week 10 — Multiple Inheritance & Mixins.**
