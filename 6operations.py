#Basic arithmetic ops
import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a ** 2)
print(a // b)

#Universal functions
'''Universal functions, or ufuncs, are fast, element-wise functions provided by NumPy that operate on arrays element-by-element. These functions perform vectorized operations, meaning they can apply a mathematical operation simultaneously across all elements of one or more arrays without explicit Python loops.'''

#sqrt()
arr = np.array([1, 4, 9, 16, 25])
print(np.sqrt(arr))

#exp()
print(np.exp(arr))

#log()
print(np.log(arr))

#abs()
print(np.abs(arr))

#negative()
print(np.negative(arr))

#ceil()
print(np.ceil(arr))

#floor()
print(np.floor(arr))

#round()
print(np.round(arr))

#Aggregation functions
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

print(np.sum(arr))          # 21 (sum of all elements)
print(np.mean(arr))         # 3.5 (average)
print(np.std(arr))          # Standard deviation
print(np.min(arr))          # 1
print(np.max(arr))          # 6
print(np.median(arr))       # 3.5
print(np.prod(arr))         # Product of all elements: 720
print(np.cumsum(arr))       # Cumulative Sum
print(np.cumprod(arr))      # Cumulative Prod

#Rounding off
rounds = np.array([1.5267, 2.17829, 3.7373])
print(np.round(rounds))
print(np.floor(rounds))
print(np.ceil(rounds))
print(np.trunc(rounds))

#Axis-wise Operations
'''You can specify axis parameter to perform operations across rows or columns:

axis=0 — down the rows (operate on each column)

axis=1 — across the columns (operate on each row)'''

arr = np.array([[1, 2, 3],
                [4, 5, 6]])

print(np.sum(arr, axis=0))  # Sum column-wise: [5 7 9]
print(np.sum(arr, axis=1))  # Sum row-wise: [ 6 15]
print(np.mean(arr, axis=0)) # Mean column-wise: [2.5 3.5 4.5]
print(np.max(arr, axis=1))  # Max row-wise: [3 6]

#Broadcasting 
'''Broadcasting is a powerful mechanism in NumPy that allows operations between arrays of different shapes in a vectorized way, without the need for explicit looping.'''

'''Broadcasting describes how NumPy treats arrays with different shapes during arithmetic operations. The smaller array is “broadcast” across the larger array so that they have compatible shapes.'''

''' Rules of Broadcasting
When operating on two arrays, NumPy compares their shapes element-wise from right to left:

If the dimensions are equal, they are compatible.

If one of the dimensions is 1, it can be broadcast to match the other.

If the dimensions are not equal and neither is 1, an error is thrown.'''

#Example 1: Add scalar to array
a = np.array([1, 2, 3])
b = 5
print(a + b)

#Example 2: Add 2D and 1D array
a = np.array([[1, 2, 3],
             [4, 5, 6]])
b = np.array([7, 8, 9])
print(a + b)

# Example 3: Broadcasting in 2D
a = np.array([[1], [2], [3]])  # shape (3,1)
b = np.array([10, 20, 30])     # shape (3,)

# This will raise an error unless reshaped properly
# Fix by reshaping b
b = b.reshape(1, 3)
print(b)

print(a + b)
