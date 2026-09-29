# Course Map — Object Oriented Programming

This document connects weekly topics, Course Learning Outcomes (CPMK/CLO), assessment evidence, and the two formal references.

## Course Learning Outcomes

| Code | Outcome |
|---|---|
| CPMK-1 | Explain OO fundamentals and model problems using objects, classes, identity, state, and behavior. |
| CPMK-2 | Design collaborating objects using encapsulation, abstraction, responsibilities, and relationships. |
| CPMK-3 | Apply inheritance, overriding, polymorphism, dynamic binding, abstract classes, multiple inheritance, and mixins appropriately. |
| CPMK-4 | Explain runtime object behavior, references, lifecycle, operator overloading, genericity, modules, exceptions, assertions, and contracts. |
| CPMK-5 | Perform OOA → OOD → OOP → OOT, including class diagrams and testing. |
| CPMK-6 | Build, test, demonstrate, defend, and reuse a complete object-oriented solution. |

## Weekly alignment

| Week | Topic | Primary CPMK | Main evidence |
|---:|---|---|---|
| 0 | Python Primer | prerequisite | readiness check |
| 1 | Thinking in Objects | CPMK-1 | object identification, identity/state/behavior |
| 2 | Classes, Objects & Instances | CPMK-1 | class/instance implementation |
| 3 | State & Behavior | CPMK-1, CPMK-2 | responsibility and state-changing methods |
| 4 | Encapsulation & Abstraction | CPMK-2 | public interface, protected state |
| 5 | Object Relationships | CPMK-2 | Client–Supplier, references, has-a |
| 6 | Inheritance | CPMK-3 | is-a, superclass/subclass, inherited behavior |
| 7 | Overriding, Polymorphism & Dynamic Binding | CPMK-3 | polymorphic method calls |
| 8 | Mid Test | CPMK-1–3 | integrated Vehicle Rental assessment |
| 9 | Abstract Classes & Inheritance Structures | CPMK-3 | deferred/abstract behavior |
| 10 | Multiple Inheritance & Mixins | CPMK-3 | multiple parents, MRO, focused mixins |
| 11 | Object Lifecycle, References & Identity | CPMK-4 | aliasing, mutation, reassignment |
| 12 | Operator Overloading, Genericity & Modules | CPMK-4 | special methods, type parametrization concept, modules |
| 13 | Exception Handling & Assertions | CPMK-4, CPMK-5 | exceptions, pre/postconditions, invariants |
| 14 | OOA, OOD, OOP & OOT | CPMK-5 | requirement-to-test workflow |
| 15 | Reusability & Design Patterns | CPMK-5, CPMK-6 | design reuse, Strategy/Factory Method-style examples |
| 16 | Final Project / Final Test | CPMK-1–6 | complete solution + demo/viva |

## Assessment alignment

| Assessment | Weight | Main CPMK |
|---|---:|---|
| Quiz / Concept Exercises | 15% | CPMK-1–5 progressively |
| Weekly Coding Labs | 20% | CPMK-1–5 progressively |
| Mid Test | 20% | CPMK-1–3 |
| Final Project | 35% | CPMK-1–6 |
| Demo / Code Explanation / Participation | 10% | CPMK-1–6, especially explanation/ownership |
| **Total** | **100%** | |

## Reference alignment

### Inggriani Liem — primary conceptual source

Used for course concepts such as:

- OOP definitions;
- class vs object;
- state and behavior;
- Client–Supplier relationships;
- inheritance;
- polymorphism and dynamic binding;
- deferred/abstract classes;
- multiple/repeated inheritance;
- runtime references and object dynamics;
- overloading and genericity;
- exception handling and assertions;
- preconditions, postconditions, and invariants;
- OOA, OOD, OOP, OOT;
- reusability and design-pattern terminology.

### OpenStax — primary Python-facing source

Used especially for:

- OOP basics in Python;
- classes and instances;
- methods;
- inheritance;
- overriding and polymorphism;
- hierarchical and multiple inheritance;
- mixins;
- variables/references and identity;
- operator overloading;
- modules containing classes;
- handling and raising exceptions.

## Scope boundaries

The course deliberately does not require:

- databases;
- REST APIs;
- web frameworks;
- GUI development;
- deployment;
- SOLID as a separate framework;
- repository pattern;
- dependency-injection frameworks;
- pytest/fixtures/mocking;
- formal sequence diagrams;
- advanced Python typing/generics;
- metaclasses or C3 algorithm internals.

These may be useful in other courses, but they are not needed to achieve the learning outcomes here.

## Progression principle

The course progression is intentionally cumulative:

```text
identify objects
→ define classes
→ assign state/behavior
→ protect state
→ connect objects
→ generalize with inheritance
→ vary behavior polymorphically
→ understand runtime objects
→ strengthen contracts
→ analyse/design/test systems
→ reuse proven design ideas
→ build and defend a complete solution
```
