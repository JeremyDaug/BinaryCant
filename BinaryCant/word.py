"""
The word class file for Binary Cant, this is effectively the only thing the
language needs.
"""

# from typing import Optional, Union
from numpy import uint64 as uint


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

# masks for the class
# sentence masks
ZEROED                = uint(0b0)
SENT_META_MASK        = uint(0b1        << 63)
SENT_TYPE_MASK        = uint(0b01       << 62)
SENT_SUBTYPE_MASK     = uint(0b00111    << 59)
AFF_TYPE_MASK         = uint(0b000001111 << 55)
EVID_MASK             = uint(0b000000000111 << 52)
WORD_COUNT_MASK       = 2**52-1
if __name__ == '__main__':
    print_word_bin(ZEROED)
    print_word_bin(SENT_META_MASK)
    print_word_bin(SENT_TYPE_MASK)
    print_word_bin(SENT_SUBTYPE_MASK)
    print_word_bin(AFF_TYPE_MASK)
    print_word_bin(EVID_MASK)
    print_word_bin(WORD_COUNT_MASK)
# word meta masks
IN_LANGUAGE_MASK      = uint(0b1 << 63)
GRAMMAR_MASK          = uint(0b0111 << 60)
TEMPORAL_MASK         = uint(0b11 << 58)
PROGRESS_MASK         = uint(0b11 << 56)
RECURRENCE_MASK       = uint(0b11 << 54)
DEGREE_MASK           = uint(0x111 << 51)
EMPHASIS_MASK         = uint(0b1 << 50)
DETERMINATIVE_MASK    = uint(0b1 << 49)
PLURALITY_MASK        = uint(0b11 << 47)
# External masks (for things without abstract meanings).
EXTERNAL_TYPE_MASK    = uint(0x111111111111111 << 32)
EXTERNAL_WORD_MASK    = uint(0xFFFFFFFF)
# Internal word masks
INTERNAL_TYPE_MASK    = uint(0x600000000000)

# Flags
SENT_META_TRUE_FLAG   = uint(0b1 << 63)
QUERY_FLAG            = uint(0b0 << 62)
Q_SUBJECT_FLAG        = uint(0b0000 << 59)
Q_OBJECT_FLAG         = uint(0b0001 << 59)
Q_CLARIFY_FLAG        = uint(0b0010 << 59)
Q_TIME_FLAG           = uint(0b0011 << 59)
Q_LOCATION_FLAG       = uint(0b0100 << 59)
Q_REASONING_FLAG      = uint(0b0101 << 59)
Q_EXPLAIN_FLAG        = uint(0b0110 << 59)
Q_SPECIFY_FLAG        = uint(0b0111 << 59)
STATEMENT_FLAG        = uint(0b1 << 62)
S_FACT_FLAG           = uint(0b1000 << 59)
S_FICTION_FLAG        = uint(0b1001 << 59)
S_UNCERTAIN_FLAG      = uint(0b1010 << 59)
S_CONDITION_FLAG      = uint(0b1011 << 59)
S_RESULT_FLAG         = uint(0b1100 << 59)
S_IMPERATIVE_FLAG     = uint(0b1101 << 59)
S_EXCLAMATORY_FLAG    = uint(0b1110 << 59)
S_UNDEFINED_FLAG      = uint(0b1111 << 59)
# Affections
A_HONEST_FLAG         = uint(0b0000 << 55)
A_DISHONEST_FLAG      = uint(0b0001 << 55)
A_HAPPY_FLAG          = uint(0b0010 << 55)
A_SAD_FLAG            = uint(0b0011 << 55)
A_FEAR_FLAG           = uint(0b0100 << 55)
A_ANGER_FLAG          = uint(0b0101 << 55)
A_ANTICIPATION_FLAG   = uint(0b0110 << 55)
A_SURPRISE_FLAG       = uint(0b0111 << 55)
A_BENEVOLENT_FLAG     = uint(0b1000 << 55)
A_MALICE_FLAG         = uint(0b1001 << 55)
A_PAIN_FLAG           = uint(0b1010 << 55)
A_PLEASURE_FLAG       = uint(0b1011 << 55)
A_UNDEF_FLAG_0        = uint(0b1100 << 55)
A_UNDEF_FLAG_1        = uint(0b1101 << 55)
A_UNDEF_FLAG_2        = uint(0b1110 << 55)
A_UNDEF_FLAG_3        = uint(0b1111 << 55)
# Evidentiality
E_OBSERVATION_FLAG    = uint(0b000 << 52)
E_QUOTATION_FLAG      = uint(0b001 << 52)
E_EXPECTATION_FLAG    = uint(0b010 << 52)
E_CONCLUSION_FLAG     = uint(0b011 << 52)
E_GENERALIZATION_FLAG = uint(0b100 << 52)
E_POSTULATE_FLAG      = uint(0b101 << 52)
E_OPINION_FLAG        = uint(0b110 << 52)
E_UNDEFINED_FLAG      = uint(0b111 << 52)


def sentence_meta_flag(word: uint) -> uint:
    """
    Returns whether the word is sentence metadata or not.
    :param word: The word to look at.
    :return: the flags (the flag should 0 if it isn't sentence metadata)
    """
    return word & SENT_META_MASK


def sentence_type(word: uint) -> uint:
    """
    Returns the sentence type (query or statement).
    :param word: The word being looked at.
    :return: True if Statement, False if Query
    :raises: ValueError if word is not sentence Metadata.
    """
    if not sentence_meta_flag(word):
        raise ValueError("Must be sentence Metadata.")
    return word & SENT_TYPE_MASK


def sentence_subtype_flags(word: uint) -> uint:
    """
    :param word: Word to check
    :return: the metadata subtype flag of the word
    :raises: ValueError if word is not sentence metadata.
    """
    if not sentence_meta_flag(word):
        raise ValueError("Must be sentence Metadata.")
    return word & SENT_SUBTYPE_MASK


def affection_flags(word: uint) -> uint:
    """
    :param word: the word to check.
    :return: the metadata affection flag of the word.
    :raises: ValueError if not sentence metadata.
    """
    if not sentence_meta_flag(word):
        raise ValueError("Must be sentence Metadata.")
    return word & AFF_TYPE_MASK


def evid_flags(word: uint) -> uint:
    """
    :param word: the word to check.
    :return: the metadata evidentiality flag of the word.
    :raise; ValueError if not sentence metadata.
    """
    if not sentence_meta_flag(word):
        raise ValueError("Must be sentence Metadata.")
    return word & EVID_MASK


def word_count(word: uint) -> uint:
    """
    :param word: The word to check.
    :return: The number of words in the sentence.
    :raise: Value error if not sentence metadata.
    """
    if not sentence_meta_flag(word):
        raise ValueError("Must be sentence metadata.")
    return word & WORD_COUNT_MASK
