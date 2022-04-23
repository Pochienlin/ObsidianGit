# Strategic Thinking | Strategy-proof voting rules

Archive?: No
End: January 18, 2022 6:45 PM
Start: January 18, 2022 3:30 PM

# Overview

## Main Concepts

1. 

# Three or more candidates

What voting rule would properly extend majority voting among pairs?

The plurality rule: Each voter casts a vote for his or her favourite candidate. Choose the candidate(s) who is (are) named most often.

# Condorcet’s challenge

Nicolas de Condorcet (1743-1794): a French philosopher, mathematician, and political scientist.

<aside>
💡 Plurality may contradict the majority opinion

</aside>

## Condorcet’s argument

Consider the following problem with 21 voters and 4 candidates.

| 3 | 5 | 7 | 6 |
| --- | --- | --- | --- |
| a | a | b | c |
| b | c | d | b |
| c | b | c | d |
| d | d | a | a |

The plurality rule chooses a with 3+5=8 votes.

Condorcet: But a is the worst candidate for a clear majority of voters (7+6=13). This majority prefers any candidate to a.

## Condorcet winner

Condorcet: c should be chosen if we abide by the majority opinion.

Reason: A majority (7+6=13) prefers c to a. Another majority (5+6=11) prefers c to b. A third majority (3+5+6=14) prefers c to d.

> A Condorcet winner is a candidate who defeats every other candidate in majority comparisons.
> 
- Defeat another candidate: More voters prefers a Condorcet winner to another candidate.
- By definition, there is a unique Condorcet winner if exists. A voting rule is Condorcet consistent if the voting rule chooses a Condorcet winner whenever it exists.
- The plurality rule is not Condorcet consistent.

## Non-existence of a Condorcet Winner

| 8 | 7 | 6 |
| --- | --- | --- |
| a | b | c |
| b | c | a |
| c | a | b |

Condorcet consistency property only specifies whom to choose whenever a Condorcet winner exists. To completely define a voting rule, we also need to specify whom to choose when a Condorcet winner does not exist.

# Borda’s challenge

Jean-Charles de Borda (1733-1799): a French mathematician, physicist, and political scientist.

<aside>
💡 Plurality may contradict the majority opinion

</aside>

| 3 | 5 | 7 | 6 |
| --- | --- | --- | --- |
| a | a | b | c |
| b | c | d | b |
| c | b | c | d |
| d | d | a | a |

## Borda’s argument

Borda: a is a poor candidate, but b, instead of c, should be chosen if we abide by the majority opinion.

Reason: b is ranked first by 7 voters (against 6 for c), first or second by 16 voters (against 11 for c), and first, second, or third by all voters (as is c).

## Borda’s idea:

The ranking of each candidate in the voters’ opinions should count — if I rank some candidate first, this should help the candidate more than if I rank him second.

## The Borda rule:

A candidate receives no points for being ranked last, one point for being ranked next to last, and so on, up to |A| − 1 points for being ranked first. A candidate with the highest total score, called a Borda winner, wins.

## Scoring voting rules

Fix a nondecreasing sequence of real numbers $s_0 ≤ s_1 ≤ ··· ≤ s_{|A|−1}$ with $s_0 < s_{|A|−1}$. 

A candidate receives $s_0$ points for being ranked last, $s_1$ points for being ranked next to last, and so on, up to $s_{|A|−1}$ points for being ranked first. A candidate with the highest total score wins

### Borda Rule:

$s_n=N, where\\n=0,...,|A|-1$

### Plurality rule

$0=s0=s_1=...=s_{|A|-2}<s_{|A|-1}=1$

### Condorcet consistent rule = ??

# Fishburn’s Theorem

<aside>
💡 There are problems where the Condorcet winner is never chosen by any scoring voting rule.

</aside>

- Implication: No Condorcet consistent voting rule can be a scoring voting rule.
- Proof: Homework question.
- Condorcet consistent voting rules and scoring voting rules are different families of rules. No comprise.

# Borda v. Condorcet | Scoring vs. Condorcet consistent rules

Condorcet supporters: The notion of majority comparisons is easy to grasp and seems closer to the people’s opinion than scores.

- Used by a number of private organizations: the Wikimedia Foundation, the Pirate Party of Sweden.

Borda supporters: There is one compelling property supporting scoring voting rules — participation.

- Used for political elections (Slovenia, the Green Party of Ireland) and elections by some educational institutions in the US (Harvard, UCLA)

# Participation

```
Starting from now, we will focus on voting rules that choose only one candidate 
for each collective decision problem.
```

1. Suppose that candidate a is chosen from the set $A$ by the electorate $N$. 
2. Next consider a voter $i$ outside $N$. Then the electorate $N ∪ \{i\}$ should select a or some candidate whom voter i prefers to a.

> If an additional vote succeeds in changing the outcome of the election. It can only be to the benefit of this “pivotal” voter.
> 

### Example

