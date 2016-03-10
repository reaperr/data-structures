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
    assert isinstance(test_empty_Queue, Queue)
    assert isinstance(test_Queue, Queue)
    assert test_Queue._container.to_string() == "(1, 2, 3)"


def test_enqueue(test_empty_Queue, test_Queue):
    test_Queue.enqueue(4)
    test_empty_Queue.enqueue(2)
    assert test_Queue._container.to_string() == "(1, 2, 3, 4)"
    assert test_empty_Queue._container.to_string() == "(2)"

def test_dequeue(test_empty_Queue, test_Queue):
    assert test_Queue.dequeue() == 1
    with pytest.raises(ValueError):
        test_empty_Queue.dequeue()

def test_peek(test_empty_Queue, test_Queue):
    assert test_Queue.peek() == 1
    assert test_empty_Queue.peek() is None

def test_size(test_empty_Queue, test_Queue):
    assert test_Queue.size() == 3
    assert test_empty_Queue.size() == 0
