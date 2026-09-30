# Module 13 Exercises — Exception Handling & Assertions

## Exercise 1 — Identify the Failure

Given:

```python
class Product:
    def __init__(self, stock):
        self.stock = stock

    def remove_stock(self, quantity):
        self.stock -= quantity
```

Start with `stock = 5` and call:

```python
remove_stock(10)
```

Answer:

1. What invalid state can appear?
2. What class invariant is violated?
3. Where should the operation reject the request?

---

## Exercise 2 — Raise an Exception

Modify `remove_stock()` so that it raises `ValueError` when:

- quantity is not positive;
- quantity exceeds available stock.

Demonstrate both failures.

---

## Exercise 3 — Handle an Expected Error

Use:

```python
try:
    ...
except ValueError as error:
    ...
```

to handle one invalid stock operation.

Explain why caller code—not necessarily Product itself—decides how the error should be presented.

---

## Exercise 4 — Exception Propagation

Create:

```python
def checkout(product, quantity):
    product.remove_stock(quantity)
```

Do not catch the exception inside `checkout()`.

Catch it in the caller instead.

Draw:

```text
Product.remove_stock()
        ↓
checkout()
        ↓
caller
```

and explain propagation.

---

## Exercise 5 — Preconditions and Postconditions

For:

```python
account.withdraw(amount)
```

write:

- two preconditions;
- one postcondition;
- one class invariant.

Use a concrete example with an old balance and amount.

---

## Exercise 6 — Assertions

After a valid stock removal, add:

```python
assert self._stock >= 0
```

Explain why this assertion represents an internal correctness assumption rather than normal user-input validation.

---

## Exercise 7 — Exception or Assertion?

Choose the more appropriate mechanism for each case:

1. user asks to withdraw a negative amount;
2. after a supposedly valid withdrawal, internal balance becomes negative;
3. caller provides an invalid product quantity;
4. an internal method reaches a state the programmer believes should be impossible.

Choose **exception** or **assertion** and explain each answer.

---

## Challenge — Inventory Transaction

Implement a Product with:

- `add_stock(quantity)`
- `remove_stock(quantity)`
- read-only `stock`

Rules:

```text
quantity > 0
stock >= 0
```

Then write three caller scenarios:

1. successful add;
2. successful remove;
3. failed remove handled with `try/except`.

State the preconditions, postconditions, and invariant explicitly.
