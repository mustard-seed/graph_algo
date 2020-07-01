"""
Basic digraph algorithms.
Inspired by Algorithms 4E
"""
from typing import List, Union
from copy import deepcopy

class Digraph(object):
    def __init__(self, v: int, edges: Union[List[int], None] = None):
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


