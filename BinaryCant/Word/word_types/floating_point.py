from numpy import float32
from numpy import uint64 as uint

flag = 'float'


def process_word(word: str) -> float32:
    return float32(float(word))


def process_bin(val: uint) -> str:
    temp = float32(0) | val
    return str(temp)
