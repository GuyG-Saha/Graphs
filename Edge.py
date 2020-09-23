
import typing

import Vertex


class Edge:
    def __init__(self, start: str, end: str, weight: float = 0, directed=True):
        """
        Directed edge of a graph
        :param start: The 'from' Vertex
        :param end: The 'to' Vertex
        :param weight: Numeric value
        :param directed: Boolean
        """
        self.start = start
        self.end = end
        self.weight = weight
        self.directed = directed

    def reverse(self):
        """
        reverse a directed edge
        :return: The edge reversed
        """
        if self.directed:
            tmp = self.start
            self.start = self.end
            self.end = tmp
            return self
        else:
            return


