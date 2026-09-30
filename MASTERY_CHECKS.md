# Mastery Checks — Self-Paced Feedback

These checks are for **independent learning feedback**. They are deliberately different from the graded/facilitated module quizzes.

## How to use this file

For each module:

1. answer the prompts **before** opening the feedback;
2. explain your reasoning, not only the final answer;
3. open the feedback and compare the reasoning;
4. rerun or modify a code example when your reasoning differs;
5. return to the module before moving on if the gap is conceptual.

The collapsible feedback below is not an answer key for the public quizzes.

---

## Module 0 — Python Readiness

### Check A

What does this return?

```python
def keep_even(values):
    result = []
    for value in values:
        if value % 2 == 0:
            result.append(value)
    return result

keep_even([1, 2, 3, 4])
```

<details>
<summary>Feedback</summary>

It returns `[2, 4]`. The important reasoning is: the loop visits every value, the condition keeps only values divisible by 2, and the function returns the new list after the loop.

</details>

### Check B

Why is this a bug?

```python
def total(prices):
    total_value = 0
    for price in prices:
        total_value += price
```

<details>
<summary>Feedback</summary>

The accumulation works internally, but the function has no `return`, so callers receive `None`. You should be able to distinguish “computed inside the function” from “returned to the caller.”

</details>

---

## Module 1 — Thinking in Objects

### Check A

Requirement: “A library member borrows a book through a loan record.”

Which concepts are strong object candidates, and which relationship object is easy to overlook?

<details>
<summary>Feedback</summary>

`Member`, `Book`, and `Loan` are strong candidates. `Loan` is easy to overlook because beginners often store a borrowed book directly inside Member. Making Loan explicit can represent the relationship itself and later hold state such as borrow date, due date, or status.

</details>

### Check B

Why is “every noun becomes a class” a weak modelling rule?

<details>
<summary>Feedback</summary>

Some nouns are better represented as values or attributes. For a simple Appointment, `status` may be a string/value while Patient, Doctor, and Appointment have clearer identity, state, behavior, and lifecycle. Class selection is a design decision, not grammar extraction.

</details>

---

## Module 2 — Classes, Objects & Instances

### Check A

One `Student` class creates three Student instances. How many class definitions and runtime Student objects are involved?

<details>
<summary>Feedback</summary>

One class definition and three Student objects. A class describes a kind of object; each constructor call creates a distinct instance with its own instance state.

</details>

### Check B

Inside `student_a.display_info()`, what does `self` refer to?

<details>
<summary>Feedback</summary>

It refers to the particular instance receiving the call: `student_a`. The same method definition can therefore read different state when invoked on another Student instance.

</details>

---

## Module 3 — State & Behavior

### Check A

Why is `order.confirm()` usually more expressive than `order.status = "confirmed"`?

<details>
<summary>Feedback</summary>

`confirm()` expresses a domain operation and gives the object responsibility for the state transition. Direct assignment exposes representation detail and makes it harder to centralize rules around how confirmation should happen.

</details>

### Check B

Is `amount` in `account.deposit(amount)` object state?

<details>
<summary>Feedback</summary>

Not normally. `amount` is an input for one call. `account.balance` is persistent object state because it remains associated with the object after the method returns.

</details>

---

## Module 4 — Encapsulation & Abstraction

### Check A

If Python still allows `product._stock = -10`, what value does the leading underscore provide?

<details>
<summary>Feedback</summary>

It communicates an interface convention: callers should treat `_stock` as internal implementation state and use public operations instead. It is not a security boundary or strict private-access mechanism.

</details>

### Check B

For a Product whose stock must never be negative, what is the invariant?

<details>
<summary>Feedback</summary>

`stock >= 0`. Public operations such as adding or removing stock should preserve that rule after successful operations.

</details>

---

## Module 5 — Object Relationships

### Check A

Why should `Appointment` usually store a Patient object rather than duplicate `patient_name`?

<details>
<summary>Feedback</summary>

