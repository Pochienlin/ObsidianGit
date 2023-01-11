# Programming for CT
UID: 202301112214
Tags: #🌱 
Links: [[Computational Thinking]]

---
ACKNOWLEDGEMENT: THESE EXERCISES ARE TAKEN FROM JSC CHAPTER 2

**CT Programming Tutorial Project 1-8 (p.36 of PDF, p.22 of JSC)**
# Arithmetic Operations. Operators and Operands. Using parenthesis


**T1**: Type a simple arithmetic expression and click the "play" button. (Enter e.g. `13 + 2`). Python should print the result. 

```python
6 - 59
```

**T2**: Try some simple expressions involving other operators (e.g. `-` for minus, `*` for multiplication, `/` for division. 
Try the following by clicking on "play" for these statements:
```python
6 - 3
3 * 7
8 / 4
7 + 2 - 3
7 * 6 * 5 * 4 * 3 * 2 * 1
```

**T3**: Try some expressions with and without parentheses (or round brackets).<br>
Is there a difference between these expressions? 
```python
 3 + 4 * 5 
```

```python
 (3 + 4 ) * 5
```
Is there a difference between these expressions? 
```python
8 - 4 / 2
```

```python
(8 - 4) / 2
```


**T4** Does Python care if you include spaces in the middle of your expressions? <br>
Is there a difference between these expressions?
- 3+4
- 3 + 4
- 3+ 4
- 3 +4

```python
3+4
```

```python
3 + 4
```

```python
3+ 4
```

```python
3 +4
```


**T5** T5: What happens if you leave out an operand? e.g. if you type `3 + * 5` instead of `3 + 4 * 5`?
(`+`, `-`, `*`, `/` are operators. The numbers they work with are operands. So in this expression: `3 + 4`, `+` is the operator; `3` and `4` are the operands.)

```python
3 + * 5
```

**T6**: Type an expression that mistakenly uses a symbol instead of a number. e.g. `3 + x`

```python
3 + x
```

You will see an error message. The error message has some unfamiliar terminology, but at this point, you can glean some
information: the message has the phrase "not defined," and "x" is enclosed in quotes, so there’s a good chance Python was complaining about the x in that expression. We’ll see how to assign values so symbols can be used in expressions later.

In grade school you might have learned a mnemonic like “My Dear Aunt Sally” to remember the
precedence of arithmetic operators (multiplication, division, addition, subtraction).
Python and other programming languages have a slightly different rule: multiplication and division
have the same precedence, as do addition and subtraction. If an expression has two operators with
the same precedence, the one on the left is applied first.

**T7**: Run the following expressions to see how Python applies these precedence rules:

```
6 / 3 * 4
```

```
8 * 3 / 4
```

```
5 - 4 + 2
```

```
7 * 4 / 2
```

```
9 - 4 - 2
```

Would any of these expressions have a different value using the “dear aunt sally” rules?<br><br>

**T8**: What do you think Python will do if you enter `8 / 2 + 5 * 3`? Type the expression below and run it. Did you get the result you expected?

I think I will get (8/2) + (5 * 3) =4+15=19

`The answer was 19.0. There was type conversion to float because of division operator that I forgot about.`

---
# Other operators
## Modulo %
- [[Modulo vs Remainder | Modulo is not always the same as remainder]] unlike what the lecture stated

## Exponent **

## Bitwise XOR ^

----
ACKNOWLEDGEMENT: THESE EXERCISES ARE TAKEN FROM JSC CHAPTER 2

**CT Programming Tutorial Project 9-19 (p.40 of PDF, p.26 of JSC)**

#Floats vs Integers. Using the sqrt function


**T9**: Use Python to evaluate a simple expression such as `3 * 5` where both operands are integers:

```
3 * 5
```

**T10** Repeat the previous expression, but use floating point numbers:

```
3.0 * 5.0
```

Can you see the difference between the outputs for these two expressions?<br><br>

**T11** 
Do you think Python will allow you to mix integers and floating point numbers? What will
happen if you try to multiply `3` by `5.0`, or add `1.0` to `6`? Try these examples and a few other
expressions that mix integers and floating point numbers. Does there seem to be a general
rule for determining what kind of output is printed?



**T12** Use Python to evaluate the expression that converts 100F to Celsius:

```
(100 - 32) * 5 / 9
```

Is this result what you expected, given the rules Python uses for evaluating arithmetic expressions?
Is it an accurate calculation of the temperature in Celsius?

**T13** Repeat the previous exercise, using Python to convert these temperature values to Celsius:
<li>90 F 
<li>70 F 
<li>212 F 
<li>32 F


**T14** The formula for converting from Celsius to Fahrenheit is <br>
```
    F=C*(9/5)+32
```
Use this formula to convert the following temperatures to Fahrenheit: 
<li>0 C 
<li>10 C 
<li>20 C 
<li>30 C 
<li>100 C



**T15** Run the following command to import the `sqrt` function from the `math` module:

```
from math import sqrt
```

**T16** Use sqrt to compute the square root of 25

```
sqrt(25)
```

**T17** The `math` module also defines some important constants. This command will import the
definition of `pi` so you can use it in the current session:

```
from math import pi
```

**T18** Verify that `pi` has been imported:

```
pi
```

```
pi/2
```


The actual value of `pi` has an infinite number of digits, but as you can see here the value used
in Python is a floating point number with a finite number of digits.<br><br>

**T19** A module named `random` has functions for generating random numbers. The `randint` ("random integer") function produces a random value between a specified minimum and maximum value. Try running these two statements:

from random import randint


```
randint(1,10)
```

You will probably see a different result than the number shown above. Repeat the call to `randint(1,10)` a few times. Are you seeing a different result each time `randint` is called? Are all the values it returns between 1 and 10?

-----
ACKNOWLEDGEMENT: THESE EXERCISES ARE TAKEN FROM JSC CHAPTER 2

CT Programming Tutorial Project 20-30 (p.44 of PDF, p.30 of JSC)

# Using variables

**T20**: Run these two expressions to define variables named `x` and `y`:

```
x = 6
y = 5
```

**T21** Try out a few expressions using these variables:

```
x + 3
```
```
x * y
```
```
(x + 3) * y
```

**T22**. Change the value of `x`:

```
x = 2
```

**T23**. Repeat the three expressions above that used `x`. Did the values of these expressions change after you changed the value of `x`?

```
x + 3
```

```
x * y
```

```
(x + 3) * y
```

**T24** Set `x` to the length of the long edge of the countertop

```
x = 109
```

**T25** Define the area of a square that is `x` centimeters on each side:

```
square = x ** 2
```

**T26** Ask Python to show you the value of this new variable

```
square
```

Is the result what you expect, i.e., is it $x^2$?



**T27**. Define the area of the missing right triangle that is x/2 centimeters on each leg, and ask
Python to show you the value of this variable:

```
triangle = ((x / 2) ** 2) / 2
```

```
triangle
```

Is this the correct value?<br><br>
**T28**. Enter an expression that computes the area of the countertop:

```
square - triangle
```

**T29**. Change the value of `x` by entering a new assignment statement:

```
x = 107
```

**T30**. Recompute the values of `square` and `triangle` using the new value of `x` and then compute the new area.

```
square = x ** 2
triangle = ((x / 2) ** 2) / 2
square - triangle
```