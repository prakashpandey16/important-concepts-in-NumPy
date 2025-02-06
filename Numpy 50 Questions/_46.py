# 46. Generate a Gaussian-distributed random array

import numpy as np

# Generate a Gaussian-distributed random array with mean 0 and standard deviation 1
arr = np.random.normal(0, 1, 10).reshape(2, 5)

# Print the generated array
print(arr)
