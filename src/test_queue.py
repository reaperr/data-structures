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
    """testing the __init__ method of Queue."""
    assert isinstance(test_empty_Queue, Queue)
    assert isinstance(test_Queue, Queue)
    assert test_Queue._container.to_string() == "(1, 2, 3)"
