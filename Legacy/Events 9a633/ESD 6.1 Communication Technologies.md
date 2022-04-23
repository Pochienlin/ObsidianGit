# Enterprise Solution Developmt | 6.1 Communication Technologies
(Message-Oriented Middleware) - 6.2

Archive?: No
End: February 17, 2022 6:45 PM
Start: February 17, 2022 3:30 PM

# **Objectives**

On completing this module, you will be able to:

- Understand basic concepts of **Message-Oriented Middleware** (**MOM**)
- Understand basic concepts of the **Advanced Message Queuing Protocol** (**AMQP**)
- Understand **different AMQP settings** that can be useful for different communication patterns

## **Topics**

- MOM
- AMQP
    - Exchange, Queue, Binding Key / Routing Key
- RabbitMQ

---

# **Message-Oriented Middleware**

> • MOM is a software which sits between two or more applications or (micro)services and allow them to exchange data in the form of **messages**
> 

---

![Untitled](Enterprise%200bac7/Untitled.png)

## Common message structure

![Untitled](Enterprise%200bac7/Untitled%201.png)

![Untitled](Enterprise%200bac7/Untitled%202.png)

## Sample message structure for an AMQP message

![Untitled](Enterprise%200bac7/Untitled%203.png)

---

# Advanced Message Queuing Protocol (AMQP)

- An **open standard protocol** for MOM
    - Define a message format that allows standard and extensible representations of various types of data
    - (In theory) Provide **interoperability** among different AMQP-compliant implementation software that can be used on either the client side or the server side

- Supports various communication patterns
    - One-to-one, one-to-many, fire-forget, request-reply, etc.
- **RabbitMQ** is an implementation of AMQP
    - **pika** is a python module for clients in python to interact with AMQP / RabbitMQ servers.

# RabbitMQ

![Untitled](Enterprise%200bac7/Untitled%204.png)

- **RabbitMQ** is a message-queueing software;
    - It supports **AMQP** (and other protocols)
- It can be called a **message broker** or **queue manager**

## RabbitMQ Messaging - Exchange

![Untitled](Enterprise%200bac7/Untitled%205.png)

### Types of exchanges

- **Direct:** A direct exchange delivers a message to a queue whose **binding key** to the exchange **matches exactly** the **routing key** of the message sent to the exchange
- **Topic:** A topic exchange does a **wildcard match** between the routing key of a message and the binding keys of the queues bound to the exchange
    - I.e., a message is sent to a queue if the queue is bound to the exchange and the routing key of the message matches the wildcard pattern of the binding key of the queue
- **Fanout:** A fanout exchange routes a message to **all** of the queues that are bound to it

## Key binding

### Routing and binding keys

Producer sets a **routing key** for a message sent to an exchange in a broker; 

- the routing key is then matched by the exchange to the **binding keys / patterns** of the queues bound to the exchange.

Sample scenarios when different types of exchanges may be more
convenient for implementing the communication patterns:

- **Fanout**: radio station broadcast / news paper subscription / email group;
- **Topic**: select which notification to receive in your facebook
account;
- **Direct**: email address / home mail box

If multiple consumers subscribe to the same queue (bounded to the same exchanges) (AMQP 0-9-1):

- Messages are **load balanced** among the consumers

![Untitled](Enterprise%200bac7/Untitled%206.png)

Analogy to Post Office- the broker provides the functionalities of a post office;

- A queue in the broker is like a post box in a post office; An exchange in the broker is like a postman who dispatches mails into different post boxes.

## FIFO: Why queue messages? Trade-offs

1. Broker memory trade-off
    1. Faster ←→ if it breaks down, message is lost (persistence)
    2. If consumer no longer logs online, messages can take up memory in an inefficient way
2. Consumer might require preparation to receive.
    1. A queue may or may not be *durable*; 
        - if not, a message sent to the queue may be lost if the broker reboots or if there is no subscriber when the message reaches the queue.
    2. An exchange may or may not be *durable*;
        - if not, the exchange would be gone if the broker reboots.
    3. A message may or may not be *persistent* (delivery_mode=2 or pika.spec.PERSISTENT_DELIVERY_MODE); 
        - if not (i.e., delivery_mode=1 or pika.spec.TRANSIENT_DELIVERY_MODE), the message would be dropped if there is no receiver online when the message is sent.

## Messaging with RabbitMQ

- The **broker** accepts and forwards messages
    - A **producer** (publisher) sends messages to the broker
    - A **consumer** (subscriber) receives messages from the broker
- A **message** can be anything, including detailed business data or simply an event. E.g.,
    - Order message- {"order id":14, cust id:"191"}
    - Order event- "New order 14 created"
- The broker can keep a message in a **queue** until a consumer takes the message off the queue
    - A queue is a name indicating a message storage in the broker
    - Many queues can be created
    - Many messages can be sent to one queue; the same message can be sent to multiple queues
- A message is routed to a queue or queues via an **exchange** in the broker and **key pattern matching**

![Untitled](Enterprise%200bac7/Untitled%207.png)

### Wildcards

You can use `*` to denote a wildcard for a single word.

You can use # to denote wildcard for 0 or more words.

## **RabbitMQ/Pika Programming Model for Python**

The connection/channel to the broker needs to be set up for each/every run of a publisher or a consumer.

The set-ups of **exchange**/**queue** may need be done only once for all sessions/connections; they can be done separately via RabbitMQ management GUI or an automated script.

In the same session/connection, a publisher/a consumer can publish/consume many messages.

"**`on_message_callback`**" refers to a function that is defined in the consumer; the function can do anything with the message received according to the business requirements.

“`basic_consume`” sets up a consumer and binds the “on_message_callback” function to all messages to be received.

“`start_consuming`” starts a loop to wait to receive any message from the queue, and automatically invokes the "on_message_callback" function to process each of the messages received. Use Ctrl + C in the cmd windows to terminate it.

![Untitled](Enterprise%200bac7/Untitled%208.png)