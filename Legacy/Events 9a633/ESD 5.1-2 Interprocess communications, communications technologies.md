# Enterprise Solution Developmt | 5.1 - 5.2 Inter-process Communications, Communication Technologies

Archive?: No
End: February 3, 2022 6:45 PM
Start: February 3, 2022 3:30 PM

---

# 5.1 ****Inter-Process Communication (IPC)****

---

### Objectives

- On completing this module, you will be able to:
- Demonstrate an understanding of the need for communication among processes and (micro)services
- Explain basic communication patterns among processes and (micro)services
- Understand variants of communication (transport) technologies

### Topics

- Communication patterns
- Communication (transport) technologies

# ****Communication****

- As defined by Cambridge Dictionary, communication is:
    - the process of sharing information, especially when this increases understanding between people or groups:
        - Transfer and exchange information
        - Collaborate
- Between enterprises, enterprise applications, software, (micro)services, etc.

## ****Need for Communication Among Processes****

- Notes about the term "process":
    - "processes" here refer to software processes running on a platform, not business processes. E.g., you can see the processes on Windows by using "Task Manager". However, software processes can be used to implement business processes.
    - (Software) processes usually refer to the dynamic, runtime instances of a software application; the same software application can have multiple processes (instances) running at the same time.

![Untitled](Enterprise%209aa48/Untitled.png)

Enterprise applications often need to use each other's functions or services, and exchange data, in order to realize business processes, within and between enterprises

- Each microservice often implements functions for one entity only
- Example entities: customer, account, product, order, payment, etc.
- Microservices can be deployed separately to different machines
- Each run of a microservice is a separate process in the OS in a machine
- Implementing a business process may require collaboration among more microservices than monolithic applications
- More communication among microservices across networks may be needed
- A status change in a microservice may induce changes in other microservices, triggering communications
- User interfaces need communications with underlying microservices

---

# ****Communication Patterns****

---

## Basic terms

### Sender || Receiver

### **Reply Data, or Reply Status, or Response**

### Synonyms

- Send: produce, push, publish, broadcast, request, trigger, …
- Sender: producer, publisher, caller, requestor, …
- Receive: accept, consume, take, get, retrieve, acquire, pick up, …
- Receiver: listener, consumer, subscriber, callee, …
- Wait to receive: wait for, listen for, subscribe for a piece of data, …
- Reply: response, feedback, return, …

<aside>
💡 Senders/receivers are NOT mutually exclusive: A sender can become a receiver when receiving a reply; a receiver can become a sender when forwarding data to another receiver.

</aside>

<aside>
💡 Which synonyms to use may depend on business scenarios and the communication technologies used.

</aside>

![Untitled](Enterprise%209aa48/Untitled%201.png)

![Untitled](Enterprise%209aa48/Untitled%202.png)

# Categorization Criteria for Communication Patterns

- How many receivers does the sender expect for the same data sent?
    - One receiver: one-to-one
        
        ![Untitled](Enterprise%209aa48/Untitled%203.png)
        
    - Many receivers: one-to-many
        
        ![Untitled](Enterprise%209aa48/Untitled%204.png)
        
        - E.g.,
            
            Email to all SMU addresses
            Public Warning System sounds an emergency message
            
    - All receivers: one-to-all
        
        ![Untitled](Enterprise%209aa48/Untitled%205.png)
        
        - E.g.,
            
            WhatsApp to a group
            Email to selected SMU addresses
            
        - Selected receivers: one-to-selected (can be zero, one, multiple, or all)
        - E.g.,
            
            Mail a letter to a person
            Email to one address
            
- Does the sender expect a reply for the data sent?
    - No: fire-and-forget (fire & forget, one-way)
        
        ![Untitled](Enterprise%209aa48/Untitled%206.png)
        
        - E.g.,
            - Send an anonymous suggestion letter
            - Radio broadcasting
            - Lecturing (old-school)
    - Yes: request-reply (request-response)
        
        ![Untitled](Enterprise%209aa48/Untitled%207.png)
        
        - E.g.,
            - Phone call
            - Flipped classroom learning & teaching
            - Place an order for a book
- Do the sender and the receiver need to be online at the same time to realize the communication?
    - Yes: synchronous (synchronized, sync.)
        
        ![Untitled](Enterprise%209aa48/Untitled%208.png)
        
        - Usually have reply data too
        - E.g.,
            - Phone call
            - Place an order for a book
    - No: asynchronous (asynchronized, async.)
        
        ![Untitled](Enterprise%209aa48/Untitled%209.png)
        
        - May or may not have reply data
        - Usually have some intermediary(-ies)
        - E.g.,
            - Mail a letter to a person
            - Email to all SMU addresses

---

# Communication Technologies (aka. Protocols)

---

