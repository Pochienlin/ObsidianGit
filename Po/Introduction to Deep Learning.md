# Introduction to Deep Learning
UID: 202212151741
Tags: #🌱 
Links: [[Artificial Intelligence (AI)]] [[Big Data]] [[Deep Learning Fundamentals with Keras]]

## Learning Objectives
 In this lesson you will learn about:

-   Exciting applications of deep learning and why it is really rewarding to learn how to leverage deep learning skills.
-   Neural networks and how most of the deep learning algorithms are inspired by the way brain functions and the neurons process data.
-   How neural networks feed data forward through the network.

## Applications
- Deep fake videos
	- Syncing an input audio to video
	- Example shows a clip where he made Barack Obama appear as if he was saying something in the video that is actually not the video's original audio
- Coloring grayscale photos

## Mathematical set up for Forward Propagation
- Neural Networks are divided into input, output and hidden layers 
![[Pasted image 20221215175735.png]]
- [[Forward Propagation]] is the process through which data passes through layers of neurons in a neural network from the input layer all the way to the output layer
	- In one neuron, the inputs pass through connections with specific weights, then the neuron processes the information and outputs a weighted sum 
	- A constant is added to the sum, known as the bias
	- The output is then mapped to a non-linear space using an activation function 
		- Activation function here uses the [[Sigmoid function]] 
	- Neural networks without an activation function are essentially linear regression models 
	- Output is determined by the weights and biases of the network 
![[Pasted image 20221215180457.png]]
![[Pasted image 20221215180525.png]]
[[Forward Propagation (Lab)]]
### Optimising biases
