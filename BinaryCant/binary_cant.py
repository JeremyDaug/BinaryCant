"""
The fire for the structure of binary cant.

Started 13-Feb-2018.
"""

import BinaryCant.Word as w
from numpy import uint64 as uint
from typing import Optional, List
from collections import deque


class FileCant:
    def __init__(self, name: str = 'empty.bc', length: int = 0,
                 data: Optional[List[uint]] = None):
        self.cant_name = name
        self.byte_length = length
        if data:
            self.file_data = data
        else:
            self.file_data = []
        return

    def load_file(self, name) -> None:
        self.cant_name = name
        with open(name, 'r') as f:
            self.byte_length = f.readline()
            self.file_data = f.read().split('\n')
        return

    def organize(self, data: deque = None) -> list:
        """
        Organizes the data into a nested list format.
        :return: An organized format of the cant in nested list format.
        """
        if data is None:
            data = deque()
            data.extend(self.file_data)
        res = []
        while len(data) > 0:
            curr = data.popleft()
            if w.sentence_meta_flag(curr) & w.SENT_META_TRUE_FLAG:
                res.append(self.organize(data))
            else:  # Not sentence meta-data
                res.append(curr)
