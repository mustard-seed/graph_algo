from digraph.digraph import Digraph

if __name__ == '__main__':
    numV = 13
    edges = [
        [4, 2],
        [2, 3],
        [3, 2],
        [6, 0],
        [0, 1],
        [2, 0],
        [11, 12],
        [12, 9],
        [9, 10],
        [9, 11],
        [7, 9], [10, 12], [11, 4], [4, 3], [3, 5], [6, 8], [8, 6], [5, 4], [0, 5], [6, 4], [6, 9], [7, 6]
    ]
    graph = Digraph(numV, edges)
    graphPrint = graph.toString()
    print('The original graph')
    print(graphPrint)
    rGraph = graph.reverse()
    print('The reverse graph')
    print(rGraph.toString())