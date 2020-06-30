from undirected_graph.graph import UndirectedGraph as graph
from undirected_graph.dfs import depthFirstSearchCC as cc


if __name__ == '__main__':
    # v = 7
    # edges = [
    #     [0, 1],
    #     [0, 2],
    #     [0, 3],
    #     [1, 2],
    #     [4, 5],
    #     [4, 6],
    #     [4, 5]
    # ]
    v = 5
    edges = [
        [0, 1],
        [1, 2],
        [2, 3],
        [0, 3]
    ]
    g = graph(v, edges)
    exploration = cc(g)
    numComponents = exploration.count
    components = [[] for i in range(0, numComponents)]
    for vertex in range(0, v):
        id = exploration.id(vertex)
        components[id].append(vertex)

    for idx, comp in enumerate(components):
        out = 'Connected component {}: '.format(idx)
        for vertex in comp:
            out += '{} '.format(vertex)
        print(out)