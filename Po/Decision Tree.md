# Decision Tree
UID: 202209191038
Tags: #🌱 
Links: [[Big Data and Business Model]] [[Techniques and Processes of Bigdata]] [[Big Data]] [[Predictive modelling]]

----
## Performance
| Performance | Evaluation |
| ----------- | ---------- |
| 90%         | Excellent  |
| 80%         | Good       |
| 70%         | Useful     |
| <70%        | Unusable   |

## Overview
A Decision Tree is an algorithm used for supervised learning problems such as classification or regression. A decision tree or a classification tree is a tree in which each internal (nonleaf) node is labeled with an input feature. The arcs coming from a node labeled with a feature are labeled with each of the possible values of the feature. 

Each leaf of the tree is labeled with a class or a probability distribution over the classes.

Related concepts:
- [[Binary tree]]
- [[Big Data]]
- [[Predictive Modelling]]
- [[Probability]]

## Types of Decision Trees
-   **Classification tree** − when the response is a nominal variable, for example if an email is spam or not.
-   **Regression tree** − when the predicted outcome can be considered a real number (e.g. the salary of a worker).

## Advantages and disadvatages
### Advantages
1. Shows most important variable on the top of the tree
2. Shows important, relevant variables only
3. Easy to understand
4. Directly convertable to rules

#### Other benefits
- Easy implementation: can draw insights from any sufficiently big dataset
- Benefits other existing methods such as 
	- Regression
	- k means clustering
	- [[Association Rule (Bigdata)]]

### Disadvantages
- Instability: tree can be completely different with introduction of a small group of new input data
- Overfitting: tree can theoretically go as deep as it needs to fit all data sets, but in the process of doing so create so many rules that they are no longer generalisable or useful

## Mitigating disadvantages
1. Using Ensemble methods to overcome instability
	- *Bagging decision trees* − These trees are used to build multiple decision trees by repeatedly resampling training data with replacement, and voting the trees for a consensus prediction. This algorithm has been called random forest.
	- *Boosting decision trees* − Gradient boosting combines weak learners; in this case, decision trees into a single strong learner, in an iterative fashion. It fits a weak tree to the data and iteratively keeps fitting weak learners in order to correct the error of the previous model.
2. Setting predefined maximum depth to overcome overfitting

## Example
![[Pasted image 20220921113724.png]]