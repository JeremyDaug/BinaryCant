import ply.lex as lex
from BinaryCant.Word.word import flag_val
from BinaryCant.lexicon import Lexicon
import BinaryCant.Word.word_const as WC
from numpy import uint64 as uint


L = Lexicon()
debug = False
SymTable = dict()


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
    r'\((int|float|rgb)\)'
    if debug:
        print(t)
    t.value = WC.EX_VAL_TYPE_DICT[t.value[1:t.value.find(')')]]
    return t


# Regular expresions with actions
def t_AFFIX(t):
    r'(pas|pre|fut|uns|pro|com|irr|con|hab|[0-6](?=(>|,|\s))|!|\?|sin|plu|num)'
    if debug:
        print(t)
    t.value = flag_val(t.value)
    return t


def t_GRAMMAR_FLAG(t):
    r'(sub|obj|top|ver|mod|rel)'
    if debug:
        print(t)
    t.value = flag_val(t.value)
    return t


def t_SENT_MOD(t):
    r'lie|hap|sad|fea|ang|ant|sur|ben|mal|pai|ple|quo|exp|con|gen|pos|opi'
    if debug:
        print(t)
    t.value = flag_val(t.value)
    return t


def t_META(t):
    r'QS|QO|QV|QT|QL|QR|QE|QC|SA|SD|SU|SC|SR|SI|S!|S\?'
    if debug:
        print(t)
    t.value = flag_val(t.value)
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


# build the lexer
lexer = lex.lex()


if __name__ == '__main__':
    test_data = ''
    with open('test_cant.can', 'r') as f:
        test_data = f.read()
    lexer.input(test_data)

    while True:
        tok = lexer.token()
        if not tok:
            break
        # print(tok)
