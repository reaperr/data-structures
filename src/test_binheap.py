# -*- coding: utf-8-*-

import pytest


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


def test_heap_check(binheap):
    binheap._heap_check(1, 3)
