# -*- coding: utf-8 -*-

from dll import DLL

class Deque(object):
    """Python Implementation of Deque Data Structure"""

    def __init__(self, iter=None):
        """Constructor Function for Deque."""
        self.container = DLL()
        if iter:
            for val in iter:
                self.container.append(val)

    def append(self, val):
        """Add val to the end of the Deque."""
        self.container.append(val)

    def appendleft(self, val):
        """Add val to the start of the Deque."""
        self.container.insert(val)

    def pop(self):
        """Remove and return the value at the end of the Deque."""
        rtn_val = self.container.shift()
        if rtn_val:
            return rtn_val
        raise AttributeError

    def popleft(self):
        """Remove and the return the value at the front of the Deque"""
        rtn_val = self.container.pop()
        if rtn_val:
            return rtn_val
        raise AttributeError

    def peek(self):
        pass

    def peekleft(self):
        pass

    def size(self):
        pass
