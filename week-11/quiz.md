# Module 11 Quiz — References & Object Identity

**Suggested duration:** 15–20 minutes

## Part A — Multiple Choice

### 1. If:

```python
b = a
```

and `a` refers to a mutable object, then typically:

A. the object is automatically deep-copied  
B. `a` and `b` can refer to the same object  
C. `a` is deleted  
D. `b` becomes a class

### 2. Python `is` asks:

A. whether values are numerically equal  
B. whether two references identify the same object  
C. whether a class inherits another  
D. whether an object is mutable

### 3. Python `==` usually asks:

A. whether two references are necessarily identical  
B. about value equality according to the objects' equality behavior  
C. whether memory has been freed  
D. whether assignment occurred

### 4. Which operation is mutation?

A. `y = [100]`  
B. `x.append(3)`  
C. `x = None`  
D. `x = y`

### 5. If two variables alias the same mutable object:

A. mutation through one reference may be visible through the other  
B. they must always have different values  
C. one of them is automatically copied  
D. they cannot be reassigned

---

## Part B — Short Answer

### 6. Explain aliasing in your own words.

### 7. What is the difference between mutation and reassignment?

### 8. Why is `id()` useful for learning about object identity but not suitable as a business identifier?

### 9. If one reference is assigned `None` but another still points to the object, why is the object still reachable?

### 10. Explain, at a high level, when an object may become eligible for automatic memory reclamation.
