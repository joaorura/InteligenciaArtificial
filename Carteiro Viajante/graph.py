class Graph:
    def __init__(self, vertex, edges):
        self.vertex = vertex
        self.edges = edges

    def distance_path(self, path):
        if len(path) == 0:
            raise ValueError

        distance = 0
        for i in range(0, len(path) - 1):
            distance += self.edges[path[i]][path[i+1]]

        return distance
