# Lecturer Operational Kit — Object Oriented Programming

**TANRI ABENG UNIVERSITY — Faculty of Engineering and Technology**  
Semester: Odd 2026/2027  
Class time: **Saturday, 08:30–11:50**  
Implementation: **Python + Google Colab**

This document is the lecturer-facing execution guide for Week 0–16.

Use it together with:

- [Course Map](COURSE_MAP.md)
- [Teaching Calendar](TEACHING_CALENDAR.md)
- [Release Plan](RELEASE_PLAN.md)
- [Teaching Readiness Audit](TEACHING_READINESS_AUDIT.md)
- [Execution Audit](EXECUTION_AUDIT.md)

---

# Operating principles

## Before every class

Confirm:

- weekly README is the current approved version;
- notebook opens correctly;
- live-code cells have been tested;
- quiz is ready;
- assignment/lab expectations are clear;
- examples do not introduce concepts scheduled for a later week;
- any student-facing deadline has been announced.

## During every class

Use this rhythm unless the weekly guide says otherwise:

```text
Review / problem
      ↓
Concept
      ↓
Live code / modelling
      ↓
Break
      ↓
Guided lab
      ↓
Challenge / discussion
      ↓
Quiz / reflection
      ↓
Bridge to next week
```

## After every class

Do three things:

1. announce exactly what is graded;
2. publish/confirm the due date;
3. note 2–3 common misconceptions for the next class opening review.

Do not treat every repository exercise as separately graded.

---

# Week 0 — Python Primer / Readiness

**Nominal window:** 28 Sep–2 Oct 2026  
**Mode:** self-study prerequisite

## Before

Prepare/announce:

- [Python Primer notebook](00-python-primer/00_python_primer.ipynb)
- [Readiness check](00-python-primer/readiness-check.md)
- OpenStax introductory Python reading as needed

Tell students:

> Week 0 is prerequisite preparation, not OOP content.

## Student focus

Students should be able to:

- use variables and expressions;
- write `if/elif/else`;
- use loops;
- write functions;
- use lists, tuples, dictionaries;
- import a module;
- read a basic Python error.

## Lecturer action

Do not spend Week 1 reteaching all Python syntax.

Collect likely readiness gaps and decide whether a short remedial clinic is needed.

## Deliverable

Recommended:

- readiness check completed;
- no major grade required.

---

# Week 1 — Introduction to OOP & Thinking in Objects

**Nominal date:** Sat, 3 Oct 2026

## Before class

Prepare:

- Week 1 README
- `01_thinking_in_objects.ipynb`
- whiteboard/slides for identity–state–behavior
- Library requirement for group modelling
- Week 1 quiz

Key reminder:

> Keep Week 1 conceptual. Do not teach `__init__`, `self`, or detailed instance state mechanics yet.

## During class — 08:30–11:50

| Time | Lecturer action |
|---|---|
| 08:30–08:45 | Ask how students would represent a clinic appointment without OO terminology. |
| 08:45–09:10 | Contrast procedural organization with object-oriented organization without declaring procedural programming “bad”. |
| 09:10–09:40 | Teach object = identity + state + behavior. |
| 09:40–10:00 | Introduce class vs object/instance conceptually. |
| 10:00–10:10 | Break. |
| 10:10–10:35 | Identify candidate objects from requirements. Emphasize: not every noun becomes a class. |
| 10:35–10:55 | Model object collaboration. |
| 10:55–11:25 | Library exercise. |
| 11:25–11:40 | Food delivery / course registration challenge discussion. |
| 11:40–11:50 | Reflection and bridge to Week 2. |

## Live code

Use only:

```python
class Patient:
    pass

patient_1 = Patient()
patient_2 = Patient()
```

Ask:

- one class or two?
- how many objects?
- are the two objects identical?

## Do not introduce yet

- `__init__`
- `self`
- inheritance
- encapsulation syntax

## After class

Graded evidence:

- small concept quiz;
- Week 1 modelling assignment/lab.

Recommended workload outside class: **1.5–2 hours**.

---

# Week 2 — Classes, Objects & Instances

**Nominal date:** Sat, 10 Oct 2026

## Before class

Prepare:

