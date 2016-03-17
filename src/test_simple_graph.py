# -*- coding: utf-8 -*-

import pytest
from simple_graph import SimpleGraph


@pytest.fixture()
def test_graph():
    test_dict = {1: [2, 3], 2: [1], 3: [2]}
    test_graph = SimpleGraph()
    test_graph._graph_content = test_dict
    return test_graph

def test_init():
    test_graph = SimpleGraph()
    assert test_graph._graph_content == {}
