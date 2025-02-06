# 29. Replace all values greater than a given number in an array with that number
import numpy as np

# Creating a NumPy array
arr = np.array([1, 3, 7, 9, 11, 15, 20])

# Printing the original array
print("Original Array:")
print(arr)

# Replacing all values greater than 10 with 10
# np.where(condition, value_if_true, value_if_false)
replaced_arr = np.where(arr > 10, 10, arr)

# Printing the modified array
print("Array After Replacing Values Greater Than 10 with 10:")
print(replaced_arr)
