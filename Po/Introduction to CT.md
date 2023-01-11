# Introduction to CT
UID: 202301111912
Tags: #🌱 
Links: [[Computational Thinking]] [[Data structures and Algorithms]]

## What is an algorithm
```ad-abstract
title: Definition from *Rosen* Ch. 3
An algorithm is a finite sequence of precise instructions for performing a computation or for solving a problem
```
1. Input and output
2. Definiteness: each step must be defined precisely
3. Correctness: must product the correct output values for each set of input values
4. Finiteness: will not go on forever
5. Generality: applicable for all problems in the desired form, not just a specific domain

```ad-quote
"Fast hardware does not make good algorithms unnecessary. On the contrary, faster hardware magnifies the superiority of better algorithms."

From "Foundations of Computer Science" lecture notes by A Prorok & A Madhavapeddy (Cambridge University)
```

### Example of a algorithm: [[ Marriage problems (Game Theory) |Gale-Shapely Deferred Choice Alogrithm ]]
![[Pasted image 20230111191930.png]]
```ad-summary
1. Given: n males and n females.
2. Each unmatched male proposes to his highest ranked female whom he hasn’t proposed to previously.
3. If the female is not matched yet, she automatically accepts.
4. If she is already matched, she picks her more preferred male and rejects one of them.
5. Repeat steps 2-4 if there is still at least one male who is unmatched. 
When every man is matched, the problem is solved.(The order of which male proposes first is not important.)
```

#### Putting G-S DA Algorithm into code
```
Each person can be in 1 of 2 states at any one time: matched or free 
All males and females are initially free

While there exists an unmatched male m who has not proposed to all females: 

Let f be the highest-ranked female to whom m has not proposed
	If f is free:  
		(m, f) are matched
	Else it means that some other pair (m', f) already exists: 
		If f prefers m to m'
			(m, f) are matched
			m' becomes free 
		Else
			# do nothing!
			(m', f) remain matched
			m remains free 
		End
	End 
End
```
1. For N males and N females, at most $N^2$ number of proposals
	1. E.g. $N=22\implies 484 \;proposals$
	2. Guarantees everyone gets married, and all marriages are stable

## Summary 
- Computational thinking is for everyone
- Elements of computational thinking include:
   - [ ] Abstract and algorithmic thinking.
   - [ ] Iteration, Decomposition, Complexity, Heuristic reasoning.
- Course emphasizes:
   - [ ] Conceptual thinking and reasoning, not programming
   - [ ] Formulating a problem in terms of how it can be computed  -[ ] Characterizing the complexity of problems and solutions
   - [ ] Designing solutions with simplicity and efficiency in mind