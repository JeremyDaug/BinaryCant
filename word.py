"""
The word class file for Binary Cant, this is effectively the only thing the
language needs.
"""

# from typing import Optional, Union
from numpy import uint64 as uint

# masks for the class
ZEROED         = uint(0x0000000000000000)
SENT_META_MASK = uint(0x8000000000000000)
SENT_TYPE_MASK = uint(0x4000000000000000)
# Constants
FLAG_GROUPS = {'grammar': {0: 'subject',
                           1: 'object',
                           2: 'topic',
                           3: 'verb',
                           4: 'modifier',
                           5: 'relation',
                           6: '[Empty]',
                           7: 'operation'},
               'temporal': {0: 'timeless',
                            1: 'past',
                            2: 'present',
                            3: 'future'},
               'progression': {0: 'unprogressed',
                               1: 'unstarted',
                               2: 'in progress',
                               3: 'complete'},
               'recurrence': {0: 'non-recurring',
                              1: 'irregular',
                              2: 'continuous',
                              3: 'habitual'},
               'degree': {0: 'unspecified',
                          1: 'none',
                          2: 'minimal',
                          3: 'small',
                          4: 'medium',
                          5: 'large',
                          6: 'maximal',
                          7: 'total'},
               'emphasis': {0: 'unemphasized',
                            1: 'emphasized'},
               'determinative': {0: 'nonspecific',
                                 1: 'specific'},
               'plurality': {0: 'unnumbered',
                             1: 'singular',
                             2: 'plural(specific)',
                             3: 'plural(nonspecific)'},
               'type': {0: 'query',
                        1: 'statement'},
               'query': {0: 'subject',
                         1: 'object',
                         2: 'clarify',
                         3: 'time',
                         4: 'location',
                         5: 'reasoning',
                         6: 'explain',
                         7: 'specify'},
               'statement': {0: 'fact',
                             1: 'fiction',
                             2: 'uncertain',
                             3: 'condition',
                             4: 'result',
                             5: 'imperative',
                             6: 'exclamatory',
                             7: '[Empty]'},
               'affection': {0: 'honest',
                             1: 'dishonest',
                             2: 'happy',
                             3: 'sad',
                             4: 'fear',
                             5: 'anger',
                             6: 'anticipation',
                             7: 'surprise',
                             8: 'benevolence',
                             9: 'malice',
                             10: '[Empty]',
                             11: '[Empty]',
                             12: '[Empty]',
                             13: '[Empty]',
                             14: '[Empty]',
                             15: '[Empty]'},
               'evidentiality': {0: 'observation',
                                 1: 'hearsay',
                                 2: 'expectation',
                                 3: 'conclusion',
                                 4: 'generalization',
                                 5: 'postulate',
                                 6: 'opinion',
                                 7: '[Empty]'}
               }


def is_sentence_meta(word: uint) -> bool:
    """
    Returns whether the word is sentence metadata or not.
    :param word: The word to look at.
    :return: True if sentence meta data.
    """
    return word & SENT_META_MASK


def sentence_type(word: uint) -> bool:
    """
    Returns the sentence type (query or statement).
    :param word: The word being looked at.
    :return: True if Statement, False if Query
    :raises: ValueError if word is not sentence Metadata.
    """
    if not is_sentence_meta(word):
        raise ValueError("Must be sentence metadata.")
    return word & SENT_TYPE_MASK


class Word:
    """
    Word class that contains all necessary information and logic for words.
    """
    def __init__(self, word: uint) -> None:
        self.word = word
        return
