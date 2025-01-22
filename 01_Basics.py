import numpy as np

# # Creating an array using NumPy
# arr1 = np.array([1, 2, 3]) # --> 1D Array/List
# arr2 = np.array([[1, 2, 3], [4, 5, 6]]) # --> 2D Array/List
# print(arr1)
# print(arr2)

# # Printing Dimension of an Array/a List
# arr3 = np.array([[1, 2, 3], [4, 5, 6]])
# print(arr3.ndim) # --> Will print 2
# print(arr3[0][0])

# # Printing Shape of an array eg. 3x3, 2x3
# arr4 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(arr4.shape) # --> Will print (3, 3) i.e. 3x3

# Printing the Datatype of an Array/a List
arr5 = np.array([1, 2, 3])
print(arr5.dtype) # --> This will print int64

arr6 = np.array([1, 2, 3], "int32")
print(arr6.dtype) # --> But, this will print int32