- Used to implement various communication patterns
    - Invocation-based: data goes point-to-point
        
        ![Untitled](Enterprise%209aa48/Untitled%2010.png)
        
        - Usually synchronous. E.g., function (method) call; HTTP; gRPC
    - Message-based (a.k.a., messaging): data goes through a message broker or intermediary(-ies)
        - Usually asynchronous.
        - E.g., AMQP, JMS, IPFS, …
        
        ![Untitled](Enterprise%209aa48/Untitled%2011.png)
        

## Sample use cases

- Invocation-based: point-to-point

- Phone call: a sender connects to a receiver by dialling a phone number; communication fails if the receiver doesn't answer
- Web browsing (via HTTP): a web browser takes us to an URL; communication fails (e.g., 404) if the website doesn't respond properly.

- Message-based: through some message intermediary(-ies)

- Email: a sender sends an email to an address; the sender needs to connect to an email server to do so; the email may go through many email servers before reaching the receiver’s email server; the receiver may or may not receive the email at the time.
- Phone voice message box: "leave a message"; the phone server stores the message, waiting for the receiver to retrieve the message sometime later.
- WhatsApp messaging: two ticks for each message sent; one indicates the message reaches the server; the other indicates the message reaches the receiver's phone.

# Language-level Function call in Python

![Untitled](Enterprise%209aa48/Untitled%2012.png)

# ****HTTP Request-Response (RR)****

![Untitled](Enterprise%209aa48/Untitled%2013.png)

![Untitled](Enterprise%209aa48/Untitled%2014.png)

- "Request-Reply" is often used as a synonym of Request-Response; both are abbreviated as RR.
- A client doesn't need to know the language or platform used to implement the server, as along as it knows the URLs and how to send http request and receive http reply.
- A client doesn't have to be a web browser.
- We'll learn using python and its built-in "requests" module to send HTTP requests and receive responses.

## ****Messaging (Publish-Subscribe)****

- A (micro)service can publish a message to a certain communication channel maintained by the broker. A message can be used to send detailed information, or simply indicate an event when something notable happens. For example, a message may contain the actual details of an order or simply an event---"a new order 123 created".
- Other (micro)services subscribe to the channels maintained by the broker. The broker relays messages to the appropriate (micro)services subscribed to the appropriate channels.
- When a (micro)service receives a message, it can update its own data entities, which might raise more events or lead to more messages being published.

![Untitled](Enterprise%209aa48/Untitled%2015.png)

- When two or more (micro)services collaborate through messages that are sent/received via a broker, the publisher is loosely coupled from the subscriber:

- When a message is sent, the subscriber does not have to be online;
- The handling of a message does not have to happen immediately after the message is received;
- Handling of the message can happen whenever the subscriber is ready to do so; the subscriber may or may not reply back to the publisher; the reply may even come from another (micro)service.

---

## Characteristics of Communication

![Untitled](Enterprise%209aa48/Untitled%2016.png)

## Similar terms for data

- Data, information, message, content, and value are mostly treated as synonyms in this course, although they have subtle differences.

### Data

- Most general among the terms; it refers to any symbols or signs of something (e.g., a situation, person, company, product, account, etc.), whether understandable or not.

### Information

- Understandable data about facts or details of something.

### Message

- Data that is usually stored in transient memory (in contrast to persistent files, databases, external storages, etc.)

### Content

- Information that is more relevant to a specific business scenario
- E.g., the content of a message may refer to the business information and networking information in the message

### Value

- An actual piece of information about a particular fact or detail
- E.g., an argument value in a function call
- Sample Data/Message — JSON
    
    ```python
    {
      "orders": [
        {
          "customer_id": "Apple TAN", 
          "order_id": 5, 
          "order_item": [
            {
              "book_id": "9781434474234", 
              "item_id": 3, 
              "order_id": 5, 
              "quantity": 1
            }, 
            {
              "book_id": "9781449474212", 
              "item_id": 2, 
              "order_id": 5, 
              "quantity": 1
            }, 
            …
          ], 
          "timestamp": "Wed, 14 Nov 2018 22:42:31 GMT"
        },
        …
    ```
    
    For this sample...
    
    - **Data**: is about the JSON data; can be a JSON file (usually in harddisk) or a JSON message (usually in memory);
    - **Information**: is about a JSON object containing a key/name-value pair ("orders" is the name/key; the value is an array of other key/name-value pairs…);
    - **Content**: is about a list of orders, likely for a book ordering scenario;
    - **Value**: is about the specific values in the orders, e.g., "Apple TAN" is a value; "9781434474234" is another value; …
    - For communications, sending data/information/message/content/value/file/etc. are all possible, depending on the traditions for describing particular scenarios or contexts and how much specific details the description is intended to provide.

---

# 5.2 Communication Technologies

---

## Objectives

- On completing this module, you will be able to:
- Identify the communication patterns which are suitable for a given scenario
- Implement the communication patterns in a given scenario by using different communication technologies

