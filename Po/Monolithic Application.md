# Monolithic application architecture
UID: 202204171535
Tags: #🌱 
Links: [[Enterprise Solution Development]] [[Enterprise Applications and Business Processes]]

The 3-tier architecture is analogous to the MVC design pattern (cf. [https://en.wikipedia.org/wiki/Model–view–controller](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller)):

- DB is the model (defining all the data), UI is the view (providing user interfaces), the server/app is the control (containing all business logics).

![Untitled](Enterprise%209b3bb/Untitled%203.png)

### Enterprise

- In the past, an enterprise application is usually built as a single unit with a single logical executable
- It usually comprises three main parts
    1. Client-side User Interface (e.g., HTML pages and javascript running on the browser)
    2. A database (consisting many tables covering multiple entities)
    3. Server-side application that handles:
        - The HTTP requests,
        - Executes business logic,
        - Retrieve and update data from the database,
        - Select and populate HTML view to be sent to the browser,
        - …
- The server-side application is usually deployed as a single package, referred to as a monolithic application or monolith

### Characteristics

Has a single code base implementing all functions needed for various business processes (e.g., one big archive file (with .war or .ear suffix) for a Java enterprise application; one folder containing various subfolders and many files for a PHP web application)

- Typically, the entire application is developed in one programming language (e.g., C++, Java, Python, or PHP) on one platform (e.g., Windows, Linux, or macOS)
    - Easier for different parts of the application to be compatible
    - Less flexibility for the choices of technologies
    - Less suitable for heterogeneous environments
- Over the years, the single code base may become large and complex, difficult to understand and maintain
    - Different parts of the application have too many interactions and dependencies, even though the code may be modularized
- Deployment of a monolith is often either all or none
    - Not easy to deploy only a part of the application due to dependencies
    - A change to one function often requires redeploying the entire application package
    - Scaling only a specific function is not possible, the entire application has to be scaled
- Example
    
    ![Untitled](Enterprise%209b3bb/Untitled%204.png)
-----
# See also
[[Microservice Architecture]]
---

