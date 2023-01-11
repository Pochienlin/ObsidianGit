# Counting problem (CT)
UID: 202301112031
Tags: #🌲 
Links: [[Computational Thinking]]

----
## What is the counting problem?
Basic operation in mathematics
1.  [[Product Rule]]
2.  [[Sum Rule]]
3. [[Permutation]] 
4. [[Combination]]


## Inclusion-exclusion problems:
> 
> Combining the [[product rule]] with the [[sum rule]]
> 

```ad-tip
If two things can be done at the same time, the sum rule will lead to double counting.  
In this case, we add the number of ways to do each task, and then subtract the number of ways to do both tasks.
```

### Integers that are multiples of $m$ and $n$
```ad-example
How many integers from 1 to 1000 are multiples of 3 or multiples of 5?
```
- Multiples of 3: {$3, 6, 9, 12, 15, ... 27, 30, 33...., 999$} 
	❖ no of integers = $1000/3 = 333$
- Multiples of 5: {$5, 10, 15, ...25, 30, 35...., 1000$} 
	❖ no of integers = $1000/5 = 200$
- **Note that multiples of both 3 and 5 (e.g., 15, 30) are counted twice**
- Multiples of both 3 and 5: {15, 30, 45, ... } 
	❖ no of integers = $1000/15 = 66$
- Inclusion-Exclusion Principle: $Total = 333 + 200 - 66 = 467$
![[Pasted image 20230111204631.png]]

## In-class exercises
```ad-question
title: Q1.  
Every car registered in Singapore has a license plate number, which begins with a letter‘S’, followed by two other letters, 4 digits, and another letter (all upper case) How many possible license plate numbers are there?
```
$$N=P_s*P_{L_1}*P_{L_2}*P_{D_1}*P_{D_2}*P_{D_3}*P_{D_4}*P_{L_3}=1*26^2*9^4*26=115316136$$
```ad-question
title: Q2.  
It turns out that all plate numbers beginning with SH are for taxis only. How many possible license plate numbers are there for non-taxis?
```
$$N_{Taxi}=P_s*P_h*P_{L_1}*P_{D_1}*P_{D_2}*P_{D_3}*P_{D_4}*P_{L_2}=1*1*26*9^4*26=4435236$$
$$N_{non-Taxi}=N-N_{Taxi}=115316136-4435236=110880900$$
```ad-question
title:Q3
You are supposed to create a new password.

• Min 6 characters and max 8 characters.  
• Alphanumeric characters (letters & numbers). • Case insensitive.  
• The password must contain at least one digit.

How many possible passwords are there?
```
$$Total=P_{6char}+P_{7char}+P_{8char}=(36^6-26^6)+(36^7-26^7)+(36^8-26^8)$$

```ad-question
title: Q4.
If passwords may only contain lower case letters and digits, how many 6-character passwords start with a lower case letter 'a' or ends with a lower case letter 'z'?
```
$$Total=P_{Starts\;with\;a}+P_{ends\;with\;z}-P_{starts\;a\;ends\;z}=36^{(6-1)}+36^{(6-1)}-36^{(6-2)}$$
$$\implies Total=2*36^5-36^4=71*36^4$$
----
## Summary
- Basics of counting principles
	- [ ] Product Rule
	- [ ] Sum Rule
		- [ ] Inclusion-exclusion principle
	- [ ] Permutation
	- [ ] Combination

