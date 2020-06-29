import undirected_graph.graph as graph

if __name__ == '__main__':
    num_vertices = 13
    edges = [
        [0, 5],
        [4, 3],
        [0, 1],
        [9, 12],
        [6, 4],
        [5, 4],
        [0, 2],
        [11, 12],
        [9, 10],
        [0, 6],
        [7, 8],
        [9, 11],
        [5, 3]
    ]
    g = graph.UndirectedGraph(num_vertices, edges)
    output = g.toString()
    print(output)