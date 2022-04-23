# Taxation and Bankruptcy Problems
UID: 202204122027
Tags: #🌱 
Links: [[Strategic Thinking]]

---

## 0. At a glance
#### Axioms
| Axioms                            | Description                                                                                                                                                                 | Examples                               |
| --------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| C-D consistency                   | Consistent to the concede and divide rule                                                                                                                                   | Talmud Rule, concede and divide method |
| Minimum Rights First              | The final claims can be broken down into the agent's minimum rights + solution to the reduced problem using the Talmud principle                                            | Talmud rule, concede and divide method |
| Equal treatment of equals         | If agent A and B both claims amount X, they ought to both receive allocation Y. This axiom is a weak fairness axiom, and does not imply unequal treatment of unequal agents | All rules learnt                       |
| Independence of Irrelevant Claims | Solution should be consistent with the truncated problem                                                                                                                    | Constraint Equal Awards, Talmud rule   |

#### Rules
| Rule name                | Concept                                                                                                                                                           |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Constrained Equal Awards | Divide estate evenly across all agents until the claimed amount                                                                                                   |
| Constrained Equal Losses | Divide losses ($c_i - \frac{\sum c - T}{n}$) among all agents (think of it as $c_i$ = agent i's before tax income, losses as equal taxation)                      |
| Proportional             | Distribute all agents' received amount by a fixed ratio of their claims                                                                                           |
| Talmud Rule              | For $\frac{\sum c_i}{2} < T$, use CEA, for  $\frac{\sum c_i}{2} > T$, use CEL, if $\frac{\sum c_i}{2} = T$, CEL CEA and proportional rule yields the same results |

## I. Division rule & Claims problem

**Division rule → Claims problem**

1. Agent ($1,...,N$)
2. Claims of agent ($c_1,...,c_N,c_i>0$)
3. Resource of size $T$ ($0≤T≤c_1+...+c_N$)

Voting rule → CDP

1. Voters
2. Candidates
3. Voters' opinion of candidates

‼️ **Solution to claims problem**

- Division of resource ($x_1,...,x_N$)
- where $0≤x_1≤c_1,...,0≤x_N≤c_N$ and
- $T=x_1+...+x_N$ (total resource is fully allocated)

### Formal definition of division rule

- Solves each **claims problem**: (1 DR for 1 CP)
    - Regardless of the number of agents $N$
    - Regardless of the amounts of their claims $c_N$
    - Regardless of the size of the resource $T$

<aside>
💡 DR is a function (like VR) for infinitely many claims problem

</aside>

## II. Division rules (constrained equal and proportional)

### Constrained equal awards rule

❗ Equal division is NOT a DR → equal share may exceed one's claim, i.e. $c_1<x_1$

![Untitled](03%20Taxatio%20abb7b/Untitled.png)

![Untitled](03%20Taxatio%20abb7b/Untitled%201.png)

### Constrained equal losses rule

<aside>
💡 Used for taxation (every agent taxed the same amount)

</aside>

- Loss of agent $i$ (tax): $c_i-x_i$
    - Taxable income: $c_i$
        - $c_1+...+c_N=$ sum of before-tax income
    - After-tax income: $x_i$
        - $T=x_1+x_2+...+x_N$
        - $T=$ sum of after-tax income
    - Total tax on all agents: $c_1+...+c_N-T$

![Untitled](03%20Taxatio%20abb7b/Untitled%202.png)

- Levelling taxation scheme

### CEA vs CEL comparison

Constrained equal **awards** rule

- Equalise $x_i$ (after-tax income)

Constrained equal **losses** rule

- Equalise $c_i-x_i$ (tax)
- Head tax (every agent pays same tax)

EXAMPLE OF COMPARISON: between s23 and s24

### Proportional rule

(the larger the claim, the larger the award)

For population $1,...,N$, claim $c_1,...,c_N≥0$, and $0≤T≤c_1+...+c_N$, award such that for each $i=1,...,N$, $x_i=\frac{c_i}{c_1+...+c_N}T$

such that 

- $x_i=\frac{c_i}{c_1+...+c_N}T≤c_i$
- $T≤c_1+...+c_N$

i.e. Award $=\frac{Claim}{Total\space{}claim}\times{Total \space{}resource}$

![Untitled](03%20Taxatio%20abb7b/Untitled%203.png)

Property of proportional solution:

$$
\frac{x_1}{x_2}=\frac{c_1}{c_2}
$$

![Untitled](03%20Taxatio%20abb7b/Untitled%204.png)

$x_1=\frac{10}{510}\times{30}$

$x_2=\frac{200}{510}\times{30}$

$x_3=\frac{300}{510}\times{30}$

## III. Contested garment problem (concede and divide)

2 step solution for 2-agent: (1) concede, (2) divide

**STEP 1**: assign concessions from one agent (A) to another

- When A1 claims $c_1$, A1 concedes $T-c_1$ to A2
    - Concession: $\max\{T-c_1,0\}$
- When A2 claims $c_2$, A2 concedes $T-c_2$ to A1
    - Concession: $\max\{T-c_2,0\}$

### Connecting CD problem to (1) CEA, (2) CEL and (3) proportional rules

<aside>
💡 Rabbi Nathan's solution (Slide 10) is an extension of concede and divide from 2 to 3 or more agents division problems

</aside>

Let $Y_{12}=\max\{T-c_1,0\}$ be agent 1's concession to agent 2

Let $Y_{21}=\max\{T-c_2,0\}$ be agent 2's concession to agent 1

$x_1=Y_{21}+\frac{1}{2}[T-Y_{12}-Y_{21}]$

$x_2=Y_{12}+\frac{1}{2}[T-Y_{12}-Y_{21}]$

- Deriving CEA and CEL with half-claim benchmark from CD
    
    **Case 1**: suppose $0≤c2≤c1$ (both concede 0)
    
    if $T≤c_2(≤c_1)$
    
    - $Y_{12}=0$
    - $Y_{21}=0$
    - $⇒x_1=x_2=0+\frac{1}{2}[T-0-0]=\frac{T}{2}$
    
    **Case 2**: suppose $0≤c_2≤T≤c_1$
    
    - $Y_{12}=0$
    - $Y_{21}=T-c_2$
    - $⇒x_1=T-c_2+\frac{1}{2}[T-(T-c_2)]=T-\frac{c_2}{2}$
    - $⇒x_2=0+\frac{1}{2}[T-(T-c_2)]=\frac{c_2}{2}$
    
    **Case 3**: suppose $0≤c_2≤c_1≤T$ (both concede)
    
    - $Y_{12}=T-c_1$
    - $Y_{21}=T-c_2$
    - $⇒x_1=T-c_2+\frac{1}{2}[T-(T-c_1)-(T-c_2)]=c_1-\frac{c_1+c_2-T}{2}$
    - $⇒x_2=T-c_1+\frac{1}{2}[T-(T-c_1)-(T-c_2)]=c_2-\frac{c_1+c_2-T}{2}$
    
    ❗ Derivation in Lecture 4 slides (between slides 31 and 32)
    
    ‼️ Total loss = (Total claim - Total resources) ⇒ Equal loss = Total loss / No. of agents
    

![Untitled](03%20Taxatio%20abb7b/Untitled%205.png)

At half claim ($T=7$)

- CD outcome = proportional rule (diagonal line connecting $T=0$ and $T=14$ passes through $T=7$)
- solution also = CEA = CEL at $T=7$

### Talmud Rule: CD based on CEA and CEL principles

if $0≤T≤\frac{c_1+...+c_N}{2}$ (up to half of total claim)

- ⇒ CEA up to half of each agent's claim

if $\frac{c_1+...+c_N}{2}≤T≤c_1+...+c_N$ (from half of total claim to total claim)

- ⇒ CEL up till half of each agent's claim

when $T=\frac{c_1+...+c_N}{2}$

- ⇒ Proportional rule: every agent gets a share in proportion to each agent's claim

## IV. CD-consistency and Talmud Rule

<aside>
💡 CD is a division method, not a division rule (refer to strict definition above), as it only addresses 2-agent claims problem → CEA and CEL are DRs

</aside>

![Untitled](03%20Taxatio%20abb7b/Untitled%206.png)

**CD 2 agents** (not a division rule)

- 2-step: concede + divide

**Talmud Rule 3 agents** (division rule)

- CEA when $T$ is small (≤ half of total claims)
- CEL when $T$ is large (≥ half of total claims)

### [Axiom] CD-consistency

A division rule (DR) is CD-consistent if for:

- each population $1,...,N$
- each claim profile $c_1,...,c_N$ (non-negative real numbers)
- each $T$ satisfying $0≤T≤c_1+...+c_N$

DR selects $x_1,...x_N$ such that each **pair** $i,j\in\{1,...N\}$

$⇒(x_i,x_j)$ is the CD solution when $x_i+x_j$ is divided between $i,j$

<aside>
💡 A CD-consistent DR generates the CD-solution when restricted to any 2-agent problem

</aside>

![Untitled](03%20Taxatio%20abb7b/Untitled%207.png)

$x_i+x_j=T$

### Uniqueness of CD-consistent DR

> Theorem (Aumann & Maschler, 1985): There is only 1 CD-consistent DR → **the Talmud rule**
> 
- Talmud rule extends CD-solution from 2-agent to 3-agent problems in a CD-consistent manner

## V. CD solution for 2-agent problem

<aside>
💡 Why is CD-solution for 2-agent problems a desirable property (axiom)?

</aside>

**Ans**: CD-solution is the only solution that satisfies the following 3 axioms

1. Equal treatment of equals 
2. Minimal rights first
3. Independence of irrelevant claims

### Equal treatment of equals (fairness axiom)

If 2 agents have the same claims, they should be awarded the same amounts (Aristotle)

- Axiom may apply to 3 or more agent problems

☑️ Proportional rule satisfies equal treatment of equals ($x_i=\frac{c_i}{c_1+...+c_N}\times{T}$)

☑️ CEA, CEL satisfies equal treatment of equals

☑️ Talmud rule satisfies equal treatment of equals (since it combines both CEA, CEL and PR)

### Minimal rights first

*Minimal rights*: MR of agent $i=\max\{T-c_j-c_k,0\}$ (in 3 candidate problem with candidates $i,j,k$)

STEPS: (L5 s22)

1. Assign MR ($m$)
2. Reduce claims and $T$ by MR
3. Apply Talmud rule ($y$)
4. Add MR back to awards ($x=m+y$)

![Untitled](03%20Taxatio%20abb7b/Untitled%208.png)

❗ *Minimal rights first*: for each population, each claim profile, and each $T$, the DR selects $(x_1,...,x_N)$ such that for each $i=1,...,N$

$⇒x_i=m_i+y_i$

where $y_i$ is solution selected by the rule based on reduced claims $c_i-m_i$ and the reduced resource $T-(m_1+...+m_N)$

![Untitled](03%20Taxatio%20abb7b/Untitled%209.png)

### Independence of irrelevant claims

Talmud solution is not affected by irrelevant claims ($c_i-T=$ irrelevant claim if $>0$)

❗ *Independence of irrelevant claims*: for each population, each claim profile, and each $T$, the DR selects $(x_1,...,x_N)$ such that for each $i=1,...,N$

$⇒x_i=y_i$

where $y_i$ is the solution selected by the DR based on the truncated claims ($\min\{c_1,T\},...,\min\{c_N,T\}$) and $T$

![Untitled](03%20Taxatio%20abb7b/Untitled%2010.png)

☑️ CEA and Talmud rule satisfies independence of irrelevant claims

❌ CEL and Proportional rule **violates** independence of irrelevant claims

- counter-example to prove for CEL: $c_1=10,c_2=6,T=8$ (L5 s28)
- PR: ratio is changed when claim is changed (when irrelevant claim is removed)
- CEL and PR depends on irrelevant claims

### Characterisation of CD solution for 2-agent problems

> Theorem (Dogan, 1996): CD is the only 2-agent division method satisfying (1) equal treatment of equals, (2) minimal rights first, and (3) independence of irrelevant claims
>