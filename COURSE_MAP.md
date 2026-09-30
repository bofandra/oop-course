# Course Map — Object Oriented Programming

This document connects module topics, Course Learning Outcomes (CLO), assessment evidence, and the two formal references.

## Course Learning Outcomes

| Code | Outcome |
|---|---|
| CLO-1 | Explain OO fundamentals and model problems using objects, classes, identity, state, and behavior. |
| CLO-2 | Design collaborating objects using encapsulation, abstraction, responsibilities, and relationships. |
| CLO-3 | Apply inheritance, overriding, polymorphism, dynamic binding, abstract classes, multiple inheritance, and mixins appropriately. |
| CLO-4 | Explain runtime object behavior, references, lifecycle, operator overloading, genericity, modules, exceptions, assertions, and contracts. |
| CLO-5 | Perform OOA → OOD → OOP → OOT, including class diagrams and testing. |
| CLO-6 | Build, test, demonstrate, defend, and reuse a complete object-oriented solution. |

## Module alignment

| Module | Topic | Primary CLO | Main evidence |
|---:|---|---|---|
| 0 | Python Primer | prerequisite | readiness check |
| 1 | Thinking in Objects | CLO-1 | object identification, identity/state/behavior |
| 2 | Classes, Objects & Instances | CLO-1 | class/instance implementation |
| 3 | State & Behavior | CLO-1, CLO-2 | responsibility and state-changing methods |
| 4 | Encapsulation & Abstraction | CLO-2 | public interface, protected state |
| 5 | Object Relationships | CLO-2 | Client–Supplier, references/associations, whole–part has-a |
| 6 | Inheritance | CLO-3 | is-a, superclass/subclass, inherited behavior |
| 7 | Overriding, Polymorphism & Dynamic Binding | CLO-3 | polymorphic method calls |
| 8 | Mid Test | CLO-1–3 | integrated Vehicle Rental assessment |
| 9 | Abstract Classes & Inheritance Structures | CLO-3 | deferred/abstract behavior |
| 10 | Multiple Inheritance & Mixins | CLO-3 | multiple parents, MRO, focused mixins |
| 11 | Object Lifecycle, References & Identity | CLO-4 | aliasing, mutation, reassignment |
| 12 | Operator Overloading, Genericity & Modules | CLO-4 | special methods, type parametrization concept, modules |
| 13 | Exception Handling & Assertions | CLO-4, CLO-5 | exceptions, pre/postconditions, invariants |
| 14 | OOA, OOD, OOP & OOT | CLO-5 | requirement-to-test workflow |
| 15 | Reusability & Design Patterns | CLO-5, CLO-6 | design reuse, Strategy/Factory Method-style examples |
| 16 | Final Project / Final Test | CLO-1–6 | complete solution + demo/viva |

## Assessment alignment

See [Assessment Alignment](ASSESSMENT_ALIGNMENT.md) for the module-by-module evidence map, difficulty progression, and assessment guardrails.

| Assessment | Weight | Main CLO |
|---|---:|---|
| Quiz / Concept Exercises | 15% | CLO-1–5 progressively |
| Module Coding Labs | 20% | CLO-1–5 progressively |
| Mid Test | 20% | CLO-1–3 |
| Final Project | 35% | CLO-1–6 |
| Demo / Code Explanation / Learning Evidence | 10% | CLO-1–6, especially explanation/ownership |
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
