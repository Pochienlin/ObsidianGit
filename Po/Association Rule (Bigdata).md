# Association Rule (Bigdata)
UID: 202209061130
Tags: #🌱 
Links: [[Big Data]] [[Big Data and Business Model]]

----
## Formalisation
$$
\{A, B\}\implies {C}(Support=S, Confidence=C)
$$
Where
-   Support $S = \frac{A \cap B \cap C}{T}$
-   Confidence C = $P(C|A\cap B)$

Here we try to find an existing group of goods $\{A,B\}$ and try to find how closely is good $C$ related to it.
### Coverage
The proportion of cases where the rule can be applied. This is sometimes called the LHS support. Coverage can be found by summing the number of baskets with the antecedent goods ({A, B} in this case), dividing it by the total number of baskets in the data set
$$
Coverage = \frac{A \cap B}{T}
$$

### Support
Refers to the proportion of sets within the database that includes the associated goods (A and B + C). The data first finds the number of datasets that includes all relevant goods, then divides this number by the total magnitude of the database.

> [!tip] paraphrasing...
> What's the probability that a customer within my online store purchases both A and B?

### Confidence
Refers to the probability that a given good C is in the same set, given that the associated precedents A and B are present within the bundle. This is also called "strength" of the association.
> [!tip] paraphrasing...
> This customer purchased A. From my past data, how likely is he to purchase B as well?
> 

### Lift Ratio
Refers to the ratio between the targeted audience's proliferation rate and the population's. i.e.
$$
\frac{P(A \cap C)}{P(A)}
$$
Where A is the observed behaviour, C is the condition of the target audience. 

> [!example]
> Out of Sogang University's students, 5% uses MacBook.
> $P(A)=0.05$, where A refers to those who use MacBooks in the college
> Out of Sogang University's social science students,20% uses MacBook.
> $P(A\cup C)=0.20$ where C refers to the group that studies social sciences
> 
> Therefore, $Lift\;Ratio = \frac{target\;proportion}{population\;proportion}=\frac{0.20}{0.05}=4.00$ 

### Leverage
> [!note]
> Leverage measures the **correlation** between item sets by comparing the support of item sets **under independence assumption and in the data set**.
#### Lift vs. Leverage
| Lift                                                   | Leverage                              |
| ------------------------------------------------------ | ------------------------------------- |
| Ratio                                                  | Difference                            |
| Find strong associations among less frequent item sets | favours item sets with higher support |
-   If **leverage = 0,** A and B are **independent** (according to probability theory, support(A U B) = support(A) x support(B) given A and B are independent).
-   If **leverage > 0**, A and B are **positively correlated**. Namely, the observed support is higher than the expected support.
-   If **leverage < 0**, A and B are **negatively correlated**. Using the supermarket example, the customers tend **NOT** to buy A and B together.

## Application
### Using Association Rule and Market Basket Analysis for ecommerce
![[case_AR0.pdf]]
#### Problem:
Retail Z sells phones and accessories online. They intend to bundle their products to improve sales, but this must target complements to be effective. The challenge is to discover which types of goods should be bundled and sold together.

#### Method: Associative rule- market basket analysis (“AR-MBA”)

##### Notation and tool:
his means that with goods A and B in a cart, we can tell how likely is associated good C will end up in the same cart. **Support** shows the number of sets in the database with all 3 items, while **Confidence** shows the probability of C being included in the set, given that A and B are included. Related to this is **Lift Ratio**: the ratio between the response in the target group and the population. E.g. If 5% of all Sogang students uses MacBook, while 20% of Social Science students in Sogang uses MacBook, the lift ratio is 20% / 5% = 4.0. Lift Ratio > 1 implies meaningful association between the population and the product.

**RapidMiner** is a rule mining tool that extracts these 3 metrics (C, S, Lift) and more. One of the 6 relations returns a result that clears the C and S threshold (0.6 and 0.3 respectively) and has Lift Ratio >1, making it the only valid rule mined. Department 2 and 5 thus has a statistical basis for bundle discounts.

---------- END OF SUMMARY -----------

#### Things that I didn’t understand

I am including this section solely for my own future review, if you are reading this for assessment purposes, please do kindly ignore this section, thank you!

- Why was there a need to put the data through Laplace transformation? What is the integral in this context? What is gain and conviction in the results table?

- What does the FP-algorithm do and how does it fit into the methodology?

- Data transformation in pg. 156-157 is concerned with binary data (i.e. type of goods only and not quantity). Such entries, no matter how many of C was purchased, will be captured as =1
	- Boolean definition ignores magnitude differences. If I buy 1 bag with 1 laptop vs. 3 cables with 1 laptop: The data will represent both as the same weight of association.
	- Perhaps the cardinality is noise for the miner for some reason? I would imagine the association between cables and laptop in these entries ought to be given more weight.
> [!tip] Response
> While quantity can be an important factor within certain scenarios, Association Rule itself is agnostic to scale. If there is a need to measure quantity as a factor of strength of association, other tools should be used in conjunction.
> 
