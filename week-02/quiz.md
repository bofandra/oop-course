# Module 2 Quiz — Classes, Objects & Instances

**Suggested duration:** 15–20 minutes

## Part A — Multiple Choice

### 1. A class is best described as:

A. one specific runtime object  
B. a definition/blueprint for a kind of object  
C. an instance attribute  
D. an imported module only

### 2. In:

```python
student = Student("S001", "Alya")
```

`student` is:

A. a class  
B. a method  
C. an instance/object  
D. a class attribute

### 3. What is the role of `__init__()` in the examples used this module?

A. Delete an instance  
B. Initialize instance state when an instance is created  
C. Import another class  
D. Create a class attribute only

### 4. Inside an instance method, `self` refers to:

A. every object in the program  
B. the class name as text  
C. the particular instance involved in the method call  
D. the Python interpreter

### 5. Which is usually an instance attribute for a Student?

A. university name shared by every student  
B. student ID  
C. institution logo shared globally  
D. campus name shared by every instance in this simplified example

### 6. Which is the best example of a class attribute in the simplified model?

A. individual student's email  
B. individual student's ID  
C. university name shared by all Student instances  
D. individual student's GPA

---

## Part B — Short Answer

### 7. What is the difference between an instance attribute and a class attribute?

### 8. Consider:

```python
class Book:
    def __init__(self, title):
        self.title = title

book_1 = Book("A")
book_2 = Book("B")
```

How many `Book` instances exist, and what is the value of `book_2.title`?

### 9. Why can one class definition represent many objects?

### 10. Write a minimal `Product` class whose constructor receives `sku` and `name` and stores both as instance attributes.
