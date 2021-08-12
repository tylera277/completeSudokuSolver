# 7/28/2021
# +SHIT MAY GO WRONG IN THIS PROGRAM, CURRENT FUNCTIONING PROGRAM
# IS THE TEST FILE, THIS IS MORE OF AN EXPERIMENTAL TEST

import numpy as np
import time
from check import Check
from check2 import Check2
from itertools import permutations


start = time.time()

# [0,0,0,0,0,0,0,0,0],

# the sudoku puzzle I want to solve.
puzzle = np.array([[6,9,0,0,0,0,0,4,1],
          [3,0,0,0,5,9,0,0,2],
          [0,0,0,6,0,0,0,0,0],
          [0,7,0,0,0,0,9,0,0],
          [0,5,0,0,9,0,0,1,0],
          [0,0,4,0,0,0,0,7,0],
          [0,0,0,0,0,8,0,0,0],
          [4,0,0,3,7,0,0,0,5],
          [5,1,0,0,0,0,0,6,8]])
puzzle.flags.writeable = False

guess = np.copy(puzzle)




#print(puzzle,guess)

c = Check(puzzle)
quad1 = c.whatUniqueNumbInQuad(1)
quad2 = c.whatUniqueNumbInQuad(2)
quad3 = c.whatUniqueNumbInQuad(3)
quad4 = c.whatUniqueNumbInQuad(4)
quad5 = c.whatUniqueNumbInQuad(5)
quad6 = c.whatUniqueNumbInQuad(6)
quad7 = c.whatUniqueNumbInQuad(7)
quad8 = c.whatUniqueNumbInQuad(8)
quad9 = c.whatUniqueNumbInQuad(9)

#print('c:',quad2)
#print(guess[0,1])

# +this makes a list of all of the possible combinations of the numbers
# missing in the quadrants, which I then plug in to the zeros
# and check to see which arrangement fills it completely
# QUAD 1 (top left)
quad1List = list(permutations(quad1, len(quad1)))
quad1ListWorks = []

# QUAD 2 (top middle)
quad2List = list(permutations(quad2, len(quad2)))
quad2ListWorks = []

# QUAD 3 (top right)
quad3List = list(permutations(quad3, len(quad3)))
quad3ListWorks = []

# QUAD 4 (middle left)
quad4List = list(permutations(quad4, len(quad4)))
quad4ListWorks = []

# QUAD 5 (middle middle)
quad5List = list(permutations(quad5, len(quad5)))
quad5ListWorks = []

# QUAD 6 (middle right)
quad6List = list(permutations(quad6, len(quad6)))
quad6ListWorks = []

# QUAD 7 (bottom left)
quad7List = list(permutations(quad7, len(quad7)))
quad7ListWorks = []

# QUAD 8 (bottom middle)
quad8List = list(permutations(quad8, len(quad8)))
quad8ListWorks = []

# QUAD 9 (middle right)
quad9List = list(permutations(quad9, len(quad9)))
quad9ListWorks = []

d = Check(puzzle)

counter = 0
zeroCounter = 0
i = 0

# +These for loops check to see which permutations work in each
# quadrant while also agreeing with the known givens in the initial
# sudoku puzzle.
for i in range(len(quad1List)):
#for i in range(409,410,1):
#while i < len(quad1List):
    counter = 0
    for l in range(0,3,1):
        for m in range(0,3,1):

            if puzzle[l, m] == 0:

                if (d.checkVertical(m,quad1List[i][zeroCounter]) or
                    d.checkHorizontal(l,quad1List[i][zeroCounter]) or
                    d.checkQuadrant(l,m, quad1List[i][zeroCounter])) == 1:

                    pass
                else:
                    guess[l,m] = quad1List[i][zeroCounter]
                    counter += 1
                zeroCounter += 1
            #print(quad1List[i][zeroCounter])
    if counter == len(quad1List[0]):
        quad1ListWorks.append(i)
        #print(guess)

    guess = np.copy(puzzle)

    zeroCounter = 0

