# UiPath Practices
UID: 202205231639
Tags: #🌱 
Links: [[UiPath]]

#  Hello world
> [!question]
> Build a workflow that prints ‘Hello World’ in a message box.

##### Process Overview
• START
• Open UiPath Studio
• Add a Sequence activity
• Add a Message Box activity
• Enter the text “Hello World”
• STOP

##### Step-by-Step Process
Step 1: Open UiPath Studio.
Step 2: Create a new process and name it as “Hello World”
Step 3: Drag a Sequence activity from the Activities panel and drop it in the Designerpanel.
Step 4: Name the Sequence activity as “Sequence – Hello World”
Step 5: Right click on the Sequence activity container and select Annotations from the context menu.
Step 6: Enter the annotation ‘This code will create a workflow to print “Hello World” in a message box.’
Step 7: Insert a Comment activity from the Activities panel within the Sequence activity.
Step 8: Enter the comment “‘Message box’ activity displays a message box with the specified text.”
Step 9: Insert a Message Box activity below the Comment activity and name it as “Message Box – Hello World”. Add the annotation “This activity displays data in a message box.”
Step 10: In the text box of the Message Box activity, enter the text “Hello World”.
Step 11: Save and run the workflow

 # Variables 
 ```ad-question
 Build a workflow that swaps two numbers using a third variable. 
 ``` 
 - Ask the user to input two numeric values and store them in two variables. 
 - Swap values of both the variables using a third variable. 
 - Display initial and swapped values of both the variables in the Output panel. Process Overview

## Process overview
-  START 
-  Use an Input Dialog activity to receive two numeric values from the user. 
-  Store the received values in two integer variables called First_Input_Value, and Second_Input_Value 
-  Declare a third integer variable called Swapping_Support_Variable 
-  Use Assign activity to assign the value of First_Input_Value to Swapping_Support_Variable 
-  Use second Assign activity to assign the value of First_Input_Value to Second_Input_Value 
-  Use third Assign activity to assign the value of Second_Input_Value to Swapping_Support_Variable 
-  Use a Write Line activity to display initial and final values of First_Input_Value and Second_Input_Value in the Output panel.
-  STOP 


Step-by-Step Process 
- Step 1: Open UiPath Studio. 
- Step 2: Create a process and name it as “Variable Swapping` 
- Step 3: Drag a Sequence activity from the Activities panel and drop in the Designer panel. 
- Step 4: Name the Sequence activity as “Sequence – ‘This code is for swapping two numbers using a third variable’` 
- Step 5: Insert a Comment activity from the Activities panel within the Sequence activity.
 
- Step 6: Add comment “Taking input of two numbers from the user and swap them by using a third variable.` 
- Step 7: Drag another Sequence activity from the Activities panel and insert it below the Comment activity. 
- Step 8: Name the Sequence activity as “Sequence – ‘For prompting the user to give the
input'`. 
- Step 9: Right-click on the Sequence activity container and select Annotations from the context menu. 
- Step 10: Enter an annotation “This code is for swapping two numbers by using a third variable.` 
- Step 11: Insert an Input Dialog activity within the second Sequence activity and name it as *“Input Dialog – `First Variable by User`. "*
- Step 12: Right-click on the Input Dialog activity container and select Annotations from the context menu. Add an annotation: *“Taking User input and storing the value in `First_Input`. "*
- Step 13: In the Input Dialog activity, enter values as shown below: 
| Title         | Label |
| ------------- | ----- |
| “First Value“ | `Please enter the first numeric value:`      |
- Step 14: In the Variables panel, create a variable for the above Input Dialog activity as shown below: 
| Name                | Variable type | Scope                                                                           | Default |
| ------------------- | ------------- | ------------------------------------------------------------------------------- | ------- |
| `First_Input_Value` | Double        | Sequence – *‘This code is for swapping two numbers by using a third variable.’* |         |
- Step 15: Go to the Properties panel of the Input Dialog activity and insert `First_Input_Value` in its Output property.
- Step 16: Insert a second Input Dialog activity below the previous Input Dialog activity, and name it as *“Input Dialog – ‘Second variable by User’*. 
- Step 17: Right-click on the Input Dialog activity container and select Annotations from the context menu. Add an annotation: “Taking User input and storing the value in `Second_Input_Value`. 
- Step 18: In the second Input Dialog activity, enter values as shown below: 
| Title          | Label                                   |
| -------------- | --------------------------------------- |
| “Second Value" | “Please enter the second numeric value: |
- Step 19: In the Variables panel, create a variable for the second Input Dialog activity as shown below: Name Variable type Scope Default Second_Input_Value Double Sequence – ‘This code is for swapping two numbers by using a third variable.’ 
- Step 20: Go to the Properties panel of the Input Dialog activity and insert the variable Second_Input_Value in its Output property. 
- Step 21: Insert a Write Line activity from the Activities panel after the second Sequence activity, and name it as “Write Line – ‘Value entered before swapping’`. 
- Step 22: Right-click on the Write Line activity container and select Annotations from the context menu. Add an annotation: “Enter the text to get the result in the Output Panel`. 
- Step 23: In the text box of the Write Line activity, enter the expression: “First Value is: ` + First_Input_Value.ToString + Environment.NewLine + “Second Value is: ` + `Second_Input_Value`.ToString 
- Step 24: Insert another Sequence activity from the Activities panel below the Write Line activity, name it as “Sequence – ‘Swapping of numbers’`. Annotate it as “This block of code will swap the values of the numbers entered`. 
- Step 25: In the Variables panel, create a new variable as shown below: 
| Name                      | Variable type | Scope                                                                         | Default |
| ------------------------- | ------------- | ----------------------------------------------------------------------------- | ------- |
| Swapping_Support_Variable | Double        | Sequence – ‘This code is for swapping two numbers by using a third variable.’ |         |
- Step 26: Insert an Assign activity in the third Sequence activity, name it as “Assign – ‘Move the First_Input_Value to Swapping_Support_Variable’` and enter the annotation: “Swap Swapping_Support with First_Input_Value`. 
- Step 27: In the Assign activity, enter values as shown below: 
| To                        | Value             |
| ------------------------- | ----------------- |
| Swapping_Support_Variable | First_Input_Value | 
  - Step 28: Insert a second Assign activity below the previous Assign activity, name it as “Assign – ‘Move the Second_Input_Value to First_Input_Value’` and Enter the annotation “Swap First_Input_Value with Second_Input_Value`. 
- Step 29: In the second Assign activity, enter values as shown below: 
| To                | Value |
| ----------------- | ----- |
| First_Input_Value |  Second_Input_Value |
- Step 30: Insert a third Assign activity below the second Assign activity, name it as “Assign – ‘To swap Swapping_Support_Variable with Second_Input_Value’` and enter annotation: “Swap Second_Input_Value with Swapping_Support`.
- Step 31: In the third Assign activity, enter values as shown below: To Value Second_Input_Value Swapping_Support_Variable 
- Step 32: Insert a Write Line activity below the third Sequence activity, name it as “Write Line – ‘Swapped Result’` and enter annotation: “Enter the text to get the result in Output Panel`. 
- Step 33: In the text box of the Write Line activity, enter the expression: “First Value after swapping is: “ + First_Input_Value.ToString + Environment.NewLine + “Second Value after swapping is: “ + Second_Input_Value.ToString` 
- Step 34: Save and run the workflow.

