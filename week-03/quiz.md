# Week 3 Quiz — State & Behavior

**Suggested duration:** 15–20 minutes

## Part A — Multiple Choice

### 1. In OOP, the current values of an object's attributes primarily represent:

A. inheritance  
B. state  
C. module structure  
D. class hierarchy

### 2. Which is behavior?

A. `status`  
B. `balance`  
C. `confirm()`  
D. `price`

### 3. Which method is most clearly read-only?

A. `deposit()`  
B. `resize()`  
C. `cancel()`  
D. `area()`

### 4. In:

```python
def deposit(self, amount):
    self.balance += amount
```

`amount` is:

A. always a class attribute  
B. an input parameter for the method call  
C. the class itself  
D. an inherited method

### 5. Which call best communicates the intent "confirm this appointment"?

A. `appointment.status = "confirmed"`  
B. `appointment.confirm()`  
C. `status = appointment`  
D. `Appointment = "confirmed"`

## Part B — Short Answer

### 6. Explain the difference between state and behavior.

### 7. Give one example of a method that reads state and one that changes state.

### 8. Why can it be useful to place behavior close to the object state it uses?

### 9. What happens to object state in this code?

```python
class Lamp:
    def __init__(self):
        self.is_on = False

    def turn_on(self):
        self.is_on = True

lamp = Lamp()
lamp.turn_on()
```

### 10. A Book can be borrowed twice in your current Week 3 implementation. What kind of design concern does this reveal for the next week?