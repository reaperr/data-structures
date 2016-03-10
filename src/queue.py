# -*- coding: utf-8 -*-

from dll import DLL


class Queue(object):
    def __init__(self, iter=None):
        self._container = DLL()
        if iter:
            for val in iter:
                self._container.append(val)
