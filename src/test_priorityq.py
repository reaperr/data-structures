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
    assert test_pq._priority_heap[0].priority == 1
    assert test_pq._priority_heap[4].priority == 2
