# Enterprise Solution Management | Support

# ESM What is Support
UID: 202204232005
Tags: #🌱 
Links: [[Enterprise Solution Management]]

-----
Tool set up

[Google Docs - create and edit documents online, for free.](https://docs.google.com/document/d/1EwP3ajo7pnHTeHIBbQhbNbyWK7hK5PpfJSEfRMYkm-o/edit)

# Overview

### Skills
- Ticketing system
- Team management
- Understanding SLAs

### Main Concepts
- [[Support objectives]]
	- [[Service level agreements]]
- [[Operating Systems]]
- [[IT Support Role]]
- [[Levels of service support]]
- System components

![Untitled](Enterprise%2078767/Untitled.png)

---
# Foundation: Enterprise solution

![Untitled](Enterprise%2078767/Untitled%201.png)

A solution is made up of various components:
- A1 – Hardware used in solution A
- A2 - Software system used in solution A
    - A2.1 - Main application for system A2
        - A2.1.1 – Component for main application A2.1
    - A2.2 - Second application in system A2
- A3 – Another software system used in solution A
    - A3.1 – Main application for system A3

![Untitled](Enterprise%2078767/Untitled%202.png)

## Example: Salesforce
- A1 – Server, networks, etc
- A2 – Products and services sales
    - A2.1 – Manage sales
        - A2.1.1 – Database for sales data
    - A2.2 - Customer management
- A3 – Company information
    - A3.1 – Website to display company information

![Untitled](Enterprise%2078767/Untitled%203.png)

# Dependencies

An application may rely on other software or libraries:

- Example: a script using Python 3 may not work on machines with Python 2.
- Large-scale dependency:
    - Example: LinkedIn with 10,000+ software components, each may have 100+ dependencies

## Virtualisation

This can become a problem. One solution is to use virtualisation. This creates an abstraction layer on top of heterogeneous hardware allowing various operating systems to run concurrently on the same hardware. Each OS runs in its own virtual machine (VM).

Cloud computing leverages virtualisation:

- Provide cheaper on-demand computing capacity
- Ease deployment: all dependencies packaged into a single VM
- Isolation: apps can run on different VMs on the same server

---

# Deployment Management

“The purpose of the deployment management practice is to move new or changed hardware, software, documentation, processes, or any other component to live environments. It may also be involved in deploying components to other environments for testing or staging.”

## [[Levels of service support]]


---

# People

Stakeholders cover business and technical:

### Business:

- Requesters
- Line managers
- Senior management
- Customers
- Etc..

### Technical teams:

- Deployment teams
- Developers
- Build and test team
- Operational staff
- Cyber security team
- Etc.


## **Responsibility Assignment Matrix - [[RACI]]**

[Responsibility Assignment Matrix (RAM) - AcqNotes](https://acqnotes.com/acqnote/careerfields/responsibility-assignment-matrix)
```ad-tip
💡 Everyone in a team should have a clear responsibility
```
[Activity 2.2 Lord of the Rings](Enterprise%2078767/Activity%202%2047486.md)

# [[User Training]]

# When Enterprise Solution are critical

Businesses often have various busy or critical times when enterprise solutions are critical. These could be due to:

- Customer deadlines
- Workload peaks e.g. financial reporting periods.
- Regular maintenance cycles for hardware or software
- Staff availability e.g. peak holiday periods
- Planned facilities changes
- Peak times of high-availability system that can never be shut down e.g. network and telephony switches

# Communication points

Good communication comes from having a kind, customer-centric concept and being good at the following things:

- **Quick response**: Customers appreciate a fast response when they ask a question or highlight a problem.
- **Acting on feedback**: Acts on any feedback received from a customer shows that their opinion matters.
- **Having empathy**: Trying to understand a customer’s point of view make a customer feel valued.
- **Customer self-service**: Allowing customers to find their own answers to problems can be very helpful.
- **Omnichannel support**: Different communication channels can support customers flexibly offering support through email, phone, live chat, and social media.
- **Going the extra mile**: Delivering value beyond the customer’s expectations or adding a personal touch be simple and can leave a positive impression.

# Support process

The support process comprises of:

- The support team
- Stakeholders (business and technical)
- Processes for handling support work
- A ticketing system

### Processes

- **Request**
    - A solution user needs something
- **Incident**
    - There is an issue with the solution (real or perceived)
- **Problem**
    - A current or potential cause of incidents
- **Change**
    - A user requests a change to the solution

## Ticketing system

A ticketing system will:

- Provide workflows for the support processes
- Log interactions with users
- Provide roles for the support team

A common ticketing system used is Jira (Jira | Issue & Project Tracking Software | Atlassian) (see Labs)

## Generic Ticketing System Process

![Untitled](Enterprise%2078767/Untitled%2010.png)

# Responsibilities
see: [[IT Support Role]]

[https://www.youtube.com/watch?v=aeEFuGnbV-s](https://www.youtube.com/watch?v=aeEFuGnbV-s)