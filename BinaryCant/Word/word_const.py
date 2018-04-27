"""
A const file for our word flags, just to organize things better.
"""
from numpy import uint64 as uint
from typing import List
from BinaryCant.Word import word_types as wt


def print_word_bin(word: uint) -> None:
    """
    Helper to print a value in binary.
    :param word: The word to print
    """
    print(format(word, '#066b'))


def print_word_hex(word: uint) -> None:
    """
    Helper to print a value in binary.
    :param word: The word to print
    """
    print(format(word, '#018x'))


class FlagCategories:
    def __init__(self, name: str, bit_shift: int, bit_length: int, keys: List[str]):
        self.name = name
        self.bit_length = bit_length
        self.values = [uint(i << bit_shift) for i in range(2**self.bit_length)]
        self.shift = uint(bit_shift)
        self.keys = dict()
        print(name)
        for key, value in zip(keys, self.values):
            print_word_bin(value)
            self.keys[key] = value
        return

    def key_regex(self) -> str:
        ret = ''
        for key in self.keys:
            ret += key + '|'
        ret = ret[:-1]
        # pass over for escape characters.
        i = 0
        while i < len(ret):
            if ret[i] in ['?']:
                ret = ret[:i] + '\\' + ret[i:]
                i += 1
            i += 1
        return ret

    def find_key(self, value: uint) -> str:
        for key, val in self.keys.items():
            if val == value:
                return key

    def masker(self, value: uint) -> uint:
        mask = uint(2**(self.bit_length+1)-1) << self.shift
        return value & mask


POINTER = FlagCategories('Pointer', 63, 1, keys=['in', 'out'])


def pointer_masker(value: uint) -> uint:
    return value & 0x8000000000000000


POINTER.masker = pointer_masker

SENTENCE_META = FlagCategories('Meta', 62, 1, keys=['meta', 'word'])
SENTENCE_TYPES = FlagCategories('Sentence Types', 58, 4,
                                # Question Flags
                                ['QS', 'QO', 'QV', 'QT', 'QL', 'QR', 'QE',
                                 'QC',
                                 # Statement Flags
                                 'SA', 'SD', 'SU', 'SC', 'SR', 'SI', 'S!',
                                 'S?'])
AFFECTIONS = FlagCategories('Affections', 54, 4,
                            ['hon', 'lie', 'hap', 'sad', 'fea', 'ang', 'ant',
                             'sur', 'ben', 'mal', 'pai', 'ple', '000', '111',
                             '222', '333'])
EVIDENTIALITY = FlagCategories('Evidentiality', 51, 3,
                               ['obv', 'quo', 'exp', 'con', 'gen', 'pos',
                                'opi', 'und'])
META_WORD_MASK = uint(2**51-1)

# word flags
GRAMMAR = FlagCategories('Grammar', 60, 3,
                         ['sub', 'obj', 'top', 'ver', 'mod', 'rel', 'und1',
                          'und2'])
TEMPORAL = FlagCategories('Temporal', 58, 2,
                          ['timeless', 'pas', 'pre', 'fut'])
PROGRESS = FlagCategories('Progress', 56, 2,
                          ['unp', 'uns', 'pro', 'com'])
RECURRENCE = FlagCategories('Recurrence', 54, 2,
                            ['unr', 'irr', 'con', 'hab'])
DEGREE = FlagCategories('Degree', 51, 3,
                        ['-', '0', '1', '2', '3', '4', '5', '6'])


def repregex() -> str:
    return r'[0-6](?=[^0-9])'


DEGREE.key_regex = repregex


EMPHASIS = FlagCategories('Emphasis', 50, 1,
                          ['une', '!'])
DETERMINATIVE = FlagCategories('Determinative', 49, 1,
                               ['undet', '?'])
PLURALITY = FlagCategories('Plurality', 47, 2,
                           ['uva', 'sin', 'plu', 'num'])
WORD_GROUP = FlagCategories('Word Group', 46, 1,
                            ['untyped', 'typed'])


WORD_TYPE = FlagCategories('Word Types', 32, 12,
                           wt.word_types)
TYPED_WORD_MASK = uint(2**33)-1  # Words with formulas for meaning.
UNTYPED_WORD_MASK = uint(2**46-1)  # words that are not formulated

Flag_Groups = [POINTER, SENTENCE_META, SENTENCE_TYPES, AFFECTIONS,
               EVIDENTIALITY, GRAMMAR, TEMPORAL, PROGRESS, RECURRENCE, DEGREE,
               EMPHASIS, DETERMINATIVE, PLURALITY, WORD_GROUP, WORD_TYPE]

Flag_Values = {}
for group in Flag_Groups:
    Flag_Values.update(group.keys)


def find_flag_group(flag: str) -> str:
    for group in Flag_Groups:
        if flag in group.keys:
            return group.name


def find_value_group(value: uint) -> str:
    if value == uint(0):
        return '?????????'
    for group in Flag_Groups:
        for key, val in group.keys.items():
            if val == value:
                return group.name
