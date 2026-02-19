"""
matrix_io.py

A small module for interactive matrix input and CSV matrix file I/O.

Author: Blake Bennett
Creation date: 2026-02-18
"""

import ast
import numpy as np


def input_row(prompt: str) -> list[float]:
    """
    Prompt the user for a row and return a list of floats.

    Parameters:
        prompt (str): Prompt displayed to the user.

    Returns:
        list[float]: List of floats parsed from the user's input.
                     Returns [] if the input is invalid.
    """
    try:
        user_text = input(prompt)
        python_obj = ast.literal_eval(user_text)
        values = list(python_obj)

        float_values = []
        for value in values:
            float_values.append(float(value))

        return float_values
    except Exception:
        return []


def input_matrix(num_rows: int) -> np.ndarray:
    """
    Prompt the user for a matrix of num_rows rows.

    Parameters:
        num_rows (int): Number of rows to input.

    Returns:
        np.ndarray: Numpy array containing the matrix data as floats.
    """
    rows = []
    for row_index in range(1, num_rows + 1):
        prompt = f"Input row {row_index} of the matrix: "
        rows.append(input_row(prompt))

    return np.array(rows, dtype=float)


def write_matrix(matrix, filename: str) -> None:
    """
    Write a matrix to a CSV file.

    Parameters:
        matrix: A list of lists or np.ndarray representing the matrix.
        filename (str): Output CSV filename.

    Returns:
        None
    """
    array_matrix = np.array(matrix, dtype=float)

    with open(filename, "w", encoding="utf-8") as file:
        for row in array_matrix:
            if len(row) == 0:
                file.write("\n")
                continue

            file.write("%g" % row[0])
            for value in row[1:]:
                file.write(", %g" % value)
            file.write("\n")


def read_matrix(filename: str) -> np.ndarray:
    """
    Read a CSV file into a numpy array of floats.

    Parameters:
        filename (str): Input CSV filename.

    Returns:
        np.ndarray: Numpy array containing the file's matrix data.
    """
    rows = []
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            stripped_line = line.strip()
            if stripped_line == "":
                continue

            parts = stripped_line.split(",")
            row = []
            for part in parts:
                row.append(float(part.strip()))
            rows.append(row)

    return np.array(rows, dtype=float)
