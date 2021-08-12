from numba import jit


class Check2:

    def __init__(self, guess):
        self.guess = guess


    def checkVerticalFinal(self, column, guessNumber):

        counter = 0

        for i in range(0,9,1):
            if self.guess[i][column] == guessNumber:
                counter += 1

        return counter

    def checkHorizontalFinal(self, row, guessNumber):

        counter = 0

        for i in range(0, 9, 1):
            if self.guess[row][i] == guessNumber:
                counter += 1

        return counter


    def checkQuadrantFinal(self, row, column, guessNumber):
        """
        Looks over the entire quadrant that the guess number
        is in and sees if is there, if it is this prints
        IN QUADRANT and if it's not, it prints NOT IN QUADRANT.
        """

        rowDiv = (row+1) / 3.0
        colDiv = (column+1) / 3.0
        state = 0
        counter = 0

        if 0.0 <= rowDiv <= 1.0:
            for i in range(0, 3, 1):
                # Quad 1
                if 0.0 <= colDiv <= 1.0:
                    for j in range(0, 3, 1):
                        if self.guess[i][j] == guessNumber:
                            state = 1
                            counter += 1
                # Quad 2
                if 1.0 < colDiv <= 2.0:
                    for j in range(3, 6, 1):
                        if self.guess[i][j] == guessNumber:
                            state = 1
                            counter += 1
                # Quad 3
                if 2.0 < colDiv <= 3.0:
                    for j in range(6, 9, 1):
                        if self.guess[i][j] == guessNumber:
                            state = 1
                            counter += 1

        if 1.0 < rowDiv <= 2.0:
            for i in range(3, 6, 1):
                # Quad 4
                if 0.0 <= colDiv <= 1.0:
                    for j in range(0, 3, 1):
                        if self.guess[i][j] == guessNumber:
                            state = 1
                            counter += 1
                # Quad 5
                if 1.0 < colDiv <= 2.0:
                    for j in range(3, 6, 1):
                        if self.guess[i][j] == guessNumber:
                            state = 1
                            counter += 1
                # Quad 6
                if 2.0 < colDiv <= 3.0:
                    for j in range(6, 9, 1):
                        if self.guess[i][j] == guessNumber:
                            state = 1
                            counter += 1

        if 2.0 < rowDiv <= 3.0:
            for i in range(6,9,1):
                # Quad 7
                if 0.0 <= colDiv <= 1.0:
                    for j in range(0, 3, 1):
                        if self.guess[i][j] == guessNumber:
                            state = 1
                            counter += 1
                # Quad 8
                if 1.0 < colDiv <= 2.0:
                    for j in range(3, 6, 1):
                        if self.guess[i][j] == guessNumber:
                            state = 1
                            counter += 1
                # Quad 9
                if 2.0 < colDiv <= 3.0:
                    for j in range(6, 9, 1):
                        if self.guess[i][j] == guessNumber:
                            state = 1
                            counter += 1

        return counter