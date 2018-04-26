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


def process_word(word: uint) -> Word:
    '''
    Process raw word.
    :param word: The word to process.
    :return: the translated word.
    '''
    result = Word()
    result.internal = POINTER.masker(word) != 0  # 1
    if not result.internal:
        result.word = 'Pointer Call:' + str(word ^ 0x7FFFFFFFFFFFFFFF)
        return result
    if SENTENCE_META.masker(word) != 0:
        return process_sentence_meta(word, result)
    else:
        process_word_base(word, result)
    return result


def process_word_base(word: uint, result: Word) -> Word:
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
