# Module 13 Assignment — Robust BankAccount

## Objective

Use exceptions and assertions to make object behavior explicit when operations cannot satisfy their required conditions.

## Task

Implement a `BankAccount` class.

## State

- `owner`
- internal `_balance`

Expose a read-only `balance` property.

## Operations

Implement:

```python
deposit(amount)
withdraw(amount)
```

## Contracts

### Class invariant

```text
balance >= 0
```

### deposit(amount)

Precondition:

```text
amount > 0
```

Postcondition after success:

```text
new balance = old balance + amount
```

### withdraw(amount)

Preconditions:

```text
amount > 0
amount <= balance
```

Postcondition after success:

```text
new balance = old balance - amount
```

## Required exception behavior

Raise `ValueError` when:

- deposit amount is zero or negative;
- withdrawal amount is zero or negative;
- withdrawal exceeds available balance.

After every successful state-changing operation, use an assertion to check:

```python
assert self._balance >= 0
```

## Required demonstration

Create at least two accounts.

Show:

1. successful deposit;
2. successful withdrawal;
3. invalid deposit handled by caller;
4. over-withdrawal handled by caller;
5. balance unchanged after a failed operation;
6. invariant still true after successful operations.

Use specific `try` / `except ValueError` handling.

## Written explanation

Answer:

1. What are the preconditions of `deposit()`?
2. What are the preconditions of `withdraw()`?
3. What are the postconditions?
4. What is the class invariant?
5. Why are invalid requested amounts handled with exceptions?
6. Why is the invariant also checked with `assert`?
7. What is exception propagation?
8. Why should caller code often decide how an exception is presented?

## Rubric

| Criterion | Weight |
|---|---:|
| Correct class/state design | 15% |
| Correct `raise ValueError` conditions | 20% |
| Correct successful state transitions | 15% |
| Correct `try/except` handling | 15% |
| Preconditions/postconditions/invariant | 15% |
| Correct assertion use | 10% |
| Written reasoning | 10% |
| **Total** | **100%** |

## Scope

Do not create custom exception classes.

Do not add persistence, databases, GUIs, or web APIs.

The focus is exceptions, assertions, and contract reasoning.
