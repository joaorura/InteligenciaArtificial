from copy import deepcopy


class Process:
    def _error_detect(self):
        error = None
        if type(self.amount_m) != int or type(self.amount_c) != int:
            error = 'Error in type of arguments\n'
        elif self.amount_m < self.amount_c:
            error = 'Error instantiating class!\n\tMissionaries less than cannibals.'

        if error is not None:
            raise ValueError(error)

    def __init__(self, amount_c, amount_m, limit):
        self.amount_m = amount_m
        self.amount_c = amount_c
        self._error_detect()

        self.queue = []
        self.path = []
        self.limit = limit

        first = [amount_m, amount_c]
        self.end = first
        boat = [0, 0]
        second = [0, 0]

        self.begin = [2, boat, first, second, None]
        self.border = self._generate_states(self.begin)

    def put(self, _list):
        if len(_list) == 0:
            return

        if len(self.queue) == self.limit:
            del self.queue[0]

        if type(_list) == type(_list[0]):
            self.queue += _list
        else:
            self.queue.append(_list)

    @staticmethod
    def append(list_1, list_2):
        if len(list_2) == 0:
            return

        if type(list_2) == type(list_2[0]):
            list_1 += list_2
        else:
            list_1.append(list_2)

    @staticmethod
    def increase(i):
        i += 1
        if i == 4:
            i = 2

        return i

    def transfer(self, state):
        aux = deepcopy(state)
        aux[4] = state
        i = aux[0] = \
            self.increase(aux[0])

        aux[i][0] += aux[1][0]
        aux[i][1] += aux[1][1]

        aux[1][0] = \
            aux[1][1] = 0

        return aux

    def _boat_generate(self, state):
        elements = []
        i = state[0]

        aux = deepcopy(state)
        aux[4] = state
        aux[i][0] -= 1
        aux[1][0] = 1
        aux[1][1] = 0
        elements.append(aux)

        aux = deepcopy(state)
        aux[4] = state
        aux[i][1] -= 1
        aux[1][0] = 0
        aux[1][1] = 1
        elements.append(aux)

        aux = deepcopy(state)
        aux[4] = state
        aux[i][0] -= 1
        aux[i][1] -= 1
        aux[1][0] = \
            aux[1][1] = 1
        elements.append(aux)

        i = 0
        while True:
            if i == len(elements):
                break

            aux = elements[i]

            if aux in self.queue or aux == state[4]:
                del elements[i]
                break
            else:
                for j in range(2, 4):
                    if aux[j][0] < 0 or aux[j][1] < 0 or aux[j][0] < aux[j][1]:
                        del elements[i]
                        i -= 1
                        break

            i += 1

        return elements

    def _generate_states(self, state):
        if state[1][0] != 0 or state[1][1] != 0:
            return self.transfer(state)
        else:
            return self._boat_generate(state)

    def start(self):
        while True:
            if len(self.border) == 0:
                return 'No ways'

            aux = deepcopy(self.border[0])
            self.path.append(aux)
            del self.border[0]

            print(aux[0:3])
            print(self.border)
            print('\n-----x-----\n')

            if aux[3] == self.end:
                return self.path

            aux = self._generate_states(aux)

            self.put(aux)
            self.append(self.border, aux)


def read_number(presentation, error='Error reading.\n\tPlease enter the data again!'):
    while True:
        try:
            _input = int(input(presentation + ': '))
            return _input
        except ValueError:
            print(error)


def main():
    amount_m = read_number('Enter the number of missionaries')
    amount_c = read_number('Enter the amount of cannibals')

    problem = Process(amount_m, amount_c, 100)
    print(problem.start())


if __name__ == '__main__':
    main()
