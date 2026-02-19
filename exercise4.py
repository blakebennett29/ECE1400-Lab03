import numpy as np

# Put your code for read_matrix(filename) here.
import numpy as np
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
    
    

#
# This is test code. Leave this code in so you can test read_matrix.
# if it works, the program will output the matrix below.
#
if __name__ == "__main__":
    ''' Test Code. Create a .csv file then read it with read_matrix.
        Print the matrix. If it works, the output should be:
        [[5.7 4.8 3.9]
         [6.6 4.3 1.2]
         [1.1 2.3 3.5]] '''
    with open("tmp.csv", "w") as f:
        f.write("5.7, 4.8, 3.9\n")
        f.write("6.6, 4.3, 1.2\n")
        f.write("1.1, 2.3, 3.5\n")
    print(read_matrix("tmp.csv"))

