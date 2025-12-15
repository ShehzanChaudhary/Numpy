import numpy as np

#Save an array to a binary file
arr = np.array([[1, 2, 3], [4, 5, 6]])
np.save('my_array.npy', arr)

#Load it back
loaded_arr = np.load('my_array.npy')
print(loaded_arr)
#Efficient and preserves data types and structure.

#Save and Load Multiple Arrays
#Save multiple arrays to a .npz archive

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

np.savez('arrays_archive.npz', arr1=a, arr2=b)
#Load and access

data = np.load('arrays_archive.npz')
print(data['arr1'])  # [1 2 3]
print(data['arr2'])  # [4 5 6]

#Saving to .txt or .csv Files
#Save array as text

arr = np.array([[1.5, 2.3], [3.1, 4.8]])
np.savetxt('array.txt', arr)

#Save with formatting

np.savetxt('formatted.txt', arr, fmt='%.2f', delimiter=',')

# Load from .txt or .csv
loaded = np.loadtxt('formatted.txt', delimiter=',')
print(loaded)
#
# Using genfromtxt() for Incomplete/Dirty Data

# If file has missing values
data = np.genfromtxt('data_with_missing.csv', delimiter=',')