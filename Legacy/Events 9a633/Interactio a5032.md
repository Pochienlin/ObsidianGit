# Interaction Design Prototyping | Interaction model

Archive?: No
End: September 1, 2021 10:15 PM
Start: September 1, 2021 7:00 PM
Tags: [IS211]

# Overview

**Mental Models**

- Understanding
- Specifying
- Using Metaphors
- Interaction Models

**Direct Manipulation Interfaces**

- Norman’s action model
- Gulf of Execution
- Gulf of Evaluation

## Main Concepts

1. 

# Mental Models

What is a **[Mental](http://www.useit.com/alertbox/mental-models.html) Model**?

> What the user believes about the system at hand - Jacob Nielsen
> 

> A mental model is an explanation of someone's thought process about how something works in the real world - Wikipedia
> 

The great interaction design problem

- Designer’s mental model becomes a conceptual model for the system
- Gaps may form between conceptual model and users’ mental models

**Conceptual model**

a high-level description of how an application is organized and operates.  It specifies the concepts that the application exposes to users and how they are organized.

- “The intended user’s model.”
    - When it doesn’t match the system implementation model, the user’s mental model will be unpredictable.
- A high-level description of how an application is organized and operates.
- Question

<aside>
💡 Main point summary

</aside>

## Concept model

A Conceptual Model specifies:

1. Objects exposed to users
2. Actions user can perform on each object
3. Attributes (user visible) of each object
4. Relationships between objects
5. type hierarchies (inheritance)
6. part/whole (containment)

### Lexicon

- Define UI terminology consistently
    - It helps users learn objects, attributes, and actions
        - In system user interface
        - In documentation
- These are NOT implementation objects
    - Users’ language independent from implementers’
    - Lexicon requires more policing and discussion
- K-Sketch Example
    - “Translate,” “Move,” or “Position”?
    - “Rotate,” “Spin,” or “Orientation”?
    - “Scale,” “Grow/Shrink,” or “Size”?

### Metaphor

![Untitled](Interactio%20a5032/Untitled.png)

Visicalc Story: [http://www.bricklin.com/visicalc.htm](http://www.bricklin.com/visicalc.htm)

`Benefits`

- Make system easier to use by creating metaphors that resemble the user’s real-world experiences
    - Eg. desktop, trash can, file cabinet, tree view, spread sheet,
- Exploit user’s familiar knowledge
    - Helps users understand unfamiliar functionality
- Gives users a language for discussing interaction

`Drawbacks`

Can be misleading, does not scale well, degrade overtime

A screenshot of Visicalc, the first spreadsheet, developed by Dan Bricklin in 1979 for the Apple II computer. This used the metaphor of a ledger sheet, a very common accounting tool. This helped new users to understand the basic operation of the spreadsheet.

![Untitled](Interactio%20a5032/Untitled%201.png)

### Interaction styles

**Instructing**

One-way verbal/textual

**Conversing**

Two-way verbal/textual

**Manipulating**

Interact with objects directly

**Exploring**

Move around in a space

## Direct Manipulation Interfaces

Properties

1. **Continuous representations** of objects
2. **Immediate** feedback on actions
    1. Instead of complete command language syntax
    2. Rapid reversible, incremental actions
3. Usage of **metaphors**

![Untitled](Interactio%20a5032/Untitled%202.png)

## Norman's action cycle

- Case study: OXO cup
    
    ![Untitled](Interactio%20a5032/Untitled%203.png)
    
    Problem is you have to repeatedly pour stuff in, lean down and check, pour stuff in…
    
    The OXO cup shows you exactly how much
    you have in there, and you don’t have to lean down to look at it.
    

### Design Considerations

- Reduce gulf of execution by making it easier to:
    - Determine the function of the device
    - Tell what actions are possible
    - Find mapping: intention → physical movement
    - Perform the action
- Reduce gulf of evaluation by making it easier to:
    - Tell what state the system is in
    - Find mapping: system state → interpretation
    - Remember the desired system state

![Untitled](Interactio%20a5032/Untitled%204.png)

# User Interface mapping

![Untitled](Interactio%20a5032/Untitled%205.png)

A lot of problems with mental models could be thought of as violations of the "Match between system and real world” heuristic. (We’ll discuss heuristics
later in the “Analytical Evaluation” lecture.

Here’s an example: I bet all of you could guess “front” and “back” correctly on the right, but not on the left.

Skeuomorphic design

![Untitled](Interactio%20a5032/Untitled%206.png)

# Summary

- [ ]  Designers specify mental models
    - Need to match system’s implementation model
    - Design tools: object/action analysis, lexicon
    - Metaphors exploit familiar knowledge, but can mislead
    - Interaction models: instruct, converse, manipulate, explore
- [ ]  Direct manipulation
    - Continuous representations with immediate feedback
    - Need handles
    - Norman’s action cycle
        - Gulf of execution: How do I specify what I want?
        - Gulf of evaluation: Did I get what I wanted?
    - Helps to map controls to the real world