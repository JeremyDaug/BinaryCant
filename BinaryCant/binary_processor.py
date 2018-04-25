from BinaryCant.Word.word import *
from BinaryCant.Word.word_const import *
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
    result = Word()
    result.internal = POINTER.masker(word)
    if not result.internal:
        result.word = word ^ POINTER_TRUE_FLAG
        return result
    if sentence_meta_flag(word):
        process_sentence_meta(word, result)
    else:
        process_word_base(word, result)
    return result


def process_word_base(word: uint, result: Word):
    grammar = grammar_flag(word)
    temporal = temporal_flag(word)
    progress = progress_flag(word)
    recurrence = recurrence_flag(word)
    degree = degree_flag(word)
    emphasis = emphasis_flag(word)
    plurality = plurality_flag(word)
    external = external_flag(word)

    return


def process_sentence_meta(word: uint, result: Word):
    result.meta = True
    val = sentence_subtype_flag(word)
    result.type = FIND_SENT_FLAG(val)
    affect = affection_flag(word)
    evidence = evid_flag(word)
    words = word_count(word)
    result.flags = [FIND_SENT_FLAG(affect), FIND_SENT_FLAG(evidence)]
    result.word = words
    return
