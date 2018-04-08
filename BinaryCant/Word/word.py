"""
The word class file for Binary Cant, this is effectively the only thing the
language needs.
"""

# from typing import Optional, Union
from BinaryCant.Word.word_const import *
from numpy import uint64 as uint


class FlagError(Exception):
    pass


def flag_val(val: str) -> uint:
    if val in TOKENDICT:
        return TOKENDICT[val]
    elif val in SENT_FLAG_DICT:
        return SENT_FLAG_DICT[val]
    else:
        raise FlagError(val + "  is not a valid flag.")


def external_pointer_flag(word: uint) -> uint:
    return word & EXTERNAL_POINTER_TRUE_FLAG


def sentence_meta_flag(word: uint) -> uint:
    """
    :param word: The word to check.
    :return: The flag of the word.
    """
    print(word & SENT_META_MASK)
    return word & SENT_META_MASK


def sentence_meta_must_be(res: bool) -> callable:
    """
    A decorator which checks if a word has a flag properly set before running
    the function.
    :param res: True if we want the word to be sentence metadata,
    false otherwise.
    :return: Callable function which has which check wrapped around it.
    :raises FlagError if the flag and the required value do not match.
    """
    def must_be_sentence_meta(func: callable):
        def wrap(word):
            flag = sentence_meta_flag(word)
            if res:  # if it must be True,
                if flag != SENT_META_TRUE_FLAG:  # but it isn't.
                    raise FlagError("Must me Sentence Metadata.")
            else:  # If it must be False,
                if flag != SENT_META_FALSE_FLAG:  # but it isn't.
                    raise FlagError("Must not be Sentence Metadata")
            func(word)
        return wrap
    return must_be_sentence_meta


@sentence_meta_must_be(True)
def sentence_type_flag(word: uint) -> uint:
    """
    :param word: Word to check.
    :return: The Metadata type flag of the word.
    """
    print(word & SENT_TYPE_MASK)
    return word & SENT_TYPE_MASK


@sentence_meta_must_be(True)
def sentence_subtype_flag(word: uint) -> uint:
    """
    :param word: Word to check
    :return: the metadata subtype flag of the word
    """
    return word & SENT_SUBTYPE_MASK


@sentence_meta_must_be(True)
def affection_flag(word: uint) -> uint:
    """
    :param word: the word to check.
    :return: the metadata affection flag of the word.
    """
    return word & AFF_TYPE_MASK


@sentence_meta_must_be(True)
def evid_flag(word: uint) -> uint:
    """
    :param word: the word to check.
    :return: the metadata evidentiality flag of the word.
    """
    return word & EVID_MASK


@sentence_meta_must_be(True)
def word_count(word: uint) -> uint:
    """
    :param word: The word to check.
    :return: The number of words in the sentence.
    :raise: Value error if not sentence metadata.
    """
    return word & WORD_COUNT_MASK


@sentence_meta_must_be(False)
def grammar_flag(word: uint) -> uint:
    """
    :param word: The word to check.
    :return: The grammar flags of the word.
    """
    return word & GRAMMAR_MASK


@sentence_meta_must_be(False)
def temporal_flag(word: uint) -> uint:
    """
    :param word: The word to check.
    :return: The temporal flag of the word.
    """
    return word & TEMPORAL_MASK


@sentence_meta_must_be(False)
def progress_flag(word: uint) -> uint:
    """
    :param word: The word to check.
    :return: The progress flag of the word.
    """
    return word & PROGRESS_MASK


@sentence_meta_must_be(False)
def recurrence_flag(word: uint) -> uint:
    """
    :param word: The word to check.
    :return: The Recurrence flag of the word.
    """
    return word & RECURRENCE_MASK


@sentence_meta_must_be(False)
def degree_flag(word: uint) -> uint:
    """
        :param word: The word to check.
        :return: The degree flag of the word.
    """
    return word & DEGREE_MASK


@sentence_meta_must_be(False)
def emphasis_flag(word: uint) -> uint:
    """
    :param word: The word to check.
    :return: The emphasis flag of the word.
    """
    return word & EMPHASIS_MASK


@sentence_meta_must_be(False)
def plurality_flag(word: uint) -> uint:
    """
    :param word: The word to check.
    :return: The pluarity flag of the word
    """
    return word & PLURALITY_MASK


@sentence_meta_must_be(False)
def external_flag(word: uint) -> uint:
    """
    :param word: The word to check.
    :return: The External type of the word.
    """
    return word & EXTERNAL_TYPE_MASK


@sentence_meta_must_be(False)
def external_word(word: uint) -> uint:
    """
    :param word: The word to check.
    :return: The external native data of the word.
    """
    return word & EXTERNAL_WORD_MASK


@sentence_meta_must_be(False)
def internal_type(word: uint) -> uint:
    """
    :param word: The word to check.
    :return: The internally defined group.
    """
    return word & INTERNAL_TYPE_MASK


@sentence_meta_must_be(False)
def internal_word(word: uint) -> uint:
    """
    :param word: The word to check.
    :return: The internal word data.
    """
    return word & INTERNAL_WORD_MASK

def process_external_word(word, val_type) -> uint:
    type_switch = {ET_INT: process_int_type,
                   ET_FLOAT: process_float_type,
                   ET_RGB: process_rbg_type}
    return type_switch[val_type](word)

def process_int_type(word: str) -> uint:
    ret = uint(int(word))
    return ret

def process_float_type(word: str) -> uint:
    ret = uint(0)
    return ret

def process_rbg_type(word: str) -> uint:
    ret = uint(0)
    return ret
