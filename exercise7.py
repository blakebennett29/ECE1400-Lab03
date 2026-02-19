import ast
import numpy as np
from matrix_io import input_row, input_matrix, write_matrix


matrix = input_matrix(2)
det = np.linalg.det(matrix)
print(f"Determinant: {det}")
