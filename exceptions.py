class GraphException(Exception):
    """Base class for other exceptions"""
    pass


class VertexUnavailable(GraphException):
    """Raised when the input vertices not found in graph"""
    pass


class VertexDegreeException(VertexUnavailable):
    """Raised when an input for vertex degree is negative"""
    pass
