# UiPath String and DataTable Manipulation
UID: 202205261310
Tags:
Links: [[UiPath String and DataTable Manipulation]]

# String Manipulation

## Methods for String Manipulation
Some of the operations that can be performed on strings are given below. You should attempt using these expressions in studio and see how they work. 
-	**Concat**: Concatenates the string representations of two specified objects. 
      - Expression: String.Concat (VarName1, VarName2)

-	**Contains**: Checks whether a specified substring occurs within a string. Returns a Boolean value (true or false).
      - Expression: VarName.Contains (“text”)

-	**Format**: Converts an entire expression (or value of objects) into a string (and inserts them into another text). Reduces complexity and increases readability.  
      - Expression: String.Format(“{0} is {1}”, VarName1, VarName2)

-	**IndexOf**: Returns the zero-based index of the first occurrence of a character in a string.
      - Expression: VarName1.IndexOf(“a”)

-	**Join**: Concatenates the elements in a collection and displays them as a string.
      - Expression: String.Join(“|”, CollVarName1)

-	**Replace**: Identifies a sequence of characters of the string type in a text and replaces it with a given string. 
      - Expression: VarName.Replace (“original”, “replaced”)

-	**Split**: Splits a string into substrings based on certain criteria set by the user. This criterion could be a space, comma, or full stop. 
      - Expression: VarName.Split(“|“c)(index)

-	**Substring**: Extracts a substring from a string using the starting index and the length. It is used to isolate or separate a substring from the original string. 
      - Expression: VarName1.Substring(startIndex, length)

[[UiPath Practices]]


# DataTable Manipulations
A DataTable is an in-memory representation of a single database table that has a collection of rows and columns
- DataTable stores data as a simple spreadsheet with rows and columns so that each piece of data can be identified based on their unique column and row coordinates

### Manipulations
1. Build
	1. Builds reliable structure for a DataTable
	2. Alows customization of several columns and type of data
	3. Configure each column with specific options
2. Read Range
	1. Reads the data from an existing file
	2. Copies the content of a worksheet
	3. created directly from the properties panel
3. Read CSV
	1. Reads the content of a CSV
	2. Stores it in a DataTable variable
4. Data Scraping
	1. Enables user to extract structured data from a browser, app or document and store it in a DataTable

### Activities
Some of the activities used for DataTable manipulations are:
- **Add Data Column: **
	- Adds a column to an existing DataTable variable.
	- The input data can be of DataColumn type or the column can be added empty, by specifying the data type and configuring the options (allowing null values, requesting unique values, auto-incrementing, default value and maximum length). 
- **Add Data Row:**
	- Adds a new row to an existing DataTable variable. 
	- The input data can be of DataRow type or can be entered as an Array Row, by matching each object with the data type of each column.
- **Merge Data Table: **
	- It is used to merge a specified DataTable with the current DataTable. 
	- The operation is simpler than the Join Data Type activity, as it provides four types of actions to take when merging – 
		- adding, ignoring, returning an error and manual input (Addwithkey option).
- **Lookup Data Table: **
	- It allows searching for a provided value in a specified DataTable and returns the RowIndex at which it was found 
	- Or can be configured to return the value from a cell with given coordinates (RowIndex and Target Column). 
- **Filter Data Table:**
	-  It allows filtering a DataTable through a Filter Wizard, using various conditions. 
	- This activity can be configured to 
		- create a new DataTable for the output of the activity, or 
		- to keep the existing one and filter out (delete) the entries that do not match the filtering conditions.
- **Join Data Tables: **
	- It combines rows from two tables by using values common to each other. 
	- It is one of the most useful activities in business scenarios, where working with more than one Data Table is very common.
- **Generate DataTable:**
	-  Creates a DataTable variable from unstructured data, by letting the user indicate the row and column separators. 
	- This option is extremely useful when data is captured from scanned documents or web scraping. 
	- In order to be able to process the data, the creation of a DataTable is the first step. 
	- The activity allows the definition of separators (any string character), but also allows the identification of elements using their position on the screen (useful when the data source is OCR).
- **For Each Row:**
	-  It is similar to the For Each loop as it iterates through all the rows in a DataTable and performs the same action. 
	- This can be very useful for manipulations that have to be done individually for each row and cannot be grouped at the column level (for example, verification of the relation between two values stored in two columns). 
- **Clear DataTable: **
	- It clears all the data entries in a DataTable. 
	- It can be very useful with DataTables that are used as intermediary tables for data moved from one table to another.
- **Output DataTable:**
	-  It is used to write a specified DataTable into a text (string variable) in a CSV format. 
	- This can serve as an intermediate step in a process or as a final step when, after several manipulations, a DataTable contains only several values.
- **Remove Data:**
	- It is a group of two activities used to remove rows or columns from an existing DataTable.
	- Rows can be identified by their index number or by inputting the DataRow as an object, and the Columns can be additionally identified by their names.
- **Remove Duplicate Rows: **
	- It is used to remove the duplicate rows, while keeping only the first occurrence.
- **Sort DataTable: **
	- It is used to sort a DataTable using a specified column as the criterion. 
	- Besides indicating which column to use in this respect, the user can choose whether the sorting will be done ascending or descending.

[[UiPath Practices]]