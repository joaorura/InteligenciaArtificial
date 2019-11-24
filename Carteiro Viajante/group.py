from copy import copy, deepcopy
from random import randint
from math import factorial


class Group:
    def __init__(self, graph, elements, sorted):
        self.graph = graph
        self.elements = elements
        self.sorted = sorted
        self.size = len(self.elements) - 1
        self.max = factorial(len(elements))
        self.weight = graph.distance_path(self.elements)

    def __eq__(self, other):
        return self.elements == other.elements and self.graph == other.graph

    def __lt__(self, other):
        return self.weight < other.weight

    def __str__(self):
        return f'Path: {self.elements} || Weight: {self.weight}'

    def copy(self):
        aux = copy(self)
        self.elements = deepcopy(self.elements)
        return aux

    def permutate(self):
        if len(self.sorted) == self.max:
            return -1

        copy = deepcopy(self.elements)

        while copy in self.sorted:
            x = randint(0, self.size)

            while True:
                y = randint(0, self.size)
                if x != y:
                    break

            aux = copy[x]
            copy[x] = copy[y]
            copy[y] = aux

        self.sorted.append(copy)
        self.elements = copy
        self.weight = self.graph.distance_path(copy)
