# Mid Test Instructor Notes — Vehicle Rental System

## Assessment intent

The Mid Test should measure whether students can integrate Weeks 1–7 into one coherent model.

The exam is intentionally not a syntax trivia test.

The expected reasoning path is:

```text
problem
  ↓
objects
  ↓
state + behavior
  ↓
relationships
  ↓
encapsulation
  ↓
inheritance
  ↓
overriding
  ↓
polymorphism
```

## Recommended duration

**150–180 minutes**

Suggested pacing:

| Time | Activity |
|---|---|
| 15–20 min | Read requirement and model objects |
| 15–20 min | Relationship design |
| 70–90 min | Python implementation |
| 20–25 min | Polymorphism demonstration |
| 15–20 min | Concept explanations and review |

## Recommended exam conditions

For an individual mastery assessment, a reasonable default is:

- individual work;
- course notes/books may be allowed if desired;
- no collaboration;
- AI/tool policy announced explicitly before the exam.

If the goal is to obtain a clean snapshot of individual OOP mastery, consider disallowing generative AI during the timed exam while allowing ordinary reference documentation. Apply institutional policy consistently.

## Expected design shape

One coherent solution may look like:

```text
Vehicle
├── Car
└── Motorcycle

Customer
   │
   ▼
 Rental
   │
   ▼
Vehicle
```

This is not the only acceptable representation, but the semantics should remain equivalent.

## Preferred responsibility split

### Vehicle

Owns:

- vehicle identity/state;
- availability state;
- operations that mark it unavailable/available;
- base rental-cost behavior or interface.

### Car / Motorcycle

Own:

- subclass-specific state;
- overridden rental-cost calculation.

### Customer

Owns:

- customer identity/state.

### Rental

Owns:

- Customer reference;
- Vehicle reference;
- rental duration;
- rental status;
- rental lifecycle;
- delegation of cost calculation to Vehicle.

## Preferred encapsulation shape

A clean implementation avoids this:

```python
self.vehicle._is_available = False
```

inside Rental.

Instead, let Vehicle own its state:

```python
class Vehicle:
    def mark_unavailable(self):
        self._is_available = False

    def mark_available(self):
        self._is_available = True
```

Then Rental collaborates with Vehicle:

```python
self.vehicle.mark_unavailable()
```

This preserves the encapsulation concept taught in Week 4.

## Acceptable error handling

Formal exception handling is not yet part of Weeks 1–7.

Therefore, students do not need custom exceptions.

If a vehicle is unavailable, acceptable Week 8 approaches include:

- returning `False`;
- printing a clear message and leaving state unchanged;
- another simple approach that preserves the rule.

Do not require Week 13 exception concepts.

## Cost calculations

Expected:

```text
Car:
daily_rate * days

Motorcycle:
daily_rate * days * 0.90
```

The most important architectural point is:

```python
self.vehicle.calculate_rental_cost(self.days)
```

inside Rental.

That demonstrates that Rental delegates behavior to the runtime Vehicle object.

## Dynamic binding explanation

A strong student explanation should communicate:

> Rental calls the same method on Vehicle-related objects. At runtime, the actual object may be a Car or Motorcycle, so the corresponding overridden implementation runs.

Do not require advanced terminology about dispatch tables or Python internals.

## Common mistakes and grading

### 1. Direct availability mutation

Example:

```python
rental.vehicle._is_available = False
```

Program may run, but deduct encapsulation points.

### 2. Car and Motorcycle are separate unrelated classes

This loses inheritance/is-a points, even if both calculate cost correctly.

### 3. Cost logic lives in Rental with type checks

Example:

```python
if isinstance(self.vehicle, Car):
    ...
```

Deduct polymorphism points.

### 4. All logic placed in one giant Rental class

Deduct object modelling/responsibility points.

### 5. Student adds exceptions

Do not penalize if correct and understandable, but do not award bonus points. Exceptions have not been formally taught yet.

### 6. Student uses an abstract base class

Do not penalize a correct solution, but do not require it or award extra marks. Abstract classes belong to Week 9.

## No public answer key

This repository is public. A full executable answer key should not be committed to the public `main` branch before the exam.

Keep any final solution/key in a private lecturer-controlled location.

## After the exam

Use common mistakes as the bridge to Week 9:

- repeated subclass behavior;
- incomplete superclass concepts;
- methods that conceptually must be implemented by every subclass.

This naturally introduces:

**Week 9 — Abstract Classes & Inheritance Structures.**
