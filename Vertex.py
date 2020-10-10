from exceptions import VertexUnavailable, VertexDegreeException

class Vertex:

    def __init__(self, symbol: str, rate=1):
        """
        :param symbol: Char to symbolize the vertex
        :param rate: For further use
        """
        self._symbol = symbol
        self._degree = 0
        self.rate = rate

    @property
    def symbol(self):
        return self.symbol

    @symbol.setter
    def symbol(self, s):
        self._symbol = s

    @property
    def degree(self):
        return self._degree

    @degree.setter
    def degree(self, d):
        if d < 0:
            raise VertexDegreeException('Degree of a vertex can not be negative')
        self._degree = d




