# Macroeconomics 1 | The Household

Archive?: No
End: August 23, 2021 11:30 AM
Start: August 23, 2021 10:00 AM
Tags: [ECON112]

# Overview

## Main Concepts

1. 

# Introduction

We are now going to gradually build up of our static macro model. This model economy has three agents:

1. a representative household;
2. a representative firm;
3. a government.

Plan for this part:

1. We first study the representative household, before moving on to the representative firm.
2. We then consider the equilibrium of the economy, its properties, and some policy implications.

Important note: Although we are interested in the impact of economic policy, we, for the most part, take the government’s behavior as given and our focus is on how the government’s actions affect the other economic agents’ decision and the economy as a whole.

This part introduces the representative household:

- there is one household representing all households in the economy;
- it is an approximation, for a model with many di§erent households is a lot more complicated to work with.

The household behaves in a competitive fashion, i.e., it takes all prices as given:

- One household who is price taker?
- Yes, the households is representative of all households and with many households assuming price-taking makes a lot more sense.

# Objective of the Household

We assume the household aims to maximize its utility. It is endowed with utility function $u(c,l),$ where 

- c is the units of the consumption good consumed and
- l is the units of leisure enjoyed.

u is assumed to be twice differentiable, with:

- $u_c(c,l) > 0$ and $u_l(c,l) > 0$: it is strictly increasing in each of its arguments.
- $u_{cc}(c,l) < 0, u_{ll}(c,l) ≤ 0$, and $u_{cc}u_{ll} - u_{cl}u_{lc} ≥ 0$: it is concave, strictly if the 2 weak inequalities are strict.

Are the following utility functions concave? Strictly concave? Are there conditions?

1. $u(c,l) = c^{\alpha} l^{\gamma}, (\alpha,\gamma) \in \{(x,y) \in (0,1)^2:x+y≤1\}$
2. $u(c,l) = v(c)+w(l)$, where v and w are strictly increasing and strictly concave.
3. $u(c,l) = u(c)+Al$, for $A > 0.$

# Constraints of the Household

1. A time constraint: $l + n ≤ h$, where  $h$ is the total units of time the household is endowed with and $n$ is the number of hours worked;
2. A budget constraint : $c ≤wn + \pi - T$ , where $w$ is the wage rate, $\pi$ **is capital income (dividends from ownership of the firm or interest from debt of the firm) and $T$ is the lump-sum tax owed to the government.

The household hence trades off consumption of the good and consumption of leisure:

- it likes both, but more leisure time means less income, in which case it can afford fewer units of the good.
- The wage rate is the opportunity cost of leisure, and we will often refer to it as the price of leisure.

# Household's maximisation problem

The problem of the household is to choose how much good and leisure to consume in order to maximize its utility given the two constraints it faces.

*and with the additional constraints that c, l, and n should be non-negative.

$$
max_{(c,l,n)}w(c,l)\; s.t.
$$

$$
c≤wn+\pi -T, \\l+n≤h
$$

Both these should be equalities to be maximised (i.e. make use of all the budgets and all the hours)

The utility function is strictly increasing in each argument, implyingthe household does not waste resources:

- the time constraint hold with equality: $n = h - l$ ;
- the budget constraint also holds with equality, thereby implying that the two constraints can be summarized into one budget constraint: $c = w (h - l ) + \pi - T$ .

The Problem can thus be rewritten as

$max_{c,l}u(c,l)\;s.t. \\c=w(h-l)+\pi-T$

with $c \;$non-negative and  $l \; \in \; [0, h]$ 

## Solving the problem

We solve this problem in two ways:

1. Graphically: we need to use a graphical representation of the utility function and of the constraints (time, budget and non-negativity);
2. Mathematically: we need to use tools used in optimization, the Lagrangian together with the Kuhn-Tucker theorem to deal with
inequality constraints.

# Graphical Solution

