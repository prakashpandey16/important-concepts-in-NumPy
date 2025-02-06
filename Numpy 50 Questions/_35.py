# 35. Find the positions of elements that satisfy a given condition
import numpy as np  # Importing NumPy library

# Creating a 1D NumPy array
arr = np.array([1, 3, 4, 2, 5, 8, 10, 34, 56, 90])

# Finding indices of elements where the value is greater than 10
arr_with_conditions = np.where(arr > 10)

# Printing the indices of elements satisfying the condition
print("Indices of elements greater than 10:")
print(arr_with_conditions)
