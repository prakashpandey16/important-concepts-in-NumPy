# 43. Compute the determinant of a matrix
import numpy as np
matrix = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])

print(matrix)
determinant_of_matrix = np.linalg.det(matrix)
print(determinant_of_matrix)
