"""
Basic digraph algorithms.
Inspired by Algorithms 4E
"""
from typing import List, Union
from copy import deepcopy

from collections import deque

class Digraph(object):
    def __init__(self, v: int, edges: Union[List[List[int]], None] = None):
        """
        Constructs a directional graph
        :param v: Number of vertices
        :param edges: Directional edges
        """
        self._v = v
        self._e = 0
        self._adjList = [[] for i in range(0, self._v)]
        if edges is not None:
            for e in edges:
                source = e[0]
                dest = e[1]
                self.addEdge(source, dest)

    def addEdge(self, source: int, dest: int)->None:
        self._adjList[source].append(dest)
        self._e += 1

    @property
    def v(self) -> int:
        """
        Get the number of vertices in the graph
        :return: v
        """
        return self._v

    @property
    def e(self) -> int:
        """
        :return: The nubmer of edges in the graph
        """
        return self._e

    def adj(self, v:int) -> List:
        """
        Returns the adjacency list of vertex v
        Complexity: proportional to the degree of v
        :param v: Index of the vertex
        :return: The adjacency list
        """
        return deepcopy(self._adjList[v])

    def toString(self) -> str:
        """
        Prints the graph to a string
        :return: The graph as a string
        """
        output = '{} vertices. {} edges\n'.format(self.v, self.e)
        for v in range(0, self._v):
            adj_list = self.adj(v)
            output += (str(v) + '-> ')
            for w in adj_list:
                output += (str(w) + ' ')
            output += '\n'
        return output

    def reverse(self):
        """
        Construct the reverse graph
        :return: The reverse graph
        """
        rGraph = Digraph(self.v, None)
        for source in range(0, self.v):
            adjList = self.adj(source)
            for dest in adjList:
                rGraph.addEdge(dest, source)
        return rGraph

class DigraphCycle(object):
    """
    APi class for finding whether is exists a cycle in a directional graph
    The main graph exploration is based on DFS
    """
    def __init__(self, g: Digraph):
        self._isMarked = [False] * g.v
        self._edgeTo = [-1] * g.v
        self._hasCycle = False
        self._dfsStack = deque()
        self._cycle = []

        for v in range(0, g.v):
            if self._isMarked[v] is False:
                self._cycle.clear()
                self._dfs(g, v)
                if self._hasCycle is True:
                    break

    def _dfs(self, g: Digraph, v: int) -> None:
        """
        Run DFS a the given digraph from the current node v
        Side-effects:
         - Update the _isMarked list
         - Update _edgeTo list
         - Update the _hasCycle flag
         - Update the _dfsStack
        :param g: The directional graph
        :param v: Vertex to run DFS from
        :return: None
        """
        self._isMarked[v] = True
        self._dfsStack.append(v)
        adjList = g.adj(v)
        for dest in adjList:
            if self._isMarked[dest] is True:
                if self._dfsStack.count(dest) > 0:
                    self._hasCycle = True
                    trace = v
                    while self._edgeTo[trace] != dest:
                        self._cycle.append(trace)
                        trace = self._edgeTo[trace]
                    self._cycle.append(trace)
                    self._cycle.append(dest)
                    break
            else:
                self._edgeTo[dest] = v
                self._dfs(g, dest)
                if self._hasCycle is True:
                    break
        self._dfsStack.pop()

    @property
    def hasCycle(self):
        return self._hasCycle

    def cycle(self):
        newList = deepcopy(self._cycle)
        newList.reverse()
        return newList

class DigraphOrder(object):
    """
    APIs for generating the pre, post, and reverse-post order of DFS on a digraph
    """
    def __init__(self, g: Digraph):
        """
        Populate the orders
        :param g:
        """
        self._isMarked = [False] * g.v
        self._preOrder = []
        self._postOrder = []
        for v in range(g.v):
            if self._isMarked[v] is False:
                self._dfs(g, v)

    def _dfs(self, g: Digraph, v: int):
        self._isMarked[v] = True
        self._preOrder.append(v)
        for d in g.adj(v):
            if self._isMarked[d] is False:
                self._dfs(g, d)
        self._postOrder.append(v)

    @property
    def preOrder(self):
        return deepcopy(self._preOrder)

    @property
    def postOrder(self):
        return deepcopy(self._postOrder)

    @property
    def reversePostOrder(self):
        newList = deepcopy(self._postOrder)
        newList.reverse()
        return newList

class DigraphTopological(object):
    """
    Perform topological sort on a given graph if it doesn't contain any directed cycles
    """
    def __init__(self, g: Digraph):
        self._toplogicalOrder = None
        self._orderFinder = None
        self._cycleFinder = DigraphCycle(g)
        if self._cycleFinder.hasCycle is False:
            self._orderFinder = DigraphOrder(g)
            self._toplogicalOrder = self._orderFinder.reversePostOrder

    @property
    def toplogicalOrder(self):
        if self._toplogicalOrder:
            return deepcopy(self._toplogicalOrder)
        else:
            return None

class DigraphSCC(object):
    """
    API for finding the strong components of a diagraph using
    the Kosaraju-Sharir algorithm
    """
    def __init__(self, g: Digraph):
        self._isMarked = [False] * g.v
        self._componentId = [-1] * g.v
        self._numSC = 0

        # First, obtain the reverse DFS post-order on the reverse graph
        rGraph = g.reverse()
        orderFinder = DigraphOrder(rGraph)
        reversePostOrder = orderFinder.reversePostOrder

        # Then, perform DFS on the original graph according to the order of the vertices in the
        # reverse DFS post order obtained on the reverse graph
        for v in reversePostOrder:
            if self._isMarked[v] is False:
                self._dfs(g, v)
                self._numSC += 1

    def _dfs(self, g: Digraph, v: int):
        self._isMarked[v] = True
        self._componentId[v] = self._numSC
        adjList = g.adj(v)
        for d in adjList:
            if self._isMarked[d] is False:
                self._dfs(g, d)

    def stronglyConnected(self, v: int, w: int) -> bool:
        """
        Determines whether two given vertices belong to the same strong component
        :param v: The first vertex
        :param w: The other vertex
        :return: True/False
        """
        return self._componentId[v] == self._componentId[w]

    @property
    def count(self) -> int:
        """
        Reports the number of strong components in the graph
        :return: int
        """
        return self._numSC

    def id(self, v: int):
        """
        Report the id of the strong component that the given vertex is in
        :param v: The given vertex
        :return: int
        """
        return self._componentId[v]


