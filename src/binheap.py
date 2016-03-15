# -*- coding: utf-8-*-


class BinaryHeap(object):
    """Python implementation of a Binary Heap Data Structure."""

    def __init__(self, iter=None):
        """Constructor function for BinaryHeap."""
        self._heap_list = []

        if iter:
            for val in iter:
                self.push(val)

    @property
    def heap_list(self):
        return self._heap_list

    def push(self, val):
        """Put new value into the heap, maintaining the heap property."""
        self._heap_list.append(val)
        #import pdb; pdb.set_trace()
        self._heap_check(self._parent_index(len(self._heap_list) - 1),
                         len(self._heap_list) - 1)

    def _heap_check(self, parent_index, child_index):
        """Check if value of child is greater or less than parent."""
        if child_index == 0 or parent_index is None:
            return
        if self._heap_list[child_index] > self._heap_list[parent_index]:
            # Swtich the location of parent and child if child is greater.
            self._heap_list[parent_index], self._heap_list[child_index] = \
                self._heap_list[child_index], self._heap_list[parent_index]
        self._heap_check(self._parent_index(parent_index), parent_index)

    def _child_index(self, parent_index):
        """Return a tuple of the parent_index' child indexes (Left, Right)."""
        return (2 * parent_index + 1, 2 * parent_index + 2)

    def _parent_index(self, child_index):
        """Return the index of the child_index's parent."""
        return (child_index - 1) // 2
