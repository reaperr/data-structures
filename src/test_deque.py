# -*- coding: utf-8 -*-

import pytest
from deque import Deque


@pytest.fixture(scope="function")
def empty_deque():
    return Deque()


@pytest.fixture(scope="function")
def deque():
    return Deque([1, 2, 3])


def test_append_empty(empty_deque):
    empty_deque.append(1)
    assert empty_deque.container.to_string() == '(1)'


def test_append(deque):
    deque.append(4)
    assert deque.container.to_string() == '(1, 2, 3, 4)'


def test_append_left_empty(empty_deque):
    empty_deque.appendleft(1)
    assert empty_deque.container.to_string() == '(1)'


def test_append_left(deque):
    deque.appendleft(5)
    assert deque.container.to_string() == '(5, 1, 2, 3)'


def test_pop_empty(empty_deque):
    with pytest.raises(AttributeError):
        empty_deque.pop()


def test_pop(deque):
    assert deque.pop() == 3


def test_popleft_empty(empty_deque):
    with pytest.raises(AttributeError):
        empty_deque.popleft()


def test_popleft(deque):
    assert deque.popleft() == 1


def test_peek_empty(empty_deque):
    assert empty_deque.peek() is None


def test_peek(deque):
    assert deque.peek() == 3


def test_peekleft_empty(empty_deque):
    assert empty_deque.peekleft() is None


def test_peekleft(deque):
    assert deque.peekleft() == 1


def test_empty_size(empty_deque):
    assert empty_deque.size() == 0


def test_size(deque):
    assert deque.size() == 3
