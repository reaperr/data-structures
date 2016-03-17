# -*- coding: utf-8 *-*


class SimpleGraph(object):
    """Python implementation of the simple graph structure."""

    def __init__(self):
        """SimpleGraph constructor."""
        self._graph_content = {}

    def nodes(self):
        """Return a list of the nodes."""
        return list(self._graph_content)

    def edges(self):
        """Return a list of nodes and their edges."""
        return list(self._graph_content.items())

    
