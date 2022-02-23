
import numpy as np

from my_monte_carlo_tree_search import MCTS
from Check import Check


def play_game():

    tree = MCTS()
    sud_board = new_sudoku_board()

    while True:

        for _ in range(1000):
            tree.do_rollout(sud_board)
        board = tree.choose(sud_board)
        board_reshape = np.reshape(board, (9, 9))
        c = Check(board_reshape)
        if c.determineNumberOfZeros() == 0:
            print('COMPLETION!')
            print(board_reshape)
            break
        print(np.reshape(board, (9, 9)))
        sud_board = board

def new_sudoku_board():
    board = tuple((0, 0, 0, 0, 0, 8, 3, 0, 0, 0, 0, 0, 0, 2, 4, 0, 9, 0, 0, 0, 4, 0, 7, 0, 0, 0, 6,
                   0, 0, 0, 0, 0, 3, 0, 7, 9, 7, 5, 0, 0, 0, 0, 0, 8, 4, 9, 2, 0, 5, 0, 0, 0, 0, 0,
                   4, 0, 0, 0, 9, 0, 1, 0, 0, 0, 3, 0, 4, 6, 0, 0, 0, 0, 0, 0, 5, 8, 0, 0, 0, 0, 0))

    #board = tuple((6, 9, 7, 8, 0, 2, 5, 4, 0, 3, 4, 1, 0, 5, 9, 6, 8, 2, 8, 2, 5, 6, 4, 1, 3, 9, 7,
    #               1, 7, 8, 2, 6, 3, 9, 5, 4, 2, 5, 6, 4, 9, 7, 8, 1, 3, 9, 3, 4, 1, 8, 5, 2, 7, 6,
    #               7, 6, 2, 5, 1, 8, 4, 3, 9, 4, 8, 9, 3, 7, 6, 1, 2, 5, 5, 1, 3, 9, 2, 4, 7, 6, 8))
    return board


if __name__ == '__main__':
    play_game()