# QUAD 2 (top middle)
for k in range(len(quad2List)):
#for k in range(634,635,1):
#while i < len(quad1List):
    counter = 0
    for l in range(0, 3, 1):
        for m in range(3, 6, 1):

            if puzzle[l, m] == 0:

                if (d.checkVertical(m,quad2List[k][zeroCounter]) == 1 or
                    d.checkHorizontal(l,quad2List[k][zeroCounter]) == 1 or
                    d.checkQuadrant(l,m, quad2List[k][zeroCounter]) == 1):

                    pass
                else:
                    guess[l,m] = quad2List[k][zeroCounter]
                    counter += 1
                    #print(counter)

                #print(guess)
                zeroCounter += 1
            #print(quad1List[i][zeroCounter])
    #if guess[0,3] == 4:
        #print(guess)
    if counter == len(quad2List[0]):
        quad2ListWorks.append(k)
        #print(guess)
    #print(guess)
    guess = np.copy(puzzle)

    zeroCounter = 0

# QUAD 3 (top right)
for j in range(len(quad3List)):
#for j in range(422,423,1):
    counter3 = 0

    for l in range(0, 3, 1):
        for m in range(6, 9, 1):

            if puzzle[l, m] == 0:

                if (d.checkVertical(m, quad3List[j][zeroCounter]) or
                    d.checkHorizontal(l, quad3List[j][zeroCounter]) or
                    d.checkQuadrant(l, m, quad3List[j][zeroCounter])) == 1:

                    pass
                else:
                    guess[l, m] = quad3List[j][zeroCounter]
                    counter3 += 1
                #print(zeroCounter)
                zeroCounter += 1
                if zeroCounter == len(quad3List[0]):
                    zeroCounter = 0

    #print(counter3)

            # print(quad1List[i][zeroCounter])
    #print(quad3List[0])
    if counter3 == len(quad3List[0]):
        quad3ListWorks.append(j)
        #print(guess)

    guess = np.copy(puzzle)

    zeroCounter = 0

# QUAD 4 (middle left)
for j in range(len(quad4List)):

    counter4 = 0

    for l in range(3, 6, 1):
        for m in range(0, 3, 1):

            if puzzle[l, m] == 0:

                if (d.checkVertical(m, quad4List[j][zeroCounter]) or
                    d.checkHorizontal(l, quad4List[j][zeroCounter]) or
                    d.checkQuadrant(l, m, quad4List[j][zeroCounter])) == 1:

                    pass
                else:
                    guess[l, m] = quad4List[j][zeroCounter]
                    counter4 += 1
                #print(zeroCounter)
                zeroCounter += 1
                if zeroCounter == len(quad4List[0]):
                    zeroCounter = 0

    #print(counter3)

            # print(quad1List[i][zeroCounter])
    #print(quad3List[0])
    if counter4 == len(quad4List[0]):
        quad4ListWorks.append(j)
        #print(guess)

    guess = np.copy(puzzle)

    zeroCounter = 0

# QUAD 5
for j in range(len(quad5List)):
#for j in range(422,423,1):
    counter5 = 0

    for l in range(3, 6, 1):
        for m in range(3, 6, 1):

            if puzzle[l, m] == 0:

                if (d.checkVertical(m, quad5List[j][zeroCounter]) or
                    d.checkHorizontal(l, quad5List[j][zeroCounter]) or
                    d.checkQuadrant(l, m, quad5List[j][zeroCounter])) == 1:

                    pass
                else:
                    guess[l, m] = quad5List[j][zeroCounter]
                    counter5 += 1
                #print(zeroCounter)
                zeroCounter += 1
                if zeroCounter == len(quad5List[0]):
                    zeroCounter = 0

    #print(counter3)

            # print(quad1List[i][zeroCounter])
    #print(quad3List[0])
    if counter5 == len(quad5List[0]):
        quad5ListWorks.append(j)
        #print(guess)

    guess = np.copy(puzzle)

    zeroCounter = 0

# QUAD 6 (top right)
for j in range(len(quad6List)):

    counter6 = 0

    for l in range(3, 6, 1):
        for m in range(6, 9, 1):

            if puzzle[l, m] == 0:

                if (d.checkVertical(m, quad6List[j][zeroCounter]) or
                    d.checkHorizontal(l, quad6List[j][zeroCounter]) or
                    d.checkQuadrant(l, m, quad6List[j][zeroCounter])) == 1:

                    pass
                else:
                    guess[l, m] = quad6List[j][zeroCounter]
                    counter6 += 1

                #print('c:',counter6)
                #print(zeroCounter)
                zeroCounter += 1
                if zeroCounter == len(quad6List[0]):
                    zeroCounter = 0

    #print(counter3)

            # print(quad1List[i][zeroCounter])
    #print(quad3List[0])
    if counter6 == len(quad6List[0]):
        quad6ListWorks.append(j)
        #print(guess)

    guess = np.copy(puzzle)

    zeroCounter = 0

