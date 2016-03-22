# -*- coding: utf-8 -*-

import pytest
from simple_graph import SimpleGraph


@pytest.fixture()
def test_graph():
    test_dict = {1: [2, 3], 2: [1], 3: [2, 10], 10: []}
    test_graph = SimpleGraph()
    test_graph._graph_content = test_dict
    return test_graph


def test_init():
    test_graph = SimpleGraph()
    assert test_graph._graph_content == {}


def test_nodes(test_graph):
    assert test_graph.nodes() == [1, 2, 3, 10]


def test_edges(test_graph):
    assert test_graph.edges() == [(1, [2, 3]), (2, [1]), (3, [2, 10]), (10, [])]


def test_add_node(test_graph):
    test_graph.add_node(4)
    assert test_graph._graph_content[4] == []


def test_add_repeat_node(test_graph):
    with pytest.raises(ValueError):
        test_graph.add_node(3)


def test_add_edge(test_graph):
    test_graph.add_edge(4, 2)
    assert test_graph._graph_content[4] == [2]


def test_del_node(test_graph):
    test_graph.del_node(3)
    assert test_graph._graph_content[1] == [2]


def test_del_edge(test_graph):
    test_graph.del_edge(3, 2)
    assert test_graph._graph_content[3] == [10]


def test_has_node(test_graph):
    assert test_graph.has_node(1) is True
    assert test_graph.has_node(5) is False


def test_neighbors(test_graph):
    assert test_graph.neighbors(2) == [1, 3]


def test_bad_neighbors(test_graph):
    with pytest.raises(ValueError):
        test_graph.neighbors(6)

def test_adjacent(test_graph):
    assert test_graph.adjacent(2, 3) is True
    assert test_graph.adjacent(2, 10) is False


def test_bad_adjacent(test_graph):
    with pytest.raises(ValueError):
        test_graph.adjacent(34, 56)


def test_dfs(test_graph):
    # cyclic
    assert test_graph.depth_first_traversal(1) == [1, 3, 10, 2]
    # non-cyclic
    assert test_graph.depth_first_traversal(2) == [2, 1, 3, 10]


def test_bfs(test_graph):
    # cyclic
    assert test_graph.breadth_first_traversal(1) == [1, 2, 3, 10]
    # non-cyclic
    assert test_graph.breadth_first_traversal(2) == [2, 1, 3, 10]
