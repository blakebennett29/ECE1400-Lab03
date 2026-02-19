"""
matrix_io.py

A small module for interactive matrix input and CSV matrix file I/O.

Author: Blake Bennett
Creation date: 2026-02-18
"""

import ast
import numpy as np


def input_row(prompt):
    """
    Prompt the user for a row and return a list of floats.

    Parameters:
        prompt (str): Prompt displayed to the user.

    Returns:
        list[float]: List of floats parsed from the user's input.
                     Returns [] if the input is invalid.
    """

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


def write_matrix(matrix, filename):
    """
    Write a matrix to a CSV file.

    Parameters:
        matrix: A list of lists or np.ndarray representing the matrix.
        filename (str): Output CSV filename.

    Returns:
        None
    """

    with open(filename, "w") as f:
        for row in matrix:
            if len(row) > 0: # row is the index
                f.write("%g"% row[0])
                for i in range(1, len(row)):
                    f.write(", %g"% row[i])
            f.write("\n")
    f.close()


def read_matrix(filename):
    """
    Read a CSV file into a numpy array of floats.

    Parameters:
        filename (str): Input CSV filename.

    Returns:
        np.ndarray: Numpy array containing the file's matrix data.
    """
    with open(filename, 'r') as file:
        matrix = []
        for line in file:
            try:
                row = list(map(float, line.split(',')))
                matrix.append(row)
            except ValueError:
                print(f"Error converting line to float: {line.strip()}")
        return np.array(matrix)
    