The function u(c,l) is a function of two variables, which is typically represented with a three-dimensional graph.

However, these graphs are, unfortunately, not so easy to work with. 

The solution used by economists is to use a two-dimensional representation by plotting indifference curves (ICs):

- An IC represents all the combinations of $c$ and $l$ yielding the same level of utility;
- That is, each IC corresponds to a given level of utility and, vice versa, each level of utility is associated with a given IC.

**Properties of ICs**

General:

- They do not cross.
- As the level of utility goes up the corresponding IC moves to the north-east.
- Please see Micro 1 and practice question on the next slide for more details.

For Macro 1, because we assume the utility function is **strictly
increasing, concave, and strictly concave** in c:

- They are decreasing, and the slope is the negative of the Marginal Rate of Substitution (MRS);
- They are convex, that is the arc joining two points on the same IC is above the IC

![Untitled](Macroecono%2005960/Untitled.png)

![Untitled](Macroecono%2005960/Untitled%201.png)

[Question 1 on page 158 in Williamson](Macroecono%2005960/Question%201%20a3af4.md)

Budget constraint - It is a simple linear relationship between c and l $c = w (h - l ) + \pi - T :$

- the slope is $-w$, which is why w is the price of leisure (also known as opportunity cost).
- $c(l=0)=wh+\pi -T, and \\ c(l=h)=\pi - T$

Non-negativity constraint - we can see from $c(l = h) = p - T$ that we need to distinguish between two cases:

- $\pi - T$ : any value for l 2 [0, h] is feasible and the household can consume even if it does not work when $p > T$ ;
- $\pi <T$: only values of _ $l\; \in \; [0,h-(T-\pi)/w]$are feasible.

![Untitled](Macroecono%2005960/Untitled%202.png)

![Untitled](Macroecono%2005960/Untitled%203.png)

**Tangency**

Since the household wishes to maximize its utility and higher utility levels are represented by ICs further to the north-east, or "higher," an optimal consumption choice is an intersection between the feasible part of the budget constraint and the "highest" IC intersecting this part of the BC.

You would probably have seen in Micro 1 cases where ICs are not convex, in which case there can be more than optimum.

But since we assume strictly convex ICs, an optimum is unique (and remember we assume the utility function is concave and ICs are convex, and we know in this case an optimum, which is a maximum in this case, is unique).

- We have to be careful though, for the optimum point might be a so-called corner solution because one of the constraints for l is binding:
- We often assume that $lim_{c→0}+ u_c(c,l) = +\infin$, which ensures the household never chooses $c = 0$.
- However, the constraints on l might be binding:
    - $l≤h$ might be binding when $p>T$ since $c>0$ for $l=h$ in this case; or
    - the constraint $l ≥  0$ might be binding if $u_l (c, l = 0)$ is finite and small enough.

![Untitled](Macroecono%2005960/Untitled%204.png)

## Internal Solution

If ICs are differentiable everywhere, which is the case if the utility function is twice differentiable, then:

- the optimum is the point of tangency between the feasible part of the budget constraint...
- ...unless one of the constraint for l is binding.
If one of the constraint for l is binding:
    1. If $l=0$ then $MRS < w$; 
    2. If $l=h$  then $MRS > w$.

### Constrained optimum

![Untitled](Macroecono%2005960/Untitled%205.png)

- Household is forced to consume more leisure than optimal

### Unconstrained optimum

![Untitled](Macroecono%2005960/Untitled%206.png)

### Case 2: $l_{max}<h$

Draw indifference curves

![Untitled](Macroecono%2005960/Untitled%207.png)

### Case 3: Constraint $I≥0$ is binding

![Untitled](Macroecono%2005960/Untitled%208.png)

### Interpretation

If the optimum is an interior solution MRS = w:

- MRS is equal to the price of leisure relative to that of the good (which is normalized to 1);
- The household is consuming just the right amount of leisure (and goods) given the price of leisure.

