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
