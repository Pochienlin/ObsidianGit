# UiPath Shortcuts
UID: 202205231531
Tags: #🌱 
Links: [[Robotics Process Automation]] [[UiPath]]

-------
Keyboard Shortcuts
The keyboard shortcuts can be used whenever the Studio is the active window. Shortcuts are available for:
- File Management
- Search
- Comment
- Debugging
- Recording
- Workflow Analysis and Execution
- Selected Activity
- Miscellaneous

> [!tip]
> The below mentioned shortcuts are the File Management shortcuts that are used to create, open, or save different kinds of files such as workflows and logs.
- Ctrl + Shift + N - Create a new Blank Process. 
	- Equivalent to clicking on the “Process” option under the New Project Panel on the welcome screen.
- Ctrl + O - Open a previously created workflow, either the .xaml or project.json file.
	- Equivalent to clicking on the “Open a Local Project” option under the New Project Panel on the welcome screen.
- Ctrl + L - Open the folder where the Log files are stored.
- Ctrl + S - Save the currently opened workflow.
- Ctrl + Shift + S - Save all the workflows that are currently open.

> [!warning]
> Note: The above 5 shortcuts can be performed either on the welcome screen of the UiPath Studio or inside a process.

- Ctrl + Tab - Move focus between workflows opened in the Designer panel.

> [!tip]
> The below mentioned shortcuts are the Selected Activity shortcuts that are performed on activities we use inside our workflow.

- Ctrl + T - Place the activity inside the Try section of a Try Catch activity.
- Ctrl + N - Create a new Sequence Diagram in the current project. 
	- Equivalent to selecting the “Sequence” option under the “New” option in the design ribbon.
- Ctrl + C - Copy the selected activity or activities to the clipboard.
- Ctrl + V - Paste the copied activity or activities inside the selected item.
- Ctrl + K - Create a variable of the same type as the required type of the activity.
- Ctrl + Space - Open the IntelliPrompt window to get variables, methods, and property names.
- F2 - Allow for renaming the selected activity.
- Shift + F2 - Add an annotation to a selected activity.
- Shift + Tab - Navigate to the previous activity or node in the Activities panel.
- Enter - Save the data added in the activity input field.
- Shift + Enter - Add a new line under the inputted text in an activity field.
- Ctrl + Enter - Add a new line above the inputted text in an activity field.

> [!tip]
> The below mentioned shortcuts are the Search shortcuts for activities, project files, switching between activities and navigating through activities.

- F3 or Ctrl + Shift + P - Opens the Command Palette.
- Ctrl + Shift + T - Opens the Add an Activity search bar.
- Ctrl + Shift + F - Opens the Go to file search bar.
- Ctrl + F - Opens the Universal Search bar.
- Ctrl + J - Opens the Jump to activity search bar.
- Ctrl + 1 - Switches to the Current File tab in the Universal Search bar.
- Ctrl + 2 - Switches to the All Files tab in the Universal Search bar.
- Ctrl + 3 - Switches to the Activities tab in the Universal Search bar.
- Ctrl + 4 - Switches to the Variables tab in the Universal Search bar.
- Ctrl + 5 - Switches to the Arguments tab in the Universal Search bar.
- Ctrl + 6 - Switches to the Imports tab in the Universal Search bar.
- Ctrl + 7 - Switches to the Project Files tab in the Universal Search bar.
- Ctrl + 8 - Switches to the Dependencies tab in the Universal Search bar.
- Ctrl + 9 - Switches to the Snippets tab in the Universal Search bar.
- Ctrl + Alt + A - Opens and focuses the search bar in Properties panel.
- Ctrl + Alt + F - Sets the focus to the search box in the Activities panel.
- Ctrl + Alt + O - Sets the focus to the search box in the UI Objects Browser panel
- Ctrl + Alt + P - Opens and focuses the search bar in the Project panel.
- Ctrl + Alt + S - Opens and focuses the search bar in the Snippets panel.
- Tab - Navigates to the next item in the panel or the next element in the activity.

> [!tip]
> The below mentioned shortcuts are the Debugging shortcuts that can be used for debugging purposes.

- F9 - Mark the selected activity with a breakpoint.
- Ctrl + Shift + B - Open the Breakpoints panel.
- Ctrl + Alt + E - Opens the Error List panel.
- F10 - When debugging, step over the execution of a block of activities in the currently selected workflow.
- F11 - When debugging, step into a block of activities and executes the first one.
- Shift + F11 - When debugging, steps out of the current container after its last activity is executed.

> [!tip]
> The below mentioned shortcuts are the Recording shortcuts that can be used for recording and selecting other recording options.

- Ctrl + Alt + B - Open the Basic Recording toolbar.
- Ctrl + Alt + C - Open the Citrix Recording toolbar.
- Ctrl + Alt + D - Open the Desktop Recording toolbar.
- Ctrl + Alt + W - Open the Web Recording toolbar.
- F2 - Add delay during a recording activity.
- F3 - Specify a custom recording region.
- F4 - Choose the UI Framework to record, which can be Default, AA, and UIA.

> [!tip]
> The below mentioned shortcuts are used for Workflow Analysis and Execution.
- F5 - Run the current project in debugging mode, starting with the .xaml file set as Main.
- Ctrl + F5 - Run the current project.
- F6 - Run the currently opened .xaml file in debugging mode.
- Ctrl + F6 - Run the currently opened .xaml file.
- F7 - Check the file for validation errors and Workflow Analyzer violations.
- Shift + F7 - Check the whole project for validation errors and Workflow Analyzer violations.
- F8 - Check the currently opened workflow for validation errors.
- Shift + F8 - Check all project files for validation errors.
- Pause - Pause the execution of the current workflow, in both normal and debug mode.
- F12 - Stop the execution of the current workflow, in both normal and debug mode.

> [!tip]
> The below mentioned shortcuts are some Miscellaneous shortcuts used for project management.

- F1 - Access a help topic associated with the currently selected element.
- Ctrl + P - Open the Manage Packages window.
- Esc - Close the Publish, Manage Packages, File Diff windows.
- Ctrl + F1 - Minimize or expand the ribbon.
- Ctrl + Shift + R - Removes all unused project dependencies.
- Ctrl + Z - Undo the last action.
- Ctrl + Y - Redo the last action you've undone.

> [!tip]
> Comment shortcuts are used for commenting out an activity which prevents it from execution while the activity remains inside the workflow.

- Ctrl + D - Ignore the activity that is currently selected by placing it into a Comment Out container.
- Ctrl + E - Remove the activity from the Comment Out container it was placed in.

> [!tip]
> Argument shortcuts are used for managing the arguments used inside the workflow.
- Ctrl + M - Create an In argument of the same type as the required type of the activity.
- Ctrl + Shift + M - Create an Out argument of the same type as the required type of the activity.
------
To know more details about keyboard shortcuts, please visit:
https://docs.uipath.com/studio/v2020.10/docs/keyboard-shortcuts