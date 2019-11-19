from _ast import keyword

from utils import check_type


class Node:
    def __init__(self, weight, station, line, father=None):
        check_type(int, station)
        check_type(int, line)

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