A reference preserves the relationship to the actual Patient object. Duplicating selected text creates another source of truth that can drift from the Patient object's state.

</details>

### Check B

Classify each relationship: “Car–Engine” and “Doctor–Person.”

<details>
<summary>Feedback</summary>

Car **has an** Engine, so composition/reference is appropriate. Doctor **is a** Person, so inheritance may be appropriate if that specialization is meaningful in the model.

</details>

---

## Module 6 — Inheritance

### Check A

What is wrong with using inheritance only because two classes share some code?

<details>
<summary>Feedback</summary>

Inheritance models a semantic subtype relationship, not merely code reuse. The key test is whether the subclass really **is a** specialized form of the superclass. Shared code alone can often be handled by composition or another helper.

</details>

### Check B

Why use `super().__init__(name)` inside a subclass constructor?

<details>
<summary>Feedback</summary>

It calls the superclass initializer to establish shared superclass-defined state, avoiding duplicated setup logic and keeping shared initialization in one place.

</details>

---

## Module 7 — Overriding, Polymorphism & Dynamic Binding

### Check A

Three Employee subclasses implement `calculate_pay()`. Why can one loop call `employee.calculate_pay()` without checking the subtype?

<details>
<summary>Feedback</summary>

The call is polymorphic. At runtime, method lookup selects the implementation appropriate to the actual object. The caller depends on the common operation rather than branching on concrete type.

</details>

### Check B

What is the difference between overriding and overloading in this course?

<details>
<summary>Feedback</summary>

**Overriding** means a subclass replaces or extends inherited behavior. **Overloading** refers to one operation/name/operator having multiple forms or meanings; Python operator overloading is handled later in Module 12.

</details>

---

## Module 8 — Mid Test Readiness

### Check A

Before attempting the Mid Test, can you take a new requirement and produce this chain without copying an old example?

```text
objects
→ state/behavior
→ relationships
→ classes
→ inheritance where justified
→ polymorphic behavior
```

<details>
<summary>Feedback</summary>

If any step depends on memorizing a previous domain rather than reasoning from the new requirement, revisit Modules 1–7. The Mid Test is primarily an integration test of modelling decisions.

</details>

### Check B

What should you avoid forcing into the solution merely to “show OOP”?

<details>
<summary>Feedback</summary>

Unnecessary inheritance, artificial classes, or polymorphism with no meaningful variation. The simplest coherent model that satisfies the requirement is stronger evidence than a design with more mechanisms.

</details>

---

## Module 9 — Abstract Classes

### Check A

When is a superclass a good candidate to be abstract?

<details>
<summary>Feedback</summary>

When the superclass represents a meaningful common specification but is not itself a complete object you intend to instantiate, and concrete descendants must provide one or more required operations.

</details>

### Check B

Can an abstract class contain implemented methods and state?

<details>
<summary>Feedback</summary>

Yes. “Abstract” does not mean empty. It can provide shared state and concrete behavior while leaving selected operations abstract for subclasses to implement.

</details>

---

## Module 10 — Multiple Inheritance & Mixins

### Check A

If both parents define `display()`, how does Python decide which inherited implementation is found first?

<details>
<summary>Feedback</summary>

Python follows the class's Method Resolution Order (MRO). Parent ordering contributes to that lookup order; inspect `ClassName.__mro__` rather than guessing.

</details>

### Check B

What makes a class a good mixin candidate?

<details>
<summary>Feedback</summary>

A mixin usually provides a small, focused reusable capability rather than the primary domain identity of the object. If the relationship is clearer as “has-a” or “uses,” composition may be preferable.

</details>

---

## Module 11 — References & Object Identity

### Check A

What happens here?

```python
a = [1, 2]
b = a
b.append(3)
```

<details>
<summary>Feedback</summary>

Both names refer to the same list object, so observing `a` gives `[1, 2, 3]`. This is aliasing plus mutation.

</details>

### Check B

What is the difference between `is` and `==`?

<details>
<summary>Feedback</summary>

`is` asks whether two references identify the same object. `==` asks whether the objects are equal according to their equality behavior. Equal value does not require identical object identity.

