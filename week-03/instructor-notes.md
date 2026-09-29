# Week 3 Instructor Notes — Attributes, Methods, State & Behavior

## Teaching goal

Students already know how to create objects with attributes.

This week should make the conceptual transition:

```text
Object has state
      ↓
Object provides behavior
      ↓
Behavior can read or change state
```

The most important design question is:

> What behavior naturally belongs to the object that owns the related state?

## Source alignment

### Inggriani Liem

Use the Diktat framing that:

- attribute values at runtime represent object **state**;
- a class also has **methods/services**;
- methods have a signature and executable body;
- services are associated with object interaction.

The Diktat also introduces preconditions/postconditions in the same broad section, but do **not** teach contracts formally here. They receive dedicated attention in Week 13.

### OpenStax

Use **11.3 Instance methods** as the Python implementation basis.

Focus on calling instance methods and working with instance attributes.

## Recommended 200-minute flow

| Time | Activity |
|---|---|
| 08:30–08:45 | Review: instances and attributes |
| 08:45–09:10 | Attribute values as object state |
| 09:10–09:35 | Instance methods as behavior |
| 09:35–10:00 | Read-only vs state-changing methods |
| 10:00–10:10 | Break |
| 10:10–10:30 | Method parameters vs object attributes |
| 10:30–10:55 | Responsibility: who owns the behavior? |
| 10:55–11:30 | Colab Book / Appointment lab |
| 11:30–11:40 | Borrow-twice challenge |
| 11:40–11:50 | Quiz / bridge to encapsulation |

## Opening example

Start from a Week 2 object:

```python
class Appointment:
    def __init__(self, patient_name, doctor_name):
        self.patient_name = patient_name
        self.doctor_name = doctor_name
        self.status = "waiting"
```

Ask:

> We can store an appointment's status. How should an appointment become confirmed?

Show direct mutation first:

```python
appointment.status = "confirmed"
```

Then:

```python
appointment.confirm()
```

Do not call the first form "illegal". Python allows it. The teaching point is that the method expresses **domain behavior** more clearly.

## State-changing vs read-only behavior

Use two simple examples:

```python
rectangle.area()
```

reads state.

```python
rectangle.resize(10, 20)
```

changes state.

Ask students to predict state before and after the call.

## Parameters vs object attributes

Use:

```python
def deposit(self, amount):
    self.balance += amount
```

Draw:

```text
amount
→ method-call input

self.balance
→ persistent object state
```

Avoid introducing local-variable lifetime internals beyond what students need.

## Responsibility heuristic

Use this wording:

> Behavior that closely depends on an object's own state is a candidate responsibility of that object.

Examples:

```text
Appointment owns status
→ confirm() can belong to Appointment

Rectangle owns width/height
→ area() can belong to Rectangle

OrderItem owns quantity + Product reference
→ subtotal() may belong to OrderItem
```

Do not present this as an absolute rule.

## Live coding sequence

Recommended:

```text
Appointment with status
        ↓
display_status()
        ↓
confirm()
        ↓
cancel()
        ↓
trace state transitions
```

Then move to `Book` and let students implement the same idea independently.

## The deliberate flaw

The Week 3 Book implementation should probably allow:

```python
book.borrow()
book.borrow()
```

This is useful.

Ask:

> What protects the object from an invalid state transition?

Do **not** solve the whole issue yet.

Use it to create the need for Week 4:

```text
State + Behavior
      ↓
Need controlled access
      ↓
Encapsulation
```

## Quiz answer key

1. **B**
2. **C**
3. **D**
4. **B**
5. **B**
6. State = data/attribute values describing the object at a point in time; behavior = operations/methods the object can perform.
7. Example: `area()` reads; `resize()` changes state.
8. It keeps behavior close to the data it needs and makes object responsibilities clearer.
9. `is_on` changes from `False` to `True`.
10. The class currently lacks rules/control around valid state changes; this motivates encapsulation/invariants in the next week.

## Assignment grading notes

Reward:

- meaningful state;
- behavior expressed as methods;
- correct before/after state reasoning;
- independent objects;
- clear explanation.

Do not reward unnecessary advanced syntax.

A student may observe that confirming a cancelled order should be invalid. That is a good observation, but the Week 3 implementation does not need to solve it yet.

## What not to teach yet

Avoid detailed treatment of:

- underscore/private conventions;
- `@property`;
- invariants;
- exceptions for invalid transitions;
- Client–Supplier relationships;
- inheritance.

Those belong to later weeks.

## Closing question

End with:

> If an object's state matters, should any code anywhere be free to change it to any value?

That leads directly to:

**Week 4 — Encapsulation & Abstraction.**