# QUAD 7 (bottom left)
for j in range(len(quad7List)):

    counter6 = 0

    for l in range(6, 9, 1):
        for m in range(0, 3, 1):

            if puzzle[l, m] == 0:

                if (d.checkVertical(m, quad7List[j][zeroCounter]) or
                    d.checkHorizontal(l, quad7List[j][zeroCounter]) or
                    d.checkQuadrant(l, m, quad7List[j][zeroCounter])) == 1:

                    pass
                else:
                    guess[l, m] = quad7List[j][zeroCounter]
                    counter6 += 1

                #print('c:',counter6)
                #print(zeroCounter)
                zeroCounter += 1
                if zeroCounter == len(quad7List[0]):
                    zeroCounter = 0

    #print(counter3)

            # print(quad1List[i][zeroCounter])
    #print(quad3List[0])
    if counter6 == len(quad7List[0]):
        quad7ListWorks.append(j)
        #print(guess)

    guess = np.copy(puzzle)

    zeroCounter = 0

# QUAD 8 (bottom middle)
for j in range(len(quad8List)):

    counter8 = 0

    for l in range(6, 9, 1):
        for m in range(3, 6, 1):

            if puzzle[l, m] == 0:

                if (d.checkVertical(m, quad8List[j][zeroCounter]) or
                    d.checkHorizontal(l, quad8List[j][zeroCounter]) or
                    d.checkQuadrant(l, m, quad8List[j][zeroCounter])) == 1:

                    pass
                else:
                    guess[l, m] = quad8List[j][zeroCounter]
                    counter8 += 1

                #print('c:',counter6)
                #print(zeroCounter)
                zeroCounter += 1
                if zeroCounter == len(quad6List[0]):
                    zeroCounter = 0

    #print(counter3)

            # print(quad1List[i][zeroCounter])
    #print(quad3List[0])
    if counter8 == len(quad8List[0]):
        quad8ListWorks.append(j)
        #print(guess)

    guess = np.copy(puzzle)

    zeroCounter = 0

# QUAD 9 (bottom right)
for j in range(len(quad9List)):

    counter9 = 0

    for l in range(6, 9, 1):
        for m in range(6, 9, 1):

            if puzzle[l, m] == 0:

                if (d.checkVertical(m, quad9List[j][zeroCounter]) or
                    d.checkHorizontal(l, quad9List[j][zeroCounter]) or
                    d.checkQuadrant(l, m, quad9List[j][zeroCounter])) == 1:

                    pass
                else:
                    guess[l, m] = quad9List[j][zeroCounter]
                    counter9 += 1

                #print('c:',counter6)
                #print(zeroCounter)
                zeroCounter += 1
                if zeroCounter == len(quad9List[0]):
                    zeroCounter = 0

    #print(counter3)

            # print(quad1List[i][zeroCounter])
    #print(quad3List[0])
    if counter9 == len(quad9List[0]):
        quad9ListWorks.append(j)
        #print(guess)

    guess = np.copy(puzzle)

    zeroCounter = 0



count = 0
counter = 0
counterer = 0
counter1 = 0
unitedList1 = []
unitedList2 = []
unitedList3 = []
unitedList4 = []
unitedList5 = []
unitedList6 = []
unitedList7 = []
unitedList8 = []
unitedList9 = []
guess = np.copy(puzzle)


