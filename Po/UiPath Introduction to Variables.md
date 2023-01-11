# UiPath Introduction to Variables
UID: 202205231651
Tags:
Links: [[Data Manipulation in RPA]]

##  Container theory of variable
UiPath subscribes to a container model of variables. Variables are containers that store a certain value out of many data types.

Variables help to pass values in an RPA process. A UiPath variable has the following properties
1. Name: Unique ID of the variable, should be descriptive
2. Type: string, int, array, datetime, bool, dataTables, QueueItem
3. Scope: local or global
4. Value

# Naming conventions
The name of a variable should be meaningful and describe the information it stores, thus making it easier to understand the purpose of the variable in the workflow.
For this, the developer must follow the following recommended best practices for naming a variable:
-   Use clear & meaningful names (the name of the variable should accurately describe its content)    
-   Keep variable names descriptive yet short    
-   Naming convention should be consistent throughout the project    

The table below specifies the 3 different naming convention that can be used:
| Case    | Camel Case | Pascal Case | Kebab Case  |
| ------- | ---------- | ----------- | ----------- |
| Example | helloWorld | HelloWorld  | Hello-World | 
Let's take an example where the developer wants to store the user's first name in a variable. The purpose of this variable is to store the first name of the user. Suppose we name this variable as "Name". In that case, it's still ambiguous whether this variable stores the user's first, last or full name. For clear understanding, the variable name should be "FirstName" so that everyone easily understands that this variable explicitly stores the user's first name. Similarly, for the last name, the variable name can be "LastName". If we want to store the full name, then the variable name can be "FullName".

# DataTable
> [!abstract] definition
> DataTable stores tabular data in rows and columns and may hold large pieces of data to act as a database
#### Usage
DataTables are used to migrate data from one  database to another, extract information from a website, and storing it in a spreadsheet

# QueueItem
> [!abstract] definition
> QueueItem is a data type unique to UiPath. This data type stores an item extracted from a queue, i.e., a container of items
#### Usage
Extracted items can be used as inputs for a subsequent step or other processes

> [!warning]
> UiPath's array only stores arrays of a single data type.

# Array vs String
| Array                                                                 | String                                                           |
| --------------------------------------------------------------------- | ---------------------------------------------------------------- |
| It is a sequential collection of elements of similar data types.      | It is a sequential collection of elements of similar data types. |
| Its elements are stored contiguously in increasing memory locations.  | It can be stored in any manner in memory locations.              |
| It is a special variable that can hold more than one value at a time. | It can hold only character data.                                 |
| Its length is predefined.                                             | Its size is not predefined.                                      |

# Variables Panel on UiPath
Enables user to create variables and modify them 
It is located at the bottom of the design panel. Minimised by default and opens on click.
- When a user renames a variable, the variable is renamed in all instances used
- If the user does not add a name, an automatically generated name is used instead
## Managing variables
### Create a variable
A variable can be created via the...
1. Variables panel
	1. Open variables panel 
2. Designer panel
	1. Drag and drop message box (or whichever activity of choice), press  `ctrl + K` (set name)
	2. Name the box.
3. Properties panel
	1. Click and existing box, go to `input` field 
	2. Press `ctrl + K` to rename the field
	3. Click its property in the properties panel
	4. Note: this is only possible if the designer panel contains at least 1 activity

### Initialising a variable
1. Name
	1. Must be unique 
	2. Make it descriptive such that others looking at the variable can infer its purpose or even data type
	3. Follows a convention and stick to it 
2. Type
	1. Browse and select from pop-up window
3. Scope
	1. Subprocess or
	2. Entire workflow
4. Default
	1. If required
### Removing a variable
A variable can be removed in two ways 
1.  Variable panel > `right-click` on variable to be deleted > select `delete`, or
2. Variable panel ? `left-click` to select variable to be deleted > press `delete` on keyboard 
#### Removing all unused variables
Go to the top ribbon > Design > Remove Unread Variable

[[UiPath Practices]]