from numpy import uint64 as uint

flag = 'rbga'


def process_word(word: str) -> uint:
    r, b, g, a = word.split(',')
    r, b, g, a = uint(int(r)), uint(int(b)), uint(int(g)), uint(int(a))
    if max(r, b, g, a, 255) != 255:
        raise ValueError('Color values must be between 0 and 255 inclusive.')
    val = (r << 24) + (b << 16) + (g << 8) + a
    return val


def process_bin(val: uint) -> str:
    r = val & 0xFF000000 / 0x1000000
    b = val & 0x00FF0000 / 0x10000
    g = val & 0x0000FF00 / 0x100
    a = val & 0x000000FF
    return '{},{},{},{}'.format(r, b, g, a)
