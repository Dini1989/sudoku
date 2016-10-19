import os

'''
for x in range(10.9): 
    print("-" * 27)

    sudokugrid = [ [1 , 7 , 5 , 2 , 9 , 4 , 8 , 3 , 6] , [6 , 2 , 3 , 1 , 8 , 7 , 9 , 4 , 5] , [8 , 9 , 4 , 5 , 6 , 3 , 2 , 7 , 1], [5 , 1 , 9 , 7 , 3 , 2 , 4 , 6 , 8] , [3 , 4 , 7 , 8 , 5 , 6 , 1 , 2 , 9] , [2 , 8 , 6 , 9 , 4 , 1 , 7 , 5 , 3] , [9 , 3 , 8 , 4 , 2 , 5 , 6 , 1 , 7] , [4 , 6 , 1 , 3 , 7 , 9 , 5 , 8 , 2] , [7 , 5 , 2 , 6 , 1 , 8 , 3 , 9 , 4]]


for row in range(0,9):
    for column in range(0,9):
        print("[" , sudokugrid[row][column] , sep="" , end="]")
    print()



print()
print("-" * 27)
print()

'''


def gridforprint(x):
    if x > 10:
        return x - 10
    if x == 10:
        return " "
    return x 

sudokugamegrid = [[10, 17, 15, 10, 19, 10, 10, 10, 16], [10, 12, 13, 10, 18, 10, 10, 14, 10], [18, 10, 10, 10, 10, 13, 10, 10, 11], [15, 10, 10, 17, 10, 12, 10, 10, 10], [10, 14, 10, 18, 10, 16, 10, 12, 10] , [10, 10, 10, 19, 10, 11, 10, 10, 13], [19, 10, 10, 14, 10, 10, 10, 10, 17], [10, 16, 10, 10, 17, 10, 15, 18, 10], [17, 10, 10, 10, 11, 10, 13, 19, 10]]



while True:
    

    print("   a  b  c  d  e  f  g  h  i")
    for row in range(0, 9):
        print(row+1, end=" ")
        for column in range(0, 9):
            print("[" , gridforprint(sudokugamegrid[row][column]), sep="" , end="]")
        print()

    print("-" * 27)

    inputfield = input("Please enter the coordinates and the value like this exaple: XYN: ")

    if sudokugamegrid[int(inputfield[0])][int(inputfield[1])] > 10:
        print("You can't modify the basefield value!'")
    else: 
        sudokugamegrid[int(inputfield[0])][int(inputfield[1])] = int(inputfield[2:])

    

