"""
The fire for the structure of binary cant.

Started 13-Feb-2018.
"""

from numpy import uint64 as uint
from word import Word


class Cant:
    def __init__(self):
        self.cantName = ''
        self.length = 0
        self.sentence = []
        return

    def translate(self) -> str:
        ret = ''
        # A stack of stacks.
        stack = []
        for word in self.sentence:
            data = Word.disect(word)
        return ret
