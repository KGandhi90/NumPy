import numpy as np

# Linear Algebra / Operations on Matrices

# Multiplication
a = np.ones((2,3))
b = np.full((3,2), 2)
mul = np.matmul(a, b)
print(mul)

# Transpose
arr = np.array([[1,2,3], [4,5,6], [7,8,9]])
transpose = np.transpose(arr)
transpose = arr.transpose() # --> Same as above
print(transpose)

# Determinant
arr2 = np.identity(3)
determinant = np.linalg.det(arr2)
print(determinant)

# Inverse
arr3 = np.array([[1, 5, 7], [9, 2, 8], [3, 6, 4]]) # --> Make sure that the matrix is not a Singular Matrix
inverse = np.linalg.inv(arr3)
print(inverse)
