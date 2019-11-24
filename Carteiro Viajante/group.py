from copy import deepcopy


class Group:
    def __init__(self, elements=[]):
        self.elements = []

    def copy(self):
        return deepcopy(self)

    def