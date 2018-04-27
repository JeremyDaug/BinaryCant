from BinaryCant.Word.word_const import *
from BinaryCant.Word.word_types import type_codes, find_code_name
from numpy import uint64 as uint


class Word:
    def __init__(self):
        self.internal = True
        self.meta = False
        self.type = ''
        self.flags = []
        self.word = ''
        return

    def __str__(self):
        ret = ''
        if self.internal:
            if self.meta:
                flags = ','
                for flag in self.flags:
                    flags += flag + ','
                flags = flags[:-1]
                return '<{} {}>'.format(self.type, flags)
            else:
                flags = ''
                for flag in self.flags:
                    flags += flag + ','
                flags = flags[:-1]
                return '{} {} <{}>'.format(self.type, self.word, flags)
        else:
            return '(pointer) {}'.format(self.word)


def process_word(word: uint) -> Word:
    """
    Process raw word.
    :param word: The word to process.
    :return: the translated word.
    """
    result = Word()
    print(bin(word))
    print(POINTER.masker(word))
    result.internal = POINTER.masker(word) != 0  # 1
    print(result.internal)
    if result.internal:
        val = word & uint(0x7FFFFFFFFFFFFFFF)
        result.word = 'Pointer Call:' + str(val)
        return result
    if SENTENCE_META.masker(word) != 0:
        return process_sentence_meta(word, result)
    else:
        return process_word_base(word, result)


def process_word_base(word: uint, result: Word) -> Word:
    """
    Processes the word as a word.
    :param word: the word binary to process.
    :param result: The Word we are returning eventually.
    :return: The Word result.
    """
    result.flags.append(GRAMMAR.find_key(GRAMMAR.masker(word)))
    result.flags.append(TEMPORAL.find_key(TEMPORAL.masker(word)))
    result.flags.append(PROGRESS.find_key(PROGRESS.masker(word)))
    result.flags.append(RECURRENCE.find_key(RECURRENCE.masker(word)))
    result.flags.append(DEGREE.find_key(DEGREE.masker(word)))
    result.flags.append(EMPHASIS.find_key(EMPHASIS.masker(word)))
    result.flags.append(PLURALITY.find_key(PLURALITY.masker(word)))
    if WORD_GROUP.masker(word) != 0:
        result.type = find_code_name(WORD_TYPE.masker(word))
        result.word = word & TYPED_WORD_MASK
    else:
        result.type = ''
        result.word = word & UNTYPED_WORD_MASK
    return result


def process_sentence_meta(word: uint, result: Word) -> Word:
    result.meta = True
    result.type = SENTENCE_TYPES.find_key(SENTENCE_TYPES.masker(word))
    result.flags.append(AFFECTIONS.find_key(AFFECTIONS.masker(word)))
    result.flags.append(EVIDENTIALITY.find_key(EVIDENTIALITY.masker(word)))
    result.count = META_WORD_MASK & word
    return result


if __name__ == '__main__':
    import BinaryCant.compiler.cant_yacc as yc
    with open('test_cant.can', 'r') as file:
        words = file.read()
    print(words)
    print('---------------------------')
    result = yc.compile('test_cant.can')
    print(result)
    for i in result:
        print(process_word(i))

