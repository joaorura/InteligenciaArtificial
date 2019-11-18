from q import _Queue
from tree import Node, Tree
import utils


class Problem:
    def __init__(self, m, c, m_end, c_end):
        utils.check_type(int, m)
        utils.check_type(int, c)

        if m < c:
            raise ValueError

        self.border = _Queue()

        self.m = [m, 0]
        self.c = [c, 0]
        root = Node(1, self.m, self.c, _Queue(100))

        self.tree = Tree(root)

        m_end = [0, m_end]
        c_end = [0, c_end]
        self.end = Node(0, m_end, c_end)

    @staticmethod
    def _get_path(node):
        path = []

        while True:
            aux = node.father

            if aux is None:
                return path
            else:
                path.append(aux)

    def _put_in_border(self, elements):
        for i in elements:
            self.border.put(i)

    def start(self):
        aux = self.tree.root.father_children()
        self._put_in_border(aux)

        while True:
            if self.border.empty():
                return 'No solution'

            now = self.border.get()
            print(f'The: {now}')
            print(f'Border: {self.border}')
            if now == self.end:
                return self._get_path(now)

            kids = now.father_children()
            self._put_in_border(kids)


def main():
    problem = Problem(3, 3, 3, 3)
    print(problem.start())


if __name__ == '__main__':
    main()