If the optimum is a corner solution MRS 6= w, because the household cannot adjust the quantity of leisure further to equate the MRS and the relative price of leisure:

- If  $l=h$ then $MRS>w$, that is the price of leisure is so low that the household would like to work more and consume more of the good, but this is not feasible because it already consumes no leisure.
- If $l=0$ then $MRS<w$,on the contrary the price of leisure is so high that the household would like to consume more leisure and consumer less goods, but it is not feasible because it entire endowment of time is already spent on leisure.

[Questions 2 and 4 on page 158 in Williamson (6th edition)](Macroecono%2005960/Questions%20%20c8973.md)

# Mathematical solution

Lagrangian is $\Lambda(c,l,\lambda) =u(c,l)+\lambda(w(h-l)+\pi-T-c)+\mu ^-l+\mu ^+(h-l)$

- Naturally, if $μ^- > 0$, then $μ^+ = 0$, and vice versa.

We assume that $lim_{c→l}=+\infin$ to ensure that $c>0$.

FOCs w.r.t.  $c$, $l$ and $\lambda$ are:

$$
u_c(c,l) = \lambda,\\
u_l(c,l)+μ^- = \lambda w+μ^+,and\\c = w(h-l)+\pi-T.
$$

If the constraints on l are not binding it is said the solution is interior (because it lies in the interior of the interval $[0, h]$, that is it is in $(0, h)$).

Let us assume that the solution is interior, in which case $μ^- =μ^+ =0$.

The first two FOCs then imply that $\frac{u_l(c,l)}{u_c(c,l)} =w$. ——— (1). That is, $MRS_{l,c}=w$, and 

<aside>
💡 the optimum is such that the slope of the relevant IC, $-MRS_{l,c}$, is equal to the negative of the relative price of leisure, $-w.$

</aside>

Expression (1) gives a relationship between c and l, and the budget constraint gives another relationship. We thus have a system of two equations with two unknowns and there will be a unique solution (unless the two equations are colinear).

How to solve for the optimal solution?

1. Express  $l$  as a function of $c$ from (1) (you can do the other way around if you prefer);
2. Plug the expression of l as a function of c into the budget constraint and solve for $c(w;\pi - T)$, the demand for goods as a function of w and of parameters.
3. Plug the expression obtained for $c$ in step 2 in the expression for $l$ from step 1 to obtain $l(w;\pi-T)$, the demand for leisure as a function of w and of parameters.

It is then important to check that $l$ indeed lies in $[0, h]$, for if it does not the solution is a corner solution and either $*μ^- > 0*$, in which case $l = 0$, or $*μ^+ > 0*$, in which case $l=h$.

### Corner solutions

Case 1: Suppose the solution obtained ignoring the constraints on $l$ is such that $l < 0$.

- unless the utility function is bizarrely shaped, the constrained optimum will be $l = 0$, i.e., the household chooses the solution closest to what it would choose in the absence of the constraint on $l.$

Case 2: Suppose instead the solution obtained ignoring the constraints on $l$  is such that $l > h$.

- again, the household chooses the solution closest to what it would choose in the absence of the constraint on $l$, i.e., the constrained optimum is $l = h$, unless the utility function is bizarrely shaped.

Consider the function $u(c,l) = min\{c,Al\}$, for A > 0, which is called a Leontief function.

- It is such that consumption and leisure are perfect complements, for the household wants to consume consumption and leisure in a given proportion so that $c = Al$:
    - Substitute $l=C / A$ into $C= w(h-l) + \pi -T$
        
        ![Untitled](Macroecono%2005960/Untitled%209.png)
        
- In fact, increasing one variable without increasing the other one does not increase utility: for any $l$ we have that $u(Al, l) = u(\hat c, l)$ for $\hat c > Al$ and that $u(Al, l) = u(Al,\hat l)$ for $\hat l > l$

