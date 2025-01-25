import numpy as np

# Boolean Masking
arr = np.genfromtxt("data.txt", delimiter=",")
arr = arr.astype("int32")

# Checking if the value are greater than 5
# print(arr > 5) # --> Prints true if the element is > 5 else prints false

# Printing only the values which greater than 5
# print(arr[arr > 5]) # --> Prints only those values which greater than 5



# Advanced Indexing
arr2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(arr2[[1, 2, 8]]) # --> The values passed are the indexes. Hence it will print [2 3 9]

arr3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr3[2, [2, 0, 1]]) # --> Will print [9 7 8]
