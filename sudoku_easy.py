import os
from copy import deepcopy


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


def helper_input():
    while True:
        inputfield = input(
            "Type check to be sure about completition. Type any other thing to continue: ")

        os.system('cls' if os.name == 'nt' else 'clear')

        if inputfield == "check":
            sudoku_list_matcher(clonelist)
            if int(sudoku_match_sum(clonelist, sudokugridsolution)) == int(50):

                table()

                print("\n!!!!!!!!!!!!YOU WON!!!!!!!!!!!!\n")
                input("Press any key to exit")
                exit()
            else:
                table()

                print("Keep play")
        else:
            break


def handleinput():
    while True:

        inputfield = input(
            "Please enter the coordinates and the value like this exaple: XYN: ")
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


sudokugamegrid = [[10, 17, 15, 2, 19, 4, 8, 3, 16],
                  [6, 12, 13, 1, 18, 7, 9, 14, 5],
                  [18, 9, 4, 5, 6, 13, 2, 7, 11],
                  [15, 1, 9, 17, 3, 12, 4, 6, 8],
                  [3, 14, 7, 18, 5, 16, 1, 12, 9],
                  [2, 8, 6, 19, 4, 11, 7, 5, 13],
                  [19, 3, 8, 14, 2, 5, 6, 1, 17],
                  [4, 16, 1, 3, 17, 9, 15, 8, 2],
                  [17, 5, 2, 6, 11, 8, 13, 19, 4]]


sudokugridsolution = [[1, 17, 15, 2, 19, 4, 8, 3, 16],
                      [6, 12, 13, 1, 18, 7, 9, 14, 5],
                      [18, 9, 4, 5, 6, 13, 2, 7, 11],
                      [15, 1, 9, 17, 3, 12, 4, 6, 8],
                      [3, 14, 7, 18, 5, 16, 1, 12, 9],
                      [2, 8, 6, 19, 4, 11, 7, 5, 13],
                      [19, 3, 8, 14, 2, 5, 6, 1, 17],
                      [4, 16, 1, 3, 17, 9, 15, 8, 2],
                      [17, 5, 2, 6, 11, 8, 13, 19, 4]]


while True:

    table()

    row, column, value = handleinput()

    sudokugamegrid[row][column] = value

    clone_list(sudokugamegrid)

    clonelist = clone_list(sudokugamegrid)

    os.system('cls' if os.name == 'nt' else 'clear')

    table()

    helper_input()
