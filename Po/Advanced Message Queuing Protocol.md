# Advanced Message Queuing Protocol
UID: 202204171736
Tags: #🌱 
Links: [[Inter-process Communication]]

## Overview: What is AMQP?
- An **open standard protocol** for [[Message-Oriented Middleware]]
    - Define a message format that allows standard and extensible representations of various types of data
    - (In theory) Provide **interoperability** among different AMQP-compliant implementation software that can be used on either the client side or the server side
- Supports various communication patterns
    - One-to-one, one-to-many, fire-forget, request-reply, etc.
    - See [[Categorization Criteria for Communication Patterns]]
- **[[RabbitMQ]]** is an implementation of AMQP
    - **pika** is a python module for clients in python to interact with AMQP / RabbitMQ servers.

## Interoperability
AMQP mandates the behavior of the messaging provider and client to the extent that implementations from different vendors are *interoperable*, in the same way as SMTP, HTTP, FTP, etc. have created interoperable systems. 

Previous standardizations of middleware have happened at the API level (e.g. JMS) and were focused on standardizing programmer interaction with different middleware implementations, rather than on providing interoperability between multiple implementations. Unlike JMS, which defines an API and a set of behaviors that a messaging implementation must provide, AMQP is a **wire-level protocol**. 
- A wire-level protocol is a description of the format of the data that is sent across the network as a stream of bytes. 
	- Consequently, any tool that can create and interpret messages that conform to this data format can interoperate with any other compliant tool irrespective of implementation language.

## Specifications
AMQP provides flow controlled, message-oriented communication with message-delivery guarantees such as: 
1. at-most-once (where each message is delivered once or never), 
2. at-least-once (where each message is certain to be delivered, but may do so multiple times) and 
3. exactly-once (where the message will always certainly arrive and do so only once),
and authentication and/or encryption based on SASL and/or TLS.

It assumes an underlying reliable transport layer protocol such as Transmission Control Protocol (TCP).

The AMQP specification is defined in several layers: 
- a type system, 
-  a symmetric, asynchronous protocol for the transfer of messages from one process to another, 
- a standard, extensible message format and
-  a set of standardised but extensible 'messaging capabilities.'

## Sample message structure for an AMQP message
![Untitled](Enterprise%200bac7/Untitled%203.png)

---
