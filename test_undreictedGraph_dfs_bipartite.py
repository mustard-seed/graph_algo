from undirected_graph.graph import UndirectedGraph as graph
from undirected_graph.dfs import depthFirstSearchBipartite as bipartiteFinder

if __name__ == '__main__':
    # numV = 5
    # edges = [
    #     [0, 1],
    #     [1, 2],
    #     [2, 3],
    #     [3, 0]
    # ]
    numV = 3
    edges = [
        [0, 1],
        [1, 2],
        [2, 0]
    ]
    g = graph(numV, edges)
    finder = bipartiteFinder(g)
    if finder.isBipartite is False:
        print ('Graph is not bipartite')
    else:
        partitions = finder.getPartitions()
        id = 0
        for partition in partitions:
            line = 'Partition {}: '.format(id)
            for vertex in partition:
                line += '{} '.format(vertex)
            print(line)
            id += 1