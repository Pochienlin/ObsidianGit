# 2.3 Microservices Design Exercise

## Objectives

- On completing this module, you will be able to:
- Design a microservices architecture for a given scenario
- Explain pros and cons of the design

## Topics

- MSA design

## Business Requirements

[Mini Case 2-Bookstore Scenario.docx](2%203%20Micros%20c1aef/Mini_Case_2-Bookstore_Scenario.docx)

Read the Mini Case: Bookstore Scenario

Draw design diagrams

## Sample overall scenarios in this bookstore

### User scenarios

- Browse books in the bookstore
- Place an order for a book
    - Likely need two UI pages, one for browsing, the other for placing an order, although they can be linked in some way (e.g., via a hyperlink or a click button)
    

### (Data) Entities

- Book
- Order
- Shipping Record
- Activity Log
- Error
- Customer
- …

### Example: Monolithic Bookstore Application

- All functionalities in the monolith are implemented in the same language, and interactions happen via function calls in the language.
- All data entities are stores in various tables in the same database.
    
    ![Untitled](2%203%20Micros%20c1aef/Untitled.png)
    

Decomposed:

![Untitled](2%203%20Micros%20c1aef/Untitled%201.png)

### Example: Scenario Overview Diagram	– A customer browses books in the bookstore

![Untitled](2%203%20Micros%20c1aef/Untitled%202.png)

![Untitled](2%203%20Micros%20c1aef/Untitled%203.png)

### Technical Overview Diagram

![Untitled](2%203%20Micros%20c1aef/Untitled%204.png)

# Discussion

- Are there clear SOA layers in this microservices design?
- Hint: where are the components/microservices in this design that implement the business processes (user scenarios)? Which component controls the workflow of the business process?
- Hint: should a business process be in the same layer as that of its constituent components/microservices?

- Pros and cons of this decomposed design versus the monolithic design
- Hint: why do we use microservices instead of monoliths? Think of an enterprise that needs to change its business functions, processes, products/services from time to time.

## Choreography as an architectural design pattern

- Implementation of a workflow or business process is a composition of services that collaborate in a distributed manner without a single-point of control
- Each service performs its own functions without knowing others, but may need to know the data passed through the workflow, in order to process the right data correctly
- The workflow or business process is completed collectively by more than one service

## Orchestration as an architectural design pattern

- Implementation of a workflow or business process is a composition of services in a single-point of control
- There is a service (i.e., the controller) controlling the workflow
- Each service, except for the controller, performs its own functions without knowing others
- The controller need to know all the other services controlled by it, and pass right data to the right services for processing

## Choreographic vs. Orchestrative

- Choreographic architectural pattern
    - No clear central controller of a business process
    - Microservices can react to any data or event received without knowing who is the sender, and send out data without knowing who is the receiver
    - Distributed coordination among microservices

- Orchestrated architectural pattern
    - A central controller, often a complex microservice, exists in a business process
    - The controller interacts with other microservices to complete a business process
    - Centralized coordination among microservices