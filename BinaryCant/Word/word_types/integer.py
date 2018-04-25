from numpy import uint64 as uint

flag = 'int'


def process_word(word: str) -> uint:
    return uint(int(word))


def process_bin(val: uint) -> str:
    return str(val)
