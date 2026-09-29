# Mid Test — Week 8

## Case Study: Vehicle Rental System

### Purpose

This assessment checks whether you can integrate the concepts from Weeks 1–7 into one coherent object-oriented solution.

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
- become available again when a rental is completed.

### Car

A Car is a Vehicle.

A Car adds:

- `seats`

For this exam, the Car rental cost is:

```text
daily_rate × rental_days
```

### Motorcycle

A Motorcycle is a Vehicle.

A Motorcycle adds:

- `engine_capacity`

For this exam, Motorcycle rental cost receives a 10% discount:

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

Initial rental status:

```text
created
```

A Rental must provide:

- `start()`
- `complete()`
- `calculate_total()`
- `display_info()`

Rules:

1. a rental can start only when its Vehicle is available;
2. when the rental starts, the Vehicle becomes unavailable;
3. when the rental completes, the Vehicle becomes available again;
4. total cost must use the Vehicle's own `calculate_rental_cost(days)` behavior.

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

- which relationships are **is-a**;
- which are object-reference / **has-a** relationships.

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
- `super().__init__()`.

Keep the design simple.

### D. Polymorphism — 15%

Demonstrate that the same call:

```python
vehicle.calculate_rental_cost(days)
```

can produce different behavior for Car and Motorcycle.

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

Follow the lecturer's exam-day instructions regarding notes, documentation, internet access, and AI tools.

## Submission

Submit the completed notebook or Python file according to the lecturer's instructions.

## Files

- [Mid Test notebook](midterm_exam.ipynb)
- [Detailed rubric](midterm_rubric.md)
