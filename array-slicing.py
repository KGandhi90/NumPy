import numpy as np

# a = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])

# # To get a specific element -> [row, col]
# print(a[1, 5]) # --> Prints 13
# print(a[1, -2]) # --> This also prints 13

# # Get a specific row
# print(a[0, : ])

# # Get a specific column
# print(a[:, 2])

# # Stepping over elements [start:stop:stepsize]
# print(a[0, 1:-1:2])

# # Replacing the element
# a[0, 3] = 10
# a[:, 2] = 20 # --> Whole column 3 will become 20
# a[:, 2] = [20, 21]
# a[1, :] = 11 # --> Whole 2nd row will become 11 
# a[1, :] = [7, 6, 5, 4, 3, 2, 1]
# print(a)

# 3D Example
b = np.array([[[1,2], [3, 4]], [[5, 6], [7, 8]]])
print(b)

# Get specific element (work outside in)
print(b[1, 0, 0])

# Replacing an element
b[:, 1, :] = [[9, 9], [8, 8]]
print(b)