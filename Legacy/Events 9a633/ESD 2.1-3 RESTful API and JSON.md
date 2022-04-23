# Enterprise Solution Developmt | Modules 2.1 – 2.3

Archive?: No
End: January 20, 2022 6:45 PM
Start: January 20, 2022 3:30 PM

---

# 2.1 Restful APIs and JSON

---

# Overview

**Objectives**

On completing this module, you will be able to:

- Demonstrate an understanding of some basic concepts of **REST APIs**
- Understand the **role of JSON** in helpingapplications exchange data
- **Develop business documents** based on JSON
- **Implement and invoke** a REST API with JSON data

**Topics**

- REST APIs
- JSON

## Main Concepts

1. 

---

# 2.1: REST APIs

---

# What is REST

- Representational State Transfer (REST)
    - Proposed by Roy Thomas Fielding in his PhD dissertation in 2000 "Architectural Styles and the Design of Network-based Software Architectures"
    - A retrospective definition of an architectural style that includes a set of principles, properties, and constraints for HTTP-based applications
- It uses the following standards
    - HTTP (Hypertext Transfer Protocol)
    - URL (Uniform Resource Locators, e.g., [https://www.google.com/maps](https://www.google.com/maps)) or URI (Uniform Resource Identifiers, e.g., a 10-digit ISBN 0-599-87118-0; a DOI 10.1145/3106237.3121282)
    - JSON, HTML, XML, JPEG, etc.
- APIs (Application Programming Interfaces) following this architecture style are referred to as
    - RESTful, REST-based, REST-way, REST-style APIs, or simply
    - REST APIs, also one kind of web services

## Architectural style

![Untitled](Enterprise%20bcef0/Untitled.png)

![Untitled](Enterprise%20bcef0/Untitled%201.png)

---

# REST Operations

Use standard HTTP operations (methods) explicitly

| Operation | Meaning |
| --- | --- |
| POST | Create a resource on the server |
| GET | Retrieve a resource from the server |
| PUT | Update a resource on the server |
| DELETE | Delete a resource from the server |

Documentation of REST APIs. E.g.,

| Resource | Method | URL | Description |
| --- | --- | --- | --- |
| book | GET | http://zoko.com:5000/book | Return a list of all available books. 

Content type/format: application/json |
| book | GET | http://zoko.com:5000/book/<isbn13> | Return information about a book <isbn13> <isbn13> should be a string of 13 digits. 

Content type/format: application/json |
| book | POST | http://zoko.com:5000/book/<isbn13> | Create a new book record on the server, return the information about the created book record.

Content type/format: application/json

Input sample: {"title":"Tale of Zelda", "price":33.40, "availability":21} |
| order | GET | http://zoko.com:5000/order/<order_id> | Return information about an order <order_id>. <order_id> should be a positive integer.

Content type/format: application/json |

# REST Characteristics

- Examples that may be used for your course project
    - National Digital Identity (NDI): [https://www.ndi-api.gov.sg/](https://www.ndi-api.gov.sg/) & [https://www.smartnation.gov.sg/initiatives/strategic-national-projects/national-digital-identity](https://www.smartnation.gov.sg/initiatives/strategic-national-projects/national-digital-identity)
    - Amazon
    - eBay
    - Facebook
    - Flickr
    - Google
    - PayPal
    - SendGrid
    - Twitter
    - Yahoo
    - …

- Client-server model
- Simple uniform (standardized) interface
- Each API is language and platform agnostic
    - Its implementation can be in any language of choice.
    - Its deployment can be on any platform of choice.
    - It can be invoked on any OS and with any language.
- Typically supports only the HTTP / HTTPS transport
- Supports a variety of data formats
    - TEXT, JSON, HTML, XML, OData, JPEG, MP4, etc.
- Uses "self-describing" data
- Layered system
    - Allow proxies, gateways, firewalls, caches, load balancers, etc. in-between clients and servers.
- Each API is often stateless
    - The server processes each API invocation in isolation; it doesn't maintain states about the client or previous API invocations.
    - The client needs to send all necessary context information to the server at the same time when invoking the API.
    - Lack standards for security, transactions, etc. that need to keep states.

---

# 2.1.2 JSON Data Format

---

# JSON

- JSON (JavaScript Object Notation) is a lightweight data-interchange format

### Example: An array/ list of books

```json
{"books": [
    {"availability": 2,
      "isbn13": "9781129474251",
      "price": 21.5,
      "title": "SQL in Nutshell"
    },
    {"availability": 25,
      "isbn13": "9781349471231",
      "price": 99.4,
      "title": "Understanding People"
    },
   …
]}
```

### Example: Customer Order

```json
{
 "name"   : "John Smith",
 "ItemID" : "20223",
 "Descrip" : "Washing Machine"
 "price"    : 1234.95,
 "shipTo"  : {"name" : "Jane Smith",
               "address" : "123 Maple Street",
               "city" : "Pretendville",
               "state" : "NY",
               "zip"   : "12345" },
 "billTo" : {"name" : "John Smith",
               "address" : "123 Maple Street",
               "city" : "Pretendville",
               "state" : "NY",
               "zip"   : "12345" }
}
```

- Easy for humans to read and write
- Easy for machines to parse and generate
    - Many languages have built-in supports
- Uses a text format that is independent of programming languages and platforms
- JSON can be "self-describing"

# JSON References for self-revision

- Data is a collection of values
- Values have types (a.k.a. data types)
    - number, string, Boolean (true or false), array, object, null (an empty value)
- Curly braces hold objects
    - An object is an unordered set of name-value pairs
    - A name is a string, also referred to as an attribute or a key
    - A value can be of any allowed type
    - Pairs are separated by commas
    - The name and the value in a pair is usually separated by a colon ':'
- Square brackets hold arrays
    - An array is an ordered list of zero or more value of any allowed type
    - Array values are usually separated by commas

# JSON Syntax Rules - Examples

- JSON Name-Value Pair

```json
"firstName" : "Jessica"
```

- Strings must be enclosed in double quotes

- JSON Object: inside a pair of curly braces

```json
{"firstName":"Jessica", "lastName": "Tan"}
```

- JSON Array: inside square brackets

```json
"students":[ {"firstName":"Jessica", "lastName": "Tan"}, 
{"firstName": "Martin", "lastName": "Wang"}, 
{"firstName": "Alan", "lastName":"Jones"}]
```

<aside>
💡 Whitespace around or between values and punctuation but not within a string value is ignored.

</aside>

# JSON Characteristics

- Self-describing: JSON data is often both human readable and machine-readable
- Allow hierarchy, that is, values within values
- Can be parsed and used by any programming language on any OS
    - JSON text data can be parsed by the standard JavaScript function (JSON.parse(…)) included in all major browsers
    - Python built-in module: import json; json.loads(…)
- Can use JSON schema to define and validate the correctness of JSON data
    - Conceptually similar to defining and validating database tables according to a database schema
- Unlikely some other data storage mechanisms (e.g., database tables), it lacks standard or efficient ways to search through the data

---

## Read more

[JSON - Wikipedia](https://en.wikipedia.org/wiki/JSON)

[JavaScript JSON](https://www.w3schools.com/js/js_json.asp)

---

# 2.2 **Service and SOA Concepts**

---

# Outline

## Objectives

- On completing this module, you will be able to:
- Understand the benefits of exposing and using functionalities through standard interfaces
- Know the concept of a service and a microservice
- Know the concept of Service-Oriented Architecture (SOA)
- Know the concept of building an enterprise solution as an assembly of (micro)services

## Topics

- (Micro)Service
- SOA

---

### Sample Monolith: Star Mall solution overview

![Untitled](Enterprise%20bcef0/Untitled%202.png)

![Untitled](Enterprise%20bcef0/Untitled%203.png)

### Sample Microservices Architecture for Star Mall

![Untitled](Enterprise%20bcef0/Untitled%204.png)

![Untitled](Enterprise%20bcef0/Untitled%205.png)

# Benefits of using Standard Interfaces

- Enable more convenient data exchange among different enterprise applications by using commonly used data formats and communication technologies
    - E.g., JSON over HTTP transport
- Language and platform agnostic
- Applications become less coupled with each other
    - Different applications can be developed and deployed with different technologies
    - All kinds of applications, including legacy ones, can be made more easily compatible with others, through standardized integration modules, adaptors, connectors, plug-ins, etc.

# Defining a Service in the software world

- The unit can be a monolithic application or a mini-application. The application can be a COTS, a custom app, or a legacy app.
- The functions in the server are said to be exposed as a service if it provides a standard interface for others to use the functionalities.
- Q: is the "hello world" python/flask program in the previous lab a service?
- Web service provides a standard interface over the web/network.

A service may be defined as:

- A unit that provides one or many functionalities needed to support business requirements and can be used by other applications or services over the network via a standard interface that is independent of programming languages and platforms
- The Service Provider Interface and the Service Consumer Interface refer to some code that is at the provider and consumer end respectively and enables data exchange between the provider and the consumer.

![Untitled](Enterprise%20bcef0/Untitled%206.png)

# Sample Order Handling through Service Interfaces

*(partial, for illustration only)*

## Service oriented architecture

- Consider turning all IT systems into services
- Each service can be small, simple, or large, complex
- Develop and maintain enterprise solutions as assemblies of loosely-coupled services
- Manage assemblies at various layers of different functionality and/or complexity. Sample layers:

![Untitled](Enterprise%20bcef0/Untitled%207.png)

[2.3 Microservices Design Exercise](Enterprise%20bcef0/2%203%20Micros%20c1aef.md)

![Untitled](Enterprise%20bcef0/Untitled%208.png)

## Microservice and MSA Revisit

- A microservice may be defined as:
    - A service that can be independently developed and deployed and provides one or a few functionalities needed to support business requirements
- Develop and maintain enterprise solutions as assemblies of loosely-coupled microservices
    - Provide all functionalities needed as microservices
    - Each microservice is relative small, simple
- Sample SOA layers with microservices:

![Untitled](Enterprise%20bcef0/Untitled%209.png)