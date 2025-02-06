# 44. Compute the eigenvalues and eigenvectors of a matrix
import numpy as np  # Importing the NumPy library

# Define a 3x3 matrix using np.array instead of np.matrix (since np.matrix is deprecated)
matrix = np.array([[1, 2, 3],  # First row
                   [4, 5, 6],  # Second row
                   [7, 8, 9]]) # Third row

# Print the matrix
print("Matrix:")
print(matrix)

# Compute eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(matrix)

# Display eigenvalues
print("\nEigenvalues:")
print(eigenvalues)

# Display eigenvectors
print("\nEigenvectors:")
print(eigenvectors)




# compute inverse of a matrix
import numpy as np  # Importing NumPy library

# Define a 3x3 matrix
matrix = np.array([[2, 3, 1],  # First row
                   [4, 5, 6],  # Second row
                   [7, 8, 9]]) # Third row

# Compute the determinant of the matrix
determinant = np.linalg.det(matrix)

# Check if the matrix is invertible (det ≠ 0)
if determinant != 0:  
    inverse_matrix = np.linalg.inv(matrix)  # Compute the inverse using NumPy
    print("Inverse of the matrix:")
    print(inverse_matrix)  # Display the inverse matrix
else:
    print("The given matrix is singular (determinant = 0) and cannot be inverted.")  # Error message if the matrix is singular
