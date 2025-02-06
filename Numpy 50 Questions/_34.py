# 34. Create a 2D array containing repeated elements
import numpy as np  # Importing NumPy library

# Creating a 2D NumPy array with repeated elements
# np.tile(array, (rows, columns)) repeats the given array in the specified shape.
arr_with_repeated_ele = np.tile([1, 2, 3, 4], (4, 1))  # Repeats row-wise

# Printing the 2D array
print("2D Array with Repeated Elements:")
print(arr_with_repeated_ele)
