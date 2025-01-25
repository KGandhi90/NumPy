import numpy as np

before = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# print(before)

after = before.reshape((4 ,2))
# print(after)

# Vertically Stacking Vectors
# Note : The size of both the arrays should be same
v1 = np.array([1, 2, 3, 4])
v2 = np.array([5, 6, 7, 8])

print(np.vstack([v1, v2, v1, v2])) # --> Keeps adding the arrays at the end. Here 4 sub-arrays will be printed in one main array

# Horizontally Stacking Vectors
h1 = np.array([1, 2, 3, 4])
h2 = np.array([5, 6, 7, 8])

print(np.hstack([h1, h2, h2])) # --> All the elements will added into one single array without any sub-arrays