# Module 13 Quiz — Exception Handling & Assertions

**Suggested duration:** 15–20 minutes

## Part A — Multiple Choice

### 1. Exception handling primarily deals with:

A. inheritance hierarchy layout  
B. runtime conditions that prevent normal completion  
C. module imports only  
D. class diagrams

### 2. Which Python statement explicitly signals an exception?

A. `assert` only  
B. `raise`  
C. `import`  
D. `return`

### 3. A precondition describes:

A. what must be true before a successful operation  
B. what must be true after program shutdown  
C. how inheritance works  
D. how modules are imported

### 4. A postcondition describes:

A. an object's class name  
B. what should be true after a successful operation  
C. only user interface output  
D. memory allocation

### 5. A class invariant describes:

A. a condition expected to remain valid for legitimate instances  
B. a temporary local variable  
C. a package name  
D. a subclass list

---

## Part B — Short Answer

### 6. Explain why `ValueError` is more suitable than silently allowing negative stock.

### 7. What is exception propagation?

### 8. Why should `except ValueError` usually be preferred over a bare `except:` for an expected validation error?

### 9. Explain the difference between an exception used for invalid caller input and an assertion used for an internal correctness assumption.

### 10. For a BankAccount with invariant `balance >= 0`, give one precondition and one postcondition for `withdraw(amount)`.
