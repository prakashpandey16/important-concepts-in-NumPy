# 27. Remove all occurrences of a specific value from an array
import numpy as np

# Creating a NumPy array
arr = np.array([1, 2, 3, 4, 4, 4, 5, 6, 7])

# Printing the original array
print("Original Array:")
print(arr)

# Removing all occurrences of the value '4'
value_to_remove = 4
arr_after_remove = arr[arr != value_to_remove]  # Keep only elements not equal to 4

# Printing the modified array
print("Array After Removing All Occurrences of 4:")
print(arr_after_remove)
