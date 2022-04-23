# Macroeconomics 1

Archive?: No
End: September 6, 2021 11:30 AM
Start: September 6, 2021 10:00 AM
Tags: [ECON112]

# Overview

This part introduces the representative firm:

- there is one firm representing all firms in the economy;
- it is an approximation, for a model with many di§erent households can be a lot more complicated to work with;
- in fact, a model with many firms can be as easy to work with as a model with a representative firm in the absence of market imperfections and when the production displays constant returns to scale.

We again assume that the firm behaves in a competitive fashion, i.e., it takes all prices as given:

- one firm who is price-taker?
- Yes, the firm is representative of all firms and with many firms assuming price-taking makes a lot more sense.

## Main Concepts

1. 

# Setting up the problem

We assume the firm’s objective is to maximize its value, that is, the value of its shares.

In our static environment this is the same as assuming that the firm wishes to maximize its profits:

- By maximizing its profits the firm maximizes the dividends it distributes to its shareholders.

Implicit in this assumption is the assumption that the firm’s management behave in the best interest of its shareholders.

- we ignore agency problems that exist when the firm’s management are not the owner(s) of the firm;
- when agency problems exist the owners need to design a contract to provide the right incentive to the management (think of stock options and similar contracts) —> contract theory/corporate finance courses.

Who are the firm’s shareholders? The representative household: the non-labor income p comes from the representative firm’s profits. We have closed the circle.

## Profits

As in micro we have that

- Profit = Revenue - Costs.

So we need to specify the revenue and costs of the firm. Revenue: the output produced is sold at price 1 (the good is the numéraire), so

- Revenue =y.

Cost: We assume the firm already owns its capital (we will study capital accumulation when we study a dynamic environment) and thus only needs to choose how much labor n to hire:

- Cost =wn.

## Production function

Setting Up the Problem The Production Function
We assume that to produce its output y the firm requires two inputs, capital k and labor n, with

$$
y =zf(k,n).
$$

f is the function which captures how output is obtained from different mixes of capital and labor. f is like a black box.

z is an index for productivity, which is often referred to as TFP, for **Total Factor Productivity**:

- It captures the impact on production of factors that are attributed to neither labor nor capital;
- At the firm level it can be its organizational structure; at the aggregate level, it can be institutions (like, the legal and political systems); infrastructure (like transport, or communication more generally), etc.

![Untitled](Macroecono%203b5dd/Untitled.png)

![Untitled](Macroecono%203b5dd/Untitled%201.png)

![Untitled](Macroecono%203b5dd/Untitled%202.png)

![Untitled](Macroecono%203b5dd/Untitled%203.png)

![Untitled](Macroecono%203b5dd/Untitled%204.png)

The marginal productivity of capital MPk is positive and decreasing (f is increasing and concave in k).

The marginal productivity of labor MPn is also positive and decreasing (f is increasing and concave in n).

Capital and labor are somewhat complementary (and imperfectly substitutable): MPk increases with n and MPn increases with k (that is the second cross derivatives of f are positive).

Production displays Constant Returns to Scale (CRS).

- This is consistent with evidence at macro level, so it fits well for our representative firm’s production function since it is the aggregate production function.
- DRS to get a distribution of firm sizes; IRS has some supporters and seems true in certain sectors, because of large fixed cost (e.g., public transport; energy) or network e§ects (e.g., amazon; Microsoft).
- Question

<aside>
💡 Main point summary

</aside>

[Questions 15 and 17 on page 160 in Williamson](Macroecono%203b5dd/Questions%20%20a4568.md)

# Optimal Choice

## Analytical Characterization

The firm’s problem is

$$
max_nzf(\bar k,n)-wn, n
$$

where $\bar k$ is the fixed capital stock.

The FOC of the problem yields that the optimal employment level is such that

$$
zf_n(\bar k,n) = w,
$$

In words, the optimal labor choice for the firm is such that the marginal productivity of labor $MP_n \equiv zf_n(\bar k,n)$  is equal to the wage rate w.

## Intuition

Remember first that we assume that $MP_n$ is decreasing in $n.$

If the firm chooses bn such that $zf_n(k,bn) > w$ the firm could increase its profit by increasing the quantity of labor it hires:

- the next units of labor are more productive, and therefore bring more revenue, than they cost;
- marginal revenue is  $zf_n(k,\tilde n)$ which is greater than marginal cost w for $\tilde n$ larger but close enough to $\hat n$.

If instead the firm chooses $zf_n(k,n) < w$, the firm could increase its profit by decreasing the amount of labor it hires:

- the last unit hired are less productive, and therefore bring in less revenue, than they cost;
- marginal revenue is $zf_n(k,\tilde n)$ which is smaller than marginal cost w for $\tilde n$ larger but close enough to $\hat n$.

![Untitled](Macroecono%203b5dd/Untitled%205.png)

![Untitled](Macroecono%203b5dd/Untitled%206.png)

## Graphical Representations $MP_n$

If we plot the MPn curve as a function of n and for given values of z and n, it is downward sloping by assumption;

- Each time either $z$ or $k$ changes, the $MP_n$ curve shifts;
- The optimal labor choice for a given wage rate is given by the level of employment for which the MPn curve crosses the horizontal line of value w.

![Untitled](Macroecono%203b5dd/Untitled%207.png)

## Graphical Representations: Production Function

The production function is strictly increasing and strictly concave when represented as a function of n for given values of z and k;

Each time either z or k changes, the production function shifts;

The cost function wn is the straight line starting at the origin and of slope w;

The optimal labor choice is the value of n for which the production function has the same slope as the cost function.

- Note that this graph can also be used for the intuition, for the vertical distance between the production and cost functions is the firm’s profit and the point where the two functions have the same slope is where the distance is maximum.

![Untitled](Macroecono%203b5dd/Untitled%208.png)

[Questions 12, 13, and 14 on page 160 in Williamson](Macroecono%203b5dd/Questions%20%2058c27.md)

### Impact of a changes in Capital and TFP

We assume that capital and labor are somewhat complementary, for we assume that $MP_n$ increases when k increases:

- If k increases, each unit of labor becomes more productive, and therefore for a given wage rate the firm increases its profit by hiring more units of labor.
- Graphically, the $MP_n$ curve shifts up, which for a given wage rate w clearly yields an increase in n.
If instead we consider an increase in TFP z:
- We also get that each unit of labor becomes more productive, and therefore the firm also increases its profit if it hires more labor.
- Graphically, the $MP_n$ curve shifts up as well, which for a given wage yields an increase in the desired quantity of labor n.

![Untitled](Macroecono%203b5dd/Untitled%209.png)

![Untitled](Macroecono%203b5dd/Untitled%2010.png)

# Labour demand curve

What happens to the quantity of labor demanded by the representative firm when the wage rate increases?

- When w rises the cost of each unit of labor increases and therefore the firm maximises its profits by decreasing the quantity of labor it hires: the units it used to hire are now less productive than they cost.
- The demand for labor from the representative firm $n^f (w;z)$ is decreasing in the wage rate w, that is, its labor demand curve is downward sloping when represented as a function of w.
- How does the labor demand curve change when k or z change? From our previous analysis we know that nf increases as k or z increases for a given w, which graphically means the labor demand curve shifts up.

![Untitled](Macroecono%203b5dd/Untitled%2011.png)

![Untitled](Macroecono%203b5dd/Untitled%2012.png)