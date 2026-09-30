# Source Boundary

This course has exactly two formal references:

1. Inggriani Liem. *Diktat Kuliah Pemrograman Berorientasi Objek*. Departemen Teknik Informatika ITB, 2003.
2. OpenStax. *Introduction to Python Programming*. 2024.

The course does not use an additional book, framework, pattern catalogue, or external tutorial as a third formal source.

## Three source categories

### 1. Formal course concept

A concept belongs to the formal course scope when it is traceable to at least one of the two references.

Examples include:

- object, class, state, behavior, and collaboration;
- encapsulation and abstraction;
- Client–Supplier and has-a / is-a distinctions;
- inheritance, overriding, polymorphism, and dynamic binding;
- deferred/abstract classes;
- multiple inheritance and mixins;
- object identity, references, aliasing, and lifecycle;
- overloading and genericity;
- exceptions, assertions, preconditions, postconditions, and invariants;
- OOA, OOD, OOP, and OOT;
- reusability and design-pattern terminology.

### 2. Minimal implementation bridge

A minimal implementation bridge is Python syntax or a small standard-library mechanism used only to express a concept that is already inside the formal scope.

An implementation bridge must not introduce a new conceptual learning outcome by itself.

Current examples include:

| Bridge | Why it is used | Formal concept being expressed |
|---|---|---|
| leading underscore convention and a small read-only `@property` example | show a practical Python public/internal-state boundary | encapsulation / abstraction |
| `abc.ABC` and `@abstractmethod` | make the deferred/abstract-class idea executable in Python | deferred/abstract class |
| simple Strategy-style Python structure | make design reuse and interchangeable behavior concrete | reusability, Strategy terminology, polymorphism |
| simple Factory Method-style Python structure | demonstrate reusable object-creation responsibility | reusability, Factory Method terminology |

These bridges are intentionally small. They are not separate formal references and must not be expanded into advanced subtopics unless the two-reference scope is deliberately changed.

### 3. Out of scope

A topic is out of scope when it is neither a concept supported by the two formal references nor a minimal implementation bridge needed to make a supported concept executable.

Examples intentionally excluded from the required course include:

- web frameworks;
- databases and REST APIs;
- deployment;
- advanced testing frameworks;
- dependency-injection frameworks;
- external design-pattern catalogues;
- SOLID as a separate required framework;
- advanced Python typing/generics machinery;
- Protocol / structural typing as a separate topic;
- metaclasses;
- the full C3 linearization algorithm.

## Rule for future changes

Before adding required material, ask:

1. Which of the two formal references supports the concept?
2. If neither reference directly teaches the Python mechanism, is it only the smallest practical bridge needed to express an already-supported concept?
3. Does the addition create a new learning outcome or merely implement an existing one?
4. Can the example be taught without importing a third conceptual framework?

If a proposed addition creates a new conceptual learning outcome that cannot be traced to either formal reference, it should stay out of the required course unless the course scope and reference policy are explicitly revised.

## Assessment rule

Implementation bridges must not become hidden assessment requirements beyond the concept they support.

For example:

- learners should understand encapsulation; they do not need advanced property mechanics;
- learners should understand abstract/deferred classes; they do not need advanced `abc` internals;
- learners should understand design reuse/pattern reasoning; they do not need a catalogue of GoF implementations.

The assessment target remains the sourced OOP concept and the learner's ability to apply and explain it.

## Related documents

- [Reference Map](REFERENCE_MAP.md)
- [Course Map](COURSE_MAP.md)
- [Assessment Alignment](ASSESSMENT_ALIGNMENT.md)