In the case of a Leontief utility function we can use the fact that the optimum choice is such that $c = Al$, then use this relationship with the budget constraint to solve for $c$ and $l$.

[Practice](Macroecono%2005960/Practice%20951f4.md)

# Proporties of Optimal choice

### Impact of increase in non-wage factors

Suppose that $\pi - T$ increases, either because $\pi$ **increases, $T$  decreases, or both, and that its new value is $\hat {\pi - T}$ .
This change creates a `pure income effect`, because there is no change in prices.

We assume that both the consumption good and leisure are normal goods, implying this pure income e§ect leads to an increase in consumption and in leisure, unless $l$ was initially at a bound.

Formally, we have that in general that $\frac{dl}{d(\pi-T)}≥0$ and if initially $l \;\in \;(0, h)$, then $\frac{dl}{d(\pi - T)} > 0$ 

If initially $l \; \in \; (0, h)$, the household is initially not constrained in its leisure choice and it will therefore be willing and able to increase the quantity of leisure it consumes and $\frac{dl}{d(\pi - T )} > 0$;

- Note that if $l$ is close to $h$ initially, then the household could end up constrained, that is it could end up at $\hat l =h$ but would be happy to consume even more leisure, i.e., consume $l > h$;

If instead $l = h$ initially, then the household cannot increase the amount of leisure it consumes and therefore $\hat l = l = h$ and thus $\frac{dl}{d(\pi - T )} = 0$;
If $l = 0$ initially, either the household was constrained because it wanted to consume a negative amount of leisure $(μ^- > 0)$, or it was just happy with consuming no leisure $(μ^- = 0)$:

- In the first case the household might not increase its leisure consumption as it could be it still wishes to consume a negative amount ($μ^- > 0$ still);
- In the second case the household increases its consumption of leisure since initially it wanted to consume just zero.

Let us now go over the `graphical representation` of the results.

An increase in non-work related resources translates into a parallel upward shift of the budget constraint.

**Case 1: initially non-binding leisure**

If initially $l \; \in \; (0, h)$, the household is initially not constrained in its leisure choice, which means the highest IC is tangent to the budget constraint in its interior

- when non-work resources increase the household is able to increase the quantity of leisure it consumes, and
- either the new highest IC is tangent to the new budget constraint in $[0, h]$,...
- ...or the new highest IC touches the new BC at $l=h$ and $MRS>w$, because the household would like to be on a IC tangent to the BC at some value $\tilde l > h$.

![Untitled](Macroecono%2005960/Untitled%2010.png)

<aside>
❓ HAS TO BE IN BC:
Pure income effect, is not subject to substitution. 
Since l and C are both normal goods, they both necessarily have to increase with non-wage factor increase, else they would not be normal

</aside>

![Untitled](Macroecono%2005960/Untitled%2011.png)

**Case 2: Initially binding leisure**

If instead $l = h$ initially, then we had $l (w ; \pi - T ) > h$ and we know $l (w ; \hat{\pi - T} ) > l (w ; p - T ) ≥ h$ so that $l = \hat l = h$, and the new highest IC is still of slope smaller than MRS at $l = h$.

If l = 0 initially: 

- If the household was just happy with consuming no leisure ($*μ^- = 0*$), then since  $l (w ; \hat{\pi - T} ) > l (w ; \pi - T ) = 0$, we see the household increases the quantity of leisure consumed, and since the highest IC was tangent to the old BC at $l = 0$, the new BC is tangent to the new BC at $l > 0$.
- If instead the household was constrained because it wanted to consume a negative amount of leisure ($*μ^- > 0*$), then we again have that $l (w ; \hat{\pi - T} ) > l (w ; p - T)$, but this time $l (w ; p - T ) < 0$, and therefore this time we could have l (w ; *p -* T ) being less, equal, or greater than 0; and the highest IC was of slope greater than $w$ at $l = 0$ initially, it might still be the case or be tangent to the new BC at $l = 0$ or for $l > 0$.
    
    ![Untitled](Macroecono%2005960/Untitled%2012.png)
    

