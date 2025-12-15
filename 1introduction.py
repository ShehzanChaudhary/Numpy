#What is Numpy

'''NumPy (short for Numerical Python) is an open-source Python library that provides support for large, multi-dimensional arrays and matrices, along with a collection of high-level mathematical functions to operate on these arrays efficiently.'''

#Why Numpy?

'''Python is a versatile language but originally lacked efficient tools for numerical computation and handling large data arrays. Python lists and loops are flexible but slow for numerical tasks. NumPy fills this gap by providing:

Efficient storage: NumPy arrays consume less memory than Python lists. [Python lists are very flexible; they can hold items of different types (ints, strings, objects) in the same list. But this flexibility comes at a cost — each element is a full Python object, with metadata, pointers, and overhead.

NumPy arrays are homogeneous, meaning all elements are of the same data type (e.g., all integers or all floats). This lets NumPy store data in a continuous block of memory.

Because of this, NumPy arrays require much less memory than lists of the same size.]


Fast computation: Written in C, it offers optimized performance for numerical operations. [NumPy is implemented in C and Cython under the hood.

Python itself is an interpreted language and slower for loops and numerical calculations.

NumPy offloads heavy computations to efficient C code, which runs much faster than pure Python.

Additionally, NumPy uses vectorized operations that apply functions on entire arrays simultaneously, avoiding slow Python loops.]

Convenient syntax: Vectorized operations (element-wise operations on arrays) make code concise and readable. [In Python lists, to add two lists element-wise, you need loops or comprehensions.

NumPy lets you write mathematical operations directly on arrays; it applies the operation element-wise automatically.]

Foundation for scientific computing: Many scientific libraries like SciPy, Pandas, Matplotlib, TensorFlow, and scikit-learn build on top of NumPy. [Because of its powerful, fast array processing capabilities, NumPy is the core building block for many other popular scientific and data science libraries.

SciPy extends NumPy with additional scientific computing algorithms (optimization, integration, interpolation).

Pandas uses NumPy arrays internally to handle tabular data efficiently.

Matplotlib relies on NumPy arrays for plotting numerical data.

TensorFlow and PyTorch build upon concepts similar to NumPy arrays for deep learning tensor operations.

scikit-learn depends on NumPy arrays for efficient machine learning algorithms.]'''

#Installing Numpy
'''pip install numpy'''

#Importing Numpy
'''import numpy as np'''

#Basic example
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Element-wise addition
print(a + b) #[5, 7, 9]

#Exercise
#1. Create a list: [1, 2, 3, 4, 5] and convert it to a NumPy array.
list1 = [1, 2, 3, 4, 5]
numparray = np.array(list1)
print(numparray)

#2. Print the type of the array using type().
print(type(numparray))

#3. Add 10 to each element of the array in one line (without loop).
print(numparray + 10)

