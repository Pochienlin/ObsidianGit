# Invocation-based
UID: 202204171717
Tags: #🌱 
Links: [[Communication technologies]] [[Communication Protocols]]

```ad-note
title: Summary
Invocation-based communication includes, but are not limited to, *Language-level function calls* and *HTTP request-response*

```
Language-level function calls are the tightest coupling among services.
HTTP methods includes:
1. PUT | updating or modifying existing data
2. POST | inserting new data
3. GET | retrieving existing data
4. DELETE | removing existing data
# Language-level Function call in Python
![Untitled](Enterprise%209aa48/Untitled%2012.png)

# HTTP Request-Response (RR)**
![Untitled](Enterprise%209aa48/Untitled%2013.png)

![Untitled](Enterprise%209aa48/Untitled%2014.png)

- "Request-Reply" is often used as a synonym of Request-Response; both are abbreviated as RR.
- A client doesn't need to know the language or platform used to implement the server, as along as it knows the URLs and how to send http request and receive http reply.
- A client doesn't have to be a web browser.
- We'll learn using python and its built-in "requests" module to send HTTP requests and receive responses.