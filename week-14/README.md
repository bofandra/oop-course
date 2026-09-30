# Module 14 — OOP Analysis, Design, Class Diagram & Testing

## Learning outcomes

By the end of this module, learners should be able to:

1. transform a short requirement into candidate objects/classes;
2. distinguish the purposes of **OOA**, **OOD**, **OOP**, and **OOT**;
3. assign state, behavior, and responsibilities to candidate classes;
4. model simple relationships in a minimal class diagram;
5. refine analysis ideas into a more concrete class design;
6. connect method contracts to the design;
7. implement the design in Python;
8. test independent classes, collaborating classes, and an end-to-end scenario using simple assertions.

## Source alignment

Inggriani Liem presents an object-oriented software-development lifecycle with four stages:

```text
OOA
→ analyse the problem

OOD
→ create the detailed design / overall solution scheme

OOP
→ implement the classes in a programming language

OOT
→ test the classes and the complete system
```

For OOA, the Diktat says the main products are diagrams from the chosen methodology, with the **class diagram** as a central product, including class relationships/associations and system dynamics/interactions.

For OOT, the Diktat gives a useful testing progression:

```text
test independent classes
        ↓
test related/collaborating classes
        ↓
test the entire system
```

This module uses a deliberately minimal class-diagram notation and plain Python `assert` statements. The goal is the OOA → OOD → OOP → OOT reasoning flow, not advanced UML or testing frameworks.

## From Module 13 to Module 14

Module 13 focused on individual object operations:

```text
precondition
operation
postcondition
invariant
```

Module 14 zooms out:

> How do we move from a problem statement to a complete object-oriented solution?

## 1. The full flow

Use this course workflow:

```text
Requirement
    ↓
OOA
    ↓
Candidate Objects / Classes
    ↓
State + Behavior + Responsibilities
    ↓
Relationships / Class Diagram
    ↓
OOD
    ↓
Detailed Class Design + Contracts
    ↓
OOP
    ↓
Python Implementation
    ↓
OOT
    ↓
Independent-Class Tests
    ↓
Collaboration Tests
    ↓
End-to-End Scenario
```

## 2. Guided example — Clinic Appointment

Requirement:

> A clinic has patients and doctors. A patient can have an appointment with a doctor. An appointment has a scheduled time and status. An appointment can be confirmed or cancelled.

### OOA — candidate objects

Possible candidate objects:

```text
Patient
Doctor
Appointment
```

The analysis question is:

> Which concepts have their own identity, state, behavior, or responsibility?

### State and behavior

```text
Patient
State:
- patient_id
- name

Doctor
State:
- doctor_id
- name
- specialty

Appointment
State:
- patient
- doctor
- scheduled_time
- status

Behavior:
- confirm()
- cancel()
```

## 3. Minimal class diagram

For this course, a simple text diagram is enough:

```text
+------------------+
| Patient          |
+------------------+
| patient_id       |
| name             |
+------------------+

          ▲
          │ referenced by
          │

+------------------+
| Appointment      |
+------------------+
| patient          |
| doctor           |
| scheduled_time   |
| status           |
+------------------+
| confirm()        |
| cancel()         |
+------------------+

          │
          │ references
          ▼

+------------------+
| Doctor           |
+------------------+
| doctor_id        |
| name             |
| specialty        |
+------------------+
```

The goal is not perfect UML syntax.

The goal is to make:

- classes;
- state;
- behavior;
- relationships

visible before coding.

## 4. OOD — refine the design

Analysis tells us the important concepts.

Design makes the solution more concrete.

Example questions:

- What attributes belong to each class?
- Which class owns each operation?
- Which state should be internal?
- Which methods need preconditions?
- Which relationships are object references?
- What should the public interface look like?

For Appointment:

```text
Appointment
- patient: Patient
- doctor: Doctor
- scheduled_time
- _status

Public:
- status
- confirm()
- cancel()
```

Possible invariant:

```text
status is one of:
scheduled
confirmed
cancelled
```

## 5. OOP — implement the classes

