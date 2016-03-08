import pytest

from linked_list import LinkedList
def test_init_LinkedList():
    test_list = LinkedList()
    test_list2 = LinkedList([1, 2, 3])
    assert isinstance(test_list, LinkedList)
    assert isinstance(test_list2, LinkedList)

def test_insert_LinkedList():
    test_list = LinkedList()
    test_list2 = LinkedList([1, 2, 3])
    test_list.insert(5)
    test_list2.insert(6)
    assert test_list.head.val == 5
    assert test_list2.head.val == 6

def test_pop_LinkedList():
    test_list = LinkedList()
    test_list2 = LinkedList([1, 2, 3])
    assert test_list.pop() is None
    assert test_list2.pop() == 3

def test_size_LinkedList():
    test_list = LinkedList()
    test_list2 = LinkedList([1, 2, 3])
    assert test_list.size() == 0
    assert test_list2.size() == 3

def test_search_LinkedList():
    from linked_list import Node
    test_list = LinkedList()
    test_list2 = LinkedList([1, 2, 3])
    test_node = Node(3)
    assert test_list2.search(3).val == test_node.val
    assert test_list.search(50) is None
    assert test_list2.search(50) is None

def test_remove_LinkedList():
    from linked_list import Node
    test_node = Node(3)
    test_list2 = LinkedList([1, 2, 3, 4, 3])
    test_list = LinkedList()
    test_list2.remove(test_node)
    assert test_list2.size() == 3
    with pytest.raises(ValueError):
        test_list.remove(test_node)


def test_display_LinkedList():
    test_list = LinkedList()
    test_list2 = LinkedList([1, 2, 3])
    assert test_list2.to_string() == '(3, 2, 1)'
