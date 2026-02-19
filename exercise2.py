import math
import sys
import numpy as np
import ast
# Copy your code for input_row(prompt) from exercise1.py here.
def input_row(prompt):
    try:
        user_input = input(prompt)
        data = ast.literal_eval(user_input)
        if not isinstance(data, (list, tuple)): #is it not a list or tuple then make it a list
    # If data is NOT already a list or a tuple (e.g., it's just a single float 5.5)
    # wrap it in a list so we can iterate over it later.
            data = [data]
        else:
            # If it IS a list or tuple, ensure it becomes a list type.
            data = list(data)
        floatlist = []
        for i in data:
            floatlist.append(float(i))
        return floatlist
    
    except ( ValueError, SyntaxError, TypeError):
        return []
# Put your code for input_matrix(row) here.
def input_matrix(num_rows):
    """
    Prompt the user for a matrix of  how many rows have them input the length of rows.

    Parameters:
        rows (int): Number of rows to input.

    Returns:
        np.ndarray: Numpy array containing the matrix data as floats.
    """
    total_rows = []
    for row_index in range(1, num_rows +1):
        prompt = f"Input row {row_index} of the matrix:"
        row = input_row(prompt)
        total_rows.append(row)
    total_rows = np.array(total_rows)
    return total_rows


#
# This is test code. Leave this code in so you can test input_row.
# if it works, you will see nothing but the prompt strings.
#
if __name__ == "__main__":
    with open("tmp.txt", "w") as f:
        f.write("[4]\n")
        f.write("1.1, 2.3, 4.5\n")
        f.write("4.4, 5.1, 6.8\n")
        f.write("1.9, 2.8, 3.7\n")
    console = sys.stdin
    sys.stdin = open('tmp.txt', 'r')
    x = input_matrix(1)
    if x[0][0] != 4:
        print("ERROR")
    x = input_matrix(3)
    v = [[1.1, 2.3, 4.5], [4.4, 5.1, 6.8], [1.9, 2.8, 3.7]]
    for i in range(3):
        for j in range(3):
            if not math.isclose(x[i][j], v[i][j]):
                print("ERROR")

    sys.stdin.close()
    sys.stdin = console
