import ply.lex as lex
from BinaryCant.compiler.lexicon import Lexicon
import BinaryCant.Word.word_const as WC
from BinaryCant.Word.word_types import types_regex

L = Lexicon()
debug = True
SymTable = dict()

# get affixes for regex
affixes = WC.TEMPORAL.key_regex() + '|'
affixes += WC.PROGRESS.key_regex() + '|'
affixes += WC.RECURRENCE.key_regex() + '|'
affixes += WC.DEGREE.key_regex() + '|'
affixes += WC.EMPHASIS.key_regex() + '|'
affixes += WC.DETERMINATIVE.key_regex() + '|'
affixes += WC.PLURALITY.key_regex()

# tokens
tokens = (
    'WORD',
    'GRAMMAR_FLAG',
    'AFFIX',
    'END',
    'META',
    'SENT_MOD',
    'TYPE',
    'LANGLE',
    'RANGLE',
    'COMMA',
)

literals = '<>,'

# Expressions
def t_END(t):
    r'<\/>'
    if debug:
        print(t)
    return t


def t_COMMA(t):
    r','
    if debug:
        print(t)
    return t


def t_LANGLE(t):
    r'<'
    if debug:
        print(t)
    return t


def t_RANGLE(t):
    r'>'
    if debug:
        print(t)
    return t


def t_TYPE(t):
    if debug:
        print(t)
    return t


# Regular expresions with actions
def t_AFFIX(t):  # dynamically made, covers word affixes
    if debug:
        print(t)
    return t


def t_GRAMMAR_FLAG(t):
    if debug:
        print(t)
    return t


def t_SENT_MOD(t):
    if debug:
        print(t)
    return t


def t_META(t):
    if debug:
        print(t)
    return t


def t_WORD(t):
    r'[^<,>\n]+'
    if debug:
        print(t)
    return t


def find_column(input, token):
    """
    Compute the column of the token.
    :param input: The input text string.
    :param token: The token instance.
    :return:
    """
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1


# newline rule
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# whitespace
t_ignore = ' \t'


# error handling
def t_error(t):
    print("Illegal character '{}'.".format(t.value[0]))
    t.lexer.skip(1)


# dynamic regex strings

t_TYPE.__doc__ = r'\(({})\)'.format(types_regex)
t_AFFIX.__doc__ = r'{}'.format(affixes)
t_GRAMMAR_FLAG.__doc__ = r'{}'.format(WC.GRAMMAR.key_regex())
sentence_mods = WC.AFFECTIONS.key_regex() + '|' + WC.EVIDENTIALITY.key_regex()
t_SENT_MOD.__doc__ = r'{}'.format(sentence_mods)
t_META.__doc__ = r'{}'.format(WC.SENTENCE_TYPES.key_regex())

# build the lexer
lexer = lex.lex()


if __name__ == '__main__':
    with open('test_cant.can', 'r') as f:
        test_data = f.read()
    lexer.input(test_data)

    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)