```python
class Patient:
    def __init__(self, patient_id, name):
        self.patient_id = patient_id
        self.name = name


class Doctor:
    def __init__(self, doctor_id, name, specialty):
        self.doctor_id = doctor_id
        self.name = name
        self.specialty = specialty


class Appointment:
    def __init__(self, patient, doctor, scheduled_time):
        self.patient = patient
        self.doctor = doctor
        self.scheduled_time = scheduled_time
        self._status = "scheduled"

    @property
    def status(self):
        return self._status

    def confirm(self):
        if self._status != "scheduled":
            raise ValueError("Only scheduled appointments can be confirmed")
        self._status = "confirmed"

    def cancel(self):
        if self._status == "cancelled":
            raise ValueError("Appointment is already cancelled")
        self._status = "cancelled"
```

## 6. OOT — test independent classes

Start small.

```python
patient = Patient("P001", "Alya")

assert patient.patient_id == "P001"
assert patient.name == "Alya"
```

Then Doctor:

```python
doctor = Doctor(
    "D001",
    "Dr. Bima",
    "General Practice"
)

assert doctor.specialty == "General Practice"
```

These are independent-class checks.

## 7. Test collaborating classes

Now test Appointment with real Patient and Doctor objects:

```python
appointment = Appointment(
    patient,
    doctor,
    "09:00"
)

assert appointment.patient is patient
assert appointment.doctor is doctor
assert appointment.status == "scheduled"
```

Then behavior:

```python
appointment.confirm()

assert appointment.status == "confirmed"
```

This tests collaboration, not merely isolated attributes.

## 8. End-to-end scenario

A simple end-to-end scenario:

```text
create Patient
      ↓
create Doctor
      ↓
create Appointment
      ↓
confirm Appointment
      ↓
verify final state
```

A test:

```python
patient = Patient("P010", "Nadia")
doctor = Doctor("D010", "Dr. Raka", "General Practice")
appointment = Appointment(patient, doctor, "10:30")

assert appointment.status == "scheduled"

appointment.confirm()

assert appointment.status == "confirmed"
assert appointment.patient.name == "Nadia"
assert appointment.doctor.name == "Dr. Raka"
```

## 9. Analysis is not coding

A common mistake:

```text
read requirement
      ↓
immediately write class syntax
```

Module 14 instead asks learners to pause:

```text
What are the objects?
What is each responsibility?
What relationships exist?
What state must remain valid?
What should be tested?
```

Only then implement.

## 10. Design is not just drawing

A class diagram is useful, but OOD also includes decisions such as:

- public interface;
- internal state;
- constructor inputs;
- method responsibilities;
- simple contracts;
- collaboration between objects.

The diagram supports design reasoning; it does not replace it.

## Main lab — University Registration

Requirement:

> A university has Students and Courses. A Student can enroll in a Course through an Enrollment. A Course has a maximum capacity. An Enrollment has an active or cancelled status. A new Enrollment may be created only if the Course still has capacity.

Work through:

```text
Requirement
→ OOA
→ Candidate classes
→ State & behavior
→ Relationships
→ Minimal class diagram
→ OOD
→ Contracts
→ OOP
→ Python
→ OOT
→ Tests
```

Do not begin with Python syntax.

## Suggested candidate concepts

Learners should derive these first.

After discussion, a reasonable model may contain:

```text
Student
Course
Enrollment
```

The exact design may vary if responsibilities remain coherent.

## Testing target

Learners should test:

1. Student independently;
2. Course independently;
3. Enrollment collaboration;
4. capacity rule;
5. cancellation state;
6. one complete registration scenario.

Use plain `assert` statements.

No `pytest` is required.

## Reflection

Answer:

> What is lost when a programmer jumps directly from a requirement to code without performing object analysis and design?

## Reading

### Inggriani Liem

Focus on:

- OOA;
- OOD;
- OOP;
- OOT;
- class diagram as a central analysis product;
- testing independent classes;
- testing classes with relationships;
- testing the entire system.

### OpenStax

Use previously studied Python chapters only as implementation support.

This module's lifecycle framing comes primarily from the Diktat.

## Module 14 package

- [Colab notebook](14_oop_analysis_design_testing.ipynb)
- [Exercises](exercises.md)
- [Quiz](quiz.md)
- [Assignment](assignment.md)
- [Instructor notes](instructor-notes.md)
- [Mastery checks with worked feedback](../MASTERY_CHECKS.md)

## Next module

Module 14 builds a complete solution systematically.

Module 15 asks:

> Once we have a working OO design, what parts of the design can be reused rather than reinvented?

That leads to:

**Module 15 — Reusability, Design Patterns & OOP Case Study.**
