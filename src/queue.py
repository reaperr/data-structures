# -*- coding: utf-8 -*-

from dll import DLL


class Queue(object):
    """Queue class that contains a DLL."""
    def __init__(self, iter=None):
        self._container = DLL()
        if iter:
            for val in iter:
                self._container.append(val)

    def enqueue(self, val):
        """Adds a value to the end of the queue."""
        self._container.append(val)

    def dequeue(self):
        """Removes and returns value from front of queue."""
        temp_value = self._container.pop()
        if temp_value:
            return temp_value
        raise ValueError

    def peek(self):
        """Returns the next value in the queue without dequeing it."""
        try:
            return self._container.head.val
        except AttributeError:
            return None

    def size(self):
        """Returns the size of the queue."""
        return self._container.size()
