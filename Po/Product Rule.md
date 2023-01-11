# Product Rule
UID: 202301112034
Tags: #🌱 
Links: [[Counting problem (CT)]]

----
```ad-abstract
title: TL;DR:
If there are $m$ ways to do one thing, and $n$ ways to do another thing, then there are $m * n$ ways of doing both things.
```

## Number of SRs
```ad-example
There are 2 floors in SCIS with seminar rooms. Each floor has 4 seminar rooms.  
How many seminar rooms are there in SCIS?
```
1. Pick a floor – 2 ways
2. Pick a seminar room – 4 ways
By product rule, there are $2*4=8$ ways

## Binary strings of length n
```ad-example
A binary string consists only of 0’s and 1’s. How many possible strings of length n may exist?
```

- A binary string of length n has n binary characters (or bits).
- Binary strings of length 3
	 - `000, 001, 010, 011, 100, 101, 110, 111`
- Each bit can be either 0 or 1, i.e., two possibilities.
- For 3 bits, we have three things to do together:    
	- pick first bit: 2 ways
	- pick second bit: 2 ways
	- pick third bit: 2 ways
- Based on Product Rule, $Total = 2 x 2 x 2 = 2^3$
- For $n$ bits, $2^n$ possibilities
