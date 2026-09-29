# Week 7 Exercises — Overriding, Polymorphism & Dynamic Binding

## Exercise 1 — Override a Method

Create:

```python
class Person:
    def introduce(self):
        print("I am a person")
```

Then create `Student(Person)` and override `introduce()`.

Demonstrate that:

```python
Person().introduce()
Student().introduce()
```

produce different behavior.

---

## Exercise 2 — Replace or Extend?

Create a superclass method:

```python
display_info()
```

Then make one subclass:

1. completely replace it;
2. another subclass call `super().display_info()` and add more output.

Explain the difference.

---

## Exercise 3 — Polymorphic Calls

Create:

- `EmailNotification`
- `SMSNotification`
- `PushNotification`

Each has:

```python
send()
```

Put all objects in one list and call:

```python
notification.send()
```

inside one loop.

Do not use type checks.

---

## Exercise 4 — Dynamic Binding Prediction

Before running:

```python
class Animal:
    def speak(self):
        print("Animal")

class Cat(Animal):
    def speak(self):
        print("Cat")

class Dog(Animal):
    def speak(self):
        print("Dog")

animals = [Animal(), Cat(), Dog()]

for animal in animals:
    animal.speak()
```

write the expected output and explain why each method is selected.

---

## Exercise 5 — Payroll

Model:

```text
Employee
├── FullTimeEmployee
├── PartTimeEmployee
└── Freelancer
```

All expose:

```python
calculate_pay()
```

but calculate it differently.

Use one loop to calculate all pay values.

---

## Exercise 6 — Remove Type Branching

Rewrite this idea:

```python
if employee_type == "full_time":
    ...
elif employee_type == "part_time":
    ...
elif employee_type == "freelancer":
    ...
```

using subclasses and polymorphism.

Explain what changed in the design.

---

## Exercise 7 — Overriding vs Overloading

In one paragraph, explain:

```text
overriding
vs
overloading
```

For Week 7, focus on overriding. Operator overloading is taught in Week 12.

---

## Challenge — Shape

Create:

```text
Shape
├── Rectangle
└── Circle
```

Both subclasses implement `area()`.

Create several shape objects and calculate each area through one loop.

Do not use abstract classes yet.
