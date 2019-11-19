from utils import check_type
from copy import deepcopy


data = [
    [0, 11, 20, 27, 40, 43, 39, 28, 18, 10, 18, 30, 30, 32],
    [11, 0, 9, 16, 29, 32, 28, 19, 11, 4, 17, 23, 21, 24],
    [20, 9, 0, 7, 20, 22, 19, 15, 10, 11, 21, 21, 13, 18],
    [27, 16, 7, 0, 13, 16, 12, 13, 13, 18, 26, 21, 11, 17],
    [40, 29, 20, 13, 0, 3, 2, 21, 25, 31, 38, 27, 16, 20],
    [43, 32, 22, 16, 3, 0, 4, 23, 28, 33, 41, 30, 17, 20],
    [39, 28, 19, 12, 2, 4, 0, 22, 25, 29, 38, 28, 13, 17],
    [28, 19, 15, 13, 21, 23, 22, 0, 9, 22, 18, 7, 25, 30],
    [18, 11, 10, 13, 25, 28, 25, 9, 0, 13, 12, 12, 23, 28],
    [10, 4, 11, 18, 31, 33, 29, 22, 13, 0, 20, 27, 20, 23],
    [18, 17, 21, 26, 38, 41, 38, 18, 12, 20, 0, 15, 35, 39],
    [30, 23, 21, 21, 27, 30, 28, 7, 12, 27, 15, 0, 31, 37],
    [30, 21, 13, 11, 16, 17, 13, 25, 23, 20, 35, 31, 0, 5],
    [32, 24, 18, 17, 20, 20, 17, 30, 28, 23, 39, 37, 5, 0]
]

test = [
    ['W', 'B', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
    ['B', 'W', 'B', 'W', 'W', 'W', 'W', 'W', 'Y', 'Y', 'W', 'W', 'W', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'W', 'W', 'W', 'R', 'W', 'W', 'W', 'R', 'W'],
    ['W', 'W', 'B', 'W', 'B', 'W', 'W', 'G', 'W', 'W', 'W', 'W', 'G', 'W'],
    ['W', 'W', 'W', 'B', 'W', 'B', 'Y', 'Y', 'W', 'W', 'W', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'W', 'B', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'W', 'Y', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'G', 'Y', 'W', 'W', 'W', 'Y', 'W', 'W', 'G', 'W', 'W'],
    ['W', 'Y', 'R', 'W', 'W', 'W', 'W', 'Y', 'W', 'W', 'R', 'W', 'W', 'W'],
    ['W', 'Y', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'R', 'W', 'W', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'G', 'W', 'W', 'W', 'W', 'W', 'W'],
    ['W', 'W', 'R', 'G', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'G'],
    ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'G', 'W']
]

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
        self.heuristic = heuristic
        self.result = None

    def _start(self):
        pass

    def get_result(self):
        if self.result is None:
            self._start()

        return self.result


def main():
    pass
    # problem = Problem(0, 3, 4, data)
    # print(problem.get_result())


if __name__ == '__main__':
    main()
