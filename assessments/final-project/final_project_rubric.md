# Final Project Detailed Rubric

The project receives a raw score out of **100**. This score maps to the **Final Project 35%** component of the course assessment.

## 1. Object-Oriented Analysis — 15 points

| Criterion | Points |
|---|---:|
| Candidate concepts/classes are identified from the requirement | 5 |
| State, behavior, and responsibilities are coherent | 5 |
| Analysis reflects the domain rather than Python syntax alone | 5 |
| **Subtotal** | **15** |

Do not require one exact class list. Reward coherent alternatives that satisfy the requirement.

## 2. Class Design & Relationships — 15 points

| Criterion | Points |
|---|---:|
| Class diagram communicates the main model | 4 |
| Object-reference / has-a relationships are appropriate | 4 |
| Inheritance relationships represent meaningful is-a relationships | 4 |
| Responsibilities are placed in sensible classes | 3 |
| **Subtotal** | **15** |

Formal UML notation is not required.

## 3. State, Behavior & Encapsulation — 10 points

| Criterion | Points |
|---|---:|
| State belongs to the appropriate objects | 3 |
| Behavior changes/reads state coherently | 3 |
| Important internal state is protected through a clear interface | 2 |
| Objects remain in valid states during normal use | 2 |
| **Subtotal** | **10** |

## 4. Inheritance & Polymorphism — 15 points

| Criterion | Points |
|---|---:|
| Inheritance is semantically justified | 4 |
| Required behavior is correctly overridden | 4 |
| At least two assignment/scoring variants are used polymorphically | 4 |
| Caller avoids unnecessary type-based branching | 3 |
| **Subtotal** | **15** |

Do not award full marks for inheritance used only to reduce duplicated code when the is-a relationship is weak.

## 5. Contracts & Exception Handling — 15 points

| Criterion | Points |
|---|---:|
| Important preconditions/invariants are identified | 4 |
| Invalid operations raise appropriate exceptions | 4 |
| Failed operations preserve valid object state | 4 |
| Contract reasoning is explained in README/design notes | 3 |
| **Subtotal** | **15** |

Custom exception classes are not required.

## 6. Python Implementation Quality — 20 points

| Criterion | Points |
|---|---:|
| Program executes and supports the required scenario | 6 |
| Methods/classes have clear responsibilities | 4 |
| Object collaboration is implemented correctly | 4 |
| Code/module organization is understandable | 3 |
| Names and implementation are readable and consistent | 3 |
| **Subtotal** | **20** |

Do not award extra points merely for frameworks, databases, advanced typing, or large code volume.

## 7. OOT / Testing — 10 points

| Criterion | Points |
|---|---:|
| Independent-class tests | 2 |
| Collaboration tests | 2 |
| Rule/exception tests | 2 |
| Polymorphism/grading tests | 2 |
| End-to-end scenario | 2 |
| **Subtotal** | **10** |

Plain Python `assert` tests are sufficient.

## Total

| Component | Weight |
|---|---:|
| OOA | 15% |
| Class design & relationships | 15% |
| State, behavior & encapsulation | 10% |
| Inheritance & polymorphism | 15% |
| Contracts & exception handling | 15% |
| Python implementation quality | 20% |
| OOT / testing | 10% |
| **Total** | **100%** |

## Grading principles

A smaller coherent solution can receive a higher score than a larger but poorly modeled one.

Do not reward complexity for its own sake.

Optional use of:

- abstract classes;
- mixins;
- operator overloading;
- genericity concepts;
- a simple design pattern

may support a good design, but these features are **not required** and do not replace the core rubric.

## Integrity / ownership check

If code quality is substantially stronger than the student's explanation, use the demo/viva to verify understanding.

The submitted artifact should be graded on demonstrated object-oriented reasoning, implementation, testing, and ownership.
