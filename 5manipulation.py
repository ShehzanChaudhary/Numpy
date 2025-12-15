#Array Manipulation
'''Array manipulation refers to the set of operations used to change the structure, shape, or content of an array without necessarily changing its data. These operations allow users to reshape, join, split, rearrange, or transform arrays to fit a particular computational need or algorithm.

It is essential in data preprocessing, scientific computing, machine learning, and numerical simulations.'''

import numpy as np

#reshape()
arr = np.arange(6)
print(arr)
print(arr.reshape((2, 3)))

#Imp:  The new shape must be compatible with the total number of elements.

#flatten() and ravel()
'''Both convert multi-dimensional arrays to 1D.

flatten() returns a copy.

ravel() returns a view (changes affect the original array).'''

arr2d = np.array([[1, 2, 3],
                  [4, 5, 6]])

print(arr2d)
print(arr2d.flatten())
print(arr2d.ravel())

arr2d = np.array([[1, 2], [3, 4]])

flat = arr2d.flatten()
ravel = arr2d.ravel()

flat[0] = 100
ravel[1] = 200

print(arr2d)
# Output:
# [[1 200]
#  [3 4]]
#Notice that modifying ravel changes the original array, but flatten does not.

#transpose()
#Switch rows and columns (swap axes).
arrT = np.array([[1, 2, 3],
                  [4, 5, 6]])
print(arrT.transpose()) #OR 
print(arrT.T)

#Concatenate()
#Join two or more arrays along an axis.

a = np.array([[1, 2, 5], [3, 4, 9]])
b = np.array([[5, 6, 7], [8, 9, 10]])

print(np.concatenate((a, b), axis=1))

#stack()
#Join arrays along a new axis.

a = np.array([1, 2])
b = np.array([3, 4])

print(np.stack((a, b), axis=0))
print(np.stack((a, b), axis=1))

#split()

a = np.array([1, 2, 3, 4, 5, 6])
print(np.split(a, 3))

#You can also split 2D arrays horizontally or vertically:

arr2d = np.arange(16).reshape(4,4)

print(np.hsplit(arr2d, 2))  
print(np.vsplit(arr2d, 2))

# Adding/Removing Dimensions
# np.newaxis or reshape for adding a dimension:
a = np.array([1, 2, 3])
print(a.shape)         # (3,)

a2 = a[:, np.newaxis]
print(a2.shape)        # (3, 1)

#squeeze() – Remove extra dimensions

a = np.array([[[1], [2], [3]]])
print(a.shape)           # (1, 3, 1)

a_squeezed = np.squeeze(a)
print(a_squeezed.shape)  # (3,)


#Exercise
#1. Create a 1D array with 12 elements and reshape it into (3,4).

first = np.arange(12)
print(first)
second = first.reshape((3, 4))
print(second)

#2. Flatten that 2D array back to 1D.
flatten = second.flatten()
print(flatten)

#3. Create two arrays and concatenate them vertically and horizontally.
third = np.array([1, 2, 3])
fourth = np.array([4, 5, 6])

vertical = np.concatenate((third, fourth), axis=0)
horizontal = np.stack((third, fourth), axis=1)

print(vertical)
print(horizontal)

#4. Split an array of 10 elements into 5 parts.
fifth = np.arange(10)
print(fifth)
print(np.split(fifth, 5))



