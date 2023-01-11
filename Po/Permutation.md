# Permutation
UID: 202301112134
Tags: #🌱 
Links: [[Counting problem (CT)]]

---

```ad-abstract
title:TL;DR:
A permutation of a set of objects is an ordered arrangement of these objects.
The number of permutations of a set of length $n$ is $n!$
```
```
Given a set S = {A, B, C}, its permutations are:
- A,B,C 
- A,C,B 
- B,A,C 
- B,C,A 
- C,A,B 
- C,B,A
```

## r-Permutation $^nP_r$
```ad-abstract
title: Definition
An r-permutation of a set of $n$ objects is an ordered arrangement of $r$ of the $n$ objects.
```
```
Given a set S = {A, B, C}, its 2-permutations are:

- A,B 
- A,C 
- B,A 
- B,C 
- C,A 
- C,B
```
$$^nP_r=\frac{n!}{(n-r)!}$$

```ad-question
title: Q1.
150 countries compete in the Olympics. How many ways are there to select 1st place, 2nd place, and 3rd place winners?
```
$$^{150}P_{3}=\frac{150!}{147!}=148*149*150=3,307,800$$