- Week 2 notebook
- one Student example
- one Product exercise
- visual explanation for class definition → instantiation → object

## During class

| Time | Lecturer action |
|---|---|
| 08:30–08:45 | Review class vs object from Week 1. |
| 08:45–09:10 | Python class definition and instantiation. |
| 09:10–09:40 | Teach `__init__()` and instance state. |
| 09:40–10:00 | Explain `self` carefully. |
| 10:00–10:10 | Break. |
| 10:10–10:35 | Instance attributes vs class attributes. |
| 10:35–11:10 | Live-code Student. |
| 11:10–11:35 | Colab exercise + Product challenge. |
| 11:35–11:50 | Quiz / reflection / Week 3 bridge. |

## Live code

Use:

```python
class Patient:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

Then instantiate two independent objects.

Key question:

> Which values belong to the class, and which belong to each instance?

## Common misconception to catch

> “self is a Python keyword.”

Correct framing: it is the conventional parameter name referring to the current instance.

## After class

Graded evidence:

- quiz;
- class/instance coding lab.

Recommended workload: **1.5–2 hours**.

---

# Week 3 — Attributes, Methods, State & Behavior

**Nominal date:** Sat, 17 Oct 2026

## Before class

Prepare:

- Appointment example;
- Rectangle `area()`;
- BankAccount `deposit()`;
- Book exercise.

## During class

| Time | Lecturer action |
|---|---|
| 08:30–08:45 | Review instances and attributes. |
| 08:45–09:10 | Attribute values as object state. |
| 09:10–09:35 | Instance methods as behavior. |
| 09:35–10:00 | Read-only vs state-changing methods. |
| 10:00–10:10 | Break. |
| 10:10–10:30 | Method parameters vs object attributes. |
| 10:30–10:55 | Responsibility: who owns the behavior? |
| 10:55–11:30 | Book / Appointment lab. |
| 11:30–11:40 | Borrow-twice challenge. |
| 11:40–11:50 | Quiz / bridge to encapsulation. |

## Live code

Preferred sequence:

```text
Rectangle.area()
→ reads state

Appointment.confirm()
→ changes state

BankAccount.deposit()
→ changes state using a parameter
```

## Teaching question

> Which object should own this behavior?

This becomes the bridge toward responsibility and encapsulation.

## After class

Graded evidence:

- state/behavior coding lab;
- concept quiz.

Recommended workload: **1.5–2 hours**.

---

# Week 4 — Encapsulation & Abstraction

**Nominal date:** Sat, 24 Oct 2026

## Before class

Prepare two BankAccount versions:

1. direct public balance mutation;
2. controlled state mutation.

Prepare Product Inventory lab.

## During class

| Time | Lecturer action |
|---|---|
| 08:30–08:45 | Revisit the deliberate invalid-state flaw from Week 3. |
| 08:45–09:10 | Encapsulation concept. |
| 09:10–09:30 | Public interface vs internal state. |
| 09:30–09:50 | Python underscore convention. |
| 09:50–10:00 | Abstraction. |
| 10:00–10:10 | Break. |
| 10:10–10:30 | Read-only `@property`. |
| 10:30–10:50 | Invariant concept. |
| 10:50–11:30 | Product Inventory lab. |
| 11:30–11:40 | Appointment challenge. |
| 11:40–11:50 | Quiz / Week 5 bridge. |

## Live code

Start with the deliberately weak example:

```python
account.balance = -1_000_000
```

Then move to:

```python
self._balance
@property
deposit()
withdraw()
```

## Key distinction

```text
Encapsulation
→ control access/change

