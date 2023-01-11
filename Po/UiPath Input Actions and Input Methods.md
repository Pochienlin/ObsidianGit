# UiPath Input Actions and Input Methods
UID: 202205262146
Tags: #🌱 
Links: [[UI Automation and Selectors]]

##  Input methods
To replicate actions, Studio supports 3 input methods for performing input actions:
1. Default
	1. Captures the input given while interacting with the UI element of the screen
2. Send Windows Messages
	1. Captures actions performed using keyboard and mouse
3. Simulate type/click
	1. Much faster than the other 2
	2. Does not capture input given by the keyboard
## Comparing the input methods
| Method              | Compatibility                        | Background | Speed | Hotkeys | Empty Field |
| ------------------- | ------------------------------------ | ---------- | ----- | ------- | ----------- |
| Default             | 100%                                 | No         | 50%   | Yes     | No          |
| Window Messages     | 80%                                  | Yes        | 50%   | Yes     | No          |
| Simulate Type/Click | 99% (Web Apps) or 60% (Desktop Apps) | Yes        | 100%  | No      | Yes         |

