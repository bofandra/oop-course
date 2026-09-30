# Week 11 Instructor Notes — Object Lifecycle, References & Object Identity

## Teaching goal

Weeks 6–10 emphasized class hierarchies.

Week 11 deliberately shifts from:

```text
class structure
```

to:

```text
runtime object structure
```

The core mental model is:

```text
variable/reference
      ↓
object
```

and several references may identify the same object.

## Source alignment

### Inggriani Liem

Use the Diktat for:

- objects as runtime entities;
- creation and manipulation;
- reference as an object identifier;
- assignment between references;
- **dynamic aliasing**;
- copy versus reference assignment;
- object destruction and garbage collection.

The Diktat states that when one reference is assigned from another, the two references can become attached to the same object; it warns that operations through one alias can therefore affect what is observed through the other.

### OpenStax

Use **3.3 Variables revisited** for the Python-facing explanation of:

- variables referring to objects;
- identity;
- aliases;
- `id()`;
- `is`.

Keep the conceptual source distinction clear.

## Suggested session flow

| Approx. duration | Activity |
|---|---|
| 15 min | Runtime review: objects vs classes |
| 25 min | References and object identity |
| 25 min | `is` vs `==` |
| 25 min | Aliasing and mutation |
| 10 min | Break |
| 25 min | Mutation vs reassignment |
| 20 min | Custom-object aliasing |
| 25 min | Lifecycle and reachability |
| 20 min | Shared Enrollment lab |
| 10 min | Quiz / Week 12 bridge |

## Opening demonstration

Write:

```python
student_a = Student("Alya")
student_b = student_a
```

Ask:

> How many Student objects exist?

Many beginners answer "two" because there are two variable names.

Draw:

```text
student_a ──┐
            ├──> one Student object
student_b ──┘
```

This drawing is the key Week 11 teaching device.

## Identity vs equality

Use lists first:

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(a is b)
```

Keep the distinction:

```text
==
value equality

is
object identity
```

Do not teach custom `__eq__()` yet; operator overloading belongs to Week 12.

## Aliasing

Use:

```python
x = [10, 20]
y = x

y.append(30)
```

Then draw the single object.

Connect explicitly to the Diktat term:

> This is the Python manifestation of the **dynamic aliasing** idea.

## Mutation vs reassignment

Mutation:

```python
y.append(30)
```

changes the shared object.

Reassignment:

```python
y = [100, 200]
```

changes which object the name `y` refers to.

Have students redraw the arrows.

## Custom objects

Move quickly from list examples to:

```python
account_b = account_a
account_b.deposit(50_000)
```

Ask why `account_a.balance` changes.

This reconnects runtime references with object-oriented domain models.

## Lifecycle

Use this deliberately simplified lifecycle:

```text
create object
   ↓
references exist
   ↓
object is used
   ↓
references disappear/rebind
   ↓
object may become unreachable
   ↓
automatic memory reclamation
```

The Diktat discusses object destruction and garbage collection. In Python, avoid promising an exact collection moment.

Do not teach:

```text
x = None means object is destroyed immediately
```

That is not the correct conceptual statement.

## id()

Use only as an observation tool.

State:

> `id()` identifies an object during its lifetime for Python runtime purposes. It is not a domain/business identifier such as student_id.

Avoid memory-address implementation claims because Python implementations are not required to expose `id()` as a literal memory address.

## Garbage collection nuance

For this course, keep it implementation-agnostic:

> When an object is no longer reachable from application references, it may become eligible for automatic memory reclamation.

Do not teach:

- CPython reference-count internals as universal Python semantics;
- `__del__()`;
- forcing `gc.collect()`;
- cyclic-GC algorithms.

## Common misconceptions

### 1. Two variable names mean two objects

False.

### 2. Assignment copies the object

Not necessarily; ordinary assignment binds another reference.

### 3. is and == are interchangeable

False.

### 4. Mutation and reassignment are the same

False.

### 5. None destroys an object

No. Rebinding one reference says nothing about other references.

## Quiz administration

The quiz answer key is intentionally not stored in the public repository. Keep the instructor key in a private instructor-controlled location.

## Assignment grading notes

The best evidence is a correct **reference diagram plus runtime demonstration**.

Do not reward unnecessary use of:

- `copy`;
- `deepcopy`;
- garbage-collector APIs;
- memory-address tricks.

If a student explains references accurately with a simpler solution, that is preferable.

## What not to teach yet

Avoid detailed treatment of:

- `__eq__()`;
- `__hash__()`;
- shallow/deep-copy implementation;
- CPython refcount internals;
- weak references;
- object finalizers.

## Closing question

End with:

> We now understand what our objects are doing at runtime. How can a class also define what `+``, `==`, or string representation should mean for its objects, and how can classes be organized into modules?

That leads directly to:

**Week 12 — Operator Overloading, Genericity & Organizing Classes into Modules.**
