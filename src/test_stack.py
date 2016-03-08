import pytest
from stack import Stack
from linked_list import LinkedList


def test_stack_init():
    """Test the __init__ method of Stack object."""
    assert isinstance(Stack(), Stack)
    assert isinstance(Stack([1, 2, 3]), Stack)
    assert issubclass(Stack, LinkedList)


def test_pop_stack():
    """Test the pop() method of Stack."""
    assert Stack([1, 2, 3]).pop() == 3
    with pytest.raises(LookupError):
        Stack().pop()


def test_push_stack():
    """Test the push(val) method of Stack."""
    stack1 = Stack([1, 2, 3])
    stack1.push(4)
    assert stack1.head.val == 4
    stack2 = Stack()
    stack2.push(1)
    assert stack2.head.val == 1