# String Manipulation with RegEx
> [!question]
> Build a workflow using Split and Contains methods that extract sentences containing “RPA” from a paragraph
- Store a paragraph in a string variable using an Assign activity.
- Store all sentences from the text in an array using a Split method. 
- Loop through each sentence and identify sentences containing “RPA” using Contains method.
- Store all identified sentences in an MS Word file.

## Process Overview

- START
- Use an Assign activity to store a paragraph in a string variable called newText.
- Use newText.Split(“.”c) and store all sentences in an array called newSentence     
- Use a For Each activity and iterate through each item in the array newSentence 
- Use an If activity within the For Each activity to identify sentence that contains the string “UiPath" in it. Use item.Contains(“RPA”) as condition.
- Use a Type Into activity to store result in an MS Word file.
- STOP

# DataTable Manipulation
> [!question]
> Build a workflow using Data Table activities to join two library databases using matching student ID and display the output in a message box. 
- Create a data table variable and populate it with student ID and name of students. 
- Create another data table variable, and populate it with student ID and book names 
- Join both the data tables based on matching student ID. 
- Remove the student ID column and sort the final data table as per student names in alphabetical order from A to Z. 
-Display the final data table containing the student and book names in a message box as a string.

## Process Overview
- START
- Use two Build Data Table activities to create two tables. Store them in two DataTable variables called dt_users and dt_overdueBooks.
      - dt_users variable contain ID of students and name of user as string.
      - dt_overdueBooks variable contain ID of students and name of books as string.  
- Use a Join Data Table activity. Choose the Inner type for the Join activity. Write the two column names to be used as Join criterion and create a new data table variable to store the output called dt_borrowedBooks.
- Use a Remove Data Column activity to delete duplicate column – student ID – by specifying its index· 
- Use a Sort Data Table activity to sort the data table based on the name of students in alphabetical order from A to Z.
- Use an Output Data Table activity to print the content of the data table to a String variable.
- Use the Message Box activity to display the output
- STOP

# List manipulation
> [!question]
> Build a workflow using Concat and Join method that merges two lists containing the UK and Spain city names, sorts it, capitalizes the first letter of each item, and displays it in a message box. 
-       Create a list containing three UK cities in all capital letters. 
-       Create another list containing three Spain cities in small letters.
-       Merge both the lists together.
-       Sort the final list in alphabetical order from A to Z. 
-       Capitalize only the first letter of all the items in the final list. 
-       Display the final list in a message box in string format.
## Process Overview
- START
- Create two List variables called SpainCities and UKCities
- For SpainCities, instantiate and populate the List from the Variables Panel, using the expression: new List (of String) from {“madrid","valencia", “barcelona"}
- For UKCities, instantiate the List from the Variables Panel using the expression: new List (of String) from {“MANCHESTER”,”BRISTOL”,”GLASGOW”}
- Merge the two List variables in a newly created List variable using Enumerable.Concat method inside an Assign activity. 
- Use the expression: Enumerable.Concat(SpainCities.AsEnumerable, UKCities.AsEnumerable).ToList. 
      - .AsEnumerable converts the two Lists to Enumerable data type. 
      - .ToList converts the outcome to List
- Use an Invoke Method activity to sort the elements in the outcome List by specifying ‘Sort’ in the ‘MethodName’ field.
- Use a For Each activity to iterate through each element in the AllCities variable and convert them to ProperCase using the StrConv method. Use the expression: StrConv(item, VbStrConv.ProperCase)
- Add the converted items to a newly created List variable AllCitiesProperCase using an Add to Collection activity.
- Use a Message Box activity to display the converted values using the String.Join method. Use the expression: String.Join(",",AllCitiesProperCase).
- STOP