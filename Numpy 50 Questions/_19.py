# 19. Create a random vector of size 10 and replace max value with 0.
import numpy as np

# Creating a random vector of size 10
arr = np.array([1,19,2,4,5,3,2,18,19,10])
print("Original array:")
print(arr)

# Finding the maximum value in the array
max_ele = np.max(arr)
print("Maximum element:", max_ele)

# Replacing all occurrences of the maximum value with 0 using NumPy indexing
# This avoids using loops and makes the operation more efficient
arr[arr == max_ele] = 0

print("Modified array:")
print(arr)

