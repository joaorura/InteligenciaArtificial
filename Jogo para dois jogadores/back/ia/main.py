from back.ia.node import Node


class Problem:
    def __init__(self, game, max_level):
        self.root = Node(game)
        self.result = None
        self.max_level = max_level

    def _min_max(self, node_father, a=[-1000], b=[1000], level=0):
        if level == self.max_level:
            return node_father.weight

        _type = level % 2
        if _type == 0:
            value = -1000
        else:
            value = 1000

        for i in range(0, len(node_father.game.board)):
            for j in range(0, len(node_father.game.board[i])):
                if node_father.game.board[i][j] == -1:
                    now = node_father.copy()
                    now.game.make_play((i, j))
                    now.avaliation()
                    node_father.children.append(now)

                    if _type == 0:
                        value = max(value, self._min_max(now, a, b, level+1))

                        if value < b[0]:
                            a[0] = max(a[0], value)
                    else:
                        value = min(value, self._min_max(now, a, b, level+1))

                        if value > a[0]:
                            b[0] = min(b[0], value)

                    now.weight = value
        return value

    def _play(self, node):
        board_0 = self.root.game.board
        board_1 = node.game.board

        for i in range(0, len(board_0)):
            for j in range(0, len(board_0[i])):
                if board_0[i][j] != board_1[i][j]:
                    return i, j

    def _decision(self):
        value = self._min_max(self.root)

        test = None
        for i in self.root.children:
            if value == i.weight:
                test = i
                break

        if test is None:
            raise ValueError

        self.result = self._play(test)

    def get_solution(self):
        if self.result is None:
            self._decision()

        return self.result
