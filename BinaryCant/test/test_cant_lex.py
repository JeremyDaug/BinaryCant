import unittest
from BinaryCant.compiler.cant_lex import lexer
from BinaryCant.Word.word_const import *


class TestCantLex(unittest.TestCase):
    def test_flags(self):
        for flag, val in Flag_Values.items():
            lexer.input(flag)
            while True:
                tok = lexer.token()
                if not tok:
                    break
                self.assertEqual(tok.value, val)
