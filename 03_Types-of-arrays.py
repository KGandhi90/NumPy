import numpy as np

# All 0s matrix
a = np.zeros((3, 3))
print(a)

# All 1s matrix
b = np.ones((2, 2), dtype="int32") # --> Can also have datatypes
print(b)

# Any other number
c = np.full((4, 4), 23, dtype="int32")
print(c)

# Any other number (full-like)
d = np.full_like(a, 4) # --> This method prints all the elements as a float
# Same as above
# d = np.full(a.shape, 4) # --> This method prints all the elements as an integer
print(d)

# Random Decimal Numbers
e = np.random.rand(4, 2, 3)
print(e)

# Random Integer Values
f = np.random.randint(7,9, size=(3,3)) # --> For random integers the last number is exclusive here 9 will be excluded
print(f)

# Identity Matrix (Diagonals are 1s)
g = np.identity(4) # --> This will always be a square matrix which means no. of rows and columns are equal
print(g)

# Repeat an array
h = np.array([1, 2, 3])
r1 = np.repeat(h, 3, 0) # --> Each element gets repeated 3 times even if the element is an array
print(r1)

'''
Practice Question
1 1 1 1 1
1 0 0 0 1
1 0 9 0 1
1 0 0 0 1 
1 1 1 1 1
'''

arr = np.ones((5, 5), dtype="int32")
arr[1:-1, 1:-1] = 0
arr[2:-2, 2:-2] = 9
print(arr)

# Copying an array
i = np.array([1, 2, 3])
j = i
j[0] = 10
print(j)
print(i) # --> This array will also get updated

# So to avoid this
k = np.array([1, 2, 3])
l = k.copy()
l[0] = 100
print(l)
print(k)
