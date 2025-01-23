import numpy as np

# Operations on elements of a single array
a = np.array([1, 2, 3, 4])
# a = a + 2 # --> Adds 2 to every element
# a = a - 2 # --> Subtracts 2 from every element
# a = a * 2 # --> Multiplies 2 to every element
# a = a / 2 # --> Divides 2 from every element
a = a ** 2 # --> Each Element raise to 2 (square)
print(a)

# Operations on 2 different arrays
arr1 = np.array([1, 4, 9, 16])
arr2 = np.array([1, 2, 3, 4])
add = arr1 + arr2
sub = arr1 - arr2
mul = arr1 * arr2
div = arr1 / arr2
print(add)
print(sub)
print(mul)
print(div)
