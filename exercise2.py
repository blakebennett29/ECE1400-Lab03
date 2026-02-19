import ast
import numpy as np


def input_row(prompt: str) -> list[float]:
    """
    Prompt the user for a row and return a list of floats.

    Parameters:
        prompt (str): The prompt displayed to the user.

    Returns:
        list[float]: A list of floats parsed from the user's input.
                     Returns [] if the input cannot be parsed.
    """
    try:
        user_text = input(prompt)
        python_obj = ast.literal_eval(user_text)
        values = list(python_obj)

        float_values = []
        for value in values:
            float_values.append(float(value))

        return float_values
    except (TypeError, ValueError, SyntaxError, NameError):
        return []


def input_matrix(num_rows: int) -> np.ndarray:
    """
    Prompt the user for num_rows rows and return a numpy matrix.

    Parameters:
        num_rows (int): Number of rows to input.

    Returns:
        np.ndarray: Matrix of floats with shape (num_rows, ncols) if inputs match,
                    but rows may be empty lists if user typed invalid input.
    """
    rows = []
    for row_index in range(1, num_rows + 1):
        prompt = f"Input row {row_index} of the matrix: "
        rows.append(input_row(prompt))

    return np.array(rows, dtype=float)


if __name__ == "__main__":
    print(input_matrix(3))
