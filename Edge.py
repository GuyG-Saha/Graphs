
import typing

import Vertex


class Edge:
    def __init__(self, start: Vertex, end: Vertex, weight: float = 0, directed=True):
        """
        :param start: The 'from' Vertex
        :param end: The 'to' Vertexv
        :param weight: Numeric value
        :param directed: Boolean
        """
        self.start = start
        self.end = end
        self.weight = weight
        self.directed = directed