Abstraction
→ expose what callers need, hide unnecessary details
```

## After class

Graded evidence:

- Product/Appointment lab;
- concept quiz.

Recommended workload: **2–2.5 hours**.

---

# Week 5 — Object Relationships

**Nominal date:** Sat, 31 Oct 2026

## Before class

Prepare:

- Patient–Doctor–Appointment;
- NotificationService client–supplier;
- Car–Engine;
- Product–OrderItem–Order.

## During class

| Time | Lecturer action |
|---|---|
| 08:30–08:45 | Review one object owning state/behavior. |
| 08:45–09:15 | Objects referencing other objects. |
| 09:15–09:40 | Client–Supplier relationship. |
| 09:40–10:00 | has-a vs is-a. |
| 10:00–10:10 | Break. |
| 10:10–10:35 | Car–Engine modelling. |
| 10:35–11:00 | Order / OrderItem / Product composition. |
| 11:00–11:35 | Library Loan lab. |
| 11:35–11:45 | Enrollment challenge. |
| 11:45–11:50 | Bridge to inheritance. |

## Live code

Best sequence:

```text
Appointment references Patient + Doctor
→ Client–Supplier
→ Car has Engine
→ Order contains OrderItems
```

## Common misconception

> “If two classes are related, inheritance should connect them.”

Counterexample:

```text
Car has Engine
Car is not an Engine
```

## After class

Graded evidence:

- relationship modelling/coding lab;
- quiz.

Recommended workload: **2–2.5 hours**.

---

# Week 6 — Inheritance

**Nominal date:** Sat, 7 Nov 2026

## Before class

Prepare:

- Person → Doctor;
- Person → Patient;
- Employee challenge.

## During class

| Time | Lecturer action |
|---|---|
| 08:30–08:45 | Review has-a vs is-a. |
| 08:45–09:10 | Inheritance concept and terminology. |
| 09:10–09:35 | Python subclass syntax. |
| 09:35–10:00 | Inherited attributes/methods. |
| 10:00–10:10 | Break. |
| 10:10–10:35 | Subclass-specific state/behavior. |
| 10:35–10:55 | `super().__init__()`. |
| 10:55–11:25 | Employee lab. |
| 11:25–11:40 | Inheritance vs composition challenge. |
| 11:40–11:50 | Quiz / Week 7 bridge. |

## Live code

Use:

```python
class Doctor(Person):
    ...
```

Then add:

```python
super().__init__(name)
```

## Decision test

Before inheritance, ask:

> Is the subclass truly a specialized form of the superclass?

Do not justify inheritance only by duplicated code.

## After class

Graded evidence:

- Employee inheritance lab;
- quiz.

Recommended workload: **2–2.5 hours**.

---

# Week 7 — Overriding, Polymorphism & Dynamic Binding

**Nominal date:** Sat, 14 Nov 2026

## Before class

Prepare:

- Person/Doctor redefinition;
- Notification hierarchy;
- Payroll lab;
- Mid Test scope reminder.

Keep take-home load lighter because Week 8 is the Mid Test.

## During class

| Time | Lecturer action |
|---|---|
| 08:30–08:45 | Review inheritance. |
| 08:45–09:10 | Redefinition / overriding. |
| 09:10–09:30 | Replace vs extend using `super()`. |
| 09:30–10:00 | Polymorphism. |
| 10:00–10:10 | Break. |
| 10:10–10:35 | Dynamic binding. |
| 10:35–11:05 | Notification live coding. |
| 11:05–11:35 | Payroll lab. |
| 11:35–11:45 | Shape challenge. |
| 11:45–11:50 | Mid Test scope bridge. |

## Live code

Core evidence:

```python
for notification in notifications:
    notification.send()
