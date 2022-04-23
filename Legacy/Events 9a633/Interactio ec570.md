# Interaction Design Prototyping || Define

Archive?: No
End: August 25, 2021 10:15 PM
Start: August 25, 2021 7:00 PM
Tags: [IS211]

# Overview

**Objectives**

- Types of requirements
- Personas
- What are they
- How do you describe them
- Scenarios
- Difference from use cases
- Types of scenarios

![Untitled](Interactio%20ec570/Untitled.png)

# POV and Problem statements

Point of view is reframing of a design challenge into an **actionable problem statement** that will launch you into generative ideation

<aside>
💡 In short, what is the problem you are trying to solve?

</aside>

**Define** – unpack and synthesize your empathy findings into needs and insights

> Composite character profile (persona) ___ (persona) user **needs** to (function) ___ because ___ (**insights**)
> 

Reframe the problem based on new insights to get a point of view

# Establishing requirements

**Important considerations**

- **Functional** and **non-functional** requirements of the system (**software engineering**)
- Data requirements (**data engineering**)
- Environmental requirements – **context** of use
- User characteristics (**persona**)
- Task description (**scenario**)

- Understanding user’s need versus want (user centricity)
- Scoping and grooming/refinement
- Data-driven feasibility assessment

## Types of requirements

1. **Functional**: What the system should do? (behave)
    1. Software engineering focus of requirement
2. **Non-functional**: (Need to be quantified) Maintainable, fast, usable, scalable, regulatory, security etc

**Data**: What kinds of data need to be stored?

- How will they be stored (e.g. database)?

- Example
    
    ![Untitled](Interactio%20ec570/Untitled%201.png)
    

# Context of use

Environment or **context** of use:

- **Physical**: dusty? noisy? vibration? light? heat? humidity? …. (e.g. ATM)
- **Social**: sharing of files, of displays, in paper, across great distances, work individually, privacy for clients
- **Organisational**: hierarchy, IT department’s attitude and remit, user support, communications structure and infrastructure, availability of training

# Types of users

- **Users**: Who are they?
- **Characteristics**: ability, background, attitude to computers
- **Behavior range (aptitude)**
    - Expertise
        - **Novice**: step-by-step (prompted),  constrained, clear information
        - **Expert**: flexibility, access/power
    - Frequency
        - **Infrequent**
        (‘casual’): clear instructions, e.g. menu paths
        - **Frequent**: short cuts

# Setting up user personas

Capture ***user characteristics***(based on observations)

- Represented as **individual** (personification)
    - Not real people, but synthesised from real user characteristics
- Represent **groups** of users
    - Have distinct set of behaviour patterns (supported by data)
        - From ranges of behaviour and motivation (goals)
    - Not stereotypes, user roles, profiles, market segments
- Bring them to life with
    - **Name**, characteristics, attitudes, activities, *goals*, personal background (profession, age, location), influencers, *frustrations*,etc.
- Develop multiple personas
- Example
    
    ![Untitled](Interactio%20ec570/Untitled%202.png)
    

# Constructing personas

- Focus on most important persona
- Be selective on important details, capture differentiating features
- Balance with time constraints
- Adopt provisional personas when making rigorous personas is impossible
- Useful for designing qualitative data gathering process

## Types of personas

**Primary**

The most important user persona

**Secondary**

Users with additional (lower priority) needs

**Supplementary**

Needs already represented by primary and secondary

**Customer**

Purchase software, but don’t use it

**Served**

Served by software, but don’t use or purchase it

1. Identify behavioral **variables**
    1. E.g. Activities, attitudes, aptitudes, motivation, occupations, skills, age groups, etc
2. Plot/Map observation/interviewed subjects into the behavioral variable range
    1. E.g.Novice to Ex pert, or Price to Service conscious, or Necessity to Entertainment
3. Identify significant behavioral **patterns**
    1. Find cluster to form basis of a persona
4. Synthesize characteristics and goals
    1. Bullet points describe characteristics and behavior
        1. E.g. Use environment, typical workday
    2. Infer goals that lead to behavior pattern
    3. Give a name and profile/personality for each persona
        1. First person point of view "I never make mistakes so I never learn."
        2. Second person "You never make mistakes so you never learn."
        3. Third person "He never makes mistakes so he never learns" and is
        much more objective
5. Check redundancy and completeness
    1. Perform additional research to find behavior missing from behavior ranges
6. Expand description of attributes and behavior
    1. Expand bullet points of characteristics to third person narrative
    2. Add important details relevant to persona, e.g. photos
7. Designatepersona types
    1. Prioritize persona as primary, secondary, etc.

## Steps

Empathy Map is a tool to help synthesize observation and create a persona. It guides you to specify:

It helps you:

- User needs: identify needs or goal
- Communications: with stakeholders
- Data: collect data from user

[Class activity ](Interactio%20ec570/Class%20acti%20094ac.md)

**Say:** What are some quotes and defining words your user said?

**Do:** Whatactions and behaviors did you notice?

**Think:**What might your user be thinking? What does this tell you about his or her beliefs?

**Feel:** What emotions might your subject be feeling?

