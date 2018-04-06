import ply.lex as lex
from BinaryCant.Word.word import flag_val
from BinaryCant.lexicon import Lexicon
import BinaryCant.Word.word_const as WC
from numpy import uint64 as uint


L = Lexicon()

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
    'INT',
    'FLOAT',
    'RGB'
)

literals = '<>(),'

# Expressions
t_END    = r'<\/>'
t_INT    = r'int'
t_FLOAT  = r'float'
t_RGB    = r'rgb'


def t_TYPE(t):
    r'int|float|rgb'
    t.value = WC.EXTERNAL_WORD_FLAG + WC.EX_VAL_TYPE_DICT[t.value]


def t_GRAMMAR_FLAG(t):
    r'(sub|obj|top|ver|mod|rel)'
    t.value = flag_val(t.value)
    return t


# Regular expresions with actions
def t_AFFIX(t):
    r'(pas|pre|fut|uns|pro|com|irr|con|hab|[0-6]|!|\?|sin|plu|num)'
    t.value = flag_val(t.value)
    return t


def t_META(t):
    r'lie|hap|sad|fea|ang|ant|sur|ben|mal|pai|ple|quo|exp|con|gen|pos|opi'
    t.value = flag_val(t.value)
    return t


def t_SENT_MOD(t):
    r'QS|QO|QV|QT|QL|QR|QE|QC|SA|SD|SU|SC|SR|SI|S!|S\?'
    t.value = flag_val(t.value)
    return t


def t_WORD(t):
    r'[a-zA-Z]+'
    ret = uint(0)
    if L.eng_contains(t.value):
        ret += L.english_to_cant(t.value)
    else:
        ret += L.eng_add(t.value)
    t.value = ret
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
lexer = lex.lex(optimize=False)


if __name__ == '__main__':
    test_data = ''
    with open('test_cant.can', 'r') as f:
        test_data = f.read()
    lexer.input(test_data)

    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)