If a voting rule chooses a in the LHS problem and c RHS, it violates participation.

| Bob | Cheryl |
| --- | --- |
| a | a |
| c | b |
| b | c |
| d | d |

*a chosen*

| Ann | Bob | Cheryl |
| --- | --- | --- |
| b | a | a |
| a | c | b |
| c | d | c |
| d | b | d |

*c chosen*

# Scoring vs. Condorcet consistent rules

## Moulin’s Theorem

All scoring voting rules — where ties are broken according to a fixed ordering of A — satisfy participation. 

If A contains four or more candidates, there is no Condorcet consistent voting rule satisfying participation.

# Voting: aggregating individual opinions???

If a voting rule does not satisfy participation, a voter can influence the outcome of election in his/her favor by not participating in the election.

- Such a voting rule fails to aggregate individual opinions!
- What can a society do to ensure participation?

## Ensuring Participation

Punish those not participating by a fine! Moral punishment: social opprobrium! 

Change to a voting rule that incentives participation: scoring voting rules.

Legal punishment: compulsory voting

- Those not participating could face prosecution, face difficulties getting a job in the public sector, and lose the right to vote for 10 years.
- Compulsory voting is enforced in Argentina, Australia, Belgium, Brazil, North Korea, Singapore,

<aside>
💡 Strategic participation suggests that a voter, once realizing that his/her own vote may influence the outcome of election, will think twice and act like a player in the game of election, trying to maximize the returns from his/her vote.

</aside>

- No participation can be prevented, but how about lying about one’s favorite candidate?
- We vote and we lie!

### IRL Examples of tactical voting

In the 2004 Canada federal election, the governing Liberal Party was able to convince many New Democratic voters to vote Liberal in order to avoid a Conservative government.

For the 2015 UK general election, [voteswap.org](http://voteswap.org/) was set up to help prevent the Conservative Party staying in government, by encouraging Green Party supporters to tactically vote for the Labour Party in listed marginal seats.

## Strategic voting under Borda rule

![Untitled](Strategic%20%2037cdd/Untitled.png)

LHS problem (true preferences): a : 3, b : 6, c : 7,
d : 2 with c winning

RHS problem (misreported preference of Ann):
a : 2, b : 7, c : 6, d : 3 with b winning in favor of Ann!

### Strategic/ Tactical voting

The strategic aspect of voting is already noticed in 1876 by Charles Dodgson:

This principle of voting makes an election more of a game of skill than a real test of the wishes of the electors.

- A voting rule fails to aggregate individual opinions if it is manipulable by strategic voting (lying), like by not participating.
- What can a society do to prevent lying? Punish those who lie? Legally? Morally?
- Change to a voting rule that voters cannot benefit by lying?

It is impossible to distinguish a strategically biased report of a voter’s preference from a truthful one.

- One’s opinion is private information (before a reliable lie detector is invented).
- Hence, an openly untruthful report is a perfectly legal move.
- Moral punishment?
- Find a voting rule that is immune to strategic voting!

# Strategy-proofness

A voting rule is strategy-proof if when any voter, no matter what the other voters report, misreport his/her own preference, the voting rule will choose a candidate that is less preferred, according to his/her true preference ordering, compared with the candidate chosen if he/she has reported his/her true preference.

## Implication

![Untitled](Strategic%20%2037cdd/Untitled%201.png)

Imagine that LHS preference of Ann is his true preference. Then

a chosen LHS $\implies$ no restriction RHS
b chosen LHS $\implies$ b or c or d chosen RHS
c chosen LHS $\implies$ c or d chosen RHS
d chosen LHS $\implies$ d chosen RHS

a chosen RHS $\implies$ a chosen LHS
b chosen RHS$\implies$ a or b chosen LHS
c chosen RHS $\implies$ a or b or c chosen LHS
d chosen RHS $\implies$ no restriction LHS

---

Class exercise:

Imaging that RHS Preference of Ann is his true preference, then:

a chosen RHS $\implies$ 
b chosen RHS$\implies$ 
c chosen RHS $\implies$ 
d chosen RHS $\implies$ 

a chosen LHS $\implies$ 
b chosen LHS$\implies$ 
c chosen LHS $\implies$ 
d chosen LHS $\implies$ 

---

# Class discussion

- How to prevent strategic voting?
- Find a voting rule that is strategy-proof.
- Is the majority rule strategy-proof ? Why?

---

# Two candidates

The majority rule: desirable in the sense of being anonymous, neutral, and strictly monotonic.

- It is also immune to strategic voting: No voter can benefit by lying.
- Reason: Any voter, no matter what other voters do, by voting for his/her less favorite candidate, either has no influence on the outcome of election, or making his/her less favorite candidate elected.

### The Farquharson-Dummett conjecture:

> voting rules with at least three issues face endemic tactical voting.
> 
> 
>     *- Dummett and Farquharson (1961). “Stability in voting”. Econometrica. 29 (1): 33-43.*
>