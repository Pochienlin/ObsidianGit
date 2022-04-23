# 05 Marriage problems

Completed: Yes
Course Code: ECON241
Priority: 🟢
Rev 1: November 12, 2021

- Table of Contents 📖

---

## I. Marriage problem

***Marriage problem***: a one-to-one matching problem that consists of:

- A set of men: $M=\{m_1,...,m_p\}$
- A set of women: $W=\{w_1,...,w_q\}$
    - $p$ does not have to $=q$
- A set of **preference rankings** of both men and women
    - For each $m\in{}M$, $\succ_m$ is a strict ordering of $W\cup\{m\}$
        - e.g. $w_r\succ_{m_y}w_g$ means $w_r$ is preferred over $w_g$ by $m_y$ (s12 preference ranking)
        - $W\cup\{m\}$ → $m$ has to rank set $W$ and also himself $m$ (i.e. singlehood)
    - For each $w\in{}W$, $\succ_w$ is a strict ordering of $M\cup\{w\}$

***Matching***: a function $f:M\cup{}W→M\cup{}W$ such that:

- For each man $m\in{M}$, $f(m)\in{}W\cup{}\{m\}$
    - e.g. if $w_r$ is matched with $m_b$ → $f(w_r)=m_b$
    - $f(\text{agent})=$ partner of agent
- For each woman $w\in{W}$, $f(w)\in{}M\cup{}\{w\}$
- For each man and each woman, $f(m)=w\Leftrightarrow{}f(w)=m$
    - Consistency requirement

Alternative outcome of matching: $f'(\text{agent})=$ ...

### Stability of marriage problem

<aside>
💡 No one deviates from matching (divorce or new pairing)

</aside>

***Stability***: Matching is stable if it is not blocked by (1) any agent, or (2) any pair (man-woman pair)

- Not blocked by any agent → **individually rational**
    - blocked by agent $i$ where $i$ is a man or woman $(i\in{}M\cup{}W)$ if $i\succ_if(i)$
    - $i$ prefers $i$ (singlehood) to $f(i)$ (if given unacceptable choice → would prefer singlehood → divorce)
- Not blocked by any pair
    - blocked by pair $(i,j)$ where $i$ is a man and $j$ is a woman $(i\in{M},j\in{W})$ if $j\succ_if(i)$ and $i\succ_jf(j)$
    - $i$ prefers $j$ to $f(i)$ and $j$ prefers $i$ to $f(j)$ (if preferred choice available → would prefer preferred choice → new pairing)

<aside>
💡 ***Stability*** implies ***individual rationality***

</aside>

### PE of marriage problem

<aside>
💡 ***Stability*** implies ***Pareto efficiency*** (Stability → PE)

</aside>

- if a matching is ***Stable*** → it is PE
- if a matching is ***Not stable*** → it may or may not be PE

![Untitled](05%20Marriag%203c8ac/Untitled.png)

**Matching 1**

❌  NOT Stable

- Blocking agent: $w_g$ (prefers singlehood; not individually rational)
- Blocking pair: $m_b$, $w_g$ (prefer each other)

❌  NOT Pareto efficient

- $m_b$, $w_g$ cannot be made better off without making $w_r$, $m_y$ **worse off**

**Matching 2**

✅  Stable

- No blocking agent
- No blocking pair

✅  Pareto efficient

**Matching 3**

❌  NOT Stable

- Blocking pair: $w_r$, $m_y$

✅  Pareto efficient

**PROOF: a stable matching implies a PE matching (a stable matching is PE)**

$f$: stable matching → **proof by contradiction** $f$ is also PE

**Setting up PBC**

$f$: stable matching, but not PE

$g$: more efficient matching than $f$

START: suppose that $g(w_1)\succ_{w_1}f(w_1)$

$w_1$ (woman 1)

...

$g(w_1)$

...

$f(w_1)$

$m_A$ (man A)

...

$g(m_A)$

...

$f(m_A)$

**STEP 1 of PBC**: prove that $w_1$ cannot be single under $g$

- $g(w_1)≠w_1$, as that would make $f(w_1)$ unacceptable and **violate $f$'s stability** ($w_1$ is a blocking agent under $g$ if $w_1$ is single)
- Therefore, $w_1$ must be matched with a man $m$ in $g$ → suppose $g(w_1)=m_A$
- Since $g$ is more efficient than $f$, no agent is worse off under $g$
    - → $m_A$ is indifferent between $g(m_A)$ and $f(m_A)$, OR
    - → $g(m_A)\succ_{m_A}f(m_A)$

**STEP 2A of PBC**: prove that $m_A$ is NOT indifferent between $g(m_A)$ and $f(m_A)$

- Since preference rankings are strict and $g(w_1)=m_A → g(m_A)=w_1$
    - $g(m_A)=f(m_A)=w_1$ (indifferent) ⇒ $g(w_1)=f(w_1)=m_A$ → contradiction since $g(w_1)\succ_{w_1}f(w_1)$ ($w_1$ is strictly better off under $g$ than $f$)
    - → $m_A$ is NOT indifferent between $g(m_A)$ and $f(m_A)$

