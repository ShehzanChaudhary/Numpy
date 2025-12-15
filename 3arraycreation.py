#np.zeros
'''Create an array filled with zeros'''
import numpy as np
zeros = np.zeros((2, 4))
print(zeros)

#np.ones
'''Create an array filled with ones'''
ones = np.ones((2, 3))
print(ones)

#np.empty
'''Creates an array without initializing the values (garbage values; faster for large arrays).'''
empty = np.empty((2, 4))
print(empty)

#np.full
full = np.full((2, 4), 9)
print(full)

#np.eye
'''Creates an identity matrix (1s on the diagonal, 0s elsewhere).'''
eye = np.eye(3)
print(eye)

#np.arange
'''Returns evenly spaced values within a given interval.'''
arange = np.arange(0, 22, 3)
print(arange)

#np.linspace
linspace = np.linspace(0, 10, 4)
print(linspace)

#Exercise
#1. Create a 4×4 matrix filled with the number 9.
matrix = np.full((4, 4), 9)
print(matrix)

#2. Create an array of 7 evenly spaced numbers between 10 and 50.
espace = np.linspace(10, 50, 7)
print(espace)