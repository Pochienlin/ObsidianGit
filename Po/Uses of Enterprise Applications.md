# Uses of Enterprise Applications
UID: 202204171612
Tags: #🌱 
Links: [[Enterprise Solution Development]] [[Enterprise Applications and Business Processes]] [[Web applications]] [[Web app development]] [[Networking Basics]]
# Interactions among Enterprise Applications
- An activity performed by a person in an enterprise can affect other parts of the enterprise or other enterprises according to the business processes
    - Examples: CFO views the financial statement that aggregates data from Account Payable Manager, Account Receivable Manager; delivery notices may trigger reactions from the courier's systems; etc.
- Enterprise applications supporting the activities need to interact and collaborate.
- The same application can be used to support different activities in different business processes
    - Example: the Excel file for tracking cash flow can be used for financial statement generation too.

![Untitled](Enterprise%209b3bb/Untitled.png)

![Untitled](Enterprise%209b3bb/Untitled%201.png)

e.g. Warehousing might be outsourced in the future: Interface has to be changed to be external facing 

<aside>
💡 When designing, systems should keep common and foreseeable changes in mind to remain flexible → advantage of micro-services (module 1.3)

</aside>

# Role of Enterprise Applications in Business Process
- An activity (can be interactive or automated) in a business process often needs supports from enterprise applications
- An enterprise application is to support various activities in various business processes
- In the context of a business process, an enterprise application can
    - Provide interface for a user to perform a business activity
    - Apply pre-defined business rules (logic) to process input data
    - Analyze data
    - Produce new data
    - Store data
    - Retrieve data
    - Send data to another application
    - ...

# Need for Enterprise Applications to Exchange Data

- An enterprise is bound to have many applications that support different business activities and handle different data relevant to different parts of the enterprise
- Some business processes require applications from two or more enterprises to collaborate
- Not all activities or data can be supported or handled in one application
- Automating the exchange of data among applications helps to automate business processes and improve productivity