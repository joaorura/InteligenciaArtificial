import interface
from utils import check_type
from queue import PriorityQueue
from list_s import list_s
from node import Node
import data


class Problem:
    def __init__(self, station_initial, line_initial, station_final, amount_lines, lines, heuristic, amount_elements=100):
        check_type(int, station_initial)
        check_type(int, station_final)
        check_type(int, amount_lines)

        check_type(list, heuristic)
        if len(heuristic) == 0 or station_initial not in lines.keys() or \
                station_final not in lines.keys():
            raise ValueError
        check_type(list, heuristic[0])

        self.station_initial = station_initial
        self.line_initial = line_initial
        self.station_final = station_final
        self.amount_lines = amount_lines
        self.lines = lines
        self.heuristic = heuristic

        self.result = None
        self.root = Node(0, station_initial, line_initial)
        self.border = PriorityQueue()
        self.elements = list_s(amount_elements)

    def _put_in_border(self, _list):
        for i in _list:
            self.border.put(i)

    def _get_path(self, element):
        _list = [element]

        while True:
            element = element.father

            if element is None:
                break

            _list.append(element)

        _list.reverse()

        return _list

    def _start(self):
        self.elements.put(self.root)
        aux = self.root.generate_children(self)
        self._put_in_border(aux)

        while True:
            if self.border.empty():
                return None

            now = self.border.get()

            if now.station == self.station_final:
                return self._get_path(now)

            aux = now.generate_children(self)
            self._put_in_border(aux)

    def get_result(self):
        if self.result is None:
            self. result = self._start()

        return self.result


def main():
    a, b, c = interface.start()

    problem = Problem(a, b, c, len(data.heuristic), data.graph, data.heuristic)
    aux = problem.get_result()

    if aux is None:
        print('No way')
        return

    print('{')
    for i in aux:
        print(f'\t{i}')
    print('}')


if __name__ == '__main__':
    main()
