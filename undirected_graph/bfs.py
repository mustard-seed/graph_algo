"""
Implementation of veraious BFS-based algorithms for undirected graphs
"""
import undirected_graph.graph as graph

from typing import List, Union
from collections import deque
from queue import Queue

class breadthFirstSearchPaths(object):

    def __init__(self, g: graph.UndirectedGraph, s:int ):
        """
        Initialize the DFS path search problem from source vertex S in graph G
        :param g: An undirected graph
        :param s: Index of the source vertex
        :return:
        """
        assert s < g.v, 'The source vertex index is out of bound!'
        self._isMarked = [False] * g.v
        self._edgeTo = [-1] * g.v
        self._reachableVertexCount = 0
        self._source = s
        self.bfs(g, s)


    def bfs (self, g: graph.UndirectedGraph, v: int) -> None:
        """
        Run DFS from the given vertex v
        :param g: The graph
        :param v: The vertex
        :return: None
        """
        self._isMarked[v] = True
        self._reachableVertexCount += 1
        queue = Queue()
        queue.put(v)

        while queue.empty() is False:
            vertex = queue.get()
            for neighbour in g.adj(vertex):
                if self._isMarked[neighbour] is False:
                    queue.put(neighbour)
                    self._isMarked[neighbour] = True
                    self._reachableVertexCount += 1
                    self._edgeTo[neighbour] = vertex



    def hasPathTo (self, v: int) -> bool:
        """
        Determines if a vertex is reachable from the search source
        :param v: Index of the destination vertex
        :return: Boolean, whether the destination is reachable
        """
        assert v < len(self._isMarked), 'Vertex index is out of bound!'
        return self._isMarked[v]

    def getPathTo (self, v: int) -> Union[List, None]:
        """
        Get a path from the search source (S) to the destination list
        :param v:
        :return:
        """
        path = None
        if self.hasPathTo(v):
            stack = deque()
            stack.append(v)
            node = v
            count = 1
            path = []
            while self._edgeTo[node] is not -1:
                node = self._edgeTo[node]
                stack.append(node)
                count += 1

            while count > 0:
                path.append(stack.pop())
                count -= 1

        return path



