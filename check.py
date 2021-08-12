
class Check:

    def __init__(self, final):
        self.final = final

    def whatUniqueNumbInQuad(self, quadrant):
        list = []

        if quadrant == 1:
            for i in range(0,3):
                for j in range(0,3):
                    if self.final[i,j] != 0:
                        list.append(self.final[i,j])

        if quadrant == 2:
            for i in range(0,3):
                for j in range(3,6):
                    if self.final[i,j] != 0:
                        list.append(self.final[i,j])

        if quadrant == 3:
            for i in range(0,3):
                for j in range(6,9):
                    if self.final[i,j] != 0:
                        list.append(self.final[i,j])

        if quadrant == 4:
            for i in range(3,6):
                for j in range(0,3):
                    if self.final[i,j] != 0:
                        list.append(self.final[i,j])

        if quadrant == 5:
            for i in range(3,6):
                for j in range(3,6):
                    if self.final[i,j] != 0:
                        list.append(self.final[i,j])

        if quadrant == 6:
            for i in range(3,6):
                for j in range(6,9):
                    if self.final[i,j] != 0:
                        list.append(self.final[i,j])

        if quadrant == 7:
            for i in range(6,9):
                for j in range(0,3):
                    if self.final[i,j] != 0:
                        list.append(self.final[i,j])

        if quadrant == 8:
            for i in range(6,9):
                for j in range(3,6):
                    if self.final[i,j] != 0:
                        list.append(self.final[i,j])

        if quadrant == 9:
            for i in range(6,9):
                for j in range(6,9):
                    if self.final[i,j] != 0:
                        list.append(self.final[i,j])
        numbList = [1,2,3,4,5,6,7,8,9]
        newList = []

        for k in range(9):
            if numbList[k] not in list:
                newList.append(numbList[k])

        return newList

    def checkVertical(self, column, guessNumber):
        """
        Looks over the entire column and checks to see if
        the guess number exists anywhere in it.
        """
        j = column
        state = 0
        counter = 0

        for m in range(0, 9, 1):
            if self.final[m][j] == guessNumber:
                state = 1

        return state

    def checkHorizontal(self, row, guessNumber):
        """
        Looks at the entire row and sees if the guess number
        exists in it.
        """
        i = row
        state = 0

        for n in range(0,9,1):
            if self.final[i][n] == guessNumber:
                state = 1

        return state

    def checkQuadrant(self, row, column, guessNumber):
        """
        Looks over the entire quadrant that the guess number
        is in and sees if is there, if it is this prints
        IN QUADRANT and if it's not, it prints NOT IN QUADRANT.
        """

        rowDiv = (row+1) / 3.0
        colDiv = (column+1) / 3.0
        #print('rowdiv:', rowDiv)
        #print('coldiv:', colDiv)
        state = 0

        if 0.0 <= rowDiv <= 1.0:
            for i in range(0, 3, 1):
                # Quad 1
                if 0.0 <= colDiv <= 1.0:
                    for j in range(0, 3, 1):
                        if self.final[i][j] == guessNumber:
                            state = 1
                # Quad 2
                if 1.0 < colDiv <= 2.0:
                    for j in range(3, 6, 1):
                        if self.final[i][j] == guessNumber:
                            #print('meh')
                            state = 1
                # Quad 3
                if 2.0 < colDiv <= 3.0:
                    for j in range(6, 9, 1):
                        if self.final[i][j] == guessNumber:
                            #print('meh')
                            state = 1

        if 1.0 < rowDiv <= 2.0:
            for i in range(3, 6, 1):
                # Quad 4
                if 0.0 <= colDiv <= 1.0:
                    for j in range(0, 3, 1):
                        if self.final[i][j] == guessNumber:
                            state = 1
                # Quad 5
                if 1.0 < colDiv < 2.0:
                    for j in range(3, 6, 1):
                        if self.final[i][j] == guessNumber:
                            state = 1
                # Quad 6
                if 2.0 < colDiv <= 3.0:
                    for j in range(6, 9, 1):
                        if self.final[i][j] == guessNumber:
                            state = 1

        if 2.0 < rowDiv <= 3.0:
            for i in range(6,9,1):
                # Quad 7
                if 0.0 <= colDiv <= 1.0:
                    for j in range(0, 3, 1):
                        if self.final[i][j] == guessNumber:
                            state = 1
                # Quad 8
                if 1.0 < colDiv <= 2.0:
                    for j in range(3, 6, 1):
                        if self.final[i][j] == guessNumber:
                            state = 1
                # Quad 9
                if 2.0 < colDiv <= 3.0:
                    for j in range(6, 9, 1):
                        if self.final[i][j] == guessNumber:
                            state = 1

        return state

