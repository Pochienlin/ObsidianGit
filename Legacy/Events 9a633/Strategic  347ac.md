# Strategic Thinking | Lecture 1: Rule of the majority

Archive?: No
End: January 11, 2022 6:45 PM
Start: January 11, 2022 3:30 PM

# Overview

[https://smu-sg.zoom.us/j/93602795437?pwd=Z2ZNM041UjMyWDBETjc4UFZkRE9GUT09](https://smu-sg.zoom.us/j/93602795437?pwd=Z2ZNM041UjMyWDBETjc4UFZkRE9GUT09)

## Main Concepts

1. 

```jsx
Decision making by a society
```

<aside>
💡 How should a society make a decision that affects the welfare of different members in different ways?

</aside>

# Voting: aggregating individual opinions

The Greek city-state of Athens 

- Around the fifth century BC
- Citizens vote for public policies

Scottish Independence Referendum in 2014 

- 55.3% vs 44.7%

UK BREXIT referendum in 2016 

- 51.9% vs 48.1%

SMUSA: Do you support changing the yearbook from a printed book to an interactive online experience?

<aside>
💡 Ever since the political philosophy of the Enlightenment, the choice of a voting rule has been a major ethical question with far-reaching implications on the behavior of most political institutions.

</aside>

# Formal definition of a voting rule

A voting rule solves each collective decision problem where several individual agents (voters) must jointly choose one/some among several outcomes (candidates), about which their opinions conflict. (Moulin (1988))

A collective decision problem consists of

- Finitely many voters: $N:=\{1,2\}$
- Finitely many candidates: $A:=\{a,b\}$
- Each voter’s opinion about candidates: a strict ranking of candidates (no indifference)

![Untitled](Strategic%20%20347ac/Untitled.png)

## Voting Rule

A voting rule chooses for each collective decision problem one or several candidate(s).

- How many collective decision problems are there?
- A voting rule is a function.

# Two candidates (e.g. referendums)

- The majority rule: A candidate is chosen whenever at least as many voters favor this candidate as the other candidate.
- It was clearly enounced more than two centuries ago, although its origin is much more ancient.
- The majority principle is commonly adopted and is often taken for granted.
    - But why?
        
        "Fairness" is predicated upon a utilitarian, egalitarian assumption of a utility function.
        

# Axiomatic approach

Axioms are precise formulations of naturally acceptable/desirable properties.

Whether does the majority rule satisfy these axioms?

Is there any other voting rule satisfying these axioms?

> 📖 May, Kenneth O. 1952. “A set of independent necessary and sufficient conditions for simple majority decisions”, Econometrica, Vol. 20, Issue 4, pp. 680-684.
> 
- Note on majority rule
    
    The majority rule is defined only for two-candidate problems.
    But the axioms that we are going to introduce can be formulated with no restrictions on either the number of voters or the number of candidates.
    The majority rule satisfies all these axioms for two-candidate problems.
    

# Anonymity

The name of voters should not matter. If voters exchange their names/preferences, the outcome of the election should not be affected.

- Example
    
    The same candidate(s) should be chosen for the following two problems
    
    ![Untitled](Strategic%20%20347ac/Untitled%201.png)
    
    ![Untitled](Strategic%20%20347ac/Untitled%202.png)
    
- Example
    
    The same candidate(s) should be chosen for the following two problems
    
    ![Untitled](Strategic%20%20347ac/Untitled%203.png)
    
    ![Untitled](Strategic%20%20347ac/Untitled%204.png)
    
- Can you provide an example of a voting rule that violates anonymity?
    
    Weighted voting, such as in US electoral college
    
    Would tie-breaker be considered non-anonymous?
    

# Neutrality

The name of candidates should not matter. 

If we exchange two candidates in the ordering of every voter, then the outcome of the election should change accordingly.

- Examples
    
    
    ![Untitled](Strategic%20%20347ac/Untitled%205.png)
    
    ![Untitled](Strategic%20%20347ac/Untitled%206.png)
    
    If a is chosen in Problem 1 (P1), then b is chosen in Problem 2 (P2).
    
    If b is chosen in P1, then a is chosen in P2.
    If c/d is chosen in P1, then c/d is chosen in P2.
    If a, c are chosen in P1, then b, c are chosen in P2.
    If b, d are chosen in P1, then a, d are chosen in P2.
    If a, b are chosen in P1, then a, b are chosen in P2.
    ······
    
    Similarly, if we know the election outcome in P2, we can predict the outcome in P1.
    
- Can you provide an example of a voting rule that violates neutrality?
    
    Coalition government
    

# Strict monotonicity

A new supporter can do no harm.

If a candidate is chosen in a problem and one voter improves the ranking of that candidate while the others’ preferences remain the same, then only that candidate should be chosen in the changed problem.

- Examples
    
    
    ![Untitled](Strategic%20%20347ac/Untitled%207.png)
    
    ![Untitled](Strategic%20%20347ac/Untitled%208.png)
    
    If we know the election outcome in P1, can we predict the outcome in P2?
    
    There are three possible outcomes in P2: 
    
    (1) a is chosen, 
    
    (2) b is chosen, and 
    
    (3) a, b are chosen.
    
    - Case 1: a chosen
        
        Consider that P1 is the initial problem. Since a is chosen in P1 and since a is improved in P2, the outcome in P2 must be a.
        Consider that P2 is the initial problem. If the outcome in P2 is a, since b is improved in P1, there is no violation of strict monotonicity.
        Therefore, the outcome in P2 must be a.
        
    - Case 2: b is chosen
        
        Consider that P1 is the initial problem. Since b is chosen in P1 and since a is improved in P2, strict monotonicity does not impose any restriction on the outcome in P2.
        Consider that P2 is the initial problem. No matter what outcome happens in P2, there is no violation of strict monotonicity.
        Therefore, all three outcomes are possible in P2.
        
    - Case 3: a, b are chosen
        
        Consider that P1 is the initial problem. Since a, b are chosen in P1 and since a is improved in P2, the outcome in P2 must be a.
        Consider that P2 is the initial problem. If the outcome in P2 is a, since b is improved in P1, there is no violation of strict monotonicity.
        Therefore, the outcome in P2 is a.
        
- Can you provide an example of a voting rule that violates strict monotonicity?
    
    Run-off elections (non-2P) or Single Transferrable Vote
    
- Practice question
    
    
    ![Untitled](Strategic%20%20347ac/Untitled%209.png)
    
    ![Untitled](Strategic%20%20347ac/Untitled%2010.png)
    
    If a voting satisfies strict monotonicity, what can you say about the following two problems?
    
    Case 1: a is chosen
    
    Case 2: b is chosen
    
    Case 3: a, b are chosen
    
    Sequence 1: P1 → P2 → P3
    
    Sequence 2: P3 → P2 → P1
    
    C1:
    
    - If S1 → from P1 to P2, a is improved. a must be chosen. from P2 → P3, a is improved, a must be chosen
    - If S2 → from P3 to P2, b is improved in P2, $P1_b>P2_b>P3_b$ and yet $P1a >P1b$, monotonic, so if a is chosen in P1, a must be chosen in P3 as well.
    
    C2: 
    
    - If S1 → P1 to P2, a is improved, non-binding
    - If S2 → from P3 to P2, non-binding
    
    C3: 
    
    - If S1 → a must be chosen because a is improved from P1 to P2, then P2 to P3.
    - If S2 → a must be chosen because b is improved from P3 to P2, then P2 to P1, and P1 chooses both a and b. B in P3 is less preferred than P1, so a must win.
    - Hint
        
        ![Untitled](Strategic%20%20347ac/Untitled%2011.png)
        

Likewise, strict monotonicity requires that if a candidate is chosen in a problem and several voters improve the ranking of that candidate while the others’ preferences remain the same, then only that candidate should still be chosen in the changed problem.

# Characterization of majority rule

## May's Theorem (1952)

There is exactly one voting rule that satisfy anonymity, neutrality, and strict monotonicity. It is the majority rule.
It is easy to see that the majority rule satisfy the three axioms. I will show that the majority rule is the only voting rule satisfying the three axioms in the three voter case. (You will prove the four voter case in homework. Group project: arbitrary number of voters.)

## Proof by contradiction: example

[“An Introduction to Proof by Contradiction”](https://nrich.maths.org/4717) (by Koerner and Neale)

What we know: 1. If Sally did not pay her parking ticket, she would have got a nasty letter from the council. 2. She did not get any nasty letters.
What we want to show: Sally paid her parking ticket.

Proof: Suppose to the contrary that she did not pay her ticket. Therefore, she should have got a nasty letter from the council. However, we know her post was particularly pleasant, and contained no nasty letters whatsoever. This is a contradiction. So our hypothesis is wrong. (modus tollens)

<aside>
❓ Fix an arbitrary voting rule that satisfies the three axioms.

</aside>

- May's theorem: proof by contradiction
    
    ### Step 1
    
    We want to show that only a is chosen (by this voting rule) in the following problem.
    
    Proof: Suppose to the contrary that either only b is chosen, or both a and b are chosen.
    
    | Ann | Bob | Cheryl |
    | --- | --- | --- |
    | a | a | a |
    | b | b | b |
    - **Case 1: Only b is chosen**
        
        By neutrality, only a is chosen in the following problem.
        
        | Ann | Bob | Cheryl |
        | --- | --- | --- |
        | b | b | b |
        | a | a | a |
        
        This problem is obtained from the problem in the previous slide by several voters’ improvement of b’s ranking. Strict monotonicity would imply that only b is chosen in this problem. However, we have concluded that only a is chosen in this problem. This means that the rule violates strict monotonicity, which contradicts the fact that it satisfies this axiom. So our hypothesis is wrong.
        
    - **Case 1: a and b are chosen**
        
        By neutrality, both a and b are also chosen in the following problem.
        
        | Ann | Bob | Cheryl |
        | --- | --- | --- |
        | b | b | b |
        | a | a | a |
        
        This problem is obtained from the problem in the previous slide by several voters’ improvement of b’s ranking. Strict monotonicity would imply that only b is chosen in this problem. However, we have concluded that only a is chosen in this problem. This means that the rule violates strict monotonicity, which contradicts the fact that it satisfies this axiom. So our hypothesis is wrong.
        
    
    ### Step 2
    
    We want to show that only a is chosen (by this voting rule) in the following problem.
    
    Proof: Suppose to the contrary that either only b is chosen, or both a and b are chosen.
    
    | Ann | Bob | Cheryl |
    | --- | --- | --- |
    | a | a | b |
    | b | b | a |
    - **Case 1: Only b is chosen**
        
        By neutrality, only a is chosen in the following problem.
        
        | Ann | Bob | Cheryl |
        | --- | --- | --- |
        | b | b | a |
        | a | a | b |
        
        By strict monotonicity, only b is chosen in the following:
        
        | Ann | Bob | Cheryl |
        | --- | --- | --- |
        | a | b | b |
        | b | a | a |
        
        Anonymity would imply that the election outcomes of the two problems in the previous slide are the same. However, we have concluded that the outcomes are different. This means that the rule violates anonymity, which contradicts the fact that it satisfies this axiom. So our hypothesis is wrong.
        
    - **Case 1: a and b are chosen**
        
        By neutrality, both a and b are also chosen in the following problem.
        
        | Ann | Bob | Cheryl |
        | --- | --- | --- |
        | b | b | a |
        | a | a | b |
        
        By strict monotonicity, improving b by one voter elects b
        
        | Ann | Bob | Cheryl |
        | --- | --- | --- |
        | a | b | b |
        | b | a | a |
        
        By anonymity, both the above should result in both a and b chosen, but only b is chosen in the second case. The rule must violate anonymity, contradicting the fact that it fulfils all the axioms
        
    
    ### Step 3
    
    We want to show that only b is chosen (by this voting rule) in the following problems.
    
    Proof: follows from steps 1 and 2 and neutrality
    
    P1:
    
    | Ann | Bob | Cheryl |
    | --- | --- | --- |
    | b | b | a |
    | a | a | b |
    
    P2
    
    | Ann | Bob | Cheryl |
    | --- | --- | --- |
    | b | b | b |
    | a | a | a |
    - P1 | **Case 1: Only a is chosen**
        
        By neutrality, only b is chosen in the following problem.
        
        | Ann | Bob | Cheryl |
        | --- | --- | --- |
        | a | a | b |
        | b | b | a |
        
        By strict monotonicity, by improving a, a must be chosen in the following:
        
        | Ann | Bob | Cheryl |
        | --- | --- | --- |
        | b | a | a |
        | a | b | b |
        
        Anonymity would imply that the election outcomes of the two problems in the previous slide are the same. The outcome of both are different. As such, it must be the case that a rule that elects a in P1 is inconsistent with our axioms
        
    - P1 | **Case 2: a and b are chosen**
        
        By neutrality, both a and b are also chosen in the following problem.
        
        | Ann | Bob | Cheryl |
        | --- | --- | --- |
        | a | a | b |
        | b | b | a |
        
        By strict monotonicity, improving a by one voter elects a
        
        | Ann | Bob | Cheryl |
        | --- | --- | --- |
        | b | a | a |
        | b | b | b |
        
        By anonymity, both the above should result in both a and b chosen, but only a is chosen in the second case. The rule must violate anonymity, contradicting the fact that it fulfils all the axioms
        
    - P2 | **Case 1: Only a is chosen**
        
        By neutrality, only b is chosen in the following problem.
        
        | Ann | Bob | Cheryl |
        | --- | --- | --- |
        | a | a | a |
        | b | b | b |
        
        By monotonicity, a is improved in the table above from P2, and so a should be chosen, however neutrality implies b must be chosen instead. This contradiction implies that monotonicity is violated
        
    - P2 | **Case 2: a and b are chosen**
        
        By neutrality, both a and b are also chosen in the following problem.
        
        | Ann | Bob | Cheryl |
        | --- | --- | --- |
        | a | a | a |
        | b | b | b |
        
        By strict monotonicity, a is improved throughout several voters, therefore only a should be chosen, however, the above implies both a and b are still chosen. Therefore monotonicity is violated.
        
    
    ### Step 4
    
    We want to show that the rule is the majority rule.
    
    Proof: 
    
    - By Step 2 and anonymity, whenever there are 2 voters preferring a to b, only a is chosen.
    - By Step 3 and anonymity, whenever there are 2 voters preferring b to a, only b is chosen.
    - By Step 1, if all voters prefer a to b, only a is chosen.
    - By Step 3, if all voters prefer b to a, only b is chosen.
        
        $$
        2a,step\;2,Anon \vdash a\\2b,step\;3, Anon \vdash b\\3a,step\;1\vdash a\\3b,step\;3\vdash b
        $$
        
    
    Hence, this voting rule is the majority rule.
    

<aside>
💡 The characterisation is tight: Dropping any one of the three axioms, there is a voting rule different from the majority rule satisfying the other two axioms. (Group project)

</aside>

[ECON241 question to myself](https://docs.google.com/presentation/d/1zxc0T9wAdVeI_1XpA0ipUgNKDCJ_ftEaDlKgFzT5lSY/edit?usp=drivesdk)

# 3 or more candidates

What voting rule would properly extend majority voting among pairs?