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
        """Insert a value at the head of the list."""
        new_node = Node(val=val, next_node=self.head)
        if self.head:
            self.head.prev_node = new_node
        else:
            self.tail = new_node
        self.head = new_node

    def append(self, val):
        """Append a value at the tail of the list."""
        new_node = Node(val=val, prev_node=self.tail)
        if self.tail:
            self.tail.next_node = new_node
        else:
            self.head = new_node
        self.tail = new_node

    def pop(self):
        """Pop the value at the head of the list."""
        try:
            rtn_value = self.head.val
            new_head = self.head.next_node
            self.head = new_head
            self.head.prev_node = None
            return rtn_value
        except AttributeError:
            return None

    def shift(self):
        """Remove the value at the tail of the list."""
        try:
            rtn_value = self.tail.val
            new_tail = self.tail.prev_node
            self.tail = new_tail
            self.tail.next_node = None
            return rtn_value
        except AttributeError:
            return None

    def remove(self, val):
        """Remove first instance of val from the list starting from head."""
        val_search = LinkedList.search(self, val)
        if val_search is None:
            raise ValueError
        try:  # Runs if removing node from middle.
            val_search.prev_node.next_node = val_search.next_node
            val_search.next_node.prev_node = val_search.prev_node
        except AttributeError:
            try:  # Runs if removing head or tail.
                if self.head == val_search:
                    self.head = val_search.next_node
                    self.head.prev_node = None
                if self.tail == val_search:
                    self.tail = val_search.prev_node
                    self.tail.next_node = None
            except AttributeError:
                # Runs if removing last node.
                self.head = None
                self.tail = None
        return val_search.val
