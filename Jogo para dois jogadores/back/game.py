LOCALS = (
    ((0, 0), (0, 1), (0, 2)),
    ((1, 0), (1, 1), (1, 2)),
    ((2, 0), (2, 1), (2, 2)),

    ((0, 0), (1, 0), (2, 0)),
    ((0, 1), (1, 1), (2, 1)),
    ((0, 2), (1, 2), (2, 2)),

    ((0, 0), (1, 1), (2, 2)),
    ((0, 2), (1, 1), (2, 0))
)

values = {
    0: 0,
    1: 1,
    2: 10,
    3: 100
}


class Game:
    def __init__(self, names=('Jogador 1', 'Jogador 2'), com_active=0):
        self.names = names
        self.com_active = com_active

        self.board = []
        self.turn = 0
        self.winner = None

        for i in range(0, 3):
            aux = []
            for j in range(0, 3):
                aux.append(-1)

            self.board.append(aux)

    def check(self):
        winner = None
        win = 0
        for i in LOCALS:
            count_x = count_o = 0
            for j in i:
                aux = self.board[j[0]][j[1]]
                if aux == 0:
                    count_x += 1
                elif aux == 1:
                    count_o += 1

            win -= values[count_x]
            win += values[count_o]

            if count_x == 3:
                winner = 0
            elif count_o == 3:
                winner = 1

            if winner is not None:
                self.winner = winner
                break

        if winner is None and self.turn == 9:
            return 2, win
        else:
            return winner, win

    def make_play(self, pos):
        if self.board[pos[0]][pos[1]] == -1 and self.winner is None:
            self.board[pos[0]][pos[1]] = self.turn % 2
        else:
            return -1

        self.turn += 1
