import utils
from copy import deepcopy


class Node:
    def __init__(self, time, m, c, father=None):
        utils.check_type(list, m)
        utils.check_type(list, c)

        self.time = time
        self.m = m
        self.c = c
        self.father = father
        self.children = []

    def __eq__(self, other):
        return type(other) == Node and self.m == other.m and \
               self.c == other.c and self.time == other.time

    def __str__(self):
        return f'T: {self.time} | M: {self.m} | C: {self.c}'

    @staticmethod
    def next_time(x):
        aux = x + 1
        return aux if aux < 2 else 0

    @staticmethod
    def _filter_elements(elements, queue=None):
        aux = 0
        while True:
            if aux == len(elements):
                break

            i = elements[aux]

            test = (i is None) or (i.c[0] > i.m[0] > 0) or \
                   (i.c[1] > i.m[1] > 0) or i.father == i
            if (not test) and queue is not None:
                test = test or i in queue

            if test:
                del elements[aux]
                aux -= 1

            aux += 1

    def _m_time(self, i, j, node):
        if node is None or node.m[i] == 0:
            return None

        aux_node = deepcopy(node)
        aux_node.m[i] -= 1
        aux_node.m[j] += 1

        return aux_node

    def _c_time(self, i, j, node):
        if node is None or node.c[i] == 0:
            return None

        aux_node = deepcopy(node)
        aux_node.c[i] -= 1
        aux_node.c[j] += 1

        return aux_node

    def father_children(self, queue=None):
        j = self.time
        i = self.next_time(j)

        elements = []

        base = deepcopy(self)
        base.father = self
        base.children.clear()
        base.time = i

        aux_m = self._m_time(i, j, base)
        aux_c = self._c_time(i, j, base)

        elements.append(aux_m)
        elements.append(aux_c)

        elements.append(self._m_time(i, j, aux_c))

        elements.append(self._m_time(i, j, aux_m))
        elements.append(self._c_time(i, j, aux_c))

        self._filter_elements(elements, queue)
        if queue is not None:
            for i in elements:
                queue.put(i)
        self.add_children(elements)

        return elements

    def add_children(self, *args):
        _len = len(args)

        if _len == 2:
            utils.check_type(int, args[0])
            utils.check_type(int, args[1])
            son = Node(args[0], args[1])
            self.children.append(son)
        elif _len == 1:
            aux = type(args[0])

            if aux == Node:
                self.children.append(args[0])
            elif aux == list:
                for i in args[0]:
                    utils.check_type(Node, i)
                    self.children.append(i)
        else:
            raise ValueError

    def remove_children(self, *args):
        _len = len(args)

        if _len == 2:
            utils.check_type(int, args[0])
            utils.check_type(int, args[1])

            for i in self.children:
                if i.m == args[0] and i.c == args[1]:
                    del i
        elif _len == 1:
            utils.check_type(type(Node), args[0])
            self.children.remove(args[0])
        else:
            raise ValueError

    def remove_all_children(self):
        self.children.clear()
