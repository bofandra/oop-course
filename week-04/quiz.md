# Module 4 Quiz — Encapsulation & Abstraction

**Suggested duration:** 15–20 minutes

## Part A — Multiple Choice

### 1. Encapsulation mainly concerns:

A. creating many unrelated global variables  
B. grouping state and behavior while controlling access to state  
C. using inheritance everywhere  
D. converting every attribute into a class

### 2. Abstraction mainly concerns:

A. exposing every implementation detail  
B. hiding details a caller does not need while exposing a useful interface  
C. preventing all methods from accessing state  
D. creating only abstract classes

### 3. In Python, a leading underscore such as `_balance`:

A. makes the attribute impossible to access externally  
B. is a convention indicating internal use  
C. deletes the attribute after each method call  
D. automatically creates a property

### 4. Which interface is more consistent with encapsulation?

A. `account.balance = account.balance - 50000`  
B. `account.withdraw(50000)`  
C. `balance = account`  
D. `BankAccount = 50000`

### 5. Which is a reasonable invariant for a simple inventory Product?

A. `stock < 0`  
B. `stock >= 0`  
C. `name == stock`  
D. `stock is always 100`

---

## Part B — Short Answer

### 6. Explain the difference between encapsulation and abstraction.

### 7. Why is `_balance` not the same as strict `private` access in some other languages?

### 8. What benefit does a read-only `@property` provide in our Module 4 examples?

### 9. A caller uses:

```python
appointment.confirm()
```

What internal detail can be hidden behind this interface?

### 10. Why is the rule `stock >= 0` useful when designing Product methods?
