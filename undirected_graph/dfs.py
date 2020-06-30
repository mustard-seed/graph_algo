"""
Implementation of veraious DFS-based algorithms for undirected graphs
"""
import undirected_graph.graph as graph

from typing import List, Union
from collections import deque
from abc import abstractmethod, ABC

class depthFirstSearch(ABC):
    """
    Base DFS algorithm
    """
    @abstractmethod
    def __init__(self, g: graph.UndirectedGraph):
        super().__init__()
        self._isMarked = [False] * g.v

    @abstractmethod
    def _apply (self, currentV: int, neighbourV: int):
        pass

    @abstractmethod
    def _preHook (self, currentV: int):
        pass

    def _dfs (self, g: graph.UndirectedGraph, v: int) -> None:
        """
        Run DFS from the given vertex v
        :param g: The graph
        :param v: The vertex
        :return: None
        """
        self._preHook(v)
        self._isMarked[v] = True
        adjList = g.adj(v)
        for neighbour in adjList:
            if self._isMarked[neighbour] is False:
                self._apply(currentV=v, neighbourV=neighbour)
                self._dfs(g, neighbour)



class depthFirstSearchPaths(depthFirstSearch):

    def __init__(self, g: graph.UndirectedGraph, s:int ):
        """
        Initialize the DFS path search problem from source vertex S in graph G
        :param g: An undirected graph
        :param s: Index of the source vertex
        :return:
        """
        super().__init__(g)
        assert s < g.v, 'The source vertex index is out of bound!'
        self._edgeTo = [-1] * g.v
        self._reachableVertexCount = 0
        self._source = s
        self._dfs(g, s)

    def _preHook(self, currentV: int):
        self._reachableVertexCount += 1

    def _apply(self, currentV: int, neighbourV: int):
        self._edgeTo[neighbourV] = currentV

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

class depthFirstSearchCC(depthFirstSearch):
    """
    Find the connected components of a graph
    """
    def __init__(self, g: graph.UndirectedGraph):
        super().__init__(g)
        # Component that each vertex belongs to
        self._componentIds = [0] * g.v
        # Count of components
        self._count = 0
        for vertex in range(0, g.v):
            if self._isMarked[vertex] is False:
                self._dfs(g, vertex)
                self._count += 1

    def _apply(self, currentV: int, neighbourV: int):
        pass

    def _preHook(self, currentV: int):
        self._componentIds[currentV] = self._count

    @property
    def count(self):
        return self._count

    def id(self, v: int) -> int:
        """
        Returns the component id that the given vertex belongs to
        :param v: Index of the given vertex
        :return: The component id
        """
        return self._componentIds[v]

