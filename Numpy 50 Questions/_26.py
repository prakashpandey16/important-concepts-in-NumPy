# 26. Find common values between two arrays.
import numpy as np

# Creating two NumPy arrays
arr = np.array([1, 4, 5, 3, 2, 4, 10])
brr = np.array([3, 4, 5, 10, 13, 24])

# Finding common values between two arrays using np.intersect1d
common_arr = np.intersect1d(arr, brr)

# Printing the common values
print("Common values between the two arrays:")
print(common_arr)
