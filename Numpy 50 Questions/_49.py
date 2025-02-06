# 49. Save and load a NumPy array to/from a file.

import numpy as np

# Create a NumPy array
arr = np.arange(0, 100).reshape(5, 20)
print("Original Array:")
print(arr)

# Save the NumPy array to a binary file using np.save()
np.save('array_data.npy', arr)

# Load the NumPy array from the binary file using np.load()
loaded_arr = np.load('array_data.npy')

# Print the loaded array to confirm it matches the original
print("\nLoaded Array:")
print(loaded_arr)
