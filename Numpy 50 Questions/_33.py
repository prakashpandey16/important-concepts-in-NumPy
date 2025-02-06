# 33. Split a NumPy array into multiple sub-arrays.
import numpy as np  # Importing the NumPy library

# Creating a 1D NumPy array
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# Printing the original array
print("Original Array:")
print(arr)

# Splitting the array into 3 equal sub-arrays
# Since the array has 12 elements, each sub-array will contain 4 elements
sub_arrays = np.split(arr, 3)

# Printing the split arrays
print("\nSplit Arrays:")
print(sub_arrays)

# Creating another 1D NumPy array with 13 elements
brr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 11, 12])

# Using np.array_split() to split the array into 5 parts
# Unlike np.split(), np.array_split() can handle cases where the array 
# length is not perfectly divisible by the number of splits.
print("\nUsing np.array_split():")
print(np.array_split(brr, 5))
