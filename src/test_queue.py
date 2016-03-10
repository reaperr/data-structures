# -*- coding: utf-8 -*-

import pytest

from queue import Queue


@pytest.fixture(scope="function")
def test_empty_Queue():
    return Queue()

@pytest.fixture(scope="function")
def test_Queue():
    return Queue([1, 2, 3])


def test_init_Queue(test_empty_Queue, test_Queue):
    """Testing the __init__ method of Queue."""
    assert isinstance(test_empty_Queue, Queue)
    assert isinstance(test_Queue, Queue)
    assert test_Queue._container.to_string() == "(1, 2, 3)"


def test_enqueue(test_empty_Queue, test_Queue):
    """Tests the enqueue method of Queue."""
    test_Queue.enqueue(4)
    test_empty_Queue.enqueue(2)
    assert test_Queue._container.to_string() == "(1, 2, 3, 4)"
    assert test_empty_Queue._container.to_string() == "(2)"
