# Message-based communication protocol
UID: 202204171725
Tags: #🌱 
Links: [[Communication Protocols]]

## **Messaging (Publish-Subscribe)**
- A (micro)service can publish a message to a certain communication channel maintained by the broker. A message can be used to send detailed information, or simply indicate an event when something notable happens. For example, a message may contain the actual details of an order or simply an event---"a new order 123 created".
- Other (micro)services subscribe to the channels maintained by the broker. The broker relays messages to the appropriate (micro)services subscribed to the appropriate channels.
- When a (micro)service receives a message, it can update its own data entities, which might raise more events or lead to more messages being published.

![Untitled](Enterprise%209aa48/Untitled%2015.png)

- When two or more (micro)services collaborate through messages that are sent/received via a broker, **the publisher is loosely coupled** from the subscriber:
- When a message is sent, the **subscriber does not have to be online**; (async)
	- The handling of a message **does not have to happen immediately** after the message is received; 
	- Handling of the message can happen whenever the subscriber is ready to do so; the subscriber may or may not reply back to the publisher; the reply may even come from another (micro)service.
