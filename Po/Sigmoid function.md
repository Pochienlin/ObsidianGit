# Sigmoid function
UID: 202212151758
Tags: #🌱 
Links: [[Introduction to Deep Learning]]

## Overview
A sigmoid function is a mathematical function having a characteristic "S"-shaped curve or sigmoid curve.

A common example of a sigmoid function is the logistic function shown in the first figure and defined by the formula:
$${\displaystyle S(x)={\frac {1}{1+e^{-x}}}={\frac {e^{x}}{e^{x}+1}}=1-S(-x).}$$

In some fields, most notably in the context of artificial neural networks, the term "sigmoid function" is used as an alias for the logistic function.

Special cases of the sigmoid function include the Gompertz curve (used in modeling systems that saturate at large values of x) and the ogee curve (used in the spillway of some dams). Sigmoid functions have domain of all real numbers, with return (response) value commonly monotonically increasing but could be decreasing. Sigmoid functions most often show a return value (y axis) in the range 0 to 1. Another commonly used range is from −1 to 1.

A wide variety of sigmoid functions including the logistic and hyperbolic tangent functions have been used as the activation function of artificial neurons. Sigmoid curves are also common in statistics as cumulative distribution functions (which go from 0 to 1), such as the integrals of the logistic density, the normal density, and Student's t probability density functions. The logistic sigmoid function is invertible, and its inverse is the logit function.

## Definition
A sigmoid function is a bounded, differentiable, real function that is defined for all real input values and has a non-negative derivative at each point and exactly one inflection point. A sigmoid "function" and a sigmoid "curve" refer to the same object.

## Properties
In general, a sigmoid function is monotonic, and has a first derivative which is bell shaped. Conversely, the integral of any continuous, non-negative, bell-shaped function (with one local maximum and no local minimum, unless degenerate) will be sigmoidal. Thus the cumulative distribution functions for many common probability distributions are sigmoidal. One such example is the error function, which is related to the cumulative distribution function of a normal distribution; another is the arctan function, which is related to the cumulative distribution function of a Cauchy distribution.

A sigmoid function is constrained by a pair of horizontal asymptotes as  $$[x\rightarrow \pm \infty].$$A sigmoid function is convex for values less than a particular point, and it is concave for values greater than that point: in many of the examples here, that point is 0.