</details>

---

## Module 12 — Operator Overloading, Genericity & Modules

### Check A

Why is `Point + Point` easier to justify than `Student + Student`?

<details>
<summary>Feedback</summary>

Point addition has a conventional, domain-consistent meaning: combine coordinates/components. Adding two Student objects has no obvious unsurprising meaning. Operator overloads should communicate semantics, not merely demonstrate syntax.

</details>

### Check B

How does genericity differ conceptually from inheritance?

<details>
<summary>Feedback</summary>

Genericity parameterizes a reusable structure by type (for example, a list of different element types). Inheritance specializes a class vertically by deriving a subtype from a more general ancestor.

</details>

---

## Module 13 — Exceptions, Assertions & Contracts

### Check A

When should invalid user/caller input normally raise an exception instead of relying on `assert`?

<details>
<summary>Feedback</summary>

Expected invalid requests such as a negative deposit or excessive withdrawal should be handled explicitly with exceptions. Assertions are better for internal assumptions that should hold if the program logic is correct.

</details>

### Check B

For `withdraw(amount)`, give one precondition, one postcondition, and one invariant.

<details>
<summary>Feedback</summary>

Example: precondition `0 < amount <= balance`; postcondition `new_balance == old_balance - amount`; invariant `balance >= 0`. Exact wording may vary, but the timing and responsibility of each condition should be clear.

</details>

### Check C

For a Rental lifecycle `created → active → completed`, how would you describe “complete only from active” in contract terms?

<details>
<summary>Feedback</summary>

Treat `status == "active"` as a state-dependent precondition of `complete()`. The separate invariant is that status must remain within the valid status set. A transition rule constrains a move; it is not automatically a class invariant.

</details>

---

## Module 14 — OOA → OOD → OOP → OOT

### Check A

What is lost when you jump directly from a requirement to Python classes?

<details>
<summary>Feedback</summary>

You skip explicit reasoning about candidate concepts, responsibilities, relationships, interfaces, and contracts. Code can still run, but the design becomes harder to justify and test systematically.

</details>

### Check B

What testing progression does this course use?

<details>
<summary>Feedback</summary>

Test independent classes first, then collaborating classes, then at least one end-to-end scenario. This makes failures easier to localize and verifies both local behavior and object collaboration.

</details>

---

## Module 15 — Reusability & Patterns

### Check A

When does a Strategy-style design help?

<details>
<summary>Feedback</summary>

When one behavior has multiple interchangeable implementations and the caller would otherwise accumulate mode/type branching. Separate strategy objects move the variation behind a common operation.

</details>

### Check B

Why should a pattern name come after the problem is understood?

<details>
<summary>Feedback</summary>

Patterns are reusable responses to recurring design problems. Starting from the pattern encourages unnecessary abstraction and “pattern forcing.” First establish the variation/responsibility problem, then decide whether the pattern clarifies it.

</details>

---

## Module 16 — Final Project Defense

These are defense prompts rather than questions with one correct answer.

### Check A

Can you trace one requirement through all four stages?

```text
Requirement
→ OOA decision
→ OOD decision
→ Python implementation
→ Test evidence
```

<details>
<summary>Feedback</summary>

A defensible project can point to concrete evidence at every step. If a class, inheritance relationship, or pattern cannot be connected back to a requirement/design need, reconsider whether it belongs.

</details>

### Check B

Can you identify one design choice you deliberately **did not** use?

<details>
<summary>Feedback</summary>

Strong OOP judgement includes rejecting unnecessary mechanisms. For example: no multiple inheritance because composition is clearer, no operator overload because the domain has no natural operator meaning, or no pattern because the simple design already handles the variation.

</details>

---

## Final mastery rule

You are not ready merely because you recognize the example.

A stronger signal is that you can:

```text
predict
→ explain
→ implement from a blank start
→ test
→ defend the design choice
```

When your answer differs from the feedback, return to the relevant module, rerun an example, change one assumption, and explain the new result before moving on.
