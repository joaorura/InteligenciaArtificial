from copy import deepcopy
from back.game import Game, LOCALS


class Node:
    def __init__(self, game, father=None):
        self.game = game
        self.father = father

        self.weight = None
        self.avaliation()
        self.children = []

    def avaliation(self):
        self.weight = self.game.check()[1]

    def copy(self):
        aux = deepcopy(self)
        aux.father = self
        aux.children.clear()

        return aux



