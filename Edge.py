
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
        self._start = start
        self._end = end
        self._weight = weight
        self._directed = directed

    @property
    def start(self):
        return self._start

    @property
    def end(self):
        return self._end

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, w):
        self._weight = w

    def reverse(self):
        """
        reverse a directed edge
        :return: The edge reversed
        """
        if self._directed:
            tmp = self._start
            self._start = self._end
            self._end = tmp
            return self
        else:
            return


