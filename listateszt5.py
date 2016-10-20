def clone_list(list1):
    ret_list = list1.copy()
    for target_list in list1:
        pass


def sudoku_list_matcher(list1):
     for i in range(0, 9):
        for n in range(0, 9):
            if list1[i][n] > 10:
                 list1[i][n] = list1[i][n] - 10


def sudoku_match_list(list1, list2):
    how_many_matches = []
    for i in range(0, 9):
        for n in range(0, 9):
            if list1[i][n] == list2[i][n]:
                how_many_matches.append(1)
            else:
                how_many_matches.append(0)
    return how_many_matches


def sudoku_match_sum(list1, list2):
    how_many_matches = []
    for i in range(0, 9):
        for n in range(0, 9):
            if list1[i][n] == list2[i][n]:
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

sudoku_list_matcher()
print(sudoku_match_list(sudokugamegrid, sudokugridsolution))
print(sudoku_match_sum(sudokugamegrid, sudokugridsolution))
