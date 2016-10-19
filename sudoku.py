import os

def gridforprint(x):
    if x > 10:
        return x - 10
    if x == 10:
        return " "
    return x     
    

sudokugamegrid = [[10, 17, 15, 10, 19, 10, 10, 10, 16], [10, 12, 13, 10, 18, 10, 10, 14, 10], [18, 10, 10, 10, 10, 13, 10, 10, 11], [15, 10, 10, 17, 10, 12, 10, 10, 10], [10, 14, 10, 18, 10, 16, 10, 12, 10], [10, 10, 10, 19, 10, 11, 10, 10, 13], [19, 10, 10, 14, 10, 10, 10, 10, 17], [10, 16, 10, 10, 17, 10, 15, 18, 10], [17, 10, 10, 10, 11, 10, 13, 19, 10]]

os.system('cls' if os.name == 'nt' else 'clear')

while True:

    print("   a  b  c  d  e  f  g  h  i \n")
    for row in range(0,9):
        print(row+1, end=" ")
        for column in range(0,9):
            print("[" , gridforprint(sudokugamegrid[row][column]), sep="" , end="]")
        print()


    print("-" * 27)

    inputfield = input("Please enter the coordinates and the value like this exaple: XYN: ")

    sudokugamegrid[int(inputfield[0])][int(inputfield[1])] = int(inputfield[2:])

