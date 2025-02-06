# 15. Multiply a 5x3 matrix by a 3x2 matrix (matrix multiplication
import numpy as np
matrix_1 = np.array([[1,2,3],
                    [4,5,6],
                    [7,8,9],
                    [9,10,11],
                    [13,14,15]])

matrix_2 = np.array([[1,2],
                     [4,5],
                     [6,7]])

print(matrix_1)
print(matrix_2)

crr = np.dot(matrix_1,matrix_2)
print(crr)
# 5x3
# 3x2