# Kolmogorov-Smirnov Method
UID: 202204191539
Tags: #🌱 
Links: [[Spreadsheet modeling]] [[ Statistics]]

## Steps
1. Distribution functions are usually defined by 4 parameters: Max, min, mean, StDev – compute these parameters from the raw data
2. Sort the raw data in ascending order (so that the x axis is in increasing order)
	1. Use small(array, k) where k is the index number.
3. Compute the cumulative relative frequency (CRF) of the raw data
	1. In discrete data, the same data may occur more than once: find freq for a value, cumulative freq, then using that we can find the CRF
	2. For continuous, we can assume it does not repeat. 
		1. Find the total count: n=50 for e.g.
		2. Divide by each index number to find the empirical cumulative frequency (each index increases by 0.02 in n=50)
	3. Go to insert > X-Y scatter to plot the data against the empirical
4. Compute cumulative relative frequency of a known distribution using raw data + initial arbitrary input parameters
	1. In **descrete** data, use uniform binomial, poisson
		1. Uniform CRF =(x - min)/(max-min) where x is the data point
		2. Binomial 
			1. BINOMDIST(number_s, trials, probability_s, cumulative)
			2. BINOMDIST(x, trials, probability_s, TRUE)
		3. Poisson
			1. POISSON(x, mean, cumulative)
			2. POISSON(x, mean, TRUE)
	2. For **continuous**, use uniform, exponential or normal
		1. Uniform CRF = (x - min)/(max-min) where x is the data point
		2. Norm
			1. NORMDIST(x, mean, stdev, cumulative)
			2. NORMDIST(x, mean, stdev, TRUE
		3. Exponential
			1. EXPONDIST(X, 1/mean, cumulative)
			2. EXPONDIST(X, 1/mean, TRUE)
5. 