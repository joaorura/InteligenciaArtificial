from copy import deepcopy
from utils import check_type


class Node:
    def __init__(self, weight, station, line, father=None):
        check_type(int, weight)
        check_type(int, station)
        check_type(str, line)

        if father is not None:
            check_type(Node, father)

        self.weight = weight
        self.station = station
        self.line = line
        self.father = father

        self.children = []

    def __eq__(self, other):
        check_type(Node, other)
        return self.weight == other.weight and self.station == other.station and self.line == other.line

    def __lt__(self, other):
        check_type(Node, other)
        return self.weight < other.weight

    def add_children(self, kids):
        k_d = type(kids)

        if k_d == Node:
            self.children.append(Node)
        elif k_d == list:
            for i in kids:
                self.children.append(i)
        else:
            raise ValueError

    def _generate(self, element, base, problem):
        base = deepcopy(base)

        base.line = element[1]
        base.station = element[0]

        if element[1] != self.line:
            base.weight += 2
        base.weight += problem.heuristic[self.station][element[0]]

        return base

    def generate_children(self, problem):
        elements = []
        base = deepcopy(self)
        base.father = self
        base.children.clear()

        for i in problem.lines[self.station]:
            aux = self._generate(i, base, problem)
            if aux not in problem.elements:
                self.children.append(aux)
                problem.elements.put(aux)
                elements.append(aux)

        return elements
