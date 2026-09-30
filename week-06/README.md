# Module 6 — Inheritance

## Learning outcomes

By the end of this session, students should be able to:

1. explain inheritance as an **is-a** relationship between a more general class and a more specific class;
2. distinguish **superclass** and **subclass**;
3. define a Python subclass using inheritance syntax;
4. access attributes and methods inherited from a superclass;
5. extend a subclass with additional state and behavior;
6. use `super().__init__()` as a simple way to reuse superclass initialization;
7. decide when inheritance is appropriate and when a **has-a** relationship is more accurate.

## Source alignment

Inggriani Liem describes inheritance as a relationship in which a descendant/child class inherits attributes and methods from an ancestor/parent class. The Diktat also emphasizes that inheritance should be designed carefully rather than added arbitrarily, and connects inheritance with the **is-a** relationship between a general class and a more specific class.

OpenStax 13.1 covers **is-a vs has-a**, superclass/subclass terminology, Python inheritance syntax, and inherited attributes/methods. OpenStax 13.2 covers inherited instance attributes and subclass-specific attributes.

This module also uses `super().__init__()` only as a small Python implementation bridge for superclass initialization; OpenStax introduces `super()` in 13.3. Method overriding and polymorphism remain the formal focus of Module 7.

## From Module 5 to Module 6

Module 5:

```text
Car has an Engine
Order has OrderItems
Appointment has Patient/Doctor references
```

Module 6 asks:

> What if one class really is a more specialized kind of another class?

```text
Doctor is a Person
Patient is a Person
Developer is an Employee
```

## 1. The is-a test

Before using inheritance, try to say:

```text
A <subclass> is a <superclass>.
```

Examples:

```text
Doctor is a Person      ✓
Patient is a Person     ✓
Developer is an Employee ✓

Car is an Engine        ✗
Order is an OrderItem   ✗
```

The last two are object relationships, not inheritance.

## 2. Superclass and subclass

Start with a general class:

```python
class Person:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(self.name)
```

Then define a more specific class:

```python
class Doctor(Person):
    pass
```

Usage:

```python
doctor = Doctor("Dr. Andi")
doctor.display_name()
```

The Doctor instance can use behavior inherited from Person.

## 3. Subclass specialization

A subclass can add state or behavior that is more specific.

```python
class Doctor(Person):
    def __init__(self, name, specialty):
        self.name = name
        self.specialty = specialty

    def diagnose(self):
        print(
            self.name,
            "is diagnosing a patient"
        )
```

Conceptually:

```text
Person
- name
- display_name()

Doctor
- inherited Person features
- specialty
- diagnose()
```

## 4. Reusing superclass initialization with super()

Instead of repeating superclass initialization:

```python
class Doctor(Person):
    def __init__(self, name, specialty):
        super().__init__(name)
        self.specialty = specialty
```

For Module 6, read this simply as:

> Initialize the Person part of this Doctor, then initialize Doctor-specific state.

Do not go into method resolution order or cooperative multiple inheritance here.

## 5. One superclass, multiple specialized subclasses

```python
class Person:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(self.name)


class Doctor(Person):
    def __init__(self, name, specialty):
        super().__init__(name)
        self.specialty = specialty

    def diagnose(self):
        print("Diagnosing")


class Patient(Person):
    def __init__(self, name, patient_id):
        super().__init__(name)
        self.patient_id = patient_id

    def show_patient_id(self):
        print(self.patient_id)
```

Now both Doctor and Patient share the general Person concept while adding their own specialization.

## 6. Inheritance is not only code reuse

Bad reason:

> I want these classes to share some code, so I will make one inherit from the other.

Better question:

> Is the subclass genuinely a specialized kind of the superclass in this model?

The Diktat explicitly warns that badly designed inheritance can create implementation difficulties.

So first test the semantic relationship.

## 7. Inherited vs subclass-specific features

For:

```text
Person
├── name
└── display_name()

Doctor(Person)
├── inherited: name
├── inherited: display_name()
├── specialty
└── diagnose()
```

Ask:

> Can a Doctor use display_name()?

Yes.

> Can a plain Person use diagnose()?

No. That method belongs to Doctor.

## Main exercise — Employees

Create:

```text
Employee
├── employee_id
├── name
└── display_info()

Developer is-a Employee
├── programming_language
└── write_code()

Designer is-a Employee
├── design_tool
└── create_design()
```

Requirements:

- use inheritance;
- use `super().__init__()` for shared Employee state;
- create one Employee, one Developer, and one Designer;
- demonstrate inherited and subclass-specific behavior.

Do not override `display_info()` yet.

## Challenge — Inheritance or composition?

For each pair, decide whether inheritance is appropriate:

1. Car / Engine
2. Doctor / Person
3. Smartphone / Battery
4. Manager / Employee
5. Order / Customer
6. SavingsAccount / BankAccount

Explain each decision with an **is-a** or **has-a** sentence.

## Light Python check

You may demonstrate:

```python
isinstance(doctor, Doctor)
isinstance(doctor, Person)
```

Use this only to reinforce:

```text
Doctor is a Person.
```

Do not turn Module 6 into a Python type-system lesson.

## Reflection

Answer:

> Why is inheritance a modelling decision rather than merely a technique for avoiding duplicated code?

## Reading

### Inggriani Liem

Focus on:

- hubungan inheritance;
- descendant/child and ancestor/parent;
- inherited attributes and methods;
- is-a as the conceptual basis of inheritance;
- caution that inheritance should be designed carefully.

### OpenStax

Read:

- **13.1 Inheritance Basics**
- **13.2 Attribute Access**

For `super().__init__()`, read only the relevant `super()` subsection of **13.3 Methods** as a Python implementation bridge.

## Module 6 package

- [Colab notebook](06_inheritance.ipynb)
- [Exercises](exercises.md)
- [Quiz](quiz.md)
- [Assignment](assignment.md)
- [Instructor notes](instructor-notes.md)

## Next module

Module 6 asks:

> How can a subclass inherit behavior?

Module 7 asks:

> What if the subclass needs a **different implementation of the same behavior**?

That leads directly to:

**Module 7 — Overriding, Polymorphism & Dynamic Binding.**
