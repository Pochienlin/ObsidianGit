# Forward Propagation
UID: 202212151751
Tags: #🌱 
Links: [[Introduction to Deep Learning]] [[Backward Propagation]]

## Overview  
In Simple terms, Forward propagation means we are moving in only one direction(forward), from input to output in a neural network.
![[Pasted image 20221215175139.png]]

### Weight notation
![[Pasted image 20221215175322.png]]
![[Pasted image 20221215175341.png]]
##  **Activation function:**

We are working on a binary classification problem, so for classification, we will use the Sigmoid function.
![](https://miro.medium.com/max/934/1*cN0McK0qEBKgCnkFpdS4Rg.png)

## Loss function 

![](https://miro.medium.com/max/1400/1*herTluRZv7FlFfbtgpw8nw.png)

Figure 7: Binary classification error

Loss function in classification, here it is binary cross-entropy.

![](https://miro.medium.com/max/1260/1*lD56U9diP14QqtxLzbQkNA.png)

For binary classification we have, y = 0 or y = 1.

![](https://miro.medium.com/max/940/1*B1WlYmfQ8AXsT4hKSeN4Lg.png)

y_pred is calculated by sigmoid function,

![](https://miro.medium.com/max/1400/1*BUERhrmp7Bl3Q-i1CaTE_Q.png)

# Summary:

1.  Calculating, Z =summation[(weights*input)+bias].
2.  Choosing Activation function = for binary classification sigmoid function.
3.  Substituting the value of “ Z ”, we will get y_pred.
4.  Calculation of Loss using binary cross-entropy.