"""
The word class file for Binary Cant, this is effectively the only thing the
language needs.
"""

# from typing import Optional, Union
from numpy import uint32

# masks for the class
OUT_LANG_MASK  = uint32(0x80000000)  # 1000 0000 0000 0000 0000 0000 0000 0000
SENT_META_MASK = 0x40000000  # 0100 0000 0000 0000 0000 0000 0000 0000
GRAMMAR_MASK   = 0x38000000  # 0011 1000 0000 0000 0000 0000 0000 0000
TEMPORAL_MASK  = 0x06000000  # 0000 0110 0000 0000 0000 0000 0000 0000
PROG_MASK      = 0x01800000  # 0000 0001 1000 0000 0000 0000 0000 0000
REC_MASK       = 0x00600000  # 0000 0000 0110 0000 0000 0000 0000 0000
DEG_MASK       = 0x001C0000  # 0000 0000 0001 1100 0000 0000 0000 0000
EMP_MASK       = 0x00020000  # 0000 0000 0000 0010 0000 0000 0000 0000
DETER_MASK     = 0x00010000  # 0000 0000 0000 0001 0000 0000 0000 0000
SPEC_WORD_MASK = 0x0000FFFF  # 0000 0000 0000 0000 1111 1111 1111 1111
PLURAL_MASK    = 0x0000C000  # 0000 0000 0000 0000 1100 0000 0000 0000
SENT_TYPE_MASK = 0x3C000000  # 0011 1100 0000 0000 0000 0000 0000 0000
AFFECT_MASK    = 0x03C00000  # 0000 0011 1100 0000 0000 0000 0000 0000
EVID_MASK      = 0x00380000  # 0000 0000 0011 1000 0000 0000 0000 0000
SENT_LENG_MASK = 0x0007FFFF  # 0000 0000 0000 0111 1111 1111 1111 1111
EXT_MASK       = 0x70000000  # 0111 0000 0000 0000 0000 0000 0000 0000
EXT_LEN_MASK   = 0x0FFFFFFF  # 0000 1111 1111 1111 1111 1111 1111 1111
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
the_dictionary = {0x00005835: "animal"}


class Word:
    """
    Word class that contains all necissary information and logic for words.
    """
    def __init__(self, data: uint32 = 0b0) -> None:
        """
        Init function.
        :param data: The input value we are storing, either string for
        untranslated data, or 32 bit int for raw binary cant.
        :raises TypeError: Must be given an int or str.
        """
        if isinstance(data, uint32):
            raise TypeError("Must be of type uint32.")
        self.v = data
        self.data = []
        self.disect()
        return

    def disect(self) -> None:
        """
        Disects the raw data into it's constituent parts, then stores it.
        """
        if self.v & OUT_LANG_MASK == 0: # within language
            self.data.append((0, 'In Language'))
            if self.v & SENT_META_MASK == 0: # word Metadata
                self.data.append((0, 'Word'))
                if self.v & GRAMMAR_MASK == 0x3800000000:
                    self.data.append((0x7, 'Operation'))
                    self.data.append((self.v & 0xF8000000, 'OpCode'))
                    return
                val = self.remove_zeroes(self.v & GRAMMAR_MASK)
                self.data.append((val, FLAG_GROUPS['grammar'][val]))
                val = self.remove_zeroes(self.v & TEMPORAL_MASK)
                self.data.append((val, FLAG_GROUPS['temporal'][val]))
                val = self.remove_zeroes(self.v & PROG_MASK)
                self.data.append((val, FLAG_GROUPS['progression'][val]))
                val = self.remove_zeroes(self.v & REC_MASK)
                self.data.append((val, FLAG_GROUPS['recurrence'][val]))
                val = self.remove_zeroes(self.v & DEG_MASK)
                self.data.append((val, FLAG_GROUPS['emphasis'][val]))
                val = self.remove_zeroes(self.v & DETER_MASK)
                self.data.append((val, FLAG_GROUPS['determinative'][val]))
                val = self.remove_zeroes(self.v & PLURAL_MASK)
                self.data.append((val, FLAG_GROUPS['plurality'][val]))
            else:  # sentence Metadata
                self.data.append((1, 'Sentence'))

        else:
            self.data.append((1, 'Outside Language'))
        return

    def to_readable(self, lang: str = 'eng') -> str:
        """
        A wrapper for readable functions, allows to call other
        languages more easily.
        :param lang: The language to call (defaults to english)
        :return: The readable version of the word.
        """
        lang_dict = {'eng': self.to_readable}
        return lang_dict[lang]()

    @staticmethod
    def remove_zeroes(val: uint32) -> uint32:
        """
        Removes 0s on a value to help isolate the value.
        :param val: the value to remove right hand 0s on.
        :return: the value after removing all right hand 0s.
        """
        while val != 0 and val % 2:
            val /= 2
        return val

    def grammar(self) -> uint32:
        """
        Returns the grammar flag of the word, does not check if the word has
        a grammar flag.
        :return: The flags of the word.
        """
        ret = self.v & GRAMMAR_MASK
        return self.remove_zeroes(ret)

    def temporal(self) -> uint32:
        """
        Returns the temporal flags of a word, does not check if it is a word.
        :return: The flags of the word.
        """
        ret = self.v & TEMPORAL_MASK
        return self.remove_zeroes(ret)

    def progress(self) -> uint32:
        """
        Returns the progress bits of the word.
        :return: The progress state.
        """
        ret = self.v & PROG_MASK
        return self.remove_zeroes(ret)

    def recurrence(self) -> uint32:
        """
        Returns recurrence flags.
        :return: the recurrence flags.
        """
        ret = self.v & REC_MASK
        return self.remove_zeroes(ret)

    def degree(self) -> uint32:
        """
        Returns the degree flags.
        :return: the degree flags.
        """
        ret = self.v & DEG_MASK
        return self.remove_zeroes(ret)

    def emphasis(self) -> uint32:
        """
        Return the emphasis flag.
        :return: the emphasis flag.
        """
        ret = self.v & EMP_MASK
        return self.remove_zeroes(ret)

    def determinative(self) -> uint32:
        """
        Return the determinative flag.
        :return: the deterinative flag.
        """
        ret = self.v & DETER_MASK
        return self.remove_zeroes(ret)

    def word(self) -> uint32:
        """
        Returns the word bits.
        :return: the word bits.
        """
        return self.v & SPEC_WORD_MASK


    def to_readable_eng(self) -> str:
        """
        Translates the binary cant of the word into readable data.
        :return: Turns the word into a readable translation.
        (not a full translation)
        """
        res = ''
        if self.v & 0x80000000 == 0:  # within language
            if self.v & 0x40000000 == 0:  # Word Metadata
                g = self.grammar()
                if g == 0x7:  # Operation
                    return 'Operation<NYM>'
                g = FLAG_GROUPS['grammar'][g]
                tem = FLAG_GROUPS['temporal'][self.temporal()]
                prog = FLAG_GROUPS['progression'][self.progress()]
                rec = FLAG_GROUPS['recurrence'][self.recurrence()]
                deg = FLAG_GROUPS['degree'][self.degree()]
                emp = FLAG_GROUPS['emphasis'][self.emphasis()]
                det = FLAG_GROUPS['determinative'][self.determinative()]
                trans = the_dictionary[self.word]
                return
        else:  # outside language
            pass
        return res
