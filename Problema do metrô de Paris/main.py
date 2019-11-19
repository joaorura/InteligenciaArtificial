from utils import check_type
from queue import PriorityQueue
import data


class Problem:
    def __init__(self, station_initial, station_final, amount_lines, lines, heuristic):
        check_type(int, station_initial)
        check_type(int, station_final)
        check_type(int, amount_lines)

        check_type(list, heuristic)
        if len(heuristic) != 0:
            raise ValueError
        check_type(list, heuristic[0])

        self.station_initial = station_initial
        self.station_final = station_final
        self.amount_lines = amount_lines
        self.lines = lines
        self.heuristic = heuristic

        self.result = None
        self.pq = PriorityQueue()
        self.elements = []

    def _start(self):
        pass

    def get_result(self):
        if self.result is None:
            self._start()

        return self.result


def main():
    pass
    problem = Problem(0, 1, data.graph['amount_colors'], data.graph, data.heuristic)
    print(problem.get_result())


if __name__ == '__main__':
    main()
