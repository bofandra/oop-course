# Module 10 Exercises — Multiple Inheritance & Mixins

## Exercise 1 — Two Parents

Create:

```text
Teacher      Researcher
     \       /
      Lecturer
```

Teacher provides `teach()`.

Researcher provides `research()`.

Lecturer inherits both and demonstrates both methods.

---

## Exercise 2 — Same Method Name

Create:

```python
class A:
    def display(self):
        print("A")

class B:
    def display(self):
        print("B")

class C(A, B):
    pass
```

Predict the output of:

```python
C().display()
```

Then inspect:

```python
C.__mro__
```

Reverse the parent order and repeat.

---

## Exercise 3 — Explain MRO

In your own words, explain:

1. what MRO is;
2. why Python needs it;
3. why parent order matters when multiple parents define the same method.

Do not explain the full C3 algorithm.

---

## Exercise 4 — Repeated / Diamond Inheritance

Model:

```text
       Person
       /    \
 Employee  Student
       \    /
    TeachingAssistant
```

Give all three upper classes a `describe()` method.

Predict which implementation runs for TeachingAssistant and verify using `__mro__`.

---

## Exercise 5 — Logging Mixin

Create:

```python
class LoggingMixin:
    def log(self, message):
        print("[LOG]", message)
```

Use it with a domain class:

```text
Person
  ↑
Doctor + LoggingMixin
```

Demonstrate that Doctor keeps its domain identity while gaining the logging capability.

---

## Exercise 6 — Export Mixin

Create an `ExportMixin` with:

```python
export_text()
```

that returns a simple string representation of an object's state.

Use it with two unrelated domain classes.

Explain why a mixin can be reused across different hierarchies.

---

## Exercise 7 — Multiple Inheritance or Composition?

For each case, choose **multiple inheritance**, **single inheritance**, **mixin**, or **composition**:

1. Doctor needs logging capability.
2. Car has an Engine.
3. TeachingAssistant is both Student and Employee in the chosen model.
4. Order uses PaymentService.
5. Report needs an export capability.
6. Manager is an Employee.

Explain every answer.

---

## Challenge — Conflict Without Type Checks

Create two parent classes that both define `process()`.

Create a child inheriting both.

Then:

1. predict the selected method;
2. inspect `__mro__`;
3. change parent order;
4. explain why this kind of conflict is a design cost of multiple inheritance.
