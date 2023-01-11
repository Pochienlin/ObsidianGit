# UiPath UI Interactions
UID: 202205262135
Tags: #🌱 
Links: [[UI Automation and Selectors]]

----
 ```ad-abstract
 UI Interactions can be divided into Input actions (clicks, typing, keyboard shortcuts, mouse hover, clipboard actions, e.g.) and Output actions (Getting text, find elements, identifying images, clipboard actions, e.g.)
```

# Input actions and methods
1. Click activity
	1. Click type can be configured (single, double, down, up)
	2. Mouse Button can also be configured (Left, right or middle)
	3. Timeout (30s as default)
	4. Key Modifiers
		1. Allows users to add ALT CTRL SHFT WIN etc.
2. Type Into activity
	1. Sends keystrokes to a UI element
	2. e.g. Entering text in an input box or word file.
	3. Customisable as well:
		1. Activate: brings specified UI to foreground before modifying
		2. Click Before Typing: useful for text areas etc that requires a click to interact
		3. Delay between keys: default to 10ms, max to 1000ms
	4. Empty Field
		1. Erases all elements before keying things in
3. Send Hotkey
	1. Sends keyboard shortcuts to a UI element
	2. Customisable: 
		1. Activate: same as above
		2. Click Before Typing
		3. Delay between key
		4. Empty field
		5. Delay Before/ After: Adds a delay before/ after the click or typing
		6. Wait for ready: waits for waits for the target to be ready by verifying certain application tag 