"""
The fire for the structure of binary cant.

Started 13-Feb-2018.
"""

import BinaryCant.Word as w
import BinaryCant.Word.word_const as WC
from BinaryCant.lexicon import Lexicon
from numpy import uint64 as uint
import re
from typing import List


class CantProcessor:
    lex = Lexicon('lexCant_default.csv')

    @staticmethod
    def process_word(word):
        ret = uint(0)
        regex = re.compile("(\([a-zA-Z]+\))?[A-Za-z0-9]+<(sub|obj|top|ver|mod|rel)(,(pas|pre|fut|uns|pro|com|irr|con|hab|[0-6]|\!|\?|sin|plu|num)+)*>")
        if regex.fullmatch(word) is None:
            CantProcessor.word_error_processing(word, regex)
        print(regex.match(word))
        # prefix data.
        valType = "Internal"
        if word.startswith("("):
            prefix = word[1:word.find(")")]
            if not CantProcessor.valid_word_prefix(prefix):
                raise SyntaxError("Word #{},{}: Improper word syntax.")
            ret += WC.EXTERNAL_WORD_FLAG
            ret += WC.WORD_TYPE_DICT[prefix]
            valType = prefix
        # process word
        eng = word[:word.find("<")]
        if eng.startswith("("):
            eng = eng[word.find(")")+1:]
        print(eng)
        if valType != "Internal":
            ret += CantProcessor.external_word(eng, valType)
        else:
            ret += CantProcessor.internal_word(eng)
        # process flags
        flags = word[word.find("<")+1:word.find(">")].split(",")
        print(flags)
        try:
            ret += CantProcessor.process_word_flags(flags)
        except SyntaxError as e:
            raise SyntaxError("Word #{},{}: " + e.msg)
        return ret

    @staticmethod
    def process_word_flags(flags: List[str]) -> uint:
        ret = uint(0)
        found = set()
        for flag in flags:
            if flag in WC.GRAMMAR_TOKENS:
                if 0 in found:
                    raise SyntaxError("too many Grammar flags.")
                else:
                    found.add(0)
            elif flag in WC.TEMPORAL_TOKENS:
                if 1 in found:
                    raise SyntaxError("too many temporal flags.")
                else:
                    found.add(1)
            elif flag in WC.PROGRESS_TOKENS:
                if 2 in found:
                    raise SyntaxError("too many progress flags.")
                else:
                    found.add(2)
            elif flag in WC.RECURRENCE_TOKENS:
                if 3 in found:
                    raise SyntaxError("too many recurrence flags.")
                else:
                    found.add(3)
            elif flag in WC.DEGREE_TOKENS:
                if 4 in found:
                    raise SyntaxError("too many degree flags.")
                else:
                    found.add(4)
            elif flag == WC.E_EMPHASIZED_TOK:
                if 5 in found:
                    raise SyntaxError("too many emphasis flags.")
                else:
                    found.add(5)
            elif flag == WC.DT_SPECIFIC_TOK:
                if 6 in found:
                    raise SyntaxError("too many determinative flags.")
                else:
                    found.add(6)
            elif flag in WC.PLURALITY_TOKENS:
                if 7 in found:
                    raise SyntaxError("too many plurality flags.")
                else:
                    found.add(7)
            ret += WC.TOKENDICT[flag]
        return ret

    def depricated(self):
        @staticmethod
        def process_grammar(flags):
            pass

        @staticmethod
        def process_temporal(flags):
            pass

        @staticmethod
        def process_progress(flags):
            pass

        @staticmethod
        def process_recurrence(flags):
            pass

        @staticmethod
        def process_degree(flags):
            pass

        @staticmethod
        def process_emphasis(flags):
            pass

        @staticmethod
        def process_determinative(flags):
            pass

        @staticmethod
        def process_plurality(flags):
            pass

    @staticmethod
    def internal_word(word):
        ret = uint(0)
        if CantProcessor.lex.eng_contains(word):
            ret += CantProcessor.lex.english_to_cant(word)
        else:
            ret += CantProcessor.lex.eng_add(word)
        return ret

    @staticmethod
    def external_word(word, val_type) -> uint:
        type_switch = {"int": CantProcessor.process_int_type,
                       "float": CantProcessor.process_float_type,
                       "rbg": CantProcessor.process_rbg_type}
        return type_switch[val_type](word)

    @staticmethod
    def process_int_type(word: str) -> uint:
        ret = uint(0)
        return ret

    @staticmethod
    def process_float_type(word: str) -> uint:
        ret = uint(0)
        return ret

    @staticmethod
    def process_rbg_type(word: str) -> uint:
        ret = uint(0)
        return ret

    @staticmethod
    def word_error_processing(word, regex):
        raise SyntaxError("Word #{},{}: Improper word syntax.")

    @staticmethod
    def valid_word_prefix(word):
        return word in WC.WORD_TYPES


if __name__ == "__main__":
    CantProcessor.process_word("(int)123<sub,!,?>")
    WC.print_word_bin(CantProcessor.process_word("greet<ver,!>"))

    try:
        CantProcessor.process_word("()123<sub,pre>")
    except SyntaxError as E:
        print(E.msg)

    try:
        CantProcessor.process_word("123<sub,pre")
    except SyntaxError as E:
        print(E.msg)

    try:
        CantProcessor.process_word("123<sub,pre,fut>")
    except SyntaxError as E:
        print(E.msg)

    CantProcessor.lex.save()
