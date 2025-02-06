# 42. Compute the dot product of two random vectors.
import numpy as np  # Importing the NumPy library

# Defining two NumPy arrays (vectors)
arr = np.array([1, 2, 4, 3, 10, 14, 34, 23])
brr = np.array([8, 9, 3, 5, 4, 3, 5, 38])

# Element-wise addition of two vectors
sum_vector = arr + brr  # You can also use np.add(arr, brr)

# Printing the result
print(sum_vector)
