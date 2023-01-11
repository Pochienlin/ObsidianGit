# Backpropagation
UID: 202212211554
Tags: #🌱 
Links: [[Forward Propagation]] [[Deep Learning Fundamentals with Keras]]

----
## Abstract
> [!abstract]
> Neural networks are trained to optimize their weights and biases for a given dataset through a supervised learning process, where each data point has a corresponding label or ground truth. 
> 
> The training process involves:
> - calculating the error between the predicted values and the ground truth labels, 
> - using this error to update the weights and biases in the network through gradient descent. 
> - The error is typically calculated as the mean squared error across all data points. 
> - The weights and biases are updated using the chain rule to find the derivative of the error with respect to each weight and bias, and applying the gradient descent equation to update them. 
> 
> The training process involves repeatedly updating the weights and biases until the error is minimized or falls below a certain threshold.
## Problem setting
Previously when discussing [[Forward Propagation]], it is evident that the output may not always reflect the Ground Truth ($T$) without some closed loop system.

## Overview
1. Calculate error $E$ between Ground Truth ($T$) and estimated output.
	1. Typically, Mean Squared Error is used, i.e.
			$$\frac{1}{2m} \sum_{i=1}^{m}(T_i-a_{2,i})^2$$
1. Propagate $E$ back into the network and update each weight and bias as per the following equation
	$$
	w_i \rightarrow w_i-\eta \frac{\delta E}{\delta w_i}
	$$
	$$
	b_i \rightarrow b_i - \eta \frac{\delta E}{\delta b_i}
	$$Where $b_i$ and $w_i$ refer to biases and weights respectively
![[Pasted image 20221221160325.png]]
#### Updating Weights $w_i$ and Biases $b_i$
For updating $w_2$, we know from [[Gradient Descent]] to follow $w_2' = w_2 - \eta \frac{\delta E}{\delta w_2}$
- To find $\frac{\delta E}{\delta w_2}$, we will need to use the [[Chain Rule]] because $E$ is not expressed in $w_2$ by default
- To do this we can use:
		$$E=\frac{1}{2} (T-a_2)^2 \rightarrow \frac{\delta E}{\delta a_2} = -(T-a_2)$$
		$$a_2= f(z_2)=\frac{1}{1+e^{-z_2}} \rightarrow \frac{\delta a_2}{\delta z_2} = a_2(1-a_2)$$
		$$z_2 = a_1*w_2+b_2 \rightarrow \frac{\delta z_2}{\delta w_2}=a_1$$
- Obtaining the above partial differentials, $\frac{\delta E}{\delta w_2}$ can be found by taking their product
![[Pasted image 20221221162530.png]]
Similarly, we can do the same for biases
![[Pasted image 20221221162831.png]]
- Note that $\frac{\delta z_2}{\delta b_2} = 1$, not $2$, as it is not a coefficient of $w_i$
### Updating $w_1$ (propagating backwards)
![[Pasted image 20221221165304.png]]
![[Pasted image 20221221165403.png]]
Similarly, $b_1$ can be found as follows:
![[Pasted image 20221221165518.png]]

----
# Propagating backwards in the first example
First, we apply forward propagation as previously done:
![[Pasted image 20221221165559.png]]
This is the predicted value by the network.
| Term  | Value  |
| ----- | ------ |
| $z_1$ | 0.415  |
| $a_1$ | 0.6023 |
| $z_2$ | 0.9210 |
| $a_2$ | 0.7153 |

Now, we assume $T=0.25$
1. We find $E$
	- $$
	E = \frac{1}{2}(T-a_2)^2= 0.5(0.25-0.7153)^2=0.1083$$
2. Then, we define the number of iterations, or Epochs, or error threshold of 0.001
	- $$epochs = 1000$$
	- or: $$\epsilon = 0.001$$
3. Define a learning rate, and let's observe how the weights and biases change after first iteration of backward propagation
	- $$\eta = 0.4$$
#### First Iteration
##### Results
| Term  | Value  |
| ----- | ------ |
| $w_2$ | 0.427  |
| $b_2$ | 0.612 |
| $w_1$ | 0.1496 |
| $b_1$ | 0.3959 |
##### $w_2$ Updating
![[Pasted image 20221221170259.png]]

##### $b_2$ Updating
![[Pasted image 20221221170419.png]]
##### $w_1$ updating
![[Pasted image 20221221170522.png]]

##### $b_1$ updating
![[Pasted image 20221221170534.png]]
This concludes 1 epoch

After this, forward propagation is done again, the weights and biases are adjusted again, and this is repeated another 999 times given 1000 epochs.

This is the training method that optimizes the weights and biases of the network.