# Week 9 Quiz — Abstract Classes & Inheritance Structures

**Suggested duration:** 15–20 minutes

## Part A — Multiple Choice

### 1. An abstract/deferred class is primarily useful when:

A. every class must be instantiated directly  
B. a general class should define shared structure or required behavior without being a complete concrete object  
C. inheritance should be avoided  
D. all methods must be private

### 2. A concrete subclass of an abstract class should:

A. ignore required abstract behavior  
B. implement the required abstract behavior before it can be meaningfully instantiated  
C. remove the superclass  
D. always use multiple inheritance

### 3. Which statement is correct?

A. Every superclass must be abstract  
B. A class becomes abstract automatically when it has subclasses  
C. A superclass can be concrete if direct instances are meaningful  
D. Abstract classes cannot contain concrete methods

### 4. In this course, Python `ABC` / `@abstractmethod` is:

A. terminology taken directly from the Diktat's Eiffel syntax  
B. a Python implementation bridge for the abstract/deferred class concept  
C. a design pattern  
D. a multiple-inheritance feature only

### 5. Which hierarchy most naturally suggests an abstract top-level class?

A. Shape → Rectangle / Circle, when generic Shape objects are not meaningful  
B. Person → Doctor / Patient, when generic Person records are allowed  
C. Car → Engine  
D. Order → Customer

---

## Part B — Short Answer

### 6. Explain the difference between an abstract/deferred class and a concrete class.

### 7. What is a deferred/abstract feature conceptually?

### 8. Can an abstract class contain implemented methods and state? Explain.

### 9. Why is returning a fake default such as `0` from `Shape.area()` sometimes weaker than requiring subclasses to implement `area()`?

### 10. How does abstract-class design relate to polymorphism from Week 7?
