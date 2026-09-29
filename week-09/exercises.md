# Week 9 Exercises — Abstract Classes & Inheritance Structures

## Exercise 1 — Concrete or Abstract?

For each class below, decide whether it is likely to be concrete or abstract in the stated model:

1. Shape in a geometry program where only Rectangle and Circle are drawable.
2. Person in a population registry where generic Person records are allowed.
3. Payment in a checkout system where only CashPayment, CardPayment, and EWalletPayment can execute payment.
4. Vehicle in a fleet system that allows generic Vehicle records.

Explain your assumption.

---

## Exercise 2 — Weak Superclass Design

Consider:

```python
class Shape:
    def area(self):
        return 0
```

Answer:

1. Why might `Shape().area() == 0` be semantically weak?
2. What requirement should subclasses satisfy instead?
3. How does an abstract/deferred class express that requirement?

---

## Exercise 3 — Build an Abstract Shape

Using Python's `abc` module, create:

```text
Shape
├── Rectangle
└── Circle
```

`Shape` requires:

```python
area()
```

Rectangle and Circle must each provide a concrete implementation.

---

## Exercise 4 — Shared Concrete Behavior

Create an abstract `Employee` class that has:

- `employee_id`
- `name`
- concrete `display_name()`
- abstract `calculate_pay()`

Then implement:

- `FullTimeEmployee`
- `PartTimeEmployee`

Explain which parts are shared and which parts are deferred to subclasses.

---

## Exercise 5 — Incomplete Subclass

Create a subclass of an abstract class but deliberately omit one required abstract method.

Try to instantiate the subclass.

Record what happens and explain why.

---

## Exercise 6 — Hierarchical Inheritance

Design:

```text
Notification
├── EmailNotification
├── SMSNotification
└── PushNotification
```

Decide:

1. Should Notification be abstract?
2. Which behavior should be required?
3. Which state/behavior could remain concrete/shared?

Explain your model before coding.

---

## Exercise 7 — Not Every Parent Is Abstract

Consider:

```text
Person
├── Doctor
└── Patient
```

Give one scenario where Person should remain concrete.

Give another scenario where making Person abstract could be reasonable.

The goal is to show that abstractness depends on the domain model, not merely on having subclasses.

---

## Challenge — Payment Hierarchy

Create:

```text
Payment
├── CashPayment
├── CardPayment
└── EWalletPayment
```

Requirements:

- Payment cannot be instantiated directly.
- Payment requires `pay(amount)`.
- Each concrete subclass implements `pay(amount)`.
- At least one shared concrete method or shared state should live in Payment.
- Call `pay()` polymorphically through a list of Payment objects.

Explain how this combines inheritance, overriding, polymorphism, and abstract-class design.
