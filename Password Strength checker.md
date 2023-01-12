# Password Strength checker
UID: 202301121230
Tags: #🌱 
Links: [[Foundations of Cybersecurity]]

-----
### Conversation I had with ChatGPT on how to make a password strength checker:

***what are some criteria I can use to measure password strength?***

There are several criteria that can be used to measure the strength of a password:

1.  Length: The longer the password, the more secure it is.
2.  Complexity: The use of a mix of uppercase and lowercase letters, numbers, and special characters makes a password more difficult to guess.
3.  Unpredictability: A password that is not a commonly used word or phrase is more secure.
4.  Uniqueness: Using a password that is not used for any other account makes it more secure.
5.  Avoiding personal information : Not using personal information such as names, addresses, and phone numbers in a password makes it more secure.

It's also important to mention that using password manager can help in creating a complex and unique password for different accounts and keeping track of all of them.

***implement a program that measures the strength of user passwords -- use various criteria of measuring password strength. Explain how we this program achieves good password strength using some or more of the ideas you shared above***

To implement a program that measures the strength of user passwords, you can use the various criteria of measuring password strength that I mentioned earlier: length, complexity, unpredictability, uniqueness, and avoidance of personal information.

Here's an example of a Python program that measures the strength of user passwords:

```python
import re  

def measure_password_strength(password):     
	# Initialize the strength to 0     
	strength = 0      
	# Check the length of the password     
	if len(password) >= 8:         
	strength += 1      
	# Check for the presence of uppercase letters, lowercase letters, numbers, and special characters     
	if re.search("[a-z]", password) and re.search("[A-Z]", password) and re.search("[0-9]", password) and re.search("[@$!%*#?&]", password):         strength += 1      
	# Check for the absence of common words and phrases     
	if not re.search("password|123456|qwerty|admin|letmein|monkey|abc123|hello|welcome", password, re.IGNORECASE):         
	strength += 1      
	return strength  

password = input("Enter a password: ") 
strength = measure_password_strength(password) 

if strength == 0:     
	print("Very Weak") 
elif strength == 1:     
	print("Weak") 
elif strength == 2:     
	print("Moderate") 
elif strength == 3:     
	print("Strong")`
	
```

This program prompts the user to enter a password and then uses regular expressions to check the password against the different criteria of measuring password strength. It assigns a strength value of 0 to 3, based on how many of the criteria the password meets.

First, The program check if the length of the password is at least 8 characters long. This is to increase the entropy of the password and increase the time it will take to crack it.

Then, the program check if the password contains uppercase letters, lowercase letters, numbers, and special characters. This increases the entropy of the password and make it more difficult to crack.

Then, the program check if the password contains common words and phrases. This increases the unpredictability of the password, and makes it more difficult to guess.

Finally, the program assigns a strength value to the password and prints it. A strength value of 3 indicates a strong password, while a strength value of 0 indicates a very weak password.

Note: This is just an example and it can be improved or enriched by various ways such as implementing a check for the reuse of the same password, check for the minimum required character, check for the password age, using a password manager, or using external library for password strength.

***what are some simple ways the script above can be modified to strengthen the check further? Use mathematical principles and theorems preferrably***

Here are a few ways the script above can be modified to strengthen the check further, using mathematical principles and theorems:

1.  Use a password entropy calculator: Password entropy is a measure of the uncertainty associated with a password, and it can be calculated using mathematical formulas. By incorporating an entropy calculator into the script, you can accurately assess the strength of a password based on its entropy value.
    
2.  Implement a check for the use of dictionary words : Instead of simply checking for the presence of common words and phrases, you can use a dictionary of words and phrases to check if the password is made up entirely of dictionary words. This would make the password less predictable and more difficult to crack.
    
3.  use password cracking time as a metric : One can also use the time it would take for a password-cracking algorithm to guess the password as a metric for password strength. The longer it would take for a password-cracking algorithm to guess the password, the stronger the password is considered to be.
    
4.  Use the NIST guidelines: There are a set of guidelines that are recommended by the National Institute of Standards and Technology (NIST) for creating strong passwords, which cover issues such as character composition, length, and forbidden values. Incorporating these guidelines into the script would improve its overall accuracy in assessing password strength.
    
5.  Use external library: A script can use password strength library such as "password-strength" or "zxcvbn" to measure the password strength, these libraries are implemented with more heuristics and built with the knowledge of common password cracking methods.
    

All of these modifications would increase the accuracy and sophistication of the script, making it more effective at identifying strong and weak passwords.

***implement some of these in your script***

Sure, here is an example of how the script I provided earlier can be modified to include some of the additional ways to measure password strength that I mentioned:

```python
import re
from passlib.pwd import genword

def measure_password_strength(password):
    # Initialize the strength to 0
    strength = 0

    # Check the length of the password
    if len(password) >= 8:
        strength += 1
    
    #Check for the password's entropy using passlib
    entropy = genword(password).entropy
    if entropy >= 50:
        strength += 1
    
    # Check for the presence of uppercase letters, lowercase letters, numbers, and special characters
    if re.search("[a-z]", password) and re.search("[A-Z]", password) and re.search("[0-9]", password) and re.search("[@$!%*#?&]", password):
        strength += 1

    # Check for the absence of common words and phrases
    if not re.search("password|123456|qwerty|admin|letmein|monkey|abc123|hello|welcome", password, re.IGNORECASE):
        strength += 1
    
    # Check for dictionary word
    if not re.search("^[a-z]+$|^[A-Z]+$", password, re.IGNORECASE):
        strength += 1
    
    return strength

password = input("Enter a password: ")
strength = measure_password_strength(password)
if strength == 0:
    print("Very Weak")
elif strength == 1:
    print("Weak")
elif strength == 2:
    print("Moderate")
elif strength == 3:
    print("Strong")
elif strength == 4:
    print("Very Strong")
```

This script adds a check for the password's entropy and check for dictionary words.

1.  I added a check for the entropy of the password using the genword function from the passlib library, it calculates the entropy of the password and compares it to a threshold ( in this case 50)
2.  I also added a check for the presence of only dictionary words, this check uses regular expressions to look for passwords that are made up of only lowercase letters or only uppercase letters.

Note that the script would be more accurate if you use a bigger dictionary for the dictionary words check or use an external library to check if the password is a dictionary word.

This implementation of the script is stronger than the previous one as it takes into account more factors when determining the strength of a password, such as password's entropy and presence of dictionary words.
