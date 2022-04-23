# Message-Oriented Middleware
UID: 202204171735
Tags: #🌱 
Links: [[Inter-process Communication]]
```ad-note
title: Summary

MOM is a software which sits between two or more applications or (micro)services and allow them to exchange data in the form of **messages**
```
# Overview
Message-oriented middleware (MOM) is software or hardware infrastructure supporting sending and receiving messages between distributed systems. MOM allows application modules to be **distributed over heterogeneous platforms** and **reduces the complexity of developing applications** that span multiple operating systems and network protocols. 

The middleware creates a distributed communications layer that insulates the application developer from the details of the various operating systems and network interfaces. 

This middleware layer allows software components that have been developed independently and that run on different networked platforms to interact with one another. Applications distributed on different network nodes use the application interface to communicate. In addition, by providing an administrative interface, this new, virtual system of interconnected applications can be made reliable and secure.

MOM provides software elements that reside in all communicating components of a client/server architecture and typically support asynchronous calls between the client and server applications. MOM reduces the involvement of application developers with the complexity of the master-slave nature of the client/server mechanism.

## Advantages
----
### Asynchronicity
Using a MOM system, a client makes an API call to send a message to a destination managed by the provider. The call invokes provider services to route and deliver the message. Once it has sent the message, the client can continue to do other work, confident that the provider retains the message until a receiving client retrieves it. The [[Message-based communication protocol]] model, coupled with the mediation of the provider, makes it possible to create a system of loosely coupled components.

See: [[Categorization Criteria for Communication Patterns]]

In asynchronous systems, message queues provide temporary storage when the destination program is busy or not connected. In addition, most asynchronous MOM systems provide **persistent storage** to back up the message queue. 
- This means that the problems with intermittent connectivity are solved. 
- It also means that should the receiver application fail for any reason, the senders can continue unaffected, as the messages they send will simply accumulate in the message queue for later processing when the receiver restarts.

### Routing
Many message-oriented middleware implementations depend on a message queue system. Some implementations permit routing logic to be provided by the messaging layer itself, while others depend on client applications to provide routing information or allow for a mix of both paradigms. Some implementations make use of broadcast or multicast distribution paradigms.

### **Transformation** (including data aggregation)
In a message-based middleware system, the message received at the destination need not be identical to the message originally sent. A MOM system with built-in intelligence can transform messages and route to match the requirements of the sender or of the recipient. 

In conjunction with the routing and broadcast/multicast facilities, one application can send a message in its own native format, and two or more other applications may each receive a copy of the message in their own native format. 

-----
## Disadvantages
The primary disadvantage of many message-oriented middleware systems is that they require an extra component in the architecture, the message transfer agent (message broker). As with any system, adding another component can lead to reductions in performance and reliability, and can also make the system as a whole more difficult and expensive to maintain.

In addition, many inter-application communications have an intrinsically synchronous aspect, with the sender specifically wanting to wait for a reply to a message before continuing (see real-time computing and near-real-time for extreme cases). Because message-based communication inherently functions asynchronously, it may not fit well in such situations. That said, most MOM systems have facilities to group a request and a response as a single pseudo-synchronous transaction.

With a synchronous messaging system, the calling function does not return until the called function has finished its task. In a loosely coupled asynchronous system, the calling client can continue to load work upon the recipient until the resources needed to handle this work are depleted and the called component fails. Of course, these conditions can be minimized or avoided by monitoring performance and adjusting message flow, but this is work that is not needed with a synchronous messaging system. The important thing is to understand the advantages and liabilities of each kind of system. Each system is appropriate for different kinds of tasks. Sometimes, a combination of the two kinds of systems is required to obtain the desired behavior.

---

![Untitled](Enterprise%200bac7/Untitled.png)

## Common message structure

![Untitled](Enterprise%200bac7/Untitled%201.png)

![Untitled](Enterprise%200bac7/Untitled%202.png)

