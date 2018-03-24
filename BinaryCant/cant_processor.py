

from numpy import uint64 as uint
from typing import List


class CantProcessor:

    def read_file(self, file_name: str) -> List[uint]:
        with open(file_name) as file:
            text = file.read()

