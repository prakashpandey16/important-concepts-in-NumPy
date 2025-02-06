# 37. Convert a boolean array to an integer array.
import numpy as np  # Importing NumPy library

# Creating a NumPy array with values from 1 to 10
arr = np.arange(1, 11)

# Creating a boolean array where True corresponds to even numbers and False to odd
boolean_arr = arr % 2 == 0

# Printing the boolean array (True for even numbers, False for odd)
print("Boolean Array:")
print(boolean_arr)

# Converting the boolean array to an integer array (True -> 1, False -> 0)
integer_arr = boolean_arr.astype(int)

# Printing the integer array (1 for True, 0 for False)
print("\nInteger Array:")
print(integer_arr)
