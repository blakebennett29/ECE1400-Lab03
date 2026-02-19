from matrix_io import read_matrix
import numpy as np

mat = read_matrix("exercise6.csv")
A = mat[::, :3]
B = mat[::, 3:]
sol = np.linalg.solve(A, B)
print(sol)
