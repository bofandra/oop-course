# Assessment Alignment — Object Oriented Programming Open Course

This document explains what each assessment is intended to measure, where the evidence comes from, and what should **not** be required before the relevant concept is taught.

## Alignment principles

The course uses four evidence levels:

1. **Recognize** — identify the concept or distinguish it from nearby concepts.
2. **Explain** — describe the concept and reasoning in the learner's own words.
3. **Apply** — implement or model the concept in a new example.
4. **Defend** — justify a design choice, explain trade-offs, and connect the decision to runtime/test evidence.

Module quizzes primarily target **Recognize + Explain**.

Module assignments primarily target **Apply + Defend**.

The Mid Test integrates Modules 1–7.

The Final Project integrates the full course, but does **not** require every optional technique to appear in one artifact. Concepts such as multiple inheritance, mixins, operator overloading, or design patterns should be used only when they improve the model.

---

## Module-level alignment

| Module | Main assessment target | Quiz evidence | Assignment / major evidence | Guardrail |
|---:|---|---|---|---|
| 0 | Python prerequisite readiness | — | readiness check | do not assess OOP yet |
| 1 | objects, identity, state, behavior, class vs object | concept distinction + modelling explanation | identify candidate objects and justify modelling choices | no detailed Python class mechanics required |
| 2 | classes, instances, `__init__`, `self`, class vs instance attributes | syntax/concept interpretation | create multiple independent instances from one class | no inheritance/encapsulation rules |
| 3 | state, behavior, methods, responsibility, state transition | distinguish state vs behavior | implement meaningful state-changing methods | validation/encapsulation intentionally incomplete |
| 4 | encapsulation, abstraction, public interface, invariant, transition rule | explain interface/internal-state and invariant/transition distinctions | preserve valid state and legal transitions through controlled public behavior | no exception architecture yet |
| 5 | Client–Supplier, references/associations, whole–part has-a, collaboration | distinguish association/reference from whole–part and is-a | model collaborating objects through references with justified relationship meaning | do not use inheritance |
| 6 | inheritance, is-a, superclass/subclass, `super()` | inheritance reasoning | implement meaningful specialization | no overriding/polymorphism required yet |
| 7 | overriding, polymorphism, dynamic binding | method-selection reasoning | polymorphic hierarchy + runtime method selection | no abstract classes or multiple inheritance |
| 8 | integration of Modules 1–7 | — | Vehicle Rental Mid Test: relationships, lifecycle rules, inheritance, overriding, polymorphism | no Module 9+ concepts or exception architecture required |
| 9 | abstract/deferred classes and required behavior | abstract vs concrete reasoning | implement ABC + concrete subclasses | no multiple inheritance |
| 10 | multiple inheritance, MRO, mixins, repeated inheritance | lookup/design reasoning | capability mixins + MRO conflict experiment | no custom MRO/C3 implementation |
| 11 | references, identity, aliasing, mutation, reassignment, lifecycle | predict runtime reference behavior | demonstrate shared references and reassignment | no deepcopy implementation |
| 12 | operator overloading, genericity concept, modules | special-method/genericity concepts | value-object operators + module organization | no advanced typing/generics |
| 13 | exceptions, assertions, pre/postconditions, invariants, state-dependent transition preconditions | contract/error-path reasoning | robust state-changing object with explicit failure paths and workflow preconditions | no custom exception hierarchy required |
| 14 | OOA → OOD → OOP → OOT | lifecycle/design distinctions | requirement-to-test integrated solution | no advanced UML/testing framework |
| 15 | code/design reuse, Strategy-style and Factory Method-style reasoning | pattern-selection reasoning | refactor real variation points and test result | do not reward pattern count |
| 16 | complete OO solution + ownership | — | Final Project artifact + separate demo/viva evidence | optional techniques only when justified |

---

## Mid Test alignment

The Mid Test intentionally assesses only material introduced in **Modules 1–7**.

| Evidence | Main CLO | What is measured |
|---|---|---|
| object identification | CLO-1 | candidate objects, state, behavior, responsibilities |
| relationship modelling | CLO-2 | is-a inheritance vs object-reference/association relationships; whole–part only when justified |
| Python implementation | CLO-1, CLO-2, CLO-3 | classes, state, methods, encapsulation, collaboration, inheritance |
| polymorphism section | CLO-3 | inherited standard behavior + overriding, same operation across subtypes, no type-branch substitute |
| concept explanation | CLO-1–3 | reasoning linked to the submitted design |

The Mid Test must **not** require:

- abstract classes;
- multiple inheritance/mixins;
- reference/aliasing theory beyond normal object collaboration;
- operator overloading/genericity;
- exceptions/contracts from Module 13;
- OOA/OOD/OOT terminology from Module 14;
- design patterns.

---

## Final Project alignment

The Final Project is the main integrated artifact for **CLO-1 through CLO-6**.

### Directly required in the artifact

- object analysis and responsibilities;
- meaningful object relationships;
- state and behavior;
- encapsulation and valid state;
- inheritance + overriding + polymorphism;
- contracts and exception handling;
- implementation;
- independent, collaboration, rule/error, polymorphism, and end-to-end tests;
- explanation of major design decisions.

### Prior-course evidence that does not need to be forced into the artifact

These concepts are directly assessed in their own modules and may be optional in the Final Project:

- multiple inheritance and mixins;
- low-level reference/aliasing demonstrations;
- operator overloading;
- genericity/type-parametrization implementation;
- design patterns when no real variation/reuse problem exists.

This prevents the capstone from becoming a checklist of mechanisms rather than a coherent design.

---

## Artifact score vs ownership score

Two separate assessment components exist:

```text
Final Project artifact
→ 35%

Demo / Code Explanation / Learning Evidence
→ 10%
```

The **35% project rubric** measures the quality of the submitted analysis, design, implementation, contracts, and tests.

The **10% demo/ownership rubric** measures whether the learner can explain, demonstrate, modify, and defend the work.

Do not double-count the same code quality in both components.

For self-paced learners, the 10% component can use learning evidence such as:

- completed reasoning/reflections;
- mastery checks;
- lab evidence;
- version history;
- recorded/self-conducted explanation;
- ability to answer the viva prompts.

Live classroom participation is not required for self-paced use.

---

## Assessment difficulty progression

The intended progression is:

```text
Modules 1–3
concept formation + small implementation

Modules 4–7
design responsibility + relationships + inheritance/polymorphism

Module 8
first integrated assessment

Modules 9–13
advanced class/runtime/error concepts

Modules 14–15
integrated development + reuse reasoning

Module 16
complete solution + defense
```

An assessment should not become harder merely by adding unrelated application-stack requirements.

Do not require databases, REST APIs, GUIs, deployment, advanced testing frameworks, or framework architecture unless a separate course explicitly introduces them.

---

## Review checklist for future changes

Before merging a new quiz or assignment, ask:

- Does every required concept already appear in the current or earlier modules?
- Does the quiz measure understanding rather than trivia?
- Does the assignment require application/justification, not only copy-paste syntax?
- Does the rubric award points to the stated learning outcome?
- Is any optional technique being accidentally made mandatory?
- Is the workload appropriate relative to the Mid Test or Final Project?
- Does learner-facing material avoid fixed cohort dates and facilitator-only notes?
- Can a self-paced learner understand how to review the result?
