from math import inf

from graph import Graph

vertex = [0, 1, 2, 3, 4]

edges = [
    [inf, 99, inf, inf, 157],
    [99, inf, 141, inf, 126],
    [inf, 141, inf, 91, 161],
    [inf, inf, 91, inf, 113],
    [157, 126, 161, 113, inf]
]

graph = Graph(vertex, edges)