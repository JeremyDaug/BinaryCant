import ply.yacc as yacc
from BinaryCant.cant_lex import lexer, tokens
from BinaryCant.Word.word import FlagError, process_external_word
from numpy import uint64 as uint
from numpy import ndarray
import numpy
from typing import List
from BinaryCant.Word import word_const as WC
from BinaryCant.lexicon import Lexicon

debug = False
lexicon = Lexicon()


class collector:
    def __init__(self, val):
        self.vals = [val]
        self.found = set()
        self.found.add(val)

    def add(self, val: str, word: bool):
        if val in self.found:
            if word:
                raise FlagError("{} already exists in the word.".format(
                    WC.FIND_WORD_FLAG(val)))
            else:
                raise FlagError("{} already exists in the word.".format(
                    WC.FIND_SENT_FLAG(val)))
        self.vals.append(val)
        self.found.add(val)


# word_list expressions
# word_list : word_list word
def p_word_list_word(p):
    'word_list : word_list word'
    p[0] = p[1]
    p[0].append(p[2])
    if debug:
        print('word_list : word_list word')


# word_list : word_list sentence
def p_word_list_sent(p):
    'word_list : word_list sentence'
    p[0] = p[1]
    p[0].extend(p[2])
    if debug:
        print('word_list : word_list sentence')


# word_list : word
def p_word_list_short(p):
    'word_list : word'
    p[0] = [p[1]]
    if debug:
        print('word_list : word')


# word_list : word_list sentence
def p_word_list_sent_short(p):
    'word_list : sentence'
    p[0] = p[1]
    if debug:
        print('word_list : sentence')


# Sentence Expression
# sentence : meta word_list END
def p_sentence_long(p):
    'sentence : meta word_list END'
    temp = p[1] + uint(len(p[2]))
    p[0] = [temp]
    p[0].extend(p[2])
    if debug:
        print('sentence : meta word_list END')


# sentence : meta END
def p_sentence_short(p):
    'sentence : meta END'
    p[0] = [p[1]]
    if debug:
        print('sentence : meta END')


# Sentence Meta Expression
# meta : < META , sent_mods >
def p_meta_long(p):
    'meta : LANGLE META COMMA sent_mods RANGLE'
    p[0] = p[2] + uint(sum(p[4].vals))
    if debug:
        print('meta : LANGLE META COMMA sent_mods RANGLE')


# meta : < META >
def p_meta_short(p):
    'meta : LANGLE META RANGLE'
    p[0] = p[2]
    if debug:
        print('meta : LANGLE META RANGLE')


# Sentence modifier list Expression
# sent_mods : sent_mods , SENT_MOD
def p_sent_mods_long(p):
    'sent_mods : sent_mods COMMA SENT_MOD'
    p[0] = p[1]
    p[0].add(p[3], False)
    if debug:
        print('sent_mods : sent_mods COMMA SENT_MOD')


# sent_mods : SENT_MOD
def p_sent_mods_short(p):
    'sent_mods : SENT_MOD'
    p[0] = collector(p[1])
    if debug:
        print('sent_mods : SENT_MOD')


# word expressions
# word : WORD < GRAMMAR_FLAG , affixes >
def p_word_long(p):
    'word : WORD LANGLE GRAMMAR_FLAG COMMA affixes RANGLE'
    if lexicon.eng_contains(p[1]):
        p[0] = lexicon.lexEng[p[1]] + p[3]
    else:
        p[0] = lexicon.eng_add(p[1]) + p[3]
    p[0] += uint(sum(p[5].vals))
    if debug:
        print('word : WORD LANGLE GRAMMAR_FLAG COMMA affixes RANGLE')


# word : WORD < GRAMMAR_FLAG >
def p_word_short(p):
    'word : WORD LANGLE GRAMMAR_FLAG RANGLE'
    if lexicon.eng_contains(p[1]):
        p[0] = lexicon.lexEng[p[1]] + p[3]
    else:
        p[0] = lexicon.eng_add(p[1]) + p[3]
    if debug:
        print('word : WORD LANGLE GRAMMAR_FLAG RANGLE')


# word : TYPE WORD < GRAMMAR_FLAG >
def p_typed_word_s(p):
    "word : TYPE WORD LANGLE GRAMMAR_FLAG RANGLE"
    p[0] = p[1] + process_external_word(p[2], p[1]) + p[4]
    if debug:
        print("word : TYPE WORD LANGLE GRAMMAR_FLAG RANGLE")


def p_typed_word_l(p):
    "word : TYPE WORD LANGLE GRAMMAR_FLAG COMMA affixes RANGLE"
    p[0] = p[1] + p[2] + p[4] + sum(p[6].vals)
    if debug:
        print("word : TYPE WORD LANGLE GRAMMAR_FLAG COMMA affixes RANGLE")


# affixes expressions
# affixes : AFFIX
def p_affixes_short(p):
    'affixes : AFFIX'
    p[0] = collector(p[1])
    if debug:
        print('affixes : AFFIX')


# affixes : affixes , AFFIX
def p_affixes_long(p):
    'affixes : affixes COMMA AFFIX'
    p[0] = p[1]
    p[0].add(p[3], True)
    if debug:
        print('affixes : affixes COMMA AFFIX')


def p_error(p):
    val = '' + str(p) + str()
    # print(val)


def save(file: str, data: List[uint]):
    out = ndarray(data, uint)
    numpy.save(file, out)


parser = yacc.yacc()


if __name__ == "__main__":
    s = ''
    with open('test_cant.can', 'r') as file:
        s = file.read()
    print(s)
    result = parser.parse(s, debug=True)
    print(result)
