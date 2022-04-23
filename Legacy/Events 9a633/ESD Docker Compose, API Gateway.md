# Enterprise Solution Developmt | Docker Compose, API gateway

Archive?: No
End: February 24, 2022 6:45 PM
Start: February 24, 2022 3:30 PM

---

Docker Compose

---

# Overview

On completing this module, you will be able to:

- Understand the need of **container management** in the context of microservices architecture
- Use **Docker Compose** to manage multiple containers

## **Topics**

- Docker Compose

## Main Concepts

1. 

# Example

![Untitled](Enterprise%20aa003/Untitled.png)

![Untitled](Enterprise%20aa003/Untitled%201.png)

- Question

<aside>
💡 Main point summary

</aside>

# **Docker Containerization Process**

- **Dockerfile** contains the instructions for Docker to build an image (FROM, COPY, RUN, etc.)

## Running Book microservice in multiple containers

![Untitled](Enterprise%20aa003/Untitled%202.png)

![Untitled](Enterprise%20aa003/Untitled%203.png)

---

# Docker Compose

![Untitled](Enterprise%20aa003/Untitled%204.png)

### Example: YAML compose

```yaml
version: "3.8"
 
services:
 
  #################################
  # Book: The Book microservice
  #################################
  book:
    image: eklum/book:1.0
    restart: always
    environment:
      dbURL: mysql+mysqlconnector://is213@host.docker.internal:3306/book
 
  #############################################
  # callbook: The test_invoke_http.py program
  #############################################
  callbook:
    image: eklum/callbook:1.0
    depends_on:
      - book
    environment:
      bookURL: http://book:5000/book
```

- A tool for **defining** and **running** multi-containers
    - Use **YAML** files to define the configurations of containers
    - Use **docker-compose** command to run containers and related operations according to the configurations in a YAML file

## YAML

- **Y**et **A**nother **M**arkup **L**anguage
    - A.k.a., **Y**AML **A**in't **M**arkup **L**anguage
    - The file suffix is usually .yml or .yaml
- Often used to describe software configurations in a human-readable way
    - Use [...] for lists/arrays and {...} for name-value maps/dictionaries.
        - Can be considered as a superset of JSON
    - Use various compact syntax for describing data
        - E.g., use Python-style indentation to indicate nesting
        - E.g., use a leading hyphen ( - ) to indicate a list element
        - E.g., use a line to separate array/map elements from each other

## Using Docker Compose

![Untitled](Enterprise%20aa003/Untitled%205.png)

- A common procedure
    - Define a **Dockerfile** for each image to be built
    - Define needed services in **docker-compose.yml**
    - Run **docker-compose up** (or other suitable command options)

---

# API Gateway

---

# **Objectives**

On completing this module, you will be able to:

- Understand the concept of an **API Gateway** and how it is useful for a microservices architecture in an enterprise solution
- Sample solution: Alternative scenario diagram | Warehouse operator processes a shipping record
    
    ![Untitled](Enterprise%20aa003/Untitled%206.png)
    

## **Topics**

- API Gateway
    - Functionalities and drawbacks
    - Kong and Konga

# Why API gateway

![Untitled](Enterprise%20aa003/Untitled%207.png)

### Enterprise Service bus

![Untitled](Enterprise%20aa003/Untitled%208.png)

![Untitled](Enterprise%20aa003/Untitled%209.png)

---

# API Gateway

![Untitled](Enterprise%20aa003/Untitled%2010.png)

> A middleware, often a software component, that **manages external access to (micro)services** in an enterprise solution.
> 
- The API Gateway exposes (micro)services as REST APIs (typically), as REST is widely used by various clients

## Functionalities and benefits

- API Gateway, as a central hub, helps to **decouple** the clients and the (micro)service providers.
- It can also implement many **functionalities commonly needed** for all the service providers.
    - (Re-)**Routing** of communication data
    - **Load balancing**
    - **Security enforcement** (e.g., access control)
    - Monitoring / logging
    - Caching
    - Versioning
    - Aggregation
    - ……

## Disadvantages

- API Gateway, as a central hub, is an additional **single-point of failure**.
- It may cause **performance degradation** and become a **bottleneck** since HTTP requests/responses going through the gateway may need additional processing.
- It is **yet another component** in an enterprise solution that needs to be developed, deployed and managed.