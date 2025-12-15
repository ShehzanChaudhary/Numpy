#Linear Algerba in Numpy
'''The numpy.linalg module in NumPy provides a set of linear algebra functions designed to perform standard matrix and vector operations efficiently. It includes routines for solving linear systems, computing matrix decompositions, eigenvalues, determinants, inverses, and norms.

This module is built on top of optimized numerical libraries like LAPACK, allowing fast and reliable computation for numerical linear algebra tasks.'''

import numpy as np

#Dot Product / Matrix Multiplication
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

dotProduct = np.dot(a, b)
print(dotProduct)

#Matrices
c = np.array([[1, 2],
              [3, 4]])
d = np.array([[5, 6],
              [7, 8]])
print(np.dot(c, d)) #Matrix Multiplication
print(c @ d) #Same

# Matrix Transpose
e = np.array([[1, 2],
              [3, 4]])
print(np.transpose(e)) #Transpose (Rows and colums are interhchanged)
print(e.T) #Same

#Identity Matrix
I = np.eye(3)
print(I) # A matrix where all the diagnoal elements are 1 and all other elements are 0

#Inverse of a Matrix
f = np.array([[1, 2],
              [3, 4]])
inverse = np.linalg.inv(f) #A⁻¹ = (1/det(A)) * adj(A)
print(inverse)
#Imp: Only square and non-singular matrices have an inverse.

#Determinant
g = np.array([[1, 2],
              [3, 4]])
det = np.linalg.det(g)
print(det)

#Eigenvalues and Eigenvectors
h = np.array([[1, 2],
              [3, 4]])
eigen_val, eigen_vec = np.linalg.eig(h)
print("Eigen Values: ", eigen_val)
print('Eigen Vector: ', eigen_vec)

#Solving Linear Equations
#Solve system of equations AX=B

j = np.array([[2, 1],
              [1, 3]])
k = np.array([8, 13])

l = np.linalg.solve(j, k)
print(l)

#Norm of a Vector or Matrix

v = np.array([3, 4])  
print(np.linalg.norm(v))  # Output: 5.0 (Euclidean norm or L2 norm)

# √3^2+4^2 = √9+16 = √25 = 5.0 

# Frobenius norm of a matrix
A = np.array([[1, 2],
              [3, 4]])
print(np.linalg.norm(A))

#√1^2+2^2+3^2+4^2 = √30 = 5.477