print('1/4...')
# +For QUAD 1,2,3
# +These for loops check each horizontal quadrant with the others,
# to see which permutations not only works with the givens but the
# other permutations in the other cells horizontal to it.
for g in quad1ListWorks:
    for h in quad2ListWorks:
        for y in quad3ListWorks:

            counter2 = 0
            guess = np.copy(puzzle)

            for m in range(0,3,1):

                for n in range(0,3,1):

                    if guess[m,n] == 0:
                        guess[m,n] = quad1List[g][count]
                        count += 1
                        #print(count)

                for o in range(3,6,1):
                    if guess[m,o] == 0:
                        guess[m,o] = quad2List[h][counter]
                        counter += 1
                        #print(g)
                        #print(counter)

                for a in range(6,9,1):
                    if guess[m,a] == 0:
                        guess[m,a] = quad3List[y][counterer]
                        counterer += 1
                        #print(counterer)
                    if counterer == len(quad3List[0]):
                        counterer = 0


            q = Check2(guess)
            for f in range(0,3,1):
                for t in range(0,9,1):

                    if (q.checkVerticalFinal(t,guess[f,t]) != 1 or
                        q.checkHorizontalFinal(f,guess[f,t]) != 1 or
                        q.checkQuadrantFinal(f,t,guess[f,t]) != 1):
                        #print('meh')
                        pass
                    else:
                        counter2 += 1
                        #print(counter2)
                        if counter2 >= 27:
                            unitedList1.append(g)
                            unitedList2.append(h)
                            unitedList3.append(y)

            #unitedList1.append(counter2)
            #print(counter2)
            #counter2 = 0
            #print('break')
            count = 0
            counter = 0
            counterer = 0
            #print(quad1List[g])
            #print(quad2List[h])
            #print(g,h)
            #print(guess)
            #if counter2 >= 12:
                #print(guess)
                #print(counter2)

guess = np.copy(puzzle)
print('2/4...')
# For QUAD 4,5,6
for z in quad4ListWorks:
    for w in quad5ListWorks:
        for e in quad6ListWorks:

            counter2 = 0
            guess = np.copy(puzzle)

            for m in range(3,6,1):

                for n in range(0,3,1):

                    if guess[m,n] == 0:
                        guess[m,n] = quad4List[z][count]
                        count += 1
                        #print(count)

                for o in range(3,6,1):
                    if guess[m,o] == 0:
                        guess[m,o] = quad5List[w][counter]
                        counter += 1
                        #print(g)
                        #print(counter)

                for a in range(6,9,1):
                    if guess[m,a] == 0:
                        guess[m,a] = quad6List[e][counterer]
                        counterer += 1
                        #print(counterer)
                    if counterer == len(quad6List[0]):
                        counterer = 0

            #print(guess)
            q = Check2(guess)
            for f in range(3,6,1):
                for t in range(0,9,1):

                    if (q.checkVerticalFinal(t,guess[f,t]) != 1 or
                        q.checkHorizontalFinal(f,guess[f,t]) != 1 or
                        q.checkQuadrantFinal(f,t,guess[f,t]) != 1):
                        #print('meh')
                        pass
                    else:
                        counter2 += 1
                        #print(counter2)
                        if counter2 >= 27:
                            unitedList4.append(z)
                            unitedList5.append(w)
                            unitedList6.append(e)
                            #print(guess)
                            #print(counter2)
                            #print(guess)
            #unitedList1.append(counter2)
            #print(counter2)
            #counter2 = 0
            #print('break')
            count = 0
            counter = 0
            counterer = 0
            #print(quad1List[g])
            #print(quad2List[h])
            #print(g,h)
            #print(guess)
            #if counter2 >= 12:
                #print(guess)
                #print(counter2)

print('3/4...')
# For QUAD 7,8,9
for u in quad7ListWorks:
    for i in quad8ListWorks:
        for d in quad9ListWorks:

            counter2 = 0
            guess = np.copy(puzzle)

            for m in range(6,9,1):

                for n in range(0,3,1):

                    if guess[m,n] == 0:
                        guess[m,n] = quad7List[u][count]
                        count += 1
                        #print(count)

                for o in range(3,6,1):
                    if guess[m,o] == 0:
                        guess[m,o] = quad8List[i][counter]
                        counter += 1
                        #print(g)
                        #print(counter)

                for a in range(6,9,1):
                    if guess[m,a] == 0:
                        guess[m,a] = quad9List[d][counterer]
                        counterer += 1
                        #print(counterer)
                    if counterer == len(quad9List[0]):
                        counterer = 0

            #print(guess)
            q = Check2(guess)
            for f in range(6,9,1):
                for t in range(0,9,1):

                    if (q.checkVerticalFinal(t,guess[f,t]) != 1 or
                        q.checkHorizontalFinal(f,guess[f,t]) != 1 or
                        q.checkQuadrantFinal(f,t,guess[f,t]) != 1):
                        #print('meh')
                        pass
                    else:
                        counter2 += 1
                        #print(counter2)
                        if counter2 >= 27:
                            unitedList7.append(u)
                            unitedList8.append(i)
                            unitedList9.append(d)
                            #print(guess)
            count = 0
            counter = 0
            counterer = 0


