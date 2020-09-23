import collections
from datetime import datetime

from typing import List

from Edge import Edge
from exceptions import GraphException, VertexUnavailable

__all__ = ['Graph']


class Graph:
    def __init__(self, description: str):
        self.graph = collections.defaultdict()
        self.weights = collections.defaultdict()
        self.vertices = set()
        self.num_edges = 0
        self.creation_time = datetime.now()
        self.description = description

    def add_edge(self, edge: Edge):
        """
        :param edge: Existing edge
        :return:
        """
        ...

    def add_new_edge(self, start: str, end: str, weight: float) -> Edge:
        """
        :param start: Start Edge
        :param end: End Edge
        :param weight: Float value for weighted edge
        :return: Edge object within the graph
        """
        self.vertices.add(start) if start not in self.vertices else ''
        self.vertices.add(end) if end not in self.vertices else ''
        if start in self.graph.keys():
            self.graph[start].append(end)
        else:
            self.graph[start] = [end]
        e = Edge(start, end, weight)
        self.weights[(start, end)] = weight
        self.num_edges += 1
        return e

    def get_edge_weight(self, start: str, end: str) -> float:
        """
        This method is based on the assumption that the graph has only one at maximum between every two vertices
        :param start: str
        :param end: str
        :return: Weight: float
        if no such weight return 0
        """
        if start == end:
            return 0
        return self.weights.get((start, end), 0)

    def search_vertex(self, symbol: str) -> bool:
        """
        This method searches for a vertex in the graph by its symbol
        :param symbol: Character
        :return: Boolean
        """
        return symbol in self.vertices

    def _get_all_leaves(self) -> List:
        """
        This method searches for all leaf vertices in the graph (vertices without children nodes)
        :return: List of chars that represent leaf vertices
        """
        keys_set = set(self.graph.keys())
        values_set = [c for sublist in self.graph.values() for c in sublist]
        values_set = set(values_set)
        diff = values_set.difference(keys_set)
        return list(diff)

    def _add_none_ending_to_leaves(self):
        """
        Adds None child to leaf_vertices
        """
        leaf_vertices = self._get_all_leaves()
        for i in leaf_vertices:
            self.graph[i] = None

    def dfs_visit(self, u, colored_vertices: dict) -> bool:
        """
        Recursive method that performs DFS visits to vertices
        :param u: This vertice is being processed or is in function call stacl
        :param colored_vertices: colors of vertices in graph
        :return: Boolean
        """
        colored_vertices[u] = 'GRAY'
        if self.graph[u]:
            for v in self.graph[u]:
                if colored_vertices[v] is 'GRAY':
                    return True
                if colored_vertices[v] is 'WHITE' and self.dfs_visit(v, colored_vertices) is True:
                    return True

        colored_vertices[u] = 'BLACK'
        return False

    def is_dag(self) -> bool:
        """
        This method checks if a given graph is Directed & A-cyclic
        :return: True if no cycles in the graph, False if there is at least one cycle
        """
        vertices_list = list(self.vertices)
        vertices_list.sort()
        colored_vertices = {v: 'WHITE' for v in vertices_list}
        for u in colored_vertices:
            if colored_vertices[u] is 'WHITE':
                if self.dfs_visit(u, colored_vertices) is True:
                    return False
        return True

    def _dijkstra_algorithm(self, start: str, end: str) -> float:
        """
        Implementation of Dijkstra's algorithm to find shortest weighted path
        :param start: Start Vertex
        :param end: Destination Vertex
        :return: Numeric float value of cheapest distance to destination vertex
        """
        queue = []
        dist = {}
        prev = {}
        visited = set()
        vertices_list = list(self.vertices)
        vertices_list.sort()
        for v in vertices_list:
            dist[v] = float('inf')
            prev[v] = None
            queue.append(v)

        dist[start] = 0

        while queue:
            u = queue.pop(0)
            if not dist[u]:
                dist[u] = self.get_edge_weight(start, u)
            visited.add(u)
            try:
                for v in self.graph[u]:
                    if v not in visited:
                        computed_weight = dist[u] + self.get_edge_weight(u, v)
                        if computed_weight < dist[v]:
                            dist[v] = computed_weight
                            prev[v] = u
            except KeyError as ex:
                return dist[end]
        return dist[end]

    def shortest_path(self, start: str, end: str, weighted: bool = False, path: List = []) -> [List, float]:
        """
        Perform shortest or cheapest path search in graph
        :param path: The result path which can be instantiated at first call
        :param start: Start Vertex
        :param end: Destination Vertex
        :param weighted: Boolean indicator if to take into account weighted measure or not
        :return: List of vertices that assemble shortest / cheapest path
        """
        if not self.search_vertex(start) or not self.search_vertex(end):
            raise VertexUnavailable("One of vertices is not found in the graph")

        if not weighted:
            path = path + [start]
            if start == end:
                return path
            try:
                if end in self.graph[start]:
                    path.append(end)
                    return path
            except KeyError as ex:
                pass
            shortest_path = None
            try:
                for vertex in self.graph[start]:
                    if vertex not in path:
                        new_path = self.shortest_path(vertex, end, weighted, path)
                        if new_path:
                            if not shortest_path or len(new_path) < len(shortest_path):
                                shortest_path = new_path
            except KeyError as ex:
                pass
            return shortest_path
        else:
            return self._dijkstra_algorithm(start, end)

    def _topological_sort_helper(self, i, visited, stack=[]):
        """
        Helper recursive function for topological sort
        :param i: index of current vertex to handle
        :param visited: list of visited vertices
        :param stack: utility data structure
        :return:
        """
        visited[i] = True
        try:
            for j in self.graph[i]:
                if visited[j] is False:
                    self._topological_sort_helper(j, visited, stack)
        except KeyError as ex:
            pass

        stack.insert(0, i)

    def topological_sort(self) -> List:
        """
        Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering
        of vertices such that for every directed edge uv, vertex u comes before v in the ordering
        :return: List as a stack of vertices
        """
        stack = []
        vertices_list = list(self.vertices)
        vertices_list.sort()
        visited = {v: False for v in vertices_list}
        for v in vertices_list:
            if visited[v] is False:
                self._topological_sort_helper(v, visited, stack)

        return stack

    def __str__(self):
        desc_str = self.description + ' created at ' + str(self.creation_time) + ' and has ' + str(self.num_edges) + \
                   ' edges' + ' and ' + str(len(self.vertices)) + ' vertices'
        return desc_str

