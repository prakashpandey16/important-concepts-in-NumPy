# 16. Extract the integer part of a random array of positive numbers.
import numpy as np
arr = np.random.random(10)*100
int_part1 = np.floor(arr)
int_part2 = arr.astype(int)
print(int_part1)
print(int_part2)



