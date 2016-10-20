import os
from copy import deepcopy

'''
for x in range(10.9):
    print("-" * 27)

for row in range(0,9):
    for column in range(0,9):
        print("[" , sudokugrid[row][column] , sep="" , end="]")
    print()



print()
print("-" * 27)
print()

'''


def gridtransformer(x):
    if x > 10:
        return x - 10
    if x == 10:
        return " "
    return x


def table():
    print("   a  b  c   d  e  f   g  h  i")
    for row in range(0, 9):
        if row == 3:
            print("  -----------------------------")
        if row == 6:
            print("  -----------------------------")
        print(row + 1, end=" ")
        for column in range(0, 9):
            if column == 3:
                print(":", end="")
            if column == 6:
                print(":", end="")
            print("[", gridtransformer(sudokugamegrid[row][column]), sep="", end="]")
        print()

    print("-" * 31)


def helper_input():
    while True:
        inputfield = input(
            "Type check to be sure about completition. Type any other thing to continue: ")

        os.system('cls' if os.name == 'nt' else 'clear')

        if inputfield == "check":
            sudoku_list_matcher(clonelist)
            if int(sudoku_match_sum(clonelist, sudokugridsolution)) == int(81):

                table()
                print(sudoku_match_sum(clonelist, sudokugridsolution))
                print("\n!!!!!!!!!!!YOU WON!!!!!!!!!!!\n")
                input("Press any key to exit")
                exit()
            else:
                table()
                print(sudoku_match_sum(clonelist, sudokugridsolution))
                print("Keep play")
        else:
            break


def handleinput():
    while True:

        inputfield = input(
            "Please enter the coordinates and the value like this exaple: XYN: ")
        try:
            inputrow = int(inputfield[0]) - 1
            inputcolumn = int(inputfield[1]) - 1
            inputvalue = int(inputfield[2:])
            if inputrow not in range(0, 9):
                raise IndexError
            if inputcolumn not in range(0, 9):
                raise IndexError
            if inputvalue not in range(1, 11):
                raise ValueError
            if sudokugamegrid[inputrow][inputcolumn] > 10:
                raise ReferenceError
            return inputrow, inputcolumn, inputvalue
        except IndexError:
            print("Your coordinate is not on the game field, please try again.")
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
        except ReferenceError:
            print("You can't modify the basefield value!")


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

"""
sudokugamegrid = [[10, 17, 15, 10, 19, 10, 10, 10, 16],
                  [10, 12, 13, 10, 18, 10, 10, 14, 10],
                  [18, 10, 10, 10, 10, 13, 10, 10, 11],
                  [15, 10, 10, 17, 10, 12, 10, 10, 10],
                  [10, 14, 10, 18, 10, 16, 10, 12, 10],
                  [10, 10, 10, 19, 10, 11, 10, 10, 13],
                  [19, 10, 10, 14, 10, 10, 10, 10, 17],
                  [10, 16, 10, 10, 17, 10, 15, 18, 10],
                  [17, 10, 10, 10, 11, 10, 13, 19, 10]]

"""
sudokugamegrid = [[6, 7, 5, 2, 9, 4, 8, 3, 6],
                  [5, 2, 3, 1, 8, 7, 9, 4, 5],
                  [8, 9, 4, 5, 6, 3, 2, 7, 1],
                  [5, 1, 9, 7, 3, 2, 4, 6, 8],
                  [4, 4, 7, 8, 5, 6, 1, 2, 9],
                  [2, 8, 6, 9, 4, 1, 7, 5, 3],
                  [9, 3, 8, 4, 2, 5, 6, 1, 7],
                  [4, 6, 1, 3, 7, 9, 5, 8, 2],
                  [7, 5, 2, 6, 1, 8, 3, 9, 4]]


sudokugridsolution = [[1, 7, 5, 2, 9, 4, 8, 3, 6],
                      [6, 2, 3, 1, 8, 7, 9, 4, 5],
                      [8, 9, 4, 5, 6, 3, 2, 7, 1],
                      [5, 1, 9, 7, 3, 2, 4, 6, 8],
                      [3, 4, 7, 8, 5, 6, 1, 2, 9],
                      [2, 8, 6, 9, 4, 1, 7, 5, 3],
                      [9, 3, 8, 4, 2, 5, 6, 1, 7],
                      [4, 6, 1, 3, 7, 9, 5, 8, 2],
                      [7, 5, 2, 6, 1, 8, 3, 9, 4]]


while True:

    table()

    row, column, value = handleinput()

    sudokugamegrid[row][column] = value

    clone_list(sudokugamegrid)

    clonelist = clone_list(sudokugamegrid)

    os.system('cls' if os.name == 'nt' else 'clear')

    table()

    helper_input()