![Untitled](Interactio%20ec570/Untitled%203.png)

# Requirement — Crafting a scenario

- Use personas in your scenarios
    - **State specific pains/goals for each persona**
- Scenarios are used early in the design process to define what the product does
    - **But avoid specifying how product works**
- Persona goals are concrete
- Products (UI) are abstract

Scenario is **informal narrative story** about a specific situation

## Scenario vs Use case

- Example 1
    
    The Thomson family enjoy outdoor activity holidays and want to try their hand at
    sailing this year. There are four members of the family: Sky who is 10 years
    old, Eamonn who is 15 years old, Claire who is 35, and Will who is 40.
    
    While out on a shopping trip they call by at the travel agents in their local town to
    start exploring the possibilities ... The travel organizer is located in a
    quiet corner of the agents’ office, where there are comfortable seats and
    playthings for young children.
    
    They all gather around the organizer and enter their initial set of requirements—a
    sailing holiday for four novices. The stand-alone console is designed so that
    all members of the family can interact easily and comfortably with it.
    
    The system’s initial suggestion is that they should consider a flotilla holiday,
    where several novice crews go sailing together and provide mutual support for
    first-time sailors …”
    
    ---
    
    # Use case
    
    1. The system displays options for investigating visa and vaccination requirements.
    2. The user chooses the option to find out about visa requirements.
    3. The system prompts user for the name of the destination country.
    4. The user enters the country’s name.
    5. The system checks that the country is valid.
    6. The system prompts the user for her nationality.
    7. The user enters her nationality.
    8. The system checks the visa requirements of the entered country for a passport holder of her nationality.
    9. The system displays the visa requirements.
    10. The system displays the option to print out the visa requirements.
    11. The user chooses to print the requirements.

Scenarios: Informal narrative story about a specific situation with a UI

- Goals are concrete
- UI is abstract

Use cases: Formal sequence of actions performed on a specific UI

- Goals are abstract
- UI is concrete

- Which is best for requirements?
    - Scenario

- Which is best for software engineering?
    - Use case
- Example 2
    
    Corrine is a form teacher of two classes in secondary school. As a responsible teacher, she wants to provide frequent updates to the parents. This would be a good time to do so because it has been a month since the Meet-The-Parents session. While on the way to school, Corrine takes out her mobile phone and starts up the **EDUTracker** application.
    After logging into the system, Corrine’s form classes are displayed. She selects “Class 3A” to update. The first student, Albert Ang’s, page is brought up with his profile details and the option to assess his performance measures. After rating Albert, Corrine assesses his performance at school and includes a comment that Albert is an extremely helpful student. After that is done, Corrine assesses the next student, John Low. In a couple of minutes, she completes all updates for her students and navigates back to the home page.
    
    Later, Corrine remembers that there will be a supplementary class next week for Class 3A’s students. She decides to notify the parents about this. She navigates to the calendar page and proceeds to add an event to the calendar. After filling in the details, the event shows up in the updated calendar.
    
- Example 3
    
    Sam is waiting at the bus stop for his bus to go back home. He is mentally drained from the day’s work and wants some kind of simple entertainment while he has a free moment. He launches FoodPorn and sees a picture of Mushroom Ravioli. He thinks it looks tasty and *likes* it. Then he sees a picture of Chicken Butter Masala, which he does not like, followed by Cheese Ham Sandwiches and then Sashimi Sushi Set, both of which he doesn’t like.
    
    He finally comes across the image of Hawaiian Pizza, which looks exceptionally delicious to him. He reads the details on this food item and likes the picture. Having found out that his favourite Brazilian Chicken Ham is used in this dish, he is convinced that he should try it. He notes that this dish is from *Bella Pizza*, and proceeds to read up more about the restaurant. He reads through the list of deals they have, and is especially interested in their latest 1-for-1 deal on all dessert items, as his girlfriend loves desserts. He *follows* *Bella
    Pizza* in order to get updates on their latest promotions and new food items, as well as to keep track of restaurants on his to-visit list.
    
    Before going to the next item, his bus arrives and he suspends browsing. He boards the bus and quickly finds a seat, allowing him to quickly resume his food browsing until he reaches home.
    

[Class Activity — writing a scenario](Interactio%20ec570/Class%20Acti%20a8071.md)

## Types of scenarios

Context scenarios

- UI is abstract
- Focus on things outside UI
- Commonly used early in design

We call these "scenarios" earlier

Key Path scenarios

- UI concrete
- Describe interactions with system
- For most important paths only

Validation Scenarios

- UI concrete
- Shorter, often less important than key path
- Used for testing
- Answer "what if..." questions

Sometimes used for validating a design after it has been fleshed out in detail

---

# Putting it together

**Establishing requirements**

- Types: functional/non-functional, data, context, users

**Constructing Personas**

- Not real people, but built from real observations
- Details help to motivate design decisions
- Pitfalls: too many personas, or too detailed

**(Context) Scenarios useful in early-stage design**

- Specific goals, abstract UI (opposite of use case)
- Other types of scenarios useful in later design stages

![Untitled](Interactio%20ec570/Untitled%204.png)