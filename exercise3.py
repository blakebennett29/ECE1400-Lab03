import numpy as np


def write_matrix(matrix, filename: str) -> None:
    """
    Write a matrix to a CSV file.

    Parameters:
        matrix: A list of lists or np.ndarray.
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


if __name__ == "__main__":
    # Should run without errors
    write_matrix([[1.1, 2.2], [4.5, 5.6]], "out.csv")
