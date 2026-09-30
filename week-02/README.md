# Module 2 — Classes, Objects & Instances

## Learning outcomes

By the end of this module, learners should be able to:

1. explain the relationship between a class and its instances;
2. define a Python class;
3. create multiple independent instances from one class;
4. use `__init__()` to initialize instance state;
5. explain what `self` refers to inside an instance method;
6. distinguish **instance attributes** from **class attributes**.

## Source alignment

Inggriani Liem describes a class as a **static description** of the set of objects that may be created from it; at runtime, the program works with objects instantiated from the class. The Diktat also connects attributes with an object's runtime state and discusses constructors as the mechanism used to create/initialize objects.

OpenStax 11.2 covers the Python implementation used this module: classes, instances, `__init__()`, `self`, instance attributes, and class attributes. The beginning of 11.3 is useful only as a light preview of instance methods; deeper state-changing behavior is reserved for Module 3.

## From Module 1 to Module 2

Module 1 asked:

> What objects exist in this problem?

Module 2 asks:

> How do we define one kind of object and create many independent instances of it?

```text
Class
  ↓
instantiate
  ↓
Object / Instance
  ↓
instance state
```

## 1. Class as a definition

```python
class Patient:
    pass
```

At this point, `Patient` describes a kind of object, but we have not yet created a particular patient.

Create two instances:

```python
patient_1 = Patient()
patient_2 = Patient()
```

Conceptually:

```text
Patient
  ├── patient_1
  └── patient_2
```

The two instances come from the same class but are separate runtime objects.

## 2. Initializing instance state

A useful object normally needs initial state.

```python
class Patient:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

Create instances:

```python
patient_1 = Patient("Budi", 30)
patient_2 = Patient("Siti", 25)
```

Now each object has its own state:

```text
patient_1
- name = "Budi"
- age  = 30

patient_2
- name = "Siti"
- age  = 25
```

## 3. What does `self` represent?

Inside an instance method, `self` refers to the particular instance involved in that method call.

For example:

```python
class Patient:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(self.name, self.age)
```

Then:

```python
patient_1.display_info()
patient_2.display_info()
```

The same method definition operates on different instance state.

Detailed responsibility and state-changing behavior are covered in Module 3. This module focuses on how instances and their attributes work.

## 4. Instance attributes

An **instance attribute** belongs to a particular instance.

```python
class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
```

```python
student_1 = Student("S001", "Alya")
student_2 = Student("S002", "Bima")
```

`student_1.name` and `student_2.name` can contain different values.

## 5. Class attributes

A **class attribute** belongs to the class and is shared as class-level information.

```python
class Student:
    university = "Example University"

    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
```

Usage:

```python
student_1 = Student("S001", "Alya")
student_2 = Student("S002", "Bima")

print(Student.university)
print(student_1.university)
print(student_2.university)
```

For this course, use a class attribute when the information logically belongs to the class and is shared by its instances.

## 6. Class attribute vs instance attribute

```text
Student

Class attribute
- university

Instance attributes
- student_id
- name
```

Ask:

> Should `name` be shared by all students?

No. It belongs to each instance.

> Should the university name be repeated separately inside every student object?

For this simple example, it can be class-level information.

## 7. Multiple instances from one class

```python
class Book:
    category = "General"

    def __init__(self, isbn, title):
        self.isbn = isbn
        self.title = title
```

```python
book_1 = Book("978-001", "Python Basics")
book_2 = Book("978-002", "Object Thinking")
```

One class can describe many objects with different state.

## Main exercise — Student

Create a `Student` class with:

Instance attributes:

- `student_id`
- `name`
- `email`

Class attribute:

- `university = "Example University"`

Create at least three instances and print each student's data.

Then answer:

1. Which data is shared?
2. Which data is unique per instance?
3. How many times is the class defined?
4. How many Student objects did you create?

## Challenge — Product

Create a `Product` class with:

- instance attributes: `sku`, `name`, `price`;
- class attribute: `store_name`.

Create three products with different values.

Add a simple `display_info()` method only to show current state. Do not add stock rules or validation yet; those belong to later modules.

## Reflection

Explain in your own words:

> If a class is defined once, how can it represent many different objects at runtime?

## Reading

### Inggriani Liem

Focus on:

- class as a static definition;
- class vs object;
- object instantiation at runtime;
- attributes as object state;
- constructor / object creation.

### OpenStax

Read:

- **11.2 Classes and instances**
- the opening part of **11.3 Instance methods** as a preview.

## Module 2 package

- [Colab notebook](02_classes_objects_instances.ipynb)
- [Exercises](exercises.md)
- [Quiz](quiz.md)
- [Assignment](assignment.md)
- [Instructor notes](instructor-notes.md)

## Next module

Module 2 gives objects state.

Module 3 asks:

> What should those objects actually **do** with that state?

```text
Attributes
   ↓
State
   ↓
Methods
   ↓
Behavior
```
