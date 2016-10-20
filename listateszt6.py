from copy import deepcopy


def clone_list(x):
    y = deepcopy(x)


def sudoku_list_matcher(x):
    for i in range(0, 9):
        for n in range(0, 9):
            if x[i][n] > 10:
                x[i][n] = x[i][n] - 10


def sudoku_match_list(x, y):
    how_many_matches = []
    for i in range(0, 9):
        for n in range(0, 9):
            if x[i][n] == y[i][n]:
                how_many_matches.append(1)
            else:
                how_many_matches.append(0)
    return how_many_matches


def sudoku_match_sum(x, y):
    how_many_matches = []
    for i in range(0, 9):
        for n in range(0, 9):
            if x[i][n] == y[i][n]:
                how_many_matches.append(1)
            else:
                how_many_matches.append(0)
    return sum(how_many_matches)


sudokugamegrid = [
    [10, 17, 15, 10, 19, 10, 10, 10, 16],
    [10, 12, 13, 10, 18, 10, 10, 14, 10],
    [18, 10, 10, 10, 10, 13, 10, 10, 11],
    [15, 10, 10, 17, 10, 12, 10, 10, 10],
    [10, 14, 10, 18, 10, 16, 10, 12, 10],
    [10, 10, 10, 19, 10, 11, 10, 10, 13],
    [19, 10, 10, 14, 10, 10, 10, 10, 17],
    [10, 16, 10, 10, 17, 10, 15, 18, 10],
    [17, 10, 10, 10, 11, 10, 13, 19, 10]]

sudokugridsolution = [
    [1, 7, 5, 2, 9, 4, 8, 3, 6],
    [6, 2, 3, 1, 8, 7, 9, 4, 5],
    [8, 9, 4, 5, 6, 3, 2, 7, 1],
    [5, 1, 9, 7, 3, 2, 4, 6, 8],
    [3, 4, 7, 8, 5, 6, 1, 2, 9],
    [2, 8, 6, 9, 4, 1, 7, 5, 3],
    [9, 3, 8, 4, 2, 5, 6, 1, 7],
    [4, 6, 1, 3, 7, 9, 5, 8, 2],
    [7, 5, 2, 6, 1, 8, 3, 9, 4]]

clonelist = clone_list(sudokugamegrid)
sudoku_list_matcher(clonelist)
sudoku_match_sum(clonelist, sudokugridsolution)
print(sudoku_match_list(clonelist, sudokugridsolution))
print(sudoku_match_sum(clonelist, sudokugridsolution))