## Topics

- Implementation of communication patterns
- HTTP

# ****HTTP Request-Response (RR)****

- "Request-Reply" is often used as a synonym of Request-Response; both are abbreviated as RR.
- A client doesn't need to know the language or platform used to implement the server, as along as it knows the URLs and how to send http request and receive http reply.
- A client doesn't have to be a web browser.
- We'll learn using python and its built-in "requests" module to send HTTP requests and receive responses.

### ****Sample Message Formats - HTTP Request & Response (GET)****

![Untitled](Enterprise%209aa48/Untitled%2017.png)

### ****Sample Message Formats - HTTP Request & Response (POST)****

![Untitled](Enterprise%209aa48/Untitled%2018.png)

![Untitled](Enterprise%209aa48/Untitled%2019.png)

![Untitled](Enterprise%209aa48/Untitled%2020.png)

---

## **Server Side: Receive HTTP Request and Send Response in Python**

### GET

```python
from flask import Flask, request

@app.route("/book/<string:isbn13>/<more>")
def find_by_isbn13(isbn13, more):
	return isbn13 + "/" + more, 200
```

### POST

```python
from flask import Flask, request

@app.route("/book/<string:isbn13>/<more>", methods=['POST'])
def create_book(isbn13, more):
	if request.is_json:
		data = request.get_json()
	else:
		data = request.get_data()
	return isbn13 + "/" + more + "/" + str(data), 200
```

---

## **Client Side: Send HTTP Request and Receive Response in Python**

JSON objects are dictionaries (i.e., key-value maps) in python, but some types of data are not valid JSON, e.g., datetime, single-quote strings, etc.

### **GET**

```python
import sys
import requests

serviceURL = "http://localhost:5000/book"

try:
	r = requests.get(serviceURL, timeout=1)
except requests.exceptions.RequestException as e:
	print(e)
	sys.exit(1)
print(r.status_code)
print(r.text)
```

### POST

```python
import requests

serviceURL = "http://localhost:5000/book"

isbn13 = "9781129474251"
bookinfo = {
	"title": "Tale of Zelda",
	"price": 33.40,
	"availability": 21
}

r = requests.post(serviceURL + "/" + isbn13,
			  json=bookinfo, timeout=1)
print(r.status_code)
print(r.text)
```

### Using `requests.request`

- References
    - Python requests module
        
        [https://docs.python-requests.org/en/latest/user/quickstart/](https://docs.python-requests.org/en/latest/user/quickstart/)
        
        [https://docs.python-requests.org/en/latest/](https://docs.python-requests.org/en/latest/)
        

```python
import requests

serviceURL = "http://localhost:5000/book"

isbn13 = "9781129474251"
bookinfo = {
	"title": "Tale of Zelda",
	"price": 33.40,
	"availability": 21
}

r = requests.request('POST',           serviceURL + "/" + isbn13,
		json=bookinfo, timeout=1)
print(r.status_code)
print(r.text)
```

---

# Bookstore scenario

---

- Communication pattern: one-to-one, synchronous request-reply between UI and Book.
- We've implemented our Book microservice in python/flask.
- The client in the UI can be written in HTML/JavaScript.

![Untitled](Enterprise%209aa48/Untitled%2021.png)

## **User Scenario Diagram – Place an order**

- This complex microservice orchestrates the communication among all other microservices for the business process.
- Sample communication patterns:
    - 1+7 : one-to-one, synchronous RR
    - 2 : one-to-one, fire & forget
    - 3+4 : one-to-one, sync RR
    - 5+6 : one-to-one, sync RR
    - "If error" case : one-to-one, fire-forget (FF)
    - 2+3 : one-to-two
    - 2+"If error" : one-to-two

![Untitled](Enterprise%209aa48/Untitled%2022.png)

### **Place an order: Implementation with HTTP Calls**

- Each of the microservices can be implemented as a python/flask program.
- When the service is reachable and running, each HTTP request always gets a reply including a HTTP status code (e.g., `200 OK; 400 BAD REQUEST; 404 NOT FOUND; 500 INTERNAL SERVER ERROR`).
- An HTTP request can fail due to various network issues.

When a HTTP service is invoked, it always returns a reply (with empty content), even if the sender doesn't need a reply, which may be wasteful.

![Untitled](Enterprise%209aa48/Untitled%2023.png)

![Untitled](Enterprise%209aa48/Untitled%2024.png)

---

# Choices of Communication Technologies

**P1 –** If a process or a user **needs an immediate response**, then the communication with all the relevant underlying microservices should use **invocation-based, synchronous communication.**

- To make it straightforward in receiving a response and avoid the perception of slow performance

**P2 –** If a process or a user **does not need an immediate response** (i.e., the process may be long-running or the user may interact at later time), then the communication with all the relevant underlying microservices should use **message-based, asynchronous communication.**