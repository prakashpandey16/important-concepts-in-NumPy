# 28. Find the nearest value in an array to a given scalar. 
import numpy as np

# Creating a NumPy array
arr = np.array([1, 3, 7, 9, 11, 15, 20])

# Given scalar value
target = 8

# Finding the nearest value
nearest_value = arr[np.abs(arr - target).argmin()]

# Printing the result
print("Original Array:")
print(arr)
print(f"Nearest value to {target} is {nearest_value}")
