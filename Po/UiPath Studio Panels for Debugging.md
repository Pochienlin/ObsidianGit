# UiPath Studio Panels for Debugging
UID: 202205231634
Tags: #🌱 
Links: [[UiPath]]

----
# Panels for Debugging

Debugging is the process of identifying and removing errors that prevent the project from functioning correctly. It is recommended to perform debugging during the design stage of the automation project, at activity, file, and project level. Debugging can be performed using several options, defined in the debug ribbon. Several panels make it easier to view the debugging process, add values or monitor variables and arguments. These panels include:

![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/mSyl15kSQIqspdeZEvCKqw_c29ae34d7a8448beb3a6a6191af139a1_Picture1.png?expiry=1653436800000&hmac=TKpew3Um36zlJUCHzI9PoQxqRHKNozbARNGDM0iIpHg)

![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/wb9vU3i2TNq_b1N4tozaAg_aa431dbc98f5453dbe368c2c1f0b4fa1_Picture2.png?expiry=1653436800000&hmac=QXKuUKmsuub_nzEAda39qe3Fg7995yrrPp8-6MTuMHY)

The Locals panel displays properties or activities and user-defined variables and arguments. The panel shows: 
- Exceptions - the description and type of the exception. 
- Arguments 
- Variables 
- Properties of previously executed activity - only input and output properties are displayed. 
- Properties of current activity 

The panel is only visible while debugging. Right-click an argument, variable or property of the currently executing activity to add it to the Watch panel and monitor its execution throughout the debugging process. The Arguments, Properties, and Variables categories can be collapsed or expanded. The same is available for complex objects, which are displayed in a tabular way.

![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/cvcmnowgR363Jp6MIJd-dA_85d8a900f70d432b80d8ce90c215eba1_Picture3.png?expiry=1653436800000&hmac=bAe2m_yocPjXa9cz9Arq2armibQAsXiPNbQWaC4uLzI)

The Call Stack panel displays the next activity to be executed and its parent containers when the project is paused in debugging. 

The panel is displayed during execution in debug mode, and it gets populated after using Step Into, Break, Slow Step, or after the execution was paused because an error or a breakpoint was encountered. Double-clicking an item in the Call Stack panel focuses and highlights the selected activity in the Designer panel. If during debugging, an activity throws an exception, it is marked in the Call Stack panel, and the activity is highlighted in red.

![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/T6EMATJ5STWhDAEyeTk10Q_4198c9bed01f40508323c539601e5ea1_Picture4.png?expiry=1653436800000&hmac=xget5AjzPV8Gh9MvBeZNL5lakbGh6EmgW6nGTh5YK4A)

Breakpoints are used to purposely pause the debugging process on an activity that may trigger execution issues. Setting a condition and/or hit count turns the simple breakpoint to a conditional one. Adding logging results turns the conditional breakpoint in a conditional tracepoint. Adding only a logging message transforms the breakpoint to a simple tracepoint. 

The Breakpoints panel displays all breakpoints in the current project, together with the file in which they are contained. The Activity Name column shows the activity with the toggled breakpoint, while the File Path column displays the file and its location. The Condition column displays conditions set to breakpoints. The Log Message column shows messages to be logged if the condition is met. Hover over the breakpoint tag on an activity to view its condition and log message.

![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/89YlaeuAQcSWJWnrgDHELA_386581d388eb427fb1d4582e3c5aa2a1_Picture5.png?expiry=1653436800000&hmac=K3JkAaQaEQL4kjgc4WUbWWc_rLOp74NNNUXXBnVbvEM)

The Watch panel is only visible during debugging. It can be set to display the values of variables or arguments, and values of user-defined expressions that are in scope. It also supports complex object variables like lists of string or dictionary variables. These values are updated after each activity execution while debugging.

![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/TrJC3iVlSouyQt4lZYqLpA_55e028d5832444bcbb69f48d7009e8a1_Picture6.png?expiry=1653436800000&hmac=B5lhODJrqFV7_HbqeoezCq3O9oFQmlikEykE_0I81dw)

The Immediate panel is only visible during debugging, and it can be used for inspecting data available at a certain point during debugging. It can evaluate variables, arguments, or statements. To do so, simply type the variable or argument name in the Immediate window and press Enter.