# -*- coding: utf-8-*-

from linked_list import LinkedList
from linked_list import Node


class DLL(LinkedList):
    """Double Linked List class that inherits LinkedList."""

    def __init__(self, iter=None):
        """Constructor for Double Linked List."""
        self.tail = None
        self.head = None
        if iter:
            for val in iter:
                self.insert(val)

    def insert(self, val):
        """Inserts value at the head of the list."""
        new_node = Node(val=val, next_node=self.head)
        if self.head:
            self.head.prev_node = new_node
        else:
            self.tail = new_node
        self.head = new_node

    def append(self, val):
        """Inserts value at the tail of the list."""
        new_node = Node(val=val, prev_node=self.tail)
        if self.tail:
            self.tail.next_node = new_node
        else:
            self.head = new_node
        self.tail = new_node

    def pop(self):
        pass
