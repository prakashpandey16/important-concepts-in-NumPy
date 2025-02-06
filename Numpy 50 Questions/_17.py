# 17. Create a 5x5 matrix with row values ranging from 0 to 4.
import numpy as np

# Method 1: Using list multiplication (less efficient)
# This creates a list by repeating [0,1,2,3,4] five times and then reshapes it into a 5x5 matrix.
matrix = np.array([0,1,2,3,4]*5).reshape(5,5)
print("Matrix using list multiplication and reshape:")
print(matrix)
print("\n")

# Method 2: Using np.tile() (more efficient)
# np.arange(5) creates [0,1,2,3,4] 
# np.tile(..., (5,1)) repeats it along rows to create a 5x5 matrix
matrix = np.tile(np.arange(5), (5,1))
print("Matrix using np.tile:")
print(matrix)
