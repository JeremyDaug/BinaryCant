"""
A file to help out with nesting stacks in stacks.
"""

from typing import Optional


class NestingStack:
    def __init__(self):
        self.data = []
        self.head = None
        return

    def traverse(self, val: Optional[list] = None):
        """
        An iterator for all the data in the nesting stack.
        :yield:
        """
        if val is None:
            val = self.data
        if isinstance(val, list):
            for value in val:
                for subvalue in self.traverse(value):
                    yield subvalue
        else:
            yield 0

    def __iter__(self):
        return

    def __next__(self):
        return
