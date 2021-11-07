# Attempting an implementation of the back-tracing algorithm

import numpy as np
from check import Check


possibilities = np.zeros((9, 9, 7))
alreadyChecked = np.zeros((9, 9, 7))

sudPuzzle = np.array([[0,0,0, 0,0,8, 3,0,0],
                      [0,0,0, 0,2,4, 0,9,0],
                      [0,0,4, 0,7,0, 0,0,6],

                      [0,0,0, 0,0,3, 0,7,9],
                      [7,5,0, 0,0,0, 0,8,4],
                      [9,2,0, 5,0,0, 0,0,0],

                      [4,0,0, 0,9,0, 1,0,0],
                      [0,3,0, 4,6,0, 0,0,0],
                      [0,0,5, 8,0,0, 0,0,0]])

# Creating an instance of the class Check
c = Check(sudPuzzle)

# +These for loops get all of the possible numbers that can go into
# the raw puzzle at each empty position, then saves them to all to an
# three dimensional array
for i in range(0, 9, 1):
    for j in range(0,9,1):
        counterino = 0
        quadrant = c.determineQuadrant(i,j)
        for k in range(1, 10, 1):
            if (((c.checkVertical(j, k)) and
                    (c.checkHorizontal(i, k)) and
                    (c.checkQuadrant(k, quadrant))) is True):

                possibilities[i][j][counterino] = k

                counterino += 1


# Place is used to access the cols and rows of the empty places
zeroRow = []
zeroCol = []
place = 0

# Getting the positions of the empty spots in the puzzle
for i in range(0, 9, 1):
    for j in range(0, 9, 1):
        if sudPuzzle[i][j] == 0:
            zeroRow.append(i)
            zeroCol.append(j)

i = 0

while True:

    x = zeroCol[place]
    y = zeroRow[place]

    d = Check(sudPuzzle)
    quadrant = d.determineQuadrant(y, x)

    test = possibilities[y][x][i]

    if ((d.checkVertical(x, test)) and
        (d.checkHorizontal(y, test)) and
        (d.checkQuadrant(test, quadrant))):

        alreadyChecked[y][x][i] = test
        place += 1
        sudPuzzle[y][x] = test
        i = 0

    elif test in alreadyChecked[y][x]:

        xCheck = zeroCol[place]
        yCheck = zeroRow[place]

        alreadyChecked[y][x][i] = test

        # +this aims to clear the memory for those checked after
        # the current box; it only retains the memory for those
        # checked previously to the current one
        for q in range(xCheck, 9, 1):
            alreadyChecked[yCheck][q] = 0
        for t in range(1, 9, 1):
            for r in range(yCheck+1, 9, 1):
                alreadyChecked[r][t] = 0

        sudPuzzle[y][x] = 0
        place -= 1

        x = zeroCol[place]
        y = zeroRow[place]

        # This
        for o in range(0, 6, 1):
            if (possibilities[y][x][o] not in alreadyChecked[y][x]) and \
                    (possibilities[y][x][o] != 0):
                i = o
                break

    else:
        alreadyChecked[y][x][i] = test
        i += 1

    e = Check(sudPuzzle)

    # Determines the number of zeros left
    numbOfZeros = e.determineNumberOfZeros()

    # End condition; if there are no zeros left,
    # exit the loop and print the final result
    if numbOfZeros == 0:
        break


print(sudPuzzle[0][:])
print(sudPuzzle[1][:])
print(sudPuzzle[2][:])
print(sudPuzzle[3][:])
print(sudPuzzle[4][:])
print(sudPuzzle[5][:])
print(sudPuzzle[6][:])
print(sudPuzzle[7][:])
print(sudPuzzle[8][:])
print("FINISHED")

