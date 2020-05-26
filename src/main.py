from graph import Graph
from UI.draw import Graphic
from coordinates import Point

MAX = 10000000
if __name__ == '__main__':
    print("------------------------------------------------------------------------")
    choice = int(
        input("Enter 0 for default data and 1 for for your own data : "))
    pointList = []
    adjacency = []
    if choice == 0:
        adjacency = [[0, 10, 6, 5], [10, 0, MAX, 15], [6, MAX, 0, 4], [5, 15, 4, 0]]
        pointList = [Point(10, 10), Point(20, 10), Point(20, 20), Point(10, 20)]

    size = len(adjacency)
    g = Graph(size)

    for i in range(0, size):
        for j in range(0, size):
            g.addEdge(i, j, adjacency[i][j])

    result = g.KruskalMST()
    Graphic.draw(pointList, result)
