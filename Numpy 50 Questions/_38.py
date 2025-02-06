# 38. Get unique elements from an array
import numpy as np  # Importing NumPy library

# Creating a NumPy array with some repeated elements
arr = np.array([1, 2, 5, 6, 2, 4, 4, 6, 7, 8, 7])

# Printing the original array
print("Original Array:")
print(arr)

# Using np.unique() to get the unique elements from the array
arr_unique = np.unique(arr)

# Printing the unique elements
print("\nUnique Elements:")
print(arr_unique)
