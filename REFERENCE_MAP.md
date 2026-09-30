# Reference Map

This map connects the course modules to the two formal references used by the open course.

## References

1. Inggriani Liem. *Diktat Kuliah Pemrograman Berorientasi Objek*. Departemen Teknik Informatika ITB, 2003.
2. OpenStax. *Introduction to Python Programming*. 2024.

The Diktat is the primary conceptual source for object-oriented terminology and modelling. OpenStax is the primary implementation-facing source for Python.

> Page numbers can vary between copies or renderings of the Diktat. For that reason, this map uses concepts/sections rather than brittle page-only citations.

## Module mapping

| Module | Course focus | Inggriani Liem alignment | OpenStax alignment | Main evidence |
|---:|---|---|---|---|
| 0 | Python prerequisite | prerequisite only | introductory Python chapters: variables, control flow, functions, collections, errors | readiness check + primer notebook |
| 1 | Thinking in objects | OOP definition; object, class, identity, state, behavior; collaboration | OOP overview as supporting context | object identification and modelling |
| 2 | Classes, objects & instances | class as static description; runtime objects; attributes; construction | §11.2 classes, instances, `__init__`, `self`, class/instance attributes; light preview of §11.3 | independent instances |
| 3 | State & behavior | attributes as object state; methods/services; interaction/message concepts | §11.3 instance methods | state-changing behavior |
| 4 | Encapsulation & abstraction | abstraction, encapsulation, visibility, class invariant | §11.1 encapsulation and abstraction | protected valid state |
| 5 | Object relationships | Client–Supplier relationship; references/contained entities; has-a whole–part distinction | previously learned class/reference mechanics | collaborating objects; association/reference vs whole–part reasoning |
| 6 | Inheritance | ancestor/descendant; inherited features; is-a modelling | §13.1 is-a vs has-a and inheritance; §13.2 inherited state; relevant `super()` material from §13.3 | meaningful specialization |
| 7 | Overriding, polymorphism & dynamic binding | redefinition, polymorphism, dynamic binding | §13.3 overriding, `super()`, polymorphism | runtime method selection |
| 8 | Mid-course assessment | integration of Modules 1–7 | integration of Modules 1–7 | Vehicle Rental assessment |
| 9 | Abstract/deferred classes | deferred feature/class and abstraction | inheritance hierarchy context; Python `abc.ABC` used as course implementation technique | abstract contract + concrete subclasses |
| 10 | Multiple inheritance & mixins | multiple/repeated inheritance; feature conflicts | §13.5 multiple inheritance, mixins, MRO context | capability mixins + lookup experiment |
| 11 | Runtime objects, references & identity | runtime object creation/manipulation/lifecycle | §3.3 variables revisited: references, identity, aliasing | mutation, aliasing, reassignment |
| 12 | Overloading, genericity & modules | overloading; genericity | §11.4 operator overloading; §11.5 modules containing classes | value-object operators + module organization |
| 13 | Exceptions & contracts | exceptions, assertions, pre/postconditions, invariants, routine contract | §§14.4–14.5 exception handling/raising | explicit failure paths + contracts |
| 14 | OOA → OOD → OOP → OOT | OO analysis/design/programming/testing lifecycle and class modelling | prior Python chapters as implementation support | requirement-to-test solution |
| 15 | Reusability & patterns | class library; design reuse; pattern concept; Strategy and Factory Method terminology | prior Python OOP chapters as implementation support | Strategy-style and Factory Method-style refactoring |
| 16 | Final project | integration of course concepts | integration of course concepts | complete solution + tests + explanation |

## Source discipline

When extending the course:

- keep conceptual claims traceable to the Diktat or an explicitly documented course interpretation;
- keep Python syntax/behavior traceable to OpenStax where the topic is covered;
- clearly mark implementation techniques that are useful but not formal topics in either reference;
- do not expand required scope merely because a Python feature exists;
- keep [COURSE_MAP.md](COURSE_MAP.md), [ASSESSMENT_ALIGNMENT.md](ASSESSMENT_ALIGNMENT.md), and this file aligned.

## Related documents

- [Course Map](COURSE_MAP.md)
- [Assessment Alignment](ASSESSMENT_ALIGNMENT.md)
- [Execution Audit](EXECUTION_AUDIT.md)