![Untitled](Macroecono%2005960/Untitled%2013.png)

### Change in wage rate

![Untitled](Macroecono%2005960/Untitled%2014.png)

![Untitled](Macroecono%2005960/Untitled%2015.png)

**Case 1: unconstrained**

Suppose that the household initially consumes an amount of leisure $l \; \in \; (0, h)$ and that the wage rate $w$ increases to $\hat w$ .

The case of a wage decrease is symmetric and you should do it as homework.

It is possible to compute the exact impact of such a change when we know the specific utility function of the household by replacing $w$ by $w$ in the expressions for the optimal values $c$ and $l$.

It is useful however to first characterize graphically the impact of the wage rate change.

Just like in micro, a wage rate change triggers two effects:

1. sub=less $l$ || **a substitution effect**: the price of leisure goes up, triggering a fall in the quantity of leisure consumed; this leads to an increase in disposable income and therefore to an increase in consumption. B*[old IC, new wages]*
2. income=more $l$ ||**an income effect**: disposable income increases ceteris paribus, which, since we assume that leisure is a normal good, leads to an increase in leisure consumed; this in turn implies a fall in income, ceteris paribus, and therefore to a fall in consumption. 
*New optimum - B[old IC, new wages]*

The total effect depends on the relative strength of the substitution and income effects.

![Untitled](Macroecono%2005960/Untitled%2016.png)

**Case 2: constrained**

When one of the constraints on $l$ is initially binding, then effects can effectively be distorted.

$l=0$ | HH might still choose $l = 0$ after the wage increase even if the income effect dominates the substitution effect because $l = 0$ is a constrained optimum

![Untitled](Macroecono%2005960/Untitled%2017.png)

$l = h$ | HH might still choose $l = h$ after the wage increase if the income effect is strong enough 

![Untitled](Macroecono%2005960/Untitled%2018.png)

General method:

- Start from initial unconstrained optimum;
- Evaluate impact of the change ignoring constraint;
- Check whether a constraint binds, and if yes then the new constrained optimum is a corner (provided the utility function is well behaved).

### Individual level

At the **individual** level we would expect the labor supply to be increasing in the wage rate up to a point and to possibly become decreasing after, with the wage rate at which the change happens would depend on the non-work resources 

Such a labor supply is said to be **backward bending**. Intuition:

- Marginal utility of consumption is very high for low levels of consumption, while marginal value of leisure is relatively low, so we can expect the HH to be very willing to work more as w increases;
- As w increases further, income generated from work increases also and leads to a decrease of the marginal utility of consumption, whereas the marginal utility of leisure has increased and one can reach a point where the HH chooses to decrease its labor supply without leading to a fall in income, because $w (h - l )$ increases still thanks to the wage rate increase.

$$
MU_C>MU_l\;when\;l<<N^S
$$

$$
w \Delta → w(h-l) \Delta;\;MU_C \nabla || MU_l\Delta \\(h-l^*)=\hat h
$$

### Aggregate level

- we typically assume that the labor supply curve is upward sloping everywhere;
    - $\because$ even though some households might decrease their labor supply, there are sufficiently many other households who are increasing their labor supply to ensure that the net effect is positive.

Data:

- for a long time in modern times no trend in hours at household level in the US (not sure for EU or Japan or SG), but this seems to have changed.
- complicated by the fact that they are also changes in life expectancy and in resources for retirement, as this changes labor choice:
    - if I know I will have a given pension at 60 for the rest of my life, then my work choices are different form those I would make if I have to save for myself (the effect could be neutral if lump sum taxes and/or everyone the same as pension funded taxes and they are the same for everyone, but in practice it is not the case)

[Practice: foreign domestic worker ban](Macroecono%2005960/Practice%20f%20aee00.md)