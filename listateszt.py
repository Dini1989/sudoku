

def match_nonmatch(list1, list2):
    how_many_matches = []
    for i in range(len(list1)):
        if list1[i] == list2[i]:
            how_many_matches.append(1)
        else:
            how_many_matches.append(0)
    return sum(how_many_matches)


sudokugamegrid = [1, 2, 3, 4]
sudokusolution = [1, 5, 3, 4]

print(match_nonmatch(sudokugamegrid, sudokusolution))
