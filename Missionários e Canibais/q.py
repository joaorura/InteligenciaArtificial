import utils
from node import Node
from copy import deepcopy


class _Queue:
    def __init__(self, max_size=0):
        self.max_size = max_size
        self.queue = []

    def __contains__(self, item):
        for i in self.queue:
            if item == i:
                return True

        return False

    def __str__(self):
        if self.empty():
            return 'Queue is empty\n'

        _str = '\n{\n'
        for i in range(0, len(self.queue)):
            _str += f'  {i}: {self.queue[i]} \n'

        _str += '}\n'

        return _str

    def reverse(self):
        self.queue.reverse()

    def empty(self):
        return len(self.queue) == 0

    def put(self, node):
        utils.check_type(Node, node)

        if self.max_size != 0 and len(self.queue) == self.max_size:
            del self.queue[0]

        self.queue.append(node)

    def get(self):
        if len(self.queue) == 0:
            raise Exception('Error, the queue it\'s empty')

        aux = deepcopy(self.queue[0])
        del self.queue[0]

        return aux
