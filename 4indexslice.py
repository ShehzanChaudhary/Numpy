#Indexing

'''Array indexing is the method of accessing individual elements of an array using their specific position (index) within the array. In NumPy (or Python), indexing starts from 0, meaning the first element is at index 0, the second at index 1, and so on. In multi-dimensional arrays, indexing is done using a comma-separated list of indices, one for each dimension. Negative indices can also be used to access elements from the end of the array.

'''

#Slicing 

'''Array slicing is the technique of extracting a portion (sub-array) of an array using a range of indices. The slice is defined using the syntax start:stop:step, where:

start is the index where the slice begins (inclusive),

stop is the index where the slice ends (exclusive),

step is the interval between indices.

Slicing allows efficient access and manipulation of specific sections of arrays without copying the entire data.'''

import numpy as np
#1D array indexing
arr1D = np.array([1, 2, 3, 4, 5])

fElement = arr1D[0]
sElement = arr1D[1]
lElement = arr1D[-1] #negative indexing

print("First element: ", fElement)
print("Second element: ", sElement)
print("Last element: ", lElement)

#2D array indexing
arr2D = np.array([[1, 2, 3],
                  [4, 5, 6]])

print(arr2D[0, 1]) # accessing 2
print(arr2D[0][1])
print(arr2D[1, 2]) # accessing 6
print(arr2D[1][2])
print(arr2D[[0, 1], [0, 2]])

#You can use both [row][col] and [row, col] syntax.

#3D array indexing
arr3D = np.array([[[1, 2, 4],
                   [4, 5, 6],
                   [7, 8, 9]]])

print(arr3D[0, 0, 1])
print(arr3D[0, 2, 0])
print(arr3D[0, 1, 1])
#array[depth_index, row_index, column_index]

#Slicing
#Syntax: arr[start:stop:step]

#1D array slicing
slicearr1D = np.array([1, 2, 3, 4, 5])

print(slicearr1D[1:4])
print(slicearr1D[0:4:2])

#2D array slicing
slicearray2D = np.array([[1, 2, 3],
                         [4, 5, 6]])

print(slicearray2D[0]) #first row
print(slicearray2D[1]) #second row
print(slicearray2D[:, 0]) #first column
print(slicearray2D[:, 1]) #second column
print(slicearray2D[:, 2]) #third column
print(slicearray2D[0:2, 1:]) #[[2, 3], [5, 6]]
print(slicearray2D[0, 0:2]) #[1, 2]

#Boolean Indexing
#Useful for filtering elements that meet a condition.

boolarr = np.array([1, 2, 3, 4, 5, 6])

print(boolarr > 3)
print(boolarr[boolarr > 3])

#Fancy Indexing
'''Fancy indexing refers to a powerful way of indexing NumPy arrays using arrays or lists of indices instead of single integer indices or slices. This allows you to access multiple array elements at once by specifying the exact indices you want, in any arbitrary order or pattern.

Unlike basic slicing which returns a view of the array (no copy), fancy indexing always returns a copy of the data.'''

fancyarray = np.array([10, 20, 30, 40, 50])
indices = [1, 3, 4]
print(fancyarray[indices])
#OR
print(fancyarray[[1, 3, 4]])

#Using 2D array
fancy2Darray = np.array([[20, 30, 40],
                         [50, 60, 70]])
print(fancy2Darray[[0, 1], [1, 2]])

#For conditional indexing
#np.where()

whereindices = np.where(fancyarray > 20)
print(whereindices)
print(fancyarray[whereindices])

#Exercise
'''1. Given arr = np.array([5, 10, 15, 20, 25]):

Slice out [10, 15]

Get all values greater than 15

Select the first and last elements using fancy indexing'''

exercise = np.array([5, 10, 15, 20, 25])

print(exercise[1:3])
print(exercise[exercise > 15])
print(exercise[[0, -1]])

'''2. For a 2D array:
a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
Extract middle column [2, 5, 8]

Slice sub-matrix [[2, 3], [5, 6]]'''

exercise2 = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

print(exercise2[:, 1])
print(exercise2[0:2, 1:])
