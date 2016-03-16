# -*- coding: utf-8-*-

import pytest
from binheap import BinaryHeap

@pytest.fixture(scope="function")
def binheap():
    return BinaryHeap([34, 25, 10, 11, 3])


def test_BinHeap_init():
    test_heap = BinaryHeap([1, 2, 3])
    assert test_heap._child_index(0) == (1, 2)
    assert test_heap._parent_index(1) == 0


def test_push(binheap):
    binheap.push(13)
    assert binheap.heap_list[2] == 13


def test_pop(binheap):
    binheap.pop()
    assert binheap.heap_list[3] == 3


def test_heap_check_up(binheap):
    binheap._heap_check_up(1, 3)


def test_heap_check_down(binheap):
    binheap._heap_check_down(0)


def test_child_index(binheap):
    assert binheap._child_index(1) == (3, 4)


def test_parent_index(binheap):
    assert binheap._parent_index(4) == 1
