from digraph.digraph import *

if __name__ == '__main__':
    numV = 13
    edges = [
        [0, 1], [0, 5], [0, 6],
        [2, 0], [2, 3],
        [3, 5],
        [4, 6],
        [5, 4], [5, 9],
        [6, 7], [6, 9],
        [7, 8],
        [9, 10], [9, 11], [9, 12],
        [11, 12]
    ]

    def checkOrder(order, graph: Digraph):
        hasSeen = [False] * graph.v
        if isinstance(order, list):
            if len(order) < graph.v:
                return False
            for v in order:
                hasSeen[v] = True
                adjList = graph.adj(v)
                for d in adjList:
                    """ If there is an edge pointing to a vertex earlier in the order, 
                    then this order is not topological """
                    if hasSeen[d] is True:
                        return False
        return True


    graph = Digraph(numV, edges)
    topologicalOrderFinder = DigraphTopological(graph)
    order = topologicalOrderFinder.toplogicalOrder
    if order:
        print('Topological order: ', order)
        isOrder = checkOrder(order, graph)
        if isOrder is False:
            print ('The proposed topological order failed the test!')
    else:
        print('The graph is not a DAG, hence it does not contain a topological order')

