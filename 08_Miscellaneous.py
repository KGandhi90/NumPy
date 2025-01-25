import numpy as np

# Load Data from a File
arr = np.genfromtxt('data.txt', delimiter=',')
print(arr.astype("int32")) # --> The default type will be float
# The astype() just makes a copy
print(arr) # --> So this will print the original array