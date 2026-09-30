# Module 15 — Reusability, Design Patterns & OOP Case Study

> **Run the notebook:** [Open Module 15 in Google Colab](https://colab.research.google.com/github/bofandra/oop-course/blob/main/week-15/15_reusability_patterns_case_study.ipynb)

## Learning outcomes

By the end of this module, learners should be able to:

1. distinguish **code reuse** from **design reuse**;
2. explain a design pattern as a reusable design idea for a recurring problem in a particular context;
3. recognize when variation in behavior may benefit from a Strategy-style object;
4. recognize when object creation may benefit from a Factory Method-style design;
5. refactor a small OO solution to make selected variation points more reusable;
6. explain why a pattern should solve a real design problem rather than merely add abstraction;
7. complete a small end-to-end OOP case study using concepts from previous modules.

## Source alignment

Inggriani Liem explicitly identifies **class library** and **design pattern** as mechanisms for reusability. The Diktat also states that object-oriented reuse can happen not only at code level but also at the **design** level.

The Diktat describes patterns as larger building blocks than individual classes or objects and as common solutions to problems in specific contexts. It lists many pattern names, including **Strategy** and **Factory Method**.

Important scope note:

> The Diktat provides the pattern concept and terminology, but it does not provide the detailed Python implementations used in this module.

Therefore:

```text
Reuse / pattern concept
Strategy & Factory Method terminology
→ sourced from Inggriani Liem

Detailed Python examples
→ course illustrations built from previously taught OOP concepts
```

This module does **not** attempt to teach a catalogue of design patterns.

## From Module 14 to Module 15

Module 14 gave us the lifecycle:

```text
Requirement
→ OOA
→ OOD
→ OOP
→ OOT
```

Module 15 asks:

> When a design problem appears repeatedly, can we reuse the design idea instead of reinventing it?

## 1. Reuse at more than one level

### Code reuse

Examples already used in this course:

```text
inherit a method
reuse a class
import a module
reuse a mixin
```

### Design reuse

A higher-level question:

> Have we seen this collaboration/variation problem before?

A design pattern gives a reusable **structure or idea**, not a finished copy-paste solution.

## 2. What is a pattern?

For this course:

> A pattern is a named, reusable design idea for a recurring problem in a particular context.

A pattern is not:

- a mandatory rule;
- a Python library;
- a replacement for analysis;
- a reason to add more classes to every program.

The problem must come first.

## 3. Recognize a variation problem

Suppose an Order calculates delivery fee this way:

```python
class Order:
    def delivery_fee(self, mode):
        if mode == "pickup":
            return 0
        elif mode == "standard":
            return 15_000
        elif mode == "express":
            return 30_000
```

This works.

But if delivery algorithms keep growing, the Order class must keep changing.

The design question becomes:

> Can the varying delivery behavior live in separate objects?

## 4. Strategy-style design

Make the common operation explicit using the abstract-class technique already learned in Module 9:

```python
from abc import ABC, abstractmethod


class DeliveryStrategy(ABC):
    @abstractmethod
    def fee(self, subtotal):
        pass


class PickupDelivery(DeliveryStrategy):
    def fee(self, subtotal):
        return 0


class StandardDelivery(DeliveryStrategy):
    def fee(self, subtotal):
        return 15_000


class ExpressDelivery(DeliveryStrategy):
    def fee(self, subtotal):
        return 30_000
```

For this course, the abstract superclass makes the common polymorphic contract visible. We intentionally do not introduce protocols or structural-typing machinery here.

Then Order collaborates with one selected strategy:

```python
class Order:
    def __init__(self, delivery_strategy):
        self.items = []
        self.delivery_strategy = delivery_strategy

    def subtotal(self):
        return sum(item.subtotal() for item in self.items)

    def total(self):
        subtotal = self.subtotal()
        return subtotal + self.delivery_strategy.fee(subtotal)
```

Conceptually:

```text
Order
  │
  │ uses
  ▼
Delivery Strategy
  ├── PickupDelivery
  ├── StandardDelivery
  └── ExpressDelivery
```

The variation is moved out of Order.

This reuses ideas learners already know:

- object relationships;
- abstract classes;
- overriding;
- polymorphism;
- dynamic binding;
- responsibility.

## 5. When Strategy-style helps

It can help when:

- one behavior has several interchangeable implementations;
- the caller should not contain a growing type/mode branch;
- new behavior variants are expected;
- each variant has a clear responsibility.

It may be unnecessary when there is only one trivial behavior and no meaningful variation.

## 6. Creation can also vary

Suppose a system creates different notification objects.

A naïve caller might contain:

```python
if channel == "email":
    notification = EmailNotification()
elif channel == "sms":
    notification = SMSNotification()
```

If creation itself becomes a recurring design decision, we can move that responsibility.

## 7. Factory Method-style example

A small course illustration:

```python
from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass


class EmailNotification(Notification):
    def send(self, message):
        print("EMAIL:", message)


class SMSNotification(Notification):
    def send(self, message):
        print("SMS:", message)
```

Creator hierarchy:

```python
class NotificationCreator(ABC):
    @abstractmethod
    def create_notification(self):
        pass

    def notify(self, message):
        notification = self.create_notification()
        notification.send(message)


class EmailNotificationCreator(NotificationCreator):
    def create_notification(self):
        return EmailNotification()


class SMSNotificationCreator(NotificationCreator):
    def create_notification(self):
        return SMSNotification()
```

Usage:

```python
creator = EmailNotificationCreator()
creator.notify("Order confirmed")
```

The creation step is represented by a method that concrete creator subclasses implement.

For this course, focus on the responsibility shift:

```text
caller
  ↓
creator abstraction
  ↓
concrete creator decides which object to build
```

Do not memorize pattern diagrams mechanically.

## 8. Pattern names come after understanding the problem

Recommended order:

```text
1. understand requirement
2. identify responsibility/variation problem
3. make a simple design
4. notice a recurring structure
5. introduce the pattern name
```

Avoid:

```text
learn pattern name
     ↓
force pattern into every project
```

## 9. Case study — Food Ordering System

Requirement:

> A food-ordering system has Customers, MenuItems, OrderItems, and Orders. An Order contains multiple OrderItems. Different delivery methods calculate different delivery fees. After an order is confirmed, the system may send a notification through different channels.

A reasonable initial model:

```text
Customer <──────────── Order
                       │
                       ├── contains ──> OrderItem ── references ──> MenuItem
                       ├── uses ──────> DeliveryStrategy
                       └── can use ───> NotificationCreator
```

## 10. Core model

```python
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class OrderItem:
    def __init__(self, menu_item, quantity):
        self.menu_item = menu_item
        self.quantity = quantity

    def subtotal(self):
        return self.menu_item.price * self.quantity


class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name
```

Then Order focuses on order responsibilities rather than implementing every delivery/notification variant internally.

## 11. End-to-end case-study flow

Use:

```text
Requirement
    ↓
OOA
    ↓
Customer / MenuItem / OrderItem / Order
    ↓
identify varying delivery behavior
    ↓
Strategy-style refactor
    ↓
identify varying notification creation
    ↓
Factory Method-style example
    ↓
OOP implementation
    ↓
OOT tests
    ↓
reflection on whether patterns improved the design
```

## 12. Reuse is not maximum abstraction

A reusable design should still be understandable.

Ask:

> Is this abstraction solving a demonstrated problem?

If not, the simpler design may be better.

This course values:

```text
clear responsibility
+
meaningful collaboration
+
appropriate reuse
```

over pattern count.

## Main exercise — Refactor Delivery Fee

Start from an Order containing:

```python
if delivery_mode == ...
```

Refactor the delivery variation into interchangeable strategy objects.

Required:

- one abstract/common `DeliveryStrategy` contract with `fee(subtotal)`;
- at least three concrete delivery strategies;
- one Order class using the strategy;
- no mode-based branching inside Order total calculation;
- one polymorphic test loop.

## Challenge — Notification Creation

Implement the small Factory Method-style notification example.

Then answer:

> What creation responsibility moved away from the caller?

## Reflection

Answer:

> When does a pattern improve reusability, and when does it merely make a small program harder to understand?

## Reading

### Inggriani Liem

Focus on:

- class library and design pattern as reusability mechanisms;
- reuse beyond code to design;
- pattern as a common solution in a specific context;
- Strategy and Factory Method terminology in the pattern appendix.

### OpenStax

Use previously studied Python OOP chapters as implementation support.

This module does not introduce an additional formal OpenStax design-pattern chapter.

## Module 15 package

- [Colab notebook](15_reusability_patterns_case_study.ipynb)
- [Exercises](exercises.md)
- [Quiz](quiz.md)
- [Assignment](assignment.md)
- [Instructor notes](instructor-notes.md)
- [Mastery checks with worked feedback](../MASTERY_CHECKS.md)

## Next module

Module 15 asks learners to integrate and reuse design ideas.

Module 16 asks them to create and defend a complete OO solution:

**Module 16 — Final Project / Final Test.**

## Course navigation

[← Module 14](../week-14/) · [Course Map](../COURSE_MAP.md) · [Module 16 →](../week-16/)
