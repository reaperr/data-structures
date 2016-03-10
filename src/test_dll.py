# -*- coding: utf-8-*-

import pytest
from linked_list import LinkedList
from dll import DLL



@pytest.fixture(scope="function")
def test_empty_DLL():
    return DLL()

@pytest.fixture(scope="function")
def test_DLL():
    return DLL([1, 2, 3])


def test_init_DLL():
    """Testing the __init__ method of DLL object."""
    assert isinstance(DLL(), DLL)
    assert isinstance(DLL([1, 2, 3]), DLL)
    assert issubclass(DLL, LinkedList)
    test_DLL = DLL()
    assert test_DLL.tail is None


def test_insert(test_empty_DLL, test_DLL):
    test_empty_DLL.insert(4)
    assert test_empty_DLL.head.val == 4
    test_DLL.insert(5)
    assert test_DLL.head.val == 5
    assert test_DLL.head.next_node.val == 3


def test_append(test_empty_DLL, test_DLL):
    test_empty_DLL.append(6)
    assert test_empty_DLL.tail.val == 6
    test_DLL.append(7)
    assert test_DLL.tail.val == 7
    assert test_DLL.tail.prev_node.val == 1

def test_pop(test_empty_DLL, test_DLL):
    assert test_empty_DLL.pop() is None
    assert test_DLL.pop() == 3
    assert test_DLL.head.val == 2

def test_shift(test_empty_DLL, test_DLL):
    assert test_empty_DLL.shift() is None
    assert test_DLL.shift() == 1
    assert test_DLL.tail.val == 2

def test_remove(test_empty_DLL, test_DLL):
    with pytest.raises(ValueError):
        test_empty_DLL.remove(3)
    test_DLL.remove(2)
    assert test_DLL.to_string() == '(3, 1)'
    test_DLL.remove(3)
    assert test_DLL.to_string() == '(1)'
    test_DLL.remove(1)
    assert test_DLL.to_string() == '()'
    long_DLL = DLL([5, 5, 6, 7, 4, 6, 0])
    long_DLL.remove(5)
    assert long_DLL.to_string() == '(0, 6, 4, 7, 6, 5)'
    long_DLL.remove(6)
    assert long_DLL.to_string() == '(0, 4, 7, 6, 5)'
