# -*- coding: utf8 -*-
from linked_list import LinkedList


class Stack(LinkedList):

    """A Stack Data Structure."""

    def pop(self):
        """Remove a value from stack and return that value."""
        rtn_val = LinkedList.pop(self)
        if rtn_val is None:
            raise LookupError
        return rtn_val

    def push(self, val):
        """Add val to the stack."""
        LinkedList.insert(self, val)
