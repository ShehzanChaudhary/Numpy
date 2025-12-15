#Random Module in Numpy
'''The random module in NumPy provides a collection of functions and tools for generating random numbers and performing random sampling operations. It allows the creation of arrays filled with random values drawn from various probability distributions such as uniform, normal (Gaussian), binomial, and others.

These functions are essential for tasks like simulations, probabilistic modeling, randomized algorithms, and data augmentation in machine learning.'''

import numpy as np

# Random integer from 0 to 9
print(np.random.randint(10))

# 1D array of 5 random integers from 0 to 99
print(np.random.randint(0, 100, size=5))

# 2D array of random integers between 10 and 50
print(np.random.randint(10, 50, size=(2, 3)))

#Random float

# Random float between 0.0 and 1.0
print(np.random.rand())

# 1D array of 4 random floats
print(np.random.rand(4))

# 2D array of random floats
print(np.random.rand(2, 3))

# Random from Normal Distribution

# Standard normal distribution (mean = 0, std = 1)
print(np.random.randn(4)) # 1D array of 4 values

# 2D array from standard normal
print(np.random.randn(2, 3))

#Custom Normal Distribution
print(np.random.normal(50, 10, 5))

#Other Distributions

# Uniform distribution between 0 and 1
print(np.random.uniform(0, 1, 5))

# Binomial distribution (n=10, p=0.5)
print(np.random.binomial(n=10, p=0.5, size=5))

# Random Choice (from a list)
choices = ['apple', 'banana', 'cherry']
print(np.random.choice(choices)) #single choice
print(np.random.choice(choices, size=2)) #sample
print(np.random.choice(choices, size=5, replace=True)) #with replacement

#Shuffle and Permutation
arr = np.array([1, 2, 3, 4, 5, 6])
np.random.shuffle(arr) #Shuffles in place
print(arr)

print(np.random.permutation(arr)) #Returns a shuffled copy

#Set Random Seed (for reproducibility)
np.random.seed(42)
print(np.random.rand(3))