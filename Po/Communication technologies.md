# Communication technologies
UID: 202204171624
Tags: #🌱 
Links: [[Inter-process Communication]]

# Sender vs. Receiver
#### Synonyms
- *Send:* produce, push, publish, broadcast, request, trigger, …
- *Sender:* producer, publisher, caller, requestor, …
- *Receive:* accept, consume, take, get, retrieve, acquire, pick up, …
- *Receiver:* listener, consumer, subscriber, callee, …
- Wait to receive: wait for, listen for, subscribe for a piece of data, …
- *Reply:* response, feedback, return, …
```ad-warning
title: Senders/receivers are NOT mutually exclusive 
A sender can become a receiver when receiving a reply; a receiver can become a sender when forwarding data to another receiver.

```

<aside>
💡 Which synonyms to use may depend on business scenarios and the communication technologies used.

</aside>

![Untitled](Enterprise%209aa48/Untitled%201.png)

![Untitled](Enterprise%209aa48/Untitled%202.png)

# [[Categorization Criteria for Communication Patterns]]

# [[Communication Protocols]]

## Similar terms for data

- Data, information, message, content, and value are mostly treated as synonyms in this course, although they have subtle differences.

##### Data
- Most general among the terms; it refers to any symbols or signs of something (e.g., a situation, person, company, product, account, etc.), whether understandable or not.

##### Information
- Understandable data about facts or details of something.

##### Message
- Data that is usually stored in transient memory (in contrast to persistent files, databases, external storages, etc.)

##### Content
- Information that is more relevant to a specific business scenario
- E.g., the content of a message may refer to the business information and networking information in the message

##### Value
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