```

Ask:

> Same call—why do different implementations run?

Then connect to runtime object type.

## Do not introduce yet

- ABC requirement;
- multiple inheritance;
- exceptions;
- patterns.

## After class

Recommended:

- finish most lab work in class;
- if submission is required, due by Thursday before Mid Test;
- Friday reserved for review.

Outside workload: **1.5–2 hours + Mid Test preparation**.

---

# Week 8 — Mid Test

**Nominal date:** Sat, 21 Nov 2026

## Before class

Prepare:

- Mid Test notebook;
- rubric;
- exam conditions;
- explicit AI/tool policy;
- submission mechanism;
- backup copy of the exam.

Verify the exam covers only Weeks 1–7.

## During class

Recommended duration:

**150–180 minutes**

Suggested flow:

```text
15–20 min  requirement analysis
15–20 min  relationships
70–90 min  Python implementation
20–25 min  polymorphism demonstration
15–20 min  explanation/review
```

## What to observe

Look for:

- object identification;
- responsibility allocation;
- encapsulation;
- has-a vs is-a;
- Vehicle inheritance;
- overriding;
- polymorphic cost calculation.

## Do not require

- abstract classes;
- exceptions;
- multiple inheritance;
- design patterns.

## After class

Do not publish an executable answer key to public `main`.

Use common mistakes as the Week 9 opening review.

---

# Week 9 — Abstract Classes & Inheritance Structures

**Nominal date:** Sat, 28 Nov 2026

## Before class

Prepare:

- weak Shape default `area() = 0`;
- Python ABC version;
- Employee abstract pay example;
- Payment lab.

## During class

| Time | Lecturer action |
|---|---|
| 08:30–08:45 | Post-Mid-Test review of superclass problems. |
| 08:45–09:10 | Concrete vs abstract/deferred class. |
| 09:10–09:35 | Deferred feature and effecting. |
| 09:35–10:00 | Python ABC implementation bridge. |
| 10:00–10:10 | Break. |
| 10:10–10:35 | Abstract class with shared concrete behavior. |
| 10:35–11:00 | Hierarchical inheritance. |
| 11:00–11:30 | Payment lab. |
| 11:30–11:40 | Abstract-or-concrete challenge. |
| 11:40–11:50 | Quiz / Week 10 bridge. |

## Live code

Deliberately show:

```python
class Shape:
    def area(self):
        return 0
```

Ask why a meaningless default is risky.

Then introduce:

```python
ABC
@abstractmethod
```

as the Python implementation bridge.

## After class

Graded evidence:

- Payment hierarchy lab;
- quiz.

Recommended workload: **2–2.5 hours**.

---

# Week 10 — Multiple Inheritance & Mixins

**Nominal date:** Sat, 5 Dec 2026

## Before class

Prepare:

- Teacher + Researcher → Lecturer;
- A/B method conflict;
- diamond hierarchy;
- LoggingMixin.

## During class

| Time | Lecturer action |
|---|---|
| 08:30–08:45 | Review Week 9 hierarchy. |
| 08:45–09:10 | Basic multiple inheritance. |
| 09:10–09:35 | Conflicting inherited methods. |
| 09:35–10:00 | Python MRO. |
| 10:00–10:10 | Break. |
| 10:10–10:35 | Repeated/diamond inheritance. |
| 10:35–11:00 | Mixin concept. |
| 11:00–11:30 | Employee + capability lab. |
| 11:30–11:40 | Diamond challenge. |
| 11:40–11:50 | Quiz / Week 11 bridge. |

## Live code

First:

```python
class C(A, B):
    pass

C().display()
print(C.__mro__)
```

Then reverse parent order.

## Scope guardrail

Do not teach:

- formal C3 algorithm;
- complex cooperative `super()` chains;
- metaclasses.

## After class

Graded evidence:

- controlled MI/mixin lab;
- quiz.

Recommended workload: **2–2.5 hours**.

---

# Week 11 — Object Lifecycle, References & Object Identity

**Nominal date:** Sat, 12 Dec 2026

## Before class

Prepare diagrams showing:

```text
name A ──┐
         ├──> one object
name B ──┘
```

Prepare list aliasing and BankAccount aliasing examples.

## During class

| Time | Lecturer action |
|---|---|
| 08:30–08:45 | Review objects vs classes at runtime. |
| 08:45–09:10 | References and identity. |
| 09:10–09:35 | `is` vs `==`. |
| 09:35–10:00 | Aliasing and mutation. |
| 10:00–10:10 | Break. |
| 10:10–10:35 | Mutation vs reassignment. |
| 10:35–10:55 | Custom-object aliasing. |
| 10:55–11:20 | Lifecycle and reachability. |
| 11:20–11:40 | Shared Enrollment lab. |
| 11:40–11:50 | Quiz / Week 12 bridge. |

## Live code

Use:

```python
x = [10, 20]
y = x
y.append(30)
```

Then:

```python
y = [100, 200]
```

Redraw the arrows after each operation.

## Do not teach

- CPython reference-count implementation as universal Python semantics;
- `__del__`;
- weak references;
- forced GC.

## After class

Graded evidence:

- shared-reference lab;
- quiz.

Recommended workload: **2–2.5 hours**.

---

# Week 12 — Operator Overloading, Genericity & Modules

**Nominal date:** Sat, 19 Dec 2026

## Before class

Prepare:

- Point with `__str__`;
- Point equality;
- Point addition;
- `models.py` + `main.py`;
- conceptual genericity examples.

## During class

| Time | Lecturer action |
|---|---|
| 08:30–08:45 | Review identity vs equality. |
| 08:45–09:10 | Overloading concept vs overriding. |
| 09:10–09:35 | `__str__()` and `__eq__()`. |
| 09:35–10:00 | `__add__()`. |
| 10:00–10:10 | Break. |
| 10:10–10:35 | Meaningful operator semantics. |
| 10:35–10:55 | Genericity concept. |
| 10:55–11:20 | Modules with classes. |
| 11:20–11:40 | Point / Money lab. |
| 11:40–11:50 | Quiz / Week 13 bridge. |

## Live code

Preferred sequence:

```text
print(Point)
→ __str__

