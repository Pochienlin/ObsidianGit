# UiPath Activities Guide
UID: 202205231608
Tags: #🌱 
Links: [[Robotics Process Automation]]

----
#### System Activities Pack:
This package contains all the basic activities used for creating automation projects. 

The activities in this pack enable the robots to:
•	Manipulate data tables by adding or extracting information.
•	Directly interact with directories and files on user’s machine, performing any action a human user would.
Several activities in this pack help in the creation and execution of the automation projects themselves, such as logical operators and expressions.

#### UI Automation Activities Pack:
It contains all the basic activities used for creating automation projects. 

These activities enable the robots to:
•	Simulate human interaction, such as performing mouse and keyboard commands or typing and extracting text, for basic UI automation.
•	Use technologies such as OCR or Image recognition to perform image and text automation.
•	Create triggers based on UI behavior, thus enabling the Robots to execute certain actions when specific events occur on a machine.
•	Perform browser interaction and window manipulation.

#### Citrix Activities Pack:
It includes activities that can be used for XenServer 7.x and Citrix Hypervisor 8.0 virtualized infrastructures.

These activities enable IT Departments to easily automate processes for on-demand management and maintenance of Citrix virtual machines, by facilitating the following actions:
•	Provision of a new server from a template (e.g. for new application deployment, DevOps, etc.).
•	Take screenshots of the virtual machines before installing update packages or different versions of a program.
•	Reboot, power on/off (e.g. for applications and OS updates, resources efficiency).

#### Cognitive Activities Pack:
It helps the user to use Google's, IBM's, Stanford's and Microsoft's APIs, and automatically process the information that they help extract. 
The package enables the user to translate text from one language to another, as well as extract relevant information from a given piece of text such as the overall sentiment, key phrases, possible encountered errors and the language used. All the cognitive activities require an API key in order to be used within workflows.

#### Credentials Activities Pack:
It contains activities that work with Windows Credential Manager. This pack enables the user to add and delete credentials for specific Microsoft authentication packages, such as NTLM, Kerberos, Negotiate, Schannel, or Passport. Robots can also use these activities to retrieve credentials or simply prompt a human user to introduce his credentials, for later usage.

#### Excel Activities Pack: 
It helps users to automate all aspects of Microsoft Excel, which is an application used by many in all types of businesses. It contains activities that enable the user to read information from a cell, columns, rows, or ranges, write to other spreadsheets or workbooks, execute macros, and extract formulas. The users can also sort data, color code it or append additional information. 

#### Form Activities Pack:
It enables the user to create custom input forms that can be used to collect data from human users, or display custom callout messages, which can detail different parts of the attended automation.

#### Mail Activities Pack:
It facilitates the automation of any email-related tasks, covering various protocols, such as IMAP, POP3 or SMTP. UiPath also features activities that are specialized for working with Outlook and Exchange. These include sending emails, receive emails, deleting emails, and sending attachments. This pack is compatible with the Microsoft Outlook versions 2010, 2013, 2016, and Office 365.

#### PDF Activities Pack:
It contains activities designed to extract data from PDF and XPS files and store it into string variables. The data can be extracted from the entire document or from a range of pages specified under the Range property found in each of the activities. In the case of scanned documents, data extraction can also be achieved by using OCR-based activities, Read PDF With OCR and Read XPS With OCR. 

#### Terminal Activities Pack:
It contains activities designed to connect to a terminal and efficiently work within it. The user can retrieve text, fields, or screen positions, send keys, text, or wait for certain text or fields to appear as triggers. The Terminal Session activity enables the user to connect to a specific environment, such as Attachmate Reflection, Attachmate Extra, etc.

#### Web Activities Pack:
It enables users to perform SOAP or HTTP requests to any web APIs that support these protocols, including UiPath's Orchestrator API. 
The pack also contains activities that enable the user to manipulate XML and JSON files, such as executing XPath queries and deserializing documents, so that data extraction is easier.

#### Abbyy Activities Pack: 
It is used for extracting intelligent data and document capture processes from both structured and unstructured documents and it can work with the FineReader and FlexiCapture Abbyy product families. Includes activities for OCR, Cloud OCR, classification, and data extraction.

#### Cryptography Activities Pack: 
It provides encryption services to the user. The package enables users to encrypt and decrypt sensitive data by using encryption protocols.

#### Database Activities Pack: 
It enables the user to connect to a database and perform actions within it. It enables the user to perform actions in relation to databases, starting with the connection to the database, including data queries (interrogations of data based on a set criterion) and data altering operations (inserting data in the database, updating the data, and so on). 

#### Exchange Server Activities Pack: 
It includes a list of activities designed for Microsoft Exchange Server 2016 and 2019 (on-premises), which is a mail, calendar, schedule, and collaboration platform developed by Microsoft.

#### FTP Activities Pack: 
It enables the user to connect to a File Transfer Protocol server and perform all the fundamental actions within it, such as searching, downloading, uploading, deleting, or creating, both for files and directories.

#### Google GSuite Activities Pack: 
It helps the user to automate Google Cloud G Suite applications, including Google Calendar, Google Drive, Google Sheets, GMail, and Google Docs. With the Google GSuite Activities Package, the user can create & modify Google Calendar events, manage Google Drive files, read & send GMail messages, create new Google Sheet spreadsheets, and Google Docs documents. 

#### Intelligent OCR Activities Pack:
It contains the infrastructure for enabling document processing flows using a complete, open, extensible approach. It allows the user to digitize documents, classify documents, extract data from documents, validate automatic classification and data extraction, and export extracted information.

Document Processing Contracts: 
It is a .NET assembly that enables the user to integrate own classification and extraction activities with the Intelligent OCR activities package by exposing all of the interfaces needed to be compatible. By referencing the contracts in the pack enables the user to implement any activities.

#### Java Activities Pack: 
It contains several new activities that help the user to harness the power of Java code. With the Java Scope activity, the user can initialize a Java library, thus providing scope for all subsequent activities. 

#### Persistence Activities Pack: 
It offers several activities that help the user to manipulate Jobs, Tasks, and Queues in Orchestrator, offering a seamless transition between robotic automation and human intervention to enhance the capabilities of RPA.\

#### Python Activities Pack: 
It enables the user to invoke Python scripts and methods in any workflow directly from UiPath by connecting to the Python environment installed on the computer. 

#### Salesforce Activities Pack: 
It enables the user to automate Salesforce processes. Using this pack, the user can perform actions such as file manipulation, record manipulation, report execution, and SOQL commands execution.

#### SAP BAPI Activities Pack: 
It enables the user to connect to an SAP system and use an Invoke SAP BAPI activity to invoke a specified BAPI.

#### Screen OCR Activities Pack: 
It offers a machine-learning based OCR for screens. It can be used as an alternative to the other OCR engines, with any of the available Screen Scraping or Computer Vision activities from the UI Automation package.

#### Workflow Foundation Activities Pack: 
It provides functionality for control flow, conditions, event handling, state management, and communicating with applications and services.

## Other Activity Packs 
Some other activity packs available in UiPath are:

•	Active Directory Domain Services Activities Pack
•	AmazonWebServices Activities Pack
•	Azure Active Directory Activities Pack
•	Azure Activities Pack
•	MLServices
•	Document Understanding ML Activities Pack
•	OmniPageOCR Activities Pack
•	Word Activities Pack
•	VMware Activities Pack
•	Integrations Microsoft Office 365 Microsoft Dynamics 365
•	Microsoft Vision Activities
•	Google Vision Activities
•	Supported Character Encoding

For more details on the activities, please refer: https://docs.uipath.com/activities