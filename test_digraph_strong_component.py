from digraph.digraph import *

if __name__ == '__main__':
    numV = 13
    edges = [
        [0, 1], [0, 5],
        [2, 0], [2, 3],
        [3, 2], [3, 5],
        [4, 3], [4, 2],
        [5, 4],
        [6, 0], [6, 4], [6, 9],
        [7, 6], [7, 8],
        [8, 7], [8, 9],
        [9, 10], [9, 11],
        [10, 12],
        [11, 12], [11, 4],
        [12, 9]
    ]

    graph = Digraph(numV, edges)
    scFinder = DigraphSCC(graph)
    print('There are {} strong components in the given graph. Component assignment of the vertices: '.format(scFinder.count))
    for v in range(0, graph.v):
        print('Vertex {}: {}'.format(v, scFinder.id(v)))


