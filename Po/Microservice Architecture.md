# Microservices Architecture
UID: 202204171530
Tags: #🌱 
Links: [[Enterprise Solution Development]] [[Enterprise Applications and Business Processes]]
- Microservices Architecture may also be written as Microservice Architecture in practice, abbreviated as **MSA**.
- It's more about the architecture when many microservices come together to form an enterprise solution, less about the architecture of individual microservices (which would be similar to the architecture of a monolithic application but at a small scale).
- Understanding of the pros and cons of MSA is an important part of ESD; its discussion will continue throughout the course.

<aside>
💡 The UIs may be decomposed into "micro-UIs" too.

</aside>
```ad-info
title: Defining MSA
A microservice may be defined as a single unit that implements only one or a few (instead of many) functionality needed to support business requirements and can be invoked by other applications (or microservices) over the network in a standard interface that is independent of programming languages and platforms
```
- Microservices are "loosely coupled" with each other
    - It can be implemented in a programming language of its own;
        - E.g., one microservice is implemented in Java; the other in Python;
    - It can be deployed and run on a platform of its own;
        - E.g., one microservice runs on Windows; the other on Linux;
    - It usually has its own data store when a data store is needed;
        - E.g., an Order microservice has its own database with an Order table; a Customer microservice has its own database with a Customer table
    - It can be scaled independently
        - E.g., instances of the same microservice that is more frequently used than others can be deployed to many machines to support concurrent processing
        Its implementation can be changed independently, as long as its interface for invocation remains the same

![Untitled](Enterprise%209b3bb/Untitled%205.png)

![Untitled](Enterprise%209b3bb/Untitled%206.png)

### Characteristics

- Microservices architecture is a style or pattern, not rigorous rules
- Each microservice is relatively small and simple in comparison with usual enterprise applications
    - A microservice can be developed and managed by a small agile team independently
    - Each development team can manage one or a few microservices
- Microservices exchange data with each other through a standard interface by using commonly used data formats and communication technologies
    - E.g. JSON over HTTP transport; messaging
- Microservices architecture promotes a methodology that develops an enterprise application or solution as an assembly of loosely-coupled microservices
- Sample Microservice architecture
    ![Untitled](Enterprise%209b3bb/Untitled%207.png)
- Sample Monolithic Bookstore Solution Overview
    
    ![Untitled](Enterprise%209b3bb/Untitled%208.png)
- Sample Microservices Bookstore Solution Overview
    
    ![Untitled](Enterprise%209b3bb/Untitled%209.png)

	### Microservice vs. Monoliths
