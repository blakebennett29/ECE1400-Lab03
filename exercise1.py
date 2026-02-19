import sys
import ast
"""
Blake Bennett
"""
# Put your code for input_row(prompt) here:
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
#
# This is test code. Leave this code in so you can test input_row.
# if it works, you will see nothing but the prompt strings.
#
if __name__ == "__main__":
    ''' Test Code. Create a file of responses then direct it to console
        input. Print ERROR if anything is amiss. '''
    with open("tmp.txt","w") as f:
        f.write("1.1, 2.3, 4.5\n")
        f.write("4.4, [5], {6}\n")
        f.write("4.4, 5.5\n")
        f.write("456 789 123\n")
        f.write("1.9, 2.8, 3.7\n")
    console = sys.stdin
    sys.stdin = open('tmp.txt','r')
    x = input_row("Input row 1: ")
    if x != [1.1, 2.3, 4.5]:
        print("ERROR")
    x = input_row("Input row 2: ")
    if x != []:
        print("ERROR")
    x = input_row("Input row 2: ")
    if x != [4.4, 5.5]:
        print("ERROR")
    x = input_row("Input row 3: ")
    if x != []:
        print("ERROR")
    x = input_row("Input row 3: ")
    if x != [1.9, 2.8, 3.7]:
        print("ERROR")
    sys.stdin.close()
    sys.stdin = console
