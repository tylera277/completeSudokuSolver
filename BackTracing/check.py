
class Check:

    def __init__(self, puzzle):
        self.puzzle = puzzle


    def checkVertical(self,column, guessNumber):
        """
        +Looks over the entire column and checks to see if
        the guess number exists anywhere in it.
        """

        counter = 0

        for m in range(0, 9, 1):
            if self.puzzle[m][column] == guessNumber:
                counter += 1

        if counter >= 1:
            return False
        else:
            return True


    def checkHorizontal(self, row, guessNumber):
        """
        +Looks at the entire row and sees if the guess number
        exists in it.
        """

        counter = 0

        for n in range(0, 9, 1):
            if self.puzzle[row][n] == guessNumber:
                counter += 1

        if counter >= 1:
            return False
        else:
            return True

    def determineQuadrant(self, row, column):

        quadNum = 0

        if 0 <= row < 3:
            if 0 <= column <3:
                quadNum = 1
            elif 3 <= column <6:
                quadNum = 2
            elif 6 <= column < 9:
                quadNum = 3
        if 3 <= row < 6:
            if 0 <= column < 3:
                quadNum = 4
            elif 3 <= column < 6:
                quadNum = 5
            elif 6 <= column < 9:
                quadNum = 6
        if 6 <= row < 9:
            if 0 <= column < 3:
                quadNum = 7
            elif 3 <= column < 6:
                quadNum = 8
            elif 6 <= column < 9:
                quadNum = 9

        return quadNum


    def checkQuadrant(self, guess, quadNumb):

        counter = 0

        if quadNumb == 1:
            for i in range(0,3,1):
                for j in range(0,3,1):
                    if self.puzzle[i][j] == guess:
                        counter += 1
        elif quadNumb == 2:
            for i in range(0,3,1):
                for j in range(3,6,1):
                    if self.puzzle[i][j] == guess:
                        counter += 1
        elif quadNumb == 3:
            for i in range(0,3,1):
                for j in range(6,9,1):
                    if self.puzzle[i][j] == guess:
                        counter += 1
        elif quadNumb == 4:
            for i in range(3,6,1):
                for j in range(0,3,1):
                    if self.puzzle[i][j] == guess:
                        counter += 1
        elif quadNumb == 5:
            for i in range(3,6,1):
                for j in range(3,6,1):
                    if self.puzzle[i][j] == guess:
                        counter += 1
        elif quadNumb == 6:
            for i in range(3,6,1):
                for j in range(6,9,1):
                    if self.puzzle[i][j] == guess:
                        counter += 1
        elif quadNumb == 7:
            for i in range(6,9,1):
                for j in range(0,3,1):
                    if self.puzzle[i][j] == guess:
                        counter += 1
        elif quadNumb == 8:
            for i in range(6,9,1):
                for j in range(3,6,1):
                    if self.puzzle[i][j] == guess:
                        counter += 1
        elif quadNumb == 9:
            for i in range(6,9,1):
                for j in range(6,9,1):
                    if self.puzzle[i][j] == guess:
                        counter += 1

        if counter >= 1:
            return False
        else:
            return True

    def determineNumberOfZeros(self):

        counter = 0
        for i in range(0,9,1):
            for j in range(0,9,1):
                if self.puzzle[i][j] == 0:
                    counter += 1

        return counter