**STEP 2B of PBC**: by contradiction (Step 2A), $g(m_A)\succ_{m_A}f(m_A)$

- $g(m_A)=w_1\succ_{m_A}f(m_A)$
- Also, $g(w_1)=m_A\succ_{w_1}f(w_1)$
- Therefore, $m_A$ and $w_1$ form a blocking pair under $f$ (since they prefer $g$)

**STEP 3 of PBC**: prove that $g$ cannot be more efficient than $f$ → $f$ is PE

CONTRADICTION:

- By Step 2B: $m_A$ and $w_1$ form a blocking pair under $f$
- By PBC set-up: $f$ is stable → no blocking pairs exist

Therefore, reject hypothesis that $g$ (a more efficient matching than $f$) exists → $f$ is PE

<aside>
💡 Implication: as long as a matching is **stable**, it is **IR** and **PE**

</aside>

## II. DA algorithm

> Theorem (Gale & Shapley, 1962): **Deferred acceptance** (DA) algorithm mimics a real-life decentralised dating process and finds the stable matching in each marriage problem
> 

**s27-37**: man-proposing DA algorithm

1. Each man proposed to top acceptable choice. Each woman tentatively accepts her most preferred acceptable proposal (and rejects all other proposals).
2. Any one rejected in Step 1 proposes to next highest acceptable choice. each woman tentatively accepts her most preferred acceptable proposal (and rejects all other proposals, including previously tentatively-accepted ones)
3. Repeat until no new proposals

### DA matching is stable

- **No blocking agent**: each agent ONLY proposes to / accepts an agent who is **acceptable** → individually rational
- **No blocking pair**: blocking pair cannot exist as a potential proposer in a blocking pair ($m_B$) is necessarily lower ranked than the DA proposer ($m_{DA}$) of the accepting agent ($w$)
    - Suppose blocking pair $(m_B,w)$ in a $m$-proposing DA algorithm
        - For $w$ to end up with $m_{DA}$, $w$ must have (1) rejected $m_B$ for being unacceptable, or (2) rejected $m_B$ because $m_B\succ_{w}m_{DA}$ → $m_B$ lower-ranked than $m_{DA}$
        - $w$'s match can only get better as the DA algorithm proceeds (in a $m$-proposing DA)
        - Contradicts $(m_B,w)$ being a blocking pair
    - PBC: s42-43

### DA matching is optimal for proposer

$f^M:$ men-proposing DA matching

$f^W:$ women-proposing DA matching

$f:$ arbitrary stable matching

<aside>
💡 Intuition: the person proposing, while rejected at times, has the ability to propose based on their preference ranking

</aside>

Arbitrary $m$

...

$f^M(m)$

...

$f(m)$

...

$f^W(m)$

Arbitrary $w$

...

$f^W(w)$

...

$f(w)$

...

$f^M(w)$

if $f^M=f^W$⇒ $f^M=f^W=f$ (as in s36) → implies that no other stable matching exist

- $f^M(m)\succsim_{m}f(m)$: for man, stable matching no better than $f^M$, and no worse than $f^W$
- $f^W(w)\succsim_{w}f(w)$: for woman, stable matching no better than $f^W$, and no worse than $f^M$

### No mechanism (including DA) is strategy-proof

- $\varphi^M:$ men-proposing mechanism
- $\varphi^W:$ women-proposing mechanism

***Strategy-proof mechanism* $\varphi$**: a mechanism is strategy-proof if given the other agents' preferences, no agent ends up with a better match by misreporting their preference

- $\varphi^M$ and $\varphi^W$ are both NOT strategy-proof
- [x]  Proof: HW6 Q3

![Untitled](05%20Marriag%203c8ac/Untitled%201.png)

$\varphi^M$: $(m_1,w_1),(m_2,w_2)$

![Untitled](05%20Marriag%203c8ac/Untitled%202.png)

$\varphi^W$: $(m_1,w_2),(m_2,w_1)$

![Untitled](05%20Marriag%203c8ac/Untitled%203.png)

$w_1$ lie $\varphi^M$: $(m_1,w_2),(m_2,w_1)$ → Not SP

![Untitled](05%20Marriag%203c8ac/Untitled%204.png)

$m_1$ lie $\varphi^W$: $(m_1,w_1),(m_2,w_2)$ → Not SP

![Untitled](05%20Marriag%203c8ac/Untitled%205.png)

$m_2$ lie $\varphi^W$: $(m_1,w_1),(m_2,w_2)$ → Not SP

> Theorem (Roth, 1982): there is no mechanism $\varphi$ that is **both stable and strategy-proof**
> 
- [x]  Proof: HW6 Q4: 2-men 2-women
- [x]  Proof: HW6 Q5: n-men m-women

> Theorem (Dubins and Freedman, 1981 & Roth, 1982): man-proposing DA mechanism is strategy-proof for men; women-proposing DA mechanism is strategy-proof for women
> 
- $\varphi^M$: no man can benefit by lying, but woman can
- $\varphi^W$: no woman can benefit by lying, but man can