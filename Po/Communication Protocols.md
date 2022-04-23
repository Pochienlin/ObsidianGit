# Communication Protocols
UID: 202204171721
Tags: #🌲 
Links: [[Communication technologies]]
## Overview
| type             | format                       | sync/ async          | coupling        |
| ---------------- | ---------------------------- | -------------------- | --------------- |
| Invocation-based | point-to-point               | usually synchronous  | tightly coupled |
| Message-based    | via messaging intermediaries | usually asynchronous | loosely coupled |
Message-based intermediaries can include other concepts such as the [[Message-Oriented Middleware]]

## What are communication protocols used for?
- Used to *implement various communication patterns*
    - [[Invocation-based]]: data goes point-to-point
        ![Untitled](Enterprise%209aa48/Untitled%2010.png)
        - Usually synchronous. E.g., function (method) call; HTTP; gRPC
    - [[Message-based communication protocol]] (a.k.a., messaging): data goes through a message broker or intermediary(-ies)
        - Usually asynchronous.
        - E.g., AMQP, JMS, IPFS, …
        
        ![Untitled](Enterprise%209aa48/Untitled%2011.png)
        
-----
## Sample use cases
- **[[Invocation-based]]:** point-to-point
	- Phone call: a sender connects to a receiver by dialling a phone number; communication fails if the receiver doesn't answer
	- Web browsing (via HTTP): a web browser takes us to an URL; communication fails (e.g., 404) if the website doesn't respond properly.
- **[[Message-based communication protocol]]:** through some message intermediary(-ies)
	- Email: a sender sends an email to an address; the sender needs to connect to an email server to do so; the email may go through many email servers before reaching the receiver’s email server; the receiver may or may not receive the email at the time.
	- Phone voice message box: "leave a message"; the phone server stores the message, waiting for the receiver to retrieve the message sometime later.
	- WhatsApp messaging: two ticks for each message sent; one indicates the message reaches the server; the other indicates the message reaches the receiver's phone.
---

## Characteristics of Communication

![Untitled](Enterprise%209aa48/Untitled%2016.png)
