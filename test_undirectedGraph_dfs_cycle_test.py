from undirected_graph.graph import UndirectedGraph as graph
from undirected_graph.dfs import depthFirstSearchCycle as cycleFinder

if __name__ == '__main__':
    # v = 5
    # edges = [
    #     [0, 1],
    #     [1, 2],
    #     [2, 3],
    #     [2, 4],
    #     [0, 4]
    # ]
    v = 4
    edges = [
        [0, 1],
        [1, 2],
        [2, 3]
    ]
    g = graph(v, edges)
    finder = cycleFinder(g)
    path = finder.cycle()
    if path:
        print ('Cycle found: {}'.format(path))
    else:
        print ('No cycle is found')