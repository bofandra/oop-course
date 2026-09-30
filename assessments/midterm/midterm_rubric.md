# Mid Test Detailed Rubric — Vehicle Rental System

Total score: **100 points**

## A. Identify Objects — 15 points

| Criterion | Points |
|---|---:|
| Identifies Vehicle, Car, Motorcycle, Customer, and Rental as relevant classes/concepts | 5 |
| Identifies meaningful state for the classes | 4 |
| Identifies meaningful behavior | 3 |
| Describes class responsibilities coherently | 3 |
| **Subtotal** | **15** |

Partial credit is appropriate when the model is different but still coherent.

Do not require students to reproduce one exact object list if their alternative design satisfies the requirement.

## B. Model Relationships — 15 points

| Criterion | Points |
|---|---:|
| Car is-a Vehicle | 3 |
| Motorcycle is-a Vehicle | 3 |
| Rental refers to/has-a Customer | 3 |
| Rental refers to/has-a Vehicle | 3 |
| Explanation/diagram clearly distinguishes is-a from has-a/reference relationships | 3 |
| **Subtotal** | **15** |

Do not require formal UML notation.

## C. Python Implementation — 40 points

### C1. Class structure — 10 points

| Criterion | Points |
|---|---:|
| Vehicle implemented correctly | 3 |
| Car and Motorcycle subclasses implemented correctly | 3 |
| Customer implemented correctly | 2 |
| Rental implemented correctly | 2 |

### C2. State & behavior — 10 points

| Criterion | Points |
|---|---:|
| Constructors establish required object state | 3 |
| Vehicle availability behavior is represented through methods/public interface | 3 |
| Rental start/complete behavior changes relevant state correctly | 2 |
| display/info behavior is coherent | 2 |

### C3. Encapsulation — 8 points

| Criterion | Points |
|---|---:|
| Availability state is treated as internal state rather than freely modified by normal caller code | 3 |
| Public method/property provides appropriate availability access | 2 |
| Rental uses Vehicle behavior to change availability instead of directly writing Vehicle internal state | 3 |

### C4. Inheritance — 6 points

| Criterion | Points |
|---|---:|
| Correct subclass syntax | 2 |
| Shared Vehicle state/behavior is inherited | 2 |
| `super().__init__()` used appropriately | 2 |

### C5. Object collaboration — 6 points

| Criterion | Points |
|---|---:|
| Rental stores Customer and Vehicle object references | 3 |
| Collaboration among Rental and Vehicle is coherent and works end-to-end | 3 |

**Section C subtotal: 40 points**

## D. Polymorphism — 15 points

| Criterion | Points |
|---|---:|
| Car and Motorcycle both provide `calculate_rental_cost(days)` | 5 |
| Implementations produce the required different calculations | 4 |
| Rental delegates total calculation to the Vehicle object | 3 |
| Demonstration uses the same method call without unnecessary type-based branching | 3 |
| **Subtotal** | **15** |

Required cost behavior:

```text
Car:
daily_rate × days

Motorcycle:
daily_rate × days × 0.90
```

## E. Concept Explanation — 15 points

Award **3 points each** for five explanations:

1. Car/Motorcycle as subclasses of Vehicle;
2. Rental holding Vehicle/Customer object references;
3. encapsulation in the design;
4. why `calculate_rental_cost()` is polymorphic;
5. dynamic binding based on runtime object.

For each answer:

- 3 = conceptually correct and linked to the submitted design;
- 2 = mostly correct but incomplete;
- 1 = vague/partially correct;
- 0 = incorrect or absent.

## Grading principles

### Reward understanding, not unnecessary complexity

A simple implementation that correctly models the requirements can receive full marks.

Do not award extra marks merely for:

- frameworks;
- databases;
- advanced typing;
- decorators unrelated to the requirement;
- design patterns;
- extra inheritance layers.

### Accept equivalent naming

For example, these names may be accepted if behavior is equivalent:

```text
mark_unavailable()
reserve()
start_rental()
```

The important point is responsibility and state ownership.

### Encapsulation note

A preferred design lets Vehicle manage its own availability:

```python
vehicle.mark_unavailable()
vehicle.mark_available()
```

or equivalent.

A Rental implementation that directly writes:

```python
self.vehicle._is_available = False
```

should lose encapsulation points even if the program runs.

### Polymorphism note

This design:

```python
if isinstance(vehicle, Car):
    ...
elif isinstance(vehicle, Motorcycle):
    ...
```

does not demonstrate the intended polymorphic solution for Section D.

## Suggested grade interpretation

Use the raw score as the Mid Test score. If a letter grade is needed, use the configured scale in `grading_config.json` or a facilitator-provided equivalent; the public open course does not assume one institution-specific scale.
