from matrix_io import read_matrix
import numpy as np

mat = read_matrix("exercise6.csv")
A = mat[::][0,2]
B = mat[::][3,4]
sol = np.linalg.solve(A, B)
print(sol)