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
        self.vertices.add(start)
        self.vertices.add(end)
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
                        alt = dist[u] + self.get_edge_weight(u, v)
                        if alt < dist[v]:
                            dist[v] = alt
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
            if end in self.graph[start]:
                path.append(end)
                return path
            shortest_path = None
            for vertex in self.graph[start]:
                if vertex not in path:
                    new_path = self.shortest_path(vertex, end, weighted, path)
                    if new_path:
                        if not shortest_path or len(new_path) < len(shortest_path):
                            shortest_path = new_path
            return shortest_path
        else:
            return self._dijkstra_algorithm(start, end)

    def __str__(self):
        desc_str = self.description + ' created at ' + str(self.creation_time) + ' and has ' + str(self.num_edges) + \
                   ' edges' + ' and ' + str(len(self.vertices)) + ' vertices'
        return desc_str

