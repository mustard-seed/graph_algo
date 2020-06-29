import undirected_graph.dfs as dfs
import undirected_graph.graph as graph

if __name__ == '__main__':
    v = 6
    s = 0
    edges = [
        [0, 5],
        [2, 4],
        [2, 3],
        [1, 2],
        [0, 1],
        [3, 4],
        [3, 5],
        [0, 2]
    ]
    g = graph.UndirectedGraph(v, edges)
    paths = dfs.depthFirstSearchPaths(g, s)
    output = ''
    for dest in range(0, 6):
        output += '{} to {}: '.format(s, dest)
        if paths.hasPathTo(dest):
            path = paths.getPathTo(dest)
            for n in path:
                if n == s:
                    output += str(n)
                else:
                    output += '-{}'.format(n)
        output += '\n'
    print (output)