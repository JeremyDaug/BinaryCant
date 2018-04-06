import ply.yacc as yacc
from BinaryCant.cant_lex import tokens, literals
from BinaryCant.Word.word import FlagError
from numpy import uint64 as uint
from numpy import ndarray
import numpy
from typing import List
from BinaryCant.Word import word_const as WC

result = []


class collector:
    def __init__(self, val):
        self.vals = [val]
        self.found = set()
        self.found.add(val)

    def add(self, val, word):
        if val in self.found:
            if word:
                raise FlagError("{} already exists in the word.".format(
                    WC.FIND_WORD_FLAG(val)))
            else:
                raise FlagError("{} already exists in the word.".format(
                    WC.FIND_SENT_FLAG(val)))
        self.vals.append(val)
        self.found.add(val)


# Sentence Meta Expression
# meta : < META , sent_mods >
def p_meta_long(p):
    'meta : "<" META "," sent_mods ">"'
    p[0] = p[2] + p[4]


# meta : < META >
def p_meta_short(p):
    'meta : "<" META ">"'
    p[0] = p[2]


# Sentence modifier list Expression
# sent_mods : sent_mods , SENT_MOD
def p_sent_mods_long(p):
    'sent_mods : sent_mods "," SENT_MOD'
    p[0] = p[1]
    p[0].add(p[3], False)


# sent_mods : SENT_MOD
def p_sent_mods_short(p):
    'sent_mods : SENT_MOD'
    p[0] = collector(p[1])


# Sentence Expression
# sentence : meta word_list END
def p_sentence_long(p):
    'sentence : meta word_list END'
    temp = p[1] + uint(len(p[2]))
    p[0] = [temp]
    p[0].extend(p[2])


# sentence : meta END
def p_sentence_short(p):
    'sentence : meta END'
    p[0] = [p[1]]


# word_list expressions
# word_list : word_list word
def p_word_list_word(p):
    'word_list : word_list word'
    p[0] = p[1]
    p[0].append(p[2])


# word_list : word_list sentence
def p_word_list_sent(p):
    'word_list : word_list sentence'
    p[0] = p[1]
    p[0].extend(p[2])


# word_list : word
def p_word_list_short(p):
    'word_list : word'
    p[0] = [p[1].val]


# word expressions
# word : WORD < GRAMMAR_FLAG , affixes >
def p_word_long(p):
    'word : WORD "<" GRAMMAR_FLAG "," affixes ">"'
    p[0] = p[1] + p[3] + sum(p[3].vals)


# word : WORD < GRAMMAR_FLAG >
def p_word_short(p):
    'word : WORD "<" GRAMMAR_FLAG ">"'
    p[0] = p[1] + p[3]


# word : "(" TYPE


# affixes expressions
# affixes : AFFIX
def p_affixes_short(p):
    'affixes : AFFIX'
    p[0] = collector(p[1])


# affixes : affixes , AFFIX
def p_affixes_long(p):
    'affixes : affixes "," AFFIX'
    p[0] = p[1]
    p[0].add(p[3])


def p_error(p):
    raise SyntaxError()


def save(file: str, data: List[uint]):
    out = ndarray(data, uint)
    numpy.save(file, out)


parser = yacc.yacc()

