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

    def add_node(self, val):
        """Add a new node to the graph."""
        try:
            checker = self._graph_content[val]
            raise ValueError
        except KeyError:
            self._graph_content[val] = []

    def add_edge(self, node1, node2):
        """Add a new edge to the graph connecting node1 to node2.

        Checks if they exist and adds them if they do not.
        """
        try:
            self.add_node(node1)
        except ValueError:
            pass
        try:
            self.add_node(node2)
        except ValueError:
            pass
        self._graph_content[node1].append(node2)
