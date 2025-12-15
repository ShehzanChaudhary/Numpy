#What is Numpy Array

'''A NumPy array (known as ndarray, short for N-dimensional array) is a grid of values, all of the same type, indexed by a tuple of non-negative integers. It is a central data structure in NumPy that allows efficient storage and manipulation of numerical data.
Unlike Python lists, NumPy arrays provide:

Homogeneous data types: All elements have the same type (e.g., all integers, all floats).

Fixed size: The size of a NumPy array is fixed at creation.

Efficient memory layout: Data stored in contiguous blocks of memory.

Multidimensional support: Arrays can be 1D, 2D, 3D, or more.'''

#Creating arrays from list or tuples
import numpy as np

a = np.array([1, 2, 4]) #1D Array
b = np.array([[1, 2], [3, 4]]) #2D Array
c = np.array([(1, 2, 3), (4, 5, 6)]) #2D Array from tuple

print(a)
print(b)
print(c)

#Types of array

#1D Array
oneD = np.array([1, 2, 3])
print(oneD.ndim)

#2D Array
twoD = np.array([[1, 2, 3],
                [4, 5, 6]])
print(twoD.ndim)

#3D Array
threeD = np.array([[[1], [2]], 
                   [[3], 
                    [4]]])
print(threeD.ndim)

#Array properties
arr = np.array([[1, 2, 3], 
                [4, 5, 6]])

print("Array:\n", arr)
print("Number of dimensions:", arr.ndim)  
print("Shape of array:", arr.shape)       
print("Total elements:", arr.size)        
print("Data type:", arr.dtype)            
print("Bytes per element:", arr.itemsize) #8
print("Total bytes:", arr.nbytes)  #itemsize * size