p1 == p2
→ __eq__

p1 + p2
→ __add__

models.py → main.py
```

## Genericity

Use concept only:

```text
LIST[BOOK]
LIST[PERSON]
LIST[POINT]
```

Do not add `TypeVar` / `Generic[T]`.

## After class

Graded evidence:

- Money/module lab;
- quiz.

Recommended workload: **2–2.5 hours**.

Operational milestone:

> Officially announce the Final Project after Week 12.

---

# Week 13 — Exception Handling & Assertions

**Nominal date:** Sat, 26 Dec 2026  
**Calendar status:** confirm against official TAU year-end calendar.

## Before class

Prepare:

- invalid BankAccount withdrawal;
- protected version with `raise ValueError`;
- `try/except`;
- contract diagram.

## During class

| Time | Lecturer action |
|---|---|
| 08:30–08:45 | Review invariant from Week 4. |
| 08:45–09:10 | Runtime failure and exceptions. |
| 09:10–09:35 | `raise` and built-in exception types. |
| 09:35–10:00 | `try/except`. |
| 10:00–10:10 | Break. |
| 10:10–10:30 | Exception propagation. |
| 10:30–10:55 | Preconditions / postconditions. |
| 10:55–11:15 | Class invariant and assertions. |
| 11:15–11:40 | BankAccount/Product lab. |
| 11:40–11:50 | Quiz / Week 14 bridge. |

## Live code

Start deliberately unsafe:

```python
self.balance -= amount
```

Then protect it:

```python
if amount > self._balance:
    raise ValueError(...)
```

Finally:

```python
assert self._balance >= 0
```

## Core distinction

```text
invalid caller input
→ exception

internal condition that should always hold
→ assertion
```

## After class

Graded evidence:

- Robust BankAccount lab;
- quiz.

Final Project action:

- students identify at least three invalid operations/contracts in their own project.

---

# Week 14 — OOA, OOD, Class Diagram & Testing

**Nominal date:** Sat, 2 Jan 2027  
**Calendar status:** confirm against official TAU year-end calendar.

## Before class

Prepare:

- Clinic Appointment requirement;
- blank class diagram area;
- OOA vs OOD comparison;
- simple assert-based tests.

## During class

| Time | Lecturer action |
|---|---|
| 08:30–08:45 | Review Week 13 contracts. |
| 08:45–09:10 | Requirement → OOA. |
| 09:10–09:35 | Candidate classes / responsibilities. |
| 09:35–10:00 | Minimal class diagram. |
| 10:00–10:10 | Break. |
| 10:10–10:35 | OOD: interfaces, references, contracts. |
| 10:35–10:55 | OOP implementation. |
| 10:55–11:20 | OOT: independent + collaboration tests. |
| 11:20–11:40 | University Registration lab. |
| 11:40–11:50 | Quiz / Week 15 bridge. |

## Live modelling

Do **not** open Python first.

Start from:

> A clinic has patients and doctors...

Ask:

```text
What concepts have identity?
What state belongs to each?
What behavior belongs to each?
What relationships exist?
```

Then move to diagram → design → code → tests.

## Workload guardrail

Use University Registration primarily as:

- in-class integration lab;
- Final Project Milestone A rehearsal.

Do not make it another large project while Final Project is active.

## Final Project Milestone A

Students should now show:

- candidate classes;
- responsibilities;
- relationships;
- class diagram;
- major invariants/preconditions.

---

# Week 15 — Reusability, Design Patterns & OOP Case Study

**Nominal date:** Sat, 9 Jan 2027

## Before class

Prepare:

- simple delivery `if/elif`;
- Strategy-style refactor;
- Factory Method-style notification example;
- Food Ordering case study.

## During class

| Time | Lecturer action |
|---|---|
| 08:30–08:45 | Review complete-design flow. |
| 08:45–09:05 | Code reuse vs design reuse. |
| 09:05–09:25 | Pattern concept. |
| 09:25–10:00 | Strategy-style delivery refactor. |
| 10:00–10:10 | Break. |
| 10:10–10:35 | Factory Method-style creation. |
| 10:35–11:10 | Food Ordering case study. |
| 11:10–11:30 | OOT / refactoring comparison. |
| 11:30–11:40 | Pattern-or-overengineering discussion. |
| 11:40–11:50 | Quiz / Final Project bridge. |

## Live code

Start with working branch logic:

```python
if mode == "pickup":
    ...
