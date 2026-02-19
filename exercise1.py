"""
Author: Blake Bennett
"""

import ast


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
    except Exception:
        return []


if __name__ == "__main__":
    # Simple test program (your instructor's file may differ)
    print(input_row("Input row 1: "))
    print(input_row("Input row 2: "))
    print(input_row("Input row 3: "))
