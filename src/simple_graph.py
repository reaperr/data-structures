# -*- coding: utf-8 *-*
from stack import Stack
from queue import Queue
import time


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
        if self.has_node(val):
            raise ValueError
        self._graph_content[val] = []

    def add_edge(self, node1, node2):
        """Add a new edge to the graph connecting node1 to node2.

        Checks if they exist and adds them if they do not.
        """
        if not self.has_node(node1):
            self.add_node(node1)
        if not self.has_node(node2):
            self.add_node(node2)
        self._graph_content[node1].append(node2)

    def del_node(self, node):
        """Remove the node from the graph if it exists. Error on Fail"""
        try:
            node_neighbors = self.neighbors(node)
            for neighbor in node_neighbors:
                self.del_edge(neighbor, node)
            del self._graph_content[node]
        except (KeyError, ValueError):
            raise ValueError

    def has_node(self, node):
        return node in self._graph_content

    def del_edge(self, node1, node2):
        """Removes the edge connected node1 to node2. Error on Fail"""
        self._graph_content[node1].remove(node2)

    def neighbors(self, node):
        """Returns a list of all nodes with edges connected to node(param)"""
        if self.has_node(node):
            return [key for key in list(self._graph_content.keys())
                    if node in self._graph_content[key]]
        raise ValueError

    def adjacent(self, node1, node2):
        if self.has_node(node1) and self.has_node(node2):
            return (node2 in self._graph_content[node1] or
                    node1 in self._graph_content[node2])
        raise ValueError

    def depth_first_traversal(self, start):
        """Return the full visited path of a depth first traversal."""
        depth_stack = Stack()
        visited = []
        depth_stack.push(start)
        while depth_stack.size() > 0:
            checker = depth_stack.pop()
            if checker not in set(visited):
                visited.append(checker)
                for item in self._graph_content[checker]:
                    depth_stack.push(item)
        return visited

    def breadth_first_traversal(self, start):
        """Return the full visited path of a breadth first traversal."""
        breadth_queue = Queue()
        visited = []
        breadth_queue.enqueue(start)
        while breadth_queue.size() > 0:
            checker = breadth_queue.dequeue()
            if checker not in set(visited):
                visited.append(checker)
                for item in self._graph_content[checker]:
                    breadth_queue.enqueue(item)
        return visited


if __name__ == '__main__':
    example_graph = SimpleGraph()
    example_graph._graph_content = {
        3: ['7', 5],
        '7': ['11', 5],
        '11': [],
        5: [10],
        10: ['7'],
    }
    print(u"Made Graph:{}").format(example_graph.edges())
    start = time.time()
    example_graph.depth_first_traversal(3)
    end = time.time()
    print(u"Depth First Travel (from 3):")
    print(example_graph.depth_first_traversal(3))
    print(u"Took {} seconds").format(end-start)
    start = time.time()
    example_graph.breadth_first_traversal(3)
    end = time.time()
    print(u"Breadth First Travel (from 3):")
    print(example_graph.breadth_first_traversal(3))
    print(u"Took {} seconds").format(end-start)

