# Mid Test — Module 8

> **Assessment notebook:** [Open Mid-Course Assessment in Google Colab](https://colab.research.google.com/github/bofandra/oop-course/blob/main/assessments/midterm/midterm_exam.ipynb)

## Case Study: Vehicle Rental System

### Purpose

This assessment checks whether you can integrate the concepts from Modules 1–7 into one coherent object-oriented solution.

You are not being tested on web development, databases, APIs, GUIs, or advanced Python.

## Scenario

A vehicle rental company rents different kinds of vehicles to customers.

The system must support:

- general vehicle information;
- cars;
- motorcycles;
- customers;
- rentals;
- vehicle availability;
- rental cost calculation;
- different cost calculation behavior for different vehicle types.

### Vehicle

Every vehicle has:

- `vehicle_id`
- `brand`
- `daily_rate`
- availability state

A vehicle must be able to:

- report whether it is available;
- become unavailable when a rental starts;
- become available again when a rental is completed;
- calculate a standard rental cost using `daily_rate × rental_days`.

The standard cost behavior belongs to Vehicle so subclasses can inherit or override it.

### Car

A Car is a Vehicle.

A Car adds:

- `seats`

For this exam, Car uses the standard Vehicle rental-cost behavior:

```text
daily_rate × rental_days
```

Car may inherit this behavior unchanged.

### Motorcycle

A Motorcycle is a Vehicle.

A Motorcycle adds:

- `engine_capacity`

Motorcycle **overrides** the inherited rental-cost behavior to apply a 10% discount:

```text
daily_rate × rental_days × 0.90
```

### Customer

A Customer has:

- `customer_id`
- `name`

### Rental

A Rental connects:

- one Customer;
- one Vehicle;
- rental duration in days;
- rental status.

Rental lifecycle:

```text
created
  ↓ start()
active
  ↓ complete()
completed
```

A Rental must provide:

- `start()`
- `complete()`
- `calculate_total()`
- `display_info()`

Rules:

1. a rental can start only when its status is `created` and its Vehicle is available;
2. when the rental starts, status becomes `active` and the Vehicle becomes unavailable;
3. a rental can complete only when its status is `active`;
4. when the rental completes, status becomes `completed` and the Vehicle becomes available again;
5. a completed rental cannot be started again;
6. total cost must use the Vehicle object's own `calculate_rental_cost(days)` behavior;
7. exceptions are not required for this assessment; an invalid lifecycle request may simply leave state unchanged or return a simple failure result.

## Exam sections

### A. Identify Objects — 15%

Identify the main objects/classes from the requirement.

For each, list:

- identity/state;
- behavior;
- brief responsibility.

### B. Model Relationships — 15%

Explain the relationships among:

- Vehicle
- Car
- Motorcycle
- Customer
- Rental

At minimum, identify:

- which relationships are **is-a** inheritance relationships;
- which are object-reference/association relationships;
- whether any relationship is meaningfully whole–part rather than assuming every stored reference is composition.

You may use a simple text diagram.

### C. Python Implementation — 40%

Implement the required classes.

Your implementation should demonstrate:

- classes and instances;
- `__init__()`;
- instance state;
- methods;
- encapsulation of availability state;
- object references;
- inheritance;
- `super().__init__()`;
- a Vehicle-level `calculate_rental_cost(days)` operation that can be inherited or overridden;
- Rental lifecycle rules for `created → active → completed`.

Keep the design simple.

### D. Polymorphism — 15%

Demonstrate that the same call:

```python
vehicle.calculate_rental_cost(days)
```

uses standard inherited behavior for Car and overridden behavior for Motorcycle.

Your Rental class should not need a long branch such as:

```python
if vehicle_type == "car":
    ...
elif vehicle_type == "motorcycle":
    ...
```

### E. Concept Explanation — 15%

Answer short questions explaining:

- why Car/Motorcycle use inheritance;
- why Rental should refer to Vehicle rather than duplicate vehicle data;
- why that reference is an association and not automatically whole–part composition;
- where encapsulation appears;
- why cost calculation is polymorphic;
- how dynamic binding determines the method implementation at runtime.

## Required demonstration

Your program must demonstrate at least:

1. one Car;
2. one Motorcycle;
3. two Customers;
4. at least two Rental objects;
5. successful rental start;
6. vehicle becoming unavailable;
7. rental completion;
8. vehicle becoming available again;
9. Car cost calculation;
10. Motorcycle cost calculation.

## Duration

Recommended: **150–180 minutes**.

## Allowed materials

For self-paced study, attempt the assessment without notes first, then review your work using the course materials and rubric. In a facilitated cohort, follow the facilitator's rules regarding notes, documentation, internet access, and AI tools.

## Submission

For self-paced study, keep the completed notebook or Python file as portfolio evidence and assess it with the supplied rubric. In a facilitated cohort, submit it according to the facilitator's instructions.

## Files

- [Mid Test notebook](midterm_exam.ipynb)
- [Detailed rubric](midterm_rubric.md)
