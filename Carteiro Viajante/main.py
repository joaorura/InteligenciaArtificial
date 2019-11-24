from group import Group
from data import graph


class Problem:
    def __init__(self, _graph, elements):
        self.graph = _graph
        self.root = Group(_graph, elements, [elements])
        self._solution = None
        self.max = 5

    def _start(self):
        _max = 0
        node_0 = self.root
        old = self.root
        while True:
            if _max == self.max:
                break

            node_1 = node_0.copy()

            if node_1.permutate() == -1:
                break

            node_0 = min(node_0, node_1)

            if node_0 == old:
                _max += 1
            else:
                old = node_0

        self._solution = node_0

    def get_solution(self):
        if self._solution is None:
            self._start()

        return self._solution


def main():
    problem = Problem(graph, graph.vertex)
    print(problem.get_solution())


if __name__ == '__main__':
    main()
