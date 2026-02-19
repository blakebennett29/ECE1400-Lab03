import numpy as np
def read_matrix(filename):
    with open(filename, 'r') as file:
        matrix = []
        for line in file:
            try:
                row = list(map(float, line.split()))
                matrix.append(row)
            except ValueError:
                print(f"Error converting line to float: {line.strip()}")
        return np.array(matrix)
    
if __name__ == "__main__":
    matrix = read_matrix("exercise4.csv")
    print(matrix)