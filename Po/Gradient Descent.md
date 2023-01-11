# Gradient Descent
UID: 202212211550
Tags: #🌱 
Links: [[Deep Learning Fundamentals with Keras]]

----
## Overview
> [!abstract]
> Gradient descent is an algorithm used to find the minimum of a function, often used in the context of neural network training. 
> - The algorithm involves taking steps towards the minimum, using the gradient of the function at the current point to determine the direction of the step and a learning rate to control the magnitude of the step. 
> - The algorithm iteratively repeats this process until the minimum is reached or a value very close to the minimum is achieved. 
> 
> The learning rate must be carefully chosen to avoid overshooting the minimum or taking too long to reach it. 
> - In the context of neural networks, the cost or loss function is used to determine the optimal values for the weights and biases in the network to minimize the error between the predicted and target values.
![[Pasted image 20221221153637.png]]
![[Pasted image 20221221153659.png]]
- This Cost Function has a global minimum – simple but allows for some maximization
> [!question]
> How to optimize the value for w?
### Example: Opitimizing gradient w
Given the following Cost Function:
$$
Z=wX,
$$
 where
$$
J(w) = \frac{1}{2m}\sum_{i=1}^{m}{(z_i-wx_i)^2}
$$
- Find the gradient of the current point
- Shift to the next point, using the Learning Rate $\eta$  as the guage for how big a step to take 
	- we take a step of $w_{i-1} ± \eta \frac{\delta J}{\delta w}$ to  the next step, $w_i$ 
	- If the gradient "descends", we keep minusing $\eta \frac{\delta J}{\delta w}$ 
	- If the gradient starts "ascending", we go back by adding instead of minusing $\eta \frac{\delta J}{\delta w}$ 
- The iterations end when we hit the minimum, or a value within a predefined threshold
> [!note] A note on Learning Rate
> - A big learning rate can seem more efficient, but risk taking steps that are too big. The value may not converge if this is the case and it may take more iterations to reach the minimum.
> - Conversely, too small a learning rate can take way too long for the algorithm to find the minimum.
