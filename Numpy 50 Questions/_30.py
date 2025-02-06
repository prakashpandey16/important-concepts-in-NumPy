# 30. Get the n largest values from an array.
import numpy as np

# Creating a NumPy array
arr = np.array([1, 93, 23, 39, 11, 15, 20])

# Finding the 2nd largest value
# Sorting the array in ascending order and selecting the second last value
largest_value = np.sort(arr)[-2]

# Printing the 2nd largest value
print("The 2nd largest value is:", largest_value)

# Finding the last 3 largest values
n = 3  # Number of largest values to extract

# Sorting the array and selecting the last 'n' values (which are the largest)
last_three_largest_values = np.sort(arr)[-n:]

# Printing the last 3 largest values
print("The last 3 largest values are:", last_three_largest_values)
