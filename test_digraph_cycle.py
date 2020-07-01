from digraph.digraph import *

if __name__ == '__main__':
    # The following case contains at least one directed cycle: 3->5->4->3
    numV = 13
    edges = [
        [4, 2],
        [2, 3],
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
    cycleFinder = DigraphCycle(graph)
    if cycleFinder.hasCycle:
        print ('Found one cycle')
        cycle = cycleFinder.cycle()
        line = ''
        for v in cycle:
            line += '{} '.format(v)
        print(line)
    else:
        print('Did not detect any cycle in the graph')