print('FINAL STEP...')

answer1a = []
answer2a = []
answer3a = []
answer4a = []
answer5a = []
answer6a = []

answer1 = []
answer2 = []
answer3 = []
answer4 = []
answer5 = []
answer6 = []
answer7 = []
answer8 = []
answer9 = []

count = 0
counter = 0
counterer = 0
countx = 0
countc = 0
countv = 0
countb = 0
countn = 0
countm = 0

#print('u:',unitedList1)
#print('u:',unitedList4)
#print('u:',unitedList7)

# + FOR FINAL PROGRAM, take the united lists from rows 1-3, 3-6 & 6-9,
# take those and run them below to see which alignment of the
# permutations for each cell agree with the others.
# + Depending on difficulty of sudoku puzzle, these three for loops
# can sometimes take VERY long to run.



for i in range(len(unitedList1)):

        for j in range(len(unitedList4)):


                #print('meh')
                counter2 = 0
                guess = np.copy(puzzle)

                for m in range(0, 3, 1):

                    for n in range(0, 3, 1):

                        if guess[m, n] == 0:
                            guess[m, n] = quad1List[unitedList1[i]][count]
                            count += 1
                            # print(count)

                    for o in range(3, 6, 1):
                        if guess[m, o] == 0:
                            guess[m, o] = quad2List[unitedList2[i]][counter]
                            counter += 1
                    # print(g)
                    # print(counter)
                    for a in range(6, 9, 1):
                        if guess[m, a] == 0:
                            guess[m, a] = quad3List[unitedList3[i]][counterer]
                            counterer += 1
                    # print(counterer)
                        if counterer == len(quad3List[0]):
                            counterer = 0


                for g in range(3, 6, 1):
                    for n in range(0, 3, 1):

                        if guess[g, n] == 0:
                            guess[g, n] = quad4List[unitedList4[j]][countx]
                            countx += 1
                            # print(count)

                    for o in range(3, 6, 1):
                        if guess[g, o] == 0:
                            guess[g, o] = quad5List[unitedList5[j]][countc]
                            countc += 1
                    # print(g)
                    # print(counter)
                    for a in range(6, 9, 1):
                        if guess[g, a] == 0:
                            guess[g, a] = quad6List[unitedList6[j]][countv]
                            countv += 1
                            # print(counterer)
                        if countv == len(quad6List[0]):
                            countv = 0


                q = Check2(guess)
                for f in range(0, 6, 1):
                    for t in range(0, 9, 1):

                        if (q.checkVerticalFinal(t, guess[f, t]) != 1 or
                            q.checkHorizontalFinal(f, guess[f, t]) != 1 or
                            q.checkQuadrantFinal(f, t, guess[f, t]) != 1):
                            #print('meh')
                            pass
                        else:
                            counter2 += 1

                            if counter2 >= 54:
                                answer1a.append(unitedList1[i])
                                answer2a.append(unitedList2[i])
                                answer3a.append(unitedList3[i])
                                answer4a.append(unitedList4[j])
                                answer5a.append(unitedList5[j])
                                answer6a.append(unitedList6[j])


                #print(counter2)

                count = 0
                counter = 0
                counterer = 0
                countx = 0
                countc = 0
                countv = 0
                countb = 0
                countn = 0
                countm = 0

