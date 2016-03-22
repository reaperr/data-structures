# -*- coding: utf-8 -*-

from binheap import BinaryHeap


class PriorityQItem(object):
    """Represents an item in a priority queue.

    Contains some value and a priority integer.
    A higher interger is a higher priority.

    """
    def __init__(self, val, priority=1):
        """Constructor function of a Priority Queue Item."""
        self._val = val
        self._priority = priority

    def __lt__(self, other_item):
        """Checking if self is less than other item based on priority."""
        return self._priority < other_item._priority

    def __gt__(self, other_item):
        """Checking if self is greater than other item based on priority."""
        return self._priority > other_item._priority


class PriorityQ(object):
    """Python implementation of the Priority Queue data structure.

    A list of Objects passed into the PriorityQ constuctror are automatically
    converted to a PriorityQueueItem with default priority of one.

    A length 2 tuple will be coverted to a PriorityQueueItem.
    Index 0 will be the value
    Index 1 will be the priority
    If you need a 2 length tuple as your value in a Item use ((v, v), p)
    """

    def __init__(self, iter=None):
        """Constructor function of a Priority Queue."""
        self._priority_heap = BinaryHeap()

        if iter:
            for val in iter:
                if isinstance(val, PriorityQItem):
                    self.insert(val)
                elif isinstance(val, tuple) and len(val) == 2:
                    self.insert(PriorityQItem(val[0], val[1]))
                else:
                    self.insert(PriorityQItem(val))

    def insert(self, item):
        """Insert a new item into our queue."""
        if isinstance(item, PriorityQItem):
            self._priority_heap.push(item)
        else:
            self._priority_heap.push(PriorityQItem(item))

    def pop(self):
        """Remove the most important item from the queue."""
        return self._priority_heap.pop()._val

    def peek(self):
        """Return the most important item without removing it from the heap."""
        return self._priority_heap._heap_list[0]._val
