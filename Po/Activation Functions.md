# Activation Functions
UID: 202212211715
Tags: #🌱 
Links: [[Deep Learning Fundamentals with Keras]]

----
## 7 types of activation functions
1. Binary step 
2. Linear identity
3. **Log/ [[Sigmoid function]]**
4. **Hyperbolic tangent**
5. **Rectified Linear Unit (ReLU)**
6. Leaky ReLU
7. **SoftMax**

## [[Sigmoid Function]], or Logarithmic functions
![[Pasted image 20221221171645.png]]
- Function is flat in the extremities, resulting in the [[vanishing gradient]] problem
- It is not symmetric around the orgin and only receives and outputs positives
- We can scale the function and translate it to take in and dispense negatives as well, similar to the next activation function.

## Hyperbolic tangent (TanH function)
![[Pasted image 20221221171834.png]]
- Scaled Sigmoid 
- Symmetry around origin
- Still encounters the [[vanishing gradient]] problem

## ReLU – Rectified Linear Unit
Most popular today. Typically only used in hidden layers.
![[Pasted image 20221221171951.png]]
- Non-linear
- Doesn't activate all neurons at the same time
	- Only a few are activated, making the network sparse and therefore efficient
- Overcomes the vanishing gradient problem
## SoftMax
![[Pasted image 20221221172208.png]]
- Also a type of [[Sigmoid function]]
- Handy for classification problems, where we are trying to classify a bunch of inputs
