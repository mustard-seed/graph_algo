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