for i in range(len(answer1a)):

            for k in range(len(unitedList7)):

                #print('meh')
                counter2 = 0
                guess = np.copy(puzzle)

                for m in range(0, 3, 1):

                    for n in range(0, 3, 1):

                        if guess[m, n] == 0:
                            guess[m, n] = quad1List[answer1a[i]][count]
                            count += 1
                            # print(count)

                    for o in range(3, 6, 1):
                        if guess[m, o] == 0:
                            guess[m, o] = quad2List[answer2a[i]][counter]
                            counter += 1
                    # print(g)
                    # print(counter)

                    for a in range(6, 9, 1):
                        if guess[m, a] == 0:
                            guess[m, a] = quad3List[answer3a[i]][counterer]
                            counterer += 1
                    # print(counterer)
                        if counterer == len(quad3List[0]):
                            counterer = 0
                for g in range(3, 6, 1):
                    for n in range(0, 3, 1):

                        if guess[g, n] == 0:
                            guess[g, n] = quad4List[answer4a[i]][countx]
                            countx += 1
                            # print(count)

                    for o in range(3, 6, 1):
                        if guess[g, o] == 0:
                            guess[g, o] = quad5List[answer5a[i]][countc]
                            countc += 1
                    # print(g)
                    # print(counter)

                    for a in range(6, 9, 1):
                        if guess[g, a] == 0:
                            guess[g, a] = quad6List[answer6a[i]][countv]
                            countv += 1
                    # print(counterer)
                        if countv == len(quad6List[0]):
                            countv = 0
                for w in range(6, 9, 1):
                    for n in range(0, 3, 1):

                        if guess[w, n] == 0:
                            guess[w, n] = quad7List[unitedList7[k]][countb]
                            countb += 1
                            # print(count)

                    for o in range(3, 6, 1):
                        if guess[w, o] == 0:
                            guess[w, o] = quad8List[unitedList8[k]][countn]
                            countn += 1
                            # print(g)
                            # print(counter)

                    for a in range(6, 9, 1):
                        if guess[w, a] == 0:
                            guess[w, a] = quad9List[unitedList9[k]][countm]
                            countm += 1
                    # print(counterer)
                        if countm == len(quad9List[0]):
                            countm = 0
                q = Check2(guess)
                for f in range(0, 9, 1):
                    for t in range(0, 9, 1):

                        if (q.checkVerticalFinal(t, guess[f, t]) != 1 or
                            q.checkHorizontalFinal(f, guess[f, t]) != 1 or
                            q.checkQuadrantFinal(f, t, guess[f, t]) != 1):
                            #print('meh')
                            pass
                        else:
                            counter2 += 1

                            if counter2 >= 81:
                                answer1.append(answer1a[i])
                                answer2.append(answer2a[i])
                                answer3.append(answer3a[i])
                                answer4.append(answer4a[i])
                                answer5.append(answer5a[i])
                                answer6.append(answer6a[i])
                                answer7.append(unitedList7[k])
                                answer8.append(unitedList8[k])
                                answer9.append(unitedList9[k])
                                break
                #print(counter2)

                count = 0
                counter = 0
                counterer = 0
                countx = 0
                countc = 0
                countv = 0
                countb = 0
                countn = 0
                countm = 0



print('SOLUTION:')
print(answer1)
print(answer2)
print(answer3)
print(answer4)
print(answer5)
print(answer6)
print(answer7)
print(answer8)
print(answer9)


# +Below this is used in order to print out the final sudoku
# puzzle that my program came up with
print('FINAL SOLUTION:')
finalSolution = np.copy(puzzle)
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
count7 = 0
count8 = 0
count9 = 0
for i in range(0,3,1):
    for j in range(0,3,1):
        if finalSolution[i,j] == 0:
            finalSolution[i,j] = quad1List[answer1[0]][count1]
            count1 += 1
    for k in range(3,6,1):
        if finalSolution[i,k] == 0:
            finalSolution[i,k] = quad2List[answer2[0]][count2]
            count2 += 1
    for l in range(6,9,1):
        if finalSolution[i,l] == 0:
            finalSolution[i,l] = quad3List[answer3[0]][count3]
            count3 += 1
for g in range(3,6,1):
    for h in range(0,3,1):
        if finalSolution[g,h] == 0:
            finalSolution[g,h] = quad4List[answer4[0]][count4]
            count4 += 1
    for t in range(3,6,1):
        if finalSolution[g,t] == 0:
            finalSolution[g,t] = quad5List[answer5[0]][count5]
            count5 += 1
    for y in range(6,9,1):
        if finalSolution[g,y] == 0:
            finalSolution[g,y] = quad6List[answer6[0]][count6]
            count6 += 1
for g in range(6,9,1):
    for h in range(0,3,1):
        if finalSolution[g,h] == 0:
            finalSolution[g,h] = quad7List[answer7[0]][count7]
            count7 += 1
    for t in range(3,6,1):
        if finalSolution[g,t] == 0:
            finalSolution[g,t] = quad8List[answer8[0]][count8]
            count8 += 1
    for y in range(6,9,1):
        if finalSolution[g,y] == 0:
            finalSolution[g,y] = quad9List[answer9[0]][count9]
            count9 += 1

print(finalSolution)


end = time.time()

print("Runtime of program:{}".format(end-start))