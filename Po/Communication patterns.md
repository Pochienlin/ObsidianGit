# Communication patterns
UID: 202204171617
Tags: #🌱 
Links: [[Enterprise Solution Development]] [[Inter-process Communication]]

## Communication
As defined by Cambridge Dictionary, communication is:
- the process of sharing information, especially when this increases understanding between people or groups:
	- Transfer and exchange information
	- Collaborate
	- Between enterprises, enterprise applications, software, (micro)services, etc.

 [[Enterprise Applications]] often need to use each other's functions or services, and exchange data, in order to realize business processes, within and between enterprises
```ad-note
title: A note on "processes" in the software context
Notes about the term "process":
- "processes" here refer to software processes running on a platform, not business processes. E.g., you can see the processes on Windows by using "Task Manager". 
- However, software processes can be used to implement business processes. (Software) processes usually refer to the dynamic, runtime instances of a software application; the same software application can have multiple processes (instances) running at the same time.

```

![Untitled](Enterprise%209aa48/Untitled.png)

Enterprise applications often need to use each other's functions or services, and exchange data, in order to realize business processes, within and between enterprises

- Each microservice often implements functions for one entity only
	- Example entities: customer, account, product, order, payment, etc.
- Microservices can be **deployed separately** to **different machines**
- Each run of a microservice is a separate process in the OS in a machine
- Implementing a business process may require collaboration among more microservices than monolithic applications
- More communication among microservices across networks may be needed
- A **status change in a microservice may induce changes in other microservices**, triggering communications
- User interfaces need communications with underlying microservices