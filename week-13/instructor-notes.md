# Week 13 Instructor Notes — Exception Handling & Assertions

## Teaching goal

Students already know how to preserve state through encapsulation.

Week 13 adds the failure path:

```text
operation requested
       ↓
can contract be satisfied?
   /             \
 yes              no
  ↓                ↓
normal result    exception
```

The key design question is:

> What should an object do when it cannot fulfill a requested operation without violating its rules?

## Source alignment

### Inggriani Liem

Use the Diktat for:

- runtime failure and exception handling;
- failure as a routine not satisfying its contract;
- assertions;
- preconditions;
- postconditions;
- class invariants;
- Client–Supplier contract thinking.

The Diktat's syntax and some details are Eiffel-specific. Do not transfer those language details directly into Python.

In particular, the Diktat includes language-specific statements about how developer exceptions are triggered. Python in this course uses explicit `raise`, following OpenStax.

### OpenStax

Use:

- **14.4 Handling Exceptions**
- **14.5 Raising Exceptions**

for Python:

- `try`;
- `except`;
- exception types;
- `raise`.

Python `assert` is used as a course implementation bridge for internal correctness assumptions.

## Suggested session flow

| Approx. duration | Activity |
|---|---|
| 15 min | Review Week 4 invariant idea |
| 25 min | Runtime failure & exceptions |
| 25 min | `raise` and built-in exception types |
| 25 min | `try` / `except` |
| 10 min | Break |
| 20 min | Exception propagation |
| 25 min | Preconditions/postconditions |
| 20 min | Class invariant & assertions |
| 25 min | BankAccount/Product lab |
| 10 min | Quiz / Week 14 bridge |

## Opening demonstration

Start with:

```python
account = BankAccount(100_000)
account.withdraw(500_000)
```

Ask:

> Should the method complete normally if it would violate `balance >= 0`?

Then show explicit rejection:

```python
if amount > self._balance:
    raise ValueError("Insufficient balance")
```

## Exception vs ordinary return value

Ask students to compare:

```python
return -1
```

with:

```python
raise ValueError("Insufficient balance")
```

The second communicates that normal completion did not occur.

Do not claim that exceptions are always superior to every error-return design. Keep the statement specific to this course's object-operation examples.

## Specific exception handling

Teach:

```python
try:
    account.withdraw(amount)
except ValueError as error:
    print(error)
```

Avoid normalizing a bare:

```python
except:
    ...
```

because it can conceal unrelated failures.

## Exception propagation

Use three layers:

```text
withdraw()
   ↓ raises
pay_bill()
   ↓ does not handle
main/caller
   ↓ handles
```

The purpose is to show that the most appropriate handling location may be above the operation that detected the problem.

## Contract model

Use a single method repeatedly:

```text
withdraw(amount)

PRE
amount > 0
amount <= balance

POST
new_balance = old_balance - amount

INVARIANT
balance >= 0
```

Connect this explicitly to the Diktat's Client–Supplier contract wording.

## Assertion guidance

Use this working distinction:

```text
expected invalid external request
→ exception

internal condition believed always true
→ assertion
```

Example:

```python
if amount <= 0:
    raise ValueError(...)

self._balance -= amount

assert self._balance >= 0
```

Do not use `assert` as the primary user-input validation mechanism.

## Common misconceptions

### 1. Exception means the whole program must stop

No. Caller code may handle an expected exception.

### 2. try/except should surround every line

No. Handle errors at a meaningful boundary.

### 3. Bare except is safest

No. It may hide unrelated problems.

### 4. Assertion and exception are identical

No. This course uses them for different roles.

### 5. Postcondition is error handling

No. A postcondition describes the state/result expected after successful completion.

## Quiz administration

The quiz answer key is intentionally not stored in the public repository. Keep the instructor key in a private instructor-controlled location.

## Assignment grading notes

Reward clear contract reasoning as much as syntax.

A student who raises `ValueError` correctly but cannot state the invariant has only demonstrated part of the learning objective.

Do not require custom exceptions.

Do not reward broad exception hierarchies or large validation frameworks.

## What not to teach yet

Avoid:

- custom exception-class architecture;
- context-manager internals;
- exception chaining;
- broad production logging patterns;
- retry frameworks;
- transaction handling;
- testing frameworks such as pytest.

## Closing question

End with:

> We can now describe what individual methods require and guarantee. How do we move from a whole problem statement to a complete object model, class design, implementation, and test?

That leads directly to:

**Week 14 — OOP Analysis, Design, Class Diagram & Testing.**
