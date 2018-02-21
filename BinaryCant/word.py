"""
The word class file for Binary Cant, this is effectively the only thing the
language needs.
"""

# from typing import Optional, Union
from BinaryCant.word_const import *
from numpy import uint64 as uint
from functools import wraps


class FlagError(Exception):
    pass


def flag_getter(mask: uint) -> callable:
    return lambda word: word & mask


sentence_meta_flag = flag_getter(SENT_META_MASK)


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
def in_language_flag(word: uint) -> uint:
    """
    :param word: The word to check.
    :return: The flag (true or false) of the word being in the language
    """
    return word & IN_LANGUAGE_MASK



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
