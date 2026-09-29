# Week 11 Exercises — Object Lifecycle, References & Object Identity

## Exercise 1 — Same Object or Different Object?

Predict each result before running:

```python
a = [1, 2]
b = a
c = [1, 2]

print(a is b)
print(a is c)
print(a == c)
```

Explain each answer.

---

## Exercise 2 — Aliasing

Run:

```python
x = [10, 20]
y = x

y.append(30)
```

Answer:

1. What is `x` now?
2. What is `y` now?
3. How many list objects are involved?
4. Why did changing through `y` affect what we observe through `x`?

---

## Exercise 3 — Mutation vs Reassignment

Start with:

```python
a = [1, 2]
b = a
```

Compare:

```python
b.append(3)
```

with:

```python
b = [100, 200]
```

Draw the reference structure after each operation.

---

## Exercise 4 — Identity vs Equality

Create two independent Student objects with the same name.

```python
student_1 = Student("Alya")
student_2 = Student("Alya")
```

Without defining `__eq__()`, inspect:

- `student_1 is student_2`
- their attribute values

Explain why "same state" and "same object" are different ideas.

---

## Exercise 5 — Shared Custom Object

Create:

```python
account_a = BankAccount(100_000)
account_b = account_a
```

Deposit through `account_b`.

Then inspect `account_a.balance`.

Explain the result using aliasing.

---

## Exercise 6 — One Reference Disappears

Create:

```python
student_a = Student("Alya")
student_b = student_a

student_a = None
```

Answer:

1. Is the Student object necessarily unreachable now?
2. Which reference still reaches it?
3. Why should `student_b.name` still work?

---

## Exercise 7 — Reference Assignment vs Copy

Explain why:

```python
b = a
```

should not automatically be described as "copying the object".

Then give a small example where treating it as a copy would cause a bug.

---

## Challenge — Shared Course Enrollment

Create one `Course` object and two `Enrollment` objects that both refer to that same Course.

Change the Course title through one reference.

Show that both Enrollment objects now observe the new title.

Then create a genuinely separate Course object with the same title and compare identity.

Explain:

- aliasing;
- shared object state;
- independent object identity.
