# -*- coding: utf-8 -*-

from priorityq import PriorityQ, PriorityQItem

import pytest

PQ_ITEM_LIST = [
    PriorityQItem(31, 1),
    PriorityQItem(32, 2),
    PriorityQItem(33, 1),
    PriorityQItem(34, 2),
    PriorityQItem(35, 1)
]


@pytest.fixture(scope="function")
def test_pq():
    return PriorityQ(PQ_ITEM_LIST)


def test_PriorityQ_init(test_pq):
    assert test_pq._priority_heap._heap_list[0]._priority == 2
    assert test_pq._priority_heap._heap_list[4]._priority == 1


def test_PriorityQ_default():
    test_pq = PriorityQ([1, 2, 3])
    assert test_pq._priority_heap._heap_list[0]._priority == 1


def test_insert(test_pq):
    test_pq.insert(PriorityQItem(12, 5))
    assert test_pq._priority_heap._heap_list[0]._priority == 5
