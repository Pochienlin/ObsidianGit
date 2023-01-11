# Vanishing Gradient
UID: 202212211708
Tags: #🌱 
Links: [[Deep Learning Fundamentals with Keras]]

----
## Overview
> [!abstract]
> The vanishing gradient problem is a problem with the sigmoid activation function that can occur during neural network training. 
> - The problem arises because the intermediate values in the network are between 0 and 1 when using the sigmoid function, which can result in the gradients becoming smaller and smaller as they are multiplied together during backpropagation. 
> - This can cause the neurons in the earlier layers of the network to learn very slowly compared to the neurons in the later layers, resulting in a slow training process and compromised prediction accuracy. 
> - To overcome this problem, other activation functions that are not prone to the vanishing gradient problem are typically used in the hidden layers of neural networks.
## A serious issue with the [[Sigmoid Function]] as an Activation Function
Using the Sigmoid Function, any weights and biases that survive the iteration has to be $$0≤w_i,b_i≤1$$
Afterwards, [[Backpropagation]] is applied. This further compresses both $w_i$ and $b_i$

The result after more epochs is that the weights and biases $\rightarrow 0$

This means that:
1. The layers in the front learn very slowly compared to the layers in the back
2. Training process will take too long
3. Prediction accuracy is compromised

This is known as the vanishing gradient problem. The more layers there are, the stronger the effect. For more layered networks, other forms of [[Activation Functions]] are required.