#Wellcome to Petya's and Dénes's sudoku game


import os
from copy import deepcopy


# Source of the grid generation.


sudokugamegrid = [[10, 17, 15, 10, 19, 10, 10, 10, 16],
                  [10, 12, 13, 10, 18, 10, 10, 14, 10],
                  [18, 10, 10, 10, 10, 13, 10, 10, 11],
                  [15, 10, 10, 17, 10, 12, 10, 10, 10],
                  [10, 14, 10, 18, 10, 16, 10, 12, 10],
                  [10, 10, 10, 19, 10, 11, 10, 10, 13],
                  [19, 10, 10, 14, 10, 10, 10, 10, 17],
                  [10, 16, 10, 10, 17, 10, 15, 18, 10],
                  [17, 10, 10, 10, 11, 10, 13, 19, 10]]


# Source of the good solution checker grid.


sudokugridsolution = [[1, 7, 5, 2, 9, 4, 8, 3, 6],
                      [6, 2, 3, 1, 8, 7, 9, 4, 5],
                      [8, 9, 4, 5, 6, 3, 2, 7, 1],
                      [5, 1, 9, 7, 3, 2, 4, 6, 8],
                      [3, 4, 7, 8, 5, 6, 1, 2, 9],
                      [2, 8, 6, 9, 4, 1, 7, 5, 3],
                      [9, 3, 8, 4, 2, 5, 6, 1, 7],
                      [4, 6, 1, 3, 7, 9, 5, 8, 2],
                      [7, 5, 2, 6, 1, 8, 3, 9, 4]]


# Generates the grid from the source and adds visuals. Also adds basic
# rules about the displayed grid (17 visualised as 7 etc.)


def gridtransformer(x):
    if x > 10:
        return x - 10
    if x == 10:
        return "·"
    return x


def table():
    bold = "\033[1m"
    reset = "\033[0;0m"
    print("   a  b  c    d  e  f    g  h  i\n")
    for row in range(0, 9):
        if row == 3:
            print("  -----------------------------")
        if row == 6:
            print("  -----------------------------")
        print(row + 1, end=" ")
        for column in range(0, 9):
            if column == 3:
                print("｜", end="")
            if column == 6:
                print("｜", end="")
            if (sudokugamegrid[row][column]) > 10:
                print(" ", "\033[93m", bold, gridtransformer(sudokugamegrid[row][column]), reset, sep="", end=" ")
            else:
                print(" ", "\033[95m", gridtransformer(sudokugamegrid[row][column]), reset, sep="", end=" ")
        print()

    print("-" * 31)


# Handles the user inputs like uninterpretable expressions. Add rules to
# the game mechanics (Immutable basic existing characters on the grid
# etc.)


def handleinput():
    while True:
        inputfield = input(
            "\nAdd the coordinates and the value.\nYou can delete with value '10'.\nOr write 'check' to check your solution.\nOr press exit to quit.\n\nEnter you choice:")
        if inputfield == str("exit"):
            exit()
        if inputfield == str("check"):
            os.system('cls' if os.name == 'nt' else 'clear')
            table()
            sudoku_list_matcher(clonelist)
            if int(sudoku_match_sum(clonelist, sudokugridsolution)) == int(81):
                table()
                print("\n!!!!!!!!!!!!YOU WON!!!!!!!!!!!!")
                input("Press any key to exit")
                exit()
            else:
                print("\nContinue the game, it's not good yet :(")
        else:
            try:
                inputrow = int(inputfield[0]) - 1
                inputcolumn = int(ord(inputfield[1])) - 97
                inputvalue = int(inputfield[2:])
                if inputrow not in range(0, 9):
                    raise IndexError
                if inputcolumn not in range(0, 9):
                    raise IndexError
                if inputvalue not in range(1, 11):
                    raise ValueError
                if sudokugamegrid[inputrow][inputcolumn] > 10:
                    raise ReferenceError
                return inputrow, inputcolumn, inputvalue,

            except IndexError:
                os.system('cls' if os.name == 'nt' else 'clear')
                table()
                print("\nYour coordinate is not on the game field, please try again.")
            except ValueError:
                os.system('cls' if os.name == 'nt' else 'clear')
                table()
                print("\nOops!  That was no valid number.  Try again...")
            except ReferenceError:
                os.system('cls' if os.name == 'nt' else 'clear')
                table()
                print("\nYou can't modify the basefield value!")


#Checking the solution by comparing the user modified basic grid with the solution grid.


def clone_list(x):
    y = deepcopy(x)
    return y


def sudoku_list_matcher(x):
    for i in range(0, 9):
        for n in range(0, 9):
            if x[i][n] > 10:
                x[i][n] = x[i][n] - 10


def sudoku_match_sum(x, y):
    how_many_matches = []
    for i in range(0, 9):
        for n in range(0, 9):
            if x[i][n] == y[i][n]:
                how_many_matches.append(1)
            else:
                how_many_matches.append(0)
    return sum(how_many_matches)


#Intro text to the program


print("\nWELLCOME TO SUDOKU\n by Petya & Dénes\n ")
print("\nAdd numbers correctly into their places. You can quit the game on the checker screen. \n ")
print("Please enter the coordinates and the value like this example: 1a5, use the helper grids to identify the coordinates. Use 10 value as delete like in this example: 1a10. \n")


#Running the functions in the proper order.


while True:

    table()

    print ("\n")

    clone_list(sudokugamegrid)

    clonelist = clone_list(sudokugamegrid)

    row, column, value = handleinput()

    os.system('cls' if os.name == 'nt' else 'clear')

    table()

    sudokugamegrid[row][column] = value

    os.system('cls' if os.name == 'nt' else 'clear')


#The file ends here. Live long and prosper!