elif mode == "standard":
    ...
```

Ask:

> What varies, and what stays stable?

Only then refactor to strategy objects.

## Pattern rule

```text
problem first
→ variation identified
→ pattern if useful
```

Do not reward pattern count.

## Workload guardrail

Food Ordering is primarily an in-class reuse lab while Final Project is active.

## Final Project Milestone B

Students should have:

- core classes implemented;
- inheritance/polymorphism working;
- exceptions/contracts working;
- independent + collaboration tests;
- one end-to-end scenario mostly working.

---

# Week 16 — Final Project / Final Test

**Nominal date:** Sat, 16 Jan 2027

## Before class

Prepare:

- student roster and demo order;
- final rubric;
- viva question bank;
- timer;
- score sheet;
- backup demo slot plan;
- explicit policy for late/technical issues.

Confirm class size.

## Capacity planning

```text
20 students × 7 min = 140 min
25 students × 7 min = 175 min
30 students × 7 min = 210 min
```

If enrollment exceeds roughly 25 students, use:

- shorter bounded slots;
- parallel assessor if available;
- 23 Jan overflow.

## During demo/viva

Recommended per student:

```text
1 min     problem + model
1–2 min   design / class diagram
2 min     end-to-end runtime demo
1 min     polymorphism + contract
1 min     test + lecturer question
```

Ask at least one question that reveals ownership.

Examples:

- Why does this class own this responsibility?
- Why inheritance here?
- Show the runtime polymorphic call.
- What invariant is protected?
- Which test checks collaboration?
- Add one small validation or test live.

## What not to assess

Do not turn viva into trivia about:

- C3 internals;
- metaclasses;
- frameworks;
- databases;
- deployment.

## After class

Record:

- Final Project score;
- separate Demo / Code Explanation / Participation score;
- any approved overflow/makeup requirement.

Do not publish a complete reference solution on public `main`.

---

# Closure / Contingency — 23 Jan 2027

Use only for:

- final corrected submission;
- demo overflow;
- approved make-up;
- technical contingency;
- brief course feedback.

Do not introduce a new major OOP topic.

---

# Lecturer quick checklist

Before semester starts:

- [ ] TAU year-end dates confirmed.
- [ ] Final Project AI policy confirmed.
- [ ] Mid Test AI/tool policy confirmed.
- [ ] Final demo class size confirmed.
- [ ] Graded vs formative weekly evidence decided.
- [ ] Private quiz key stored outside public repo.
- [ ] Final reference solution, if any, stored privately.

Every Friday:

- [ ] Saturday notebook runs.
- [ ] README/assignment matches taught scope.
- [ ] Quiz is ready.
- [ ] No answer key is public.
- [ ] Live-code sequence is known.
- [ ] Student deliverable is clear.

Every Saturday after class:

- [ ] Graded deliverable announced.
- [ ] Due date announced.
- [ ] Common misconceptions recorded.
- [ ] Next-week prerequisite/reminder sent.
