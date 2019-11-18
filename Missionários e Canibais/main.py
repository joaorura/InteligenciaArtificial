from q import _Queue
from node import Node
import utils


class Problem:
    def __init__(self, m, c, m_end, c_end, size_queue=100):
        utils.check_type(int, m)
        utils.check_type(int, c)

        if m < c or m_end < c_end:
            raise ValueError

        self.result = None
        self.border = _Queue()
        self.root = Node(1, [m, 0], [c, 0])

        self.queue = _Queue(size_queue)

        self.end = ([0, m_end], [0, c_end])

    @staticmethod
    def _get_path(node):
        path = _Queue()
        path.put(node)

        while True:
            node = node.father

            if node is None:
                break
            else:
                path.put(node)

        path.reverse()
        return path

    def _put_in_border(self, elements):
        for i in elements:
            self.border.put(i)

    def _start(self):
        self.queue.put(self.root)
        aux = self.root.father_children(self.queue)
        self._put_in_border(aux)

        while True:
            if self.border.empty():
                return 'No solution'

            now = self.border.get()
            # debug
            # print(f'The: {now}')
            # print(f'Border: {self.border}')
            if now.m == self.end[0] and now.c == self.end[1]:
                self.result = self._get_path(now)

            kids = now.father_children(self.queue)
            self._put_in_border(kids)

    def get_result(self):
        if self.result is None:
            self._start()

        return self.result


def main():
    problem = Problem(3, 3, 3, 3)
    print(problem.get_result())


if __name__ == '__main__':
    main()
