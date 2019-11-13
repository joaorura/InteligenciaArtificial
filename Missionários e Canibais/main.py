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

    def __init__(self, amount_c, amount_m):
        self.amount_m = amount_m
        self.amount_c = amount_c

        self._error_detect()

        self.path = []

        first = [amount_m, amount_c]
        self.end = first
        boat = [0, 0]
        second = [0, 0]

        self.begin = [2, boat, first, second]
        self.border = self._generate_states(self.begin)

    @staticmethod
    def increase(i):
        i += 1
        if i == 4:
            i = 2

        return i

    def transfer(self, state):
        state = deepcopy(state)

        i = state[0]

        state[0] = self.increase(i)
        state[i][0] += state[1][0]
        state[i][1] += state[1][1]

        state[1][0] = \
            state[1][0] = 0

        return state

    def _boat_generate(self, state):
        elements = []
        i = state[0]
        new = self.increase(i)

        if state[i][0] >= state[i][1]:
            aux = deepcopy(state)
            aux[0] = new
            aux[i][1] -= 1
            aux[1][0] = 0
            aux[1][1] = 1

            elements.append(aux)

            aux = deepcopy(state)
            aux[0] = new
            aux[i][0] -= 1
            aux[i][1] -= 1
            aux[1][0] = \
                aux[1][1] = 1
            elements.append(aux)

        if state[i][0] > state[i][1]:
            aux = deepcopy(state)
            aux[0] = new
            aux[i][0] -= 1
            aux[1][0] = 1
            aux[1][1] = 0
            elements.append(aux)

        return elements

    def _generate_states(self, state):
        if state[1][0] != 0 or state[1][1] != 0:
            return self.transfer(state)
        else:
            aux = self._boat_generate(state)
            return aux

    def start(self):
        while True:
            if len(self.border) == 0:
                return None

            aux = self.border[0]
            del self.border[0]

            if aux == self.end:
                self.path.append(aux)
                return self.path

            self.border.append(self._generate_states(aux))


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

    problem = Process(amount_m, amount_c)
    print(problem.start())


if __name__ == '__main__':
    main()
