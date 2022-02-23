"""
Work that is largely inspired from
https://gist.github.com/qpwo/c538c6f73727e254fdc7fab81024f6e1

"""

from collections import defaultdict
from abc import ABC, abstractmethod
from Check import Check

import math
import random

import numpy as np


class MCTS:

    def __init__(self, exploration_weight=0.9):
        self.Q = defaultdict(int)
        self.N = defaultdict(int)
        self.children = dict()  # children of each node
        self.exploration_weight = exploration_weight

    def choose(self, node):
        if node not in self.children:
            return self.find_random_child(node)
        def score(n):
            if self.N[n] == 0:
                return float('-inf')
            return self.Q[n] / self.N[n]
        return max(self.children[node], key=score)

    def do_rollout(self, node):
        """Make the tree one layer better."""

        path = self._select(node)
        leaf = path[-1]
        self._expand(leaf)
        reward = self._simulate(leaf)
        self._backpropagate(path, reward)

    def _select(self, node):
        """Find an unexplored descendant of `node`"""
        path = []

        while True:
            path.append(node)
            if node not in self.children or not self.children[node]:
                return path

            unexplored = self.children[node] - self.children.keys()
            if unexplored:
                n = unexplored.pop()
                path.append(n)
                return path

            node = self._uct_select(node)

    def _expand(self, node):
        """Update the `children` dict with the children of node"""
        if node in self.children:
            return
        self.children[node] = self.find_children(node)

    def _simulate(self, node):
        """Returns the reward for a random simulation (to completion) """
        while True:
            node_reshaped = np.reshape(node, (9, 9))
            c = Check(node_reshaped)
            if c.determineNumberOfZeros() == 0:
                if self.is_bad_terminal(node):
                    reward = -1
                    return reward
                if self.is_good_terminal(node):
                    reward = 1
                    #print(reward)
                    return reward

            node = self.find_random_child(node)

    def _backpropagate(self, path, reward):
        """Send the reward back up to the ancestors of the leaf"""
        for node in reversed(path):

            self.N[node] += 1
            self.Q[node] += reward
        # print(path, reward)

    def _uct_select(self, node):

        log_N_vertex = math.log(self.N[node])

        def uct(n):
            return self.Q[n] / self.N[n] + self.exploration_weight \
                    * math.sqrt(log_N_vertex / self.N[n])

        return max(self.children[node], key=uct)


    def is_bad_terminal(self, node):
        node_reshaped = np.reshape(node, (9, 9))

        # Check rows
        for i in range(0,9,1):
            numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for j in range(0,9,1):
                try: numbers.remove(node_reshaped[i][j])
                except ValueError: pass
            # print("GERANIMO:", len(numbers))

            if len(numbers) != 0:
                return True

        # Check rows
        for i in range(0, 9, 1):
            numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for j in range(0, 9, 1):
                try:
                    numbers.remove(node_reshaped[j][i])
                except ValueError:
                    pass
            #print('beep')
            if len(numbers) != 0:
                return True

        # Check Quadrants
        # 1
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(0,3,1):
            for j in range(0,3,1):
                try:numbers.remove(node_reshaped[i][j])
                except ValueError: pass
        if len(numbers) != 0:
            return True
        # 2
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(0, 3, 1):
            for j in range(3, 6, 1):
                try:
                    numbers.remove(node_reshaped[i][j])
                except ValueError:
                    pass
        if len(numbers) != 0:
            return True
        # 3
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(0, 3, 1):
            for j in range(6, 9, 1):
                try:
                    numbers.remove(node_reshaped[i][j])
                except ValueError:
                    pass
        if len(numbers) != 0:
            return True

        # 4
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(3, 6, 1):
            for j in range(0, 3, 1):
                try:
                    numbers.remove(node_reshaped[i][j])
                except ValueError:
                    pass
        if len(numbers) != 0:
            return True
        # 5
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(3, 6, 1):
            for j in range(3, 6, 1):
                try:
                    numbers.remove(node_reshaped[i][j])
                except ValueError:
                    pass
        if len(numbers) != 0:
            return True
        # 6
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(3, 6, 1):
            for j in range(6, 9, 1):
                try:
                    numbers.remove(node_reshaped[i][j])
                except ValueError:
                    pass
        if len(numbers) != 0:
            return True

        # 7
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(6, 9, 1):
            for j in range(0, 3, 1):
                try:
                    numbers.remove(node_reshaped[i][j])
                except ValueError:
                    pass
        if len(numbers) != 0:
            return True
        # 8
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(6, 9, 1):
            for j in range(3, 6, 1):
                try:
                    numbers.remove(node_reshaped[i][j])
                except ValueError:
                    pass
        if len(numbers) != 0:
            return True
        # 9
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(6, 9, 1):
            for j in range(6, 9, 1):
                try:
                    numbers.remove(node_reshaped[i][j])
                except ValueError:
                    pass
        if len(numbers) != 0:
            return True

    def is_good_terminal(self, node):
        node_reshaped = np.reshape(node, (9, 9))
        c = Check(node_reshaped)

        # Check columns
        for i in range(0,9,1):
            numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for j in range(0,9,1):
                try:
                    numbers.remove(node_reshaped[i][j])
                except ValueError:
                    pass
            if len(numbers) != 0:
                return False

        # Check rows
        for i in range(0, 9, 1):
            numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for j in range(0, 9, 1):
                try:
                    numbers.remove(node_reshaped[i][j])
                except ValueError:
                    pass
            if len(numbers) != 0:
                return False

        # Check Quadrants
        # 1
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(0,3,1):
            for j in range(0,3,1):
                try:
                    numbers.remove(node_reshaped[i][j])
                except ValueError:
                    pass
        if len(numbers) != 0:
            return False
        # 2
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(0, 3, 1):
            for j in range(3, 6, 1):
                try:
                    numbers.remove(node_reshaped[i][j])
                except ValueError:
                    pass
        if len(numbers) != 0:
            return False
        # 3
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(0, 3, 1):
            for j in range(6, 9, 1):
                try:
                    numbers.remove(node_reshaped[i][j])
                except ValueError:
                    pass
        if len(numbers) != 0:
            return False

        # 4
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(3, 6, 1):
            for j in range(0, 3, 1):
                try:
                    numbers.remove(node_reshaped[i][j])
                except ValueError:
                    pass
        if len(numbers) != 0:
            return False
        # 5
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(3, 6, 1):
            for j in range(3, 6, 1):
                try:
                    numbers.remove(node_reshaped[i][j])
                except ValueError:
                    pass
        if len(numbers) != 0:
            return False
        # 6
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(3, 6, 1):
            for j in range(6, 9, 1):
                try:
                    numbers.remove(node_reshaped[i][j])
                except ValueError:
                    pass
        if len(numbers) != 0:
            return False

        # 7
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(6, 9, 1):
            for j in range(0, 3, 1):
                try:
                    numbers.remove(node_reshaped[i][j])
                except ValueError:
                    pass
        if len(numbers) != 0:
            return False
        # 8
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(6, 9, 1):
            for j in range(3, 6, 1):
                try:
                    numbers.remove(node_reshaped[i][j])
                except ValueError:
                    pass
        if len(numbers) != 0:

            return False
        # 9
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(6, 9, 1):
            for j in range(6, 9, 1):
                try:
                    numbers.remove(node_reshaped[i][j])
                except ValueError:
                    pass
        if len(numbers) != 0:

            return False

        return True



    def find_children(self, node):
        openings = []
        for i in range(len(node)):
            if node[i] == 0:
                openings.append(i)
        print(openings)
        return {self.cycle_nine(i, k, node) for i in openings for k in range(1, 10, 1)}

    def cycle_nine(self, index, number, node):
        node_reshaped = np.array(node)
        node_reshaped[index] = number
        return tuple(node_reshaped)

    def find_random_child(self, node):
        possibilities = []
        node_reshaped = np.array(node)
        for i in range(len(node_reshaped)):
            if node_reshaped[i] == 0:
                possibilities.append(i)
        random_index = random.choice(possibilities)

        numbers = [1,2,3,4,5,6,7,8,9]
        random_number = random.choice(numbers)
        node_reshaped[random_index] = random_number

        return tuple(node_reshaped)


