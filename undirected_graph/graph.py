"""
Basic undirected graph APIs
Ported from the Jave implementation in Algorithm 4E
Author: James Liu
"""
from typing import List
from copy import deepcopy


class UndirectedGraph (object):
    def __init__(self, v : int, edges:List[List[int]] = None):
        """
        Initializes an undirected graph with v vertices, and the connections as provided
        Space complexity of the graph: V + E
        :param v: The number of vertices
        :param edges: List of undirected edges
        """
        assert v > 0, 'Graph must contain at least one node'
        self._v = v
        self._e = 0
        self._adj_list = [[] for i in range(0, v)]
        if edges is not None:
            # Construct the adjacency list
            for e in edges:
                v1 = e[0]
                v2 = e[1]
                self.addEdge(v1, v2)

    @property
    def v(self) -> int:
        """
        Get the number of vertices in the graph
        :return: v
        """
        return self._v

    @property
    def e(self)-> int:
        """
        :return: The nubmer of edges in the graph
        """
        return self._e

    def addEdge(self, v:int, w:int) -> None:
        """
        Add an edge to the graph.
        Complexity: onstant time
        :param v: Vertex 0 index
        :param w: Vertex 1 index
        :return: None
        """
        assert v < self._v and w < self._v, 'Both vertex indices must be less than the number of vertices in the graph'
        self._adj_list[v].append(w)
        self._adj_list[w].append(v)
        self._e += 1

    def adj(self, v:int) -> List:
        """
        Returns the adjacency list of vertex v
        Complexity: proportional to the degree of v
        :param v: Index of the vertex
        :return: The adjacency list
        """
        return deepcopy(self._adj_list[v])


    def toString(self) -> str:
        """
        Prints the graph to a string
        :return: The graph as a string
        """
        output = '{} vertices. {} edges\n'.format(self.v, self.e)
        for v in range(0, self._v):
            adj_list = self.adj(v)
            output += (str(v) + ': ')
            for w in adj_list:
                output += (str(w) + ' ')
            output += '\n'
        return output



