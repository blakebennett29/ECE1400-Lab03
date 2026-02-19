import math
import ast

# Put your code for write_matrix(matrix) here.
def write_matrix(matrix, filename):
    with open(filename, "w") as f:
        for row in matrix:
            if len(row) > 0: # row is the index
                f.write("%g"% row[0])
                for i in range(1, len(row)):
                    f.write(", %g"% row[i])
            f.write("\n")
    f.close()



#
# This is test code. Leave this code in so you can test write_matrix.
# if it works, the program will finish quietly without error.
#
if __name__ == "__main__":
    ''' Test Code. Create a matrix and write it to a file. Check that
        file to see it is correct. Print ERROR if anything is amiss.'''
    mat = [[1.1, 2.3, 3.5], [5.0, 4.0, 3.0], [6.6, 4.3, 1.2]]
    write_matrix(mat, "tmp.csv")
    with open("tmp.csv", "r") as f:
        s = f.readlines()
        for i in range(3):
            t = ast.literal_eval(s[i].strip())
            for j in range(3):
                if not math.isclose(t[j], mat[i][j]):
                    print("ERROR")
                
