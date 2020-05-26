from models import Graph
from collections import defaultdict
if __name__ == '__main__':
    adjacency = [[0, 10, 6, 5], [10, 0, 0, 15], [6, 0, 0, 4], [5, 15, 4, 0]]
    size = len(adjacency)
    g = Graph(4)
    for i in range(0, size):
        for j in range(0, size):
            g.addEdge(i, j, adjacency[i][j])

    g.KruskalMST()
