# Combination
UID: 202301112142
Tags: #🌱 
Links: [[Counting problem (CT)]]

-----
```ad-abstract
A combination of a set of objects is an unordered selection of these objects.

The number of combinations of a set of length n is 1.
```
- Given a set S = {$A,B,C$}, its combination is:
	- {$A,B,C$}

## r-Combination $^nC_r$
An r-combination of a set of n objects is an unordered selection of r objects out of the n objects.
```
- Given a set S = {A, B, C}, its 2-combinations are
   - A,B 
   - A,C 
   - B,C
```
$$^nC_r=\frac{n!}{r!(n-r)!}=\frac{^nP_r}{r!}$$
```ad-question
title:Q1.
150 countries compete in the Olympics. How many ways to select the top 3 winners if we do not care about their specific ranking?
```
$$^nC_r=\frac{^nP_r}{r!}=148*149*150/3!=551,300$$

```ad-question
title: Q2.
1.  How many permutations of the letters A to H if the three letters "ABC" have to occur consecutively?
2. What if they must appear together but not necessarily consecutively?
```
$$i)\;\;\;^6P_6=6!$$
Think of this as 6 chunks: [(A B C), D, E, F, G, H]
$$ii)\;\;\;^6P_6*{^3P_3}=6!*3!$$
```ad-question
title: Q3.
You are inviting 3 other guests (so there are 4 diners including yourself) to have dinner at home. Your rectangular dining table can seat 6.  
How many different seating arrangements can you have?
```
$$^6P_{4}/^2P_2=6!/2!=3*4*5*6=360$$

```ad-question
title: Q4.
We would like to form a 7-member committee, consisting of 3 faculty members and 4 students. There are 40 faculty members and 300 students.  
How many different ways can we form the committee?
```
$$^{40}C_3*{^{300}C_4}=\frac{40!}{3!(36)}*\frac{300!}{4!(296!)}$$
```ad-question
title: Q5.
How many ways are there for 3 men and 3 women to stand in a line so that no two women stand next to each other?
```
possible combinations:
101010
010101
011010
010110
$$4*{^3P_3*{^3P_3}=4*3!*3!=96}$$
OR think of it as 
[  ]$m_1$[  ]$m_2$[  ]$m_3$[  ]
- Choose permutations for the3 women to fill the 4 slots OR choose 1 slot to leave behind
- Multiply by Permutation for men, Permutation for women



