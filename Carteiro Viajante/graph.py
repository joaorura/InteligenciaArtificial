class Graph:
    def __init__(self, vertex, edges=[]):
        self.vertex = vertex
        self.edges = edges

    def add_edge(self, v, u, weight):
        edge = [v, u, weight]
        self.edges.append(edge)