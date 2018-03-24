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


class WordProcessor:
    """
    A class that translates
    """
    lex = Lexicon('lexCant_default.csv')

    @staticmethod
    def process_word(word):
        try:
            ret = uint(0)
            regex = re.compile("(\([a-zA-Z]+\))?[A-Za-z0-9]+<(sub|obj|top|ver|mod|rel)(,(pas|pre|fut|uns|pro|com|irr|con|hab|[0-6]|\!|\?|sin|plu|num)+)*>")
            match = regex.fullmatch(word)
            # print(match)
            if match is None:
                WordProcessor.word_error_processing(word)
            # print(regex.match(word))
            # prefix data.
            valType = "Internal"
            if word.startswith("("):
                prefix = word[1:word.find(")")]
                if not WordProcessor.valid_word_prefix(prefix):
                    raise SyntaxError("No such type exists.")
                ret += WC.EXTERNAL_WORD_FLAG
                ret += WC.WORD_TYPE_DICT[prefix]
                valType = prefix
            # process word
            eng = word[:word.find("<")]
            if eng.startswith("("):
                eng = eng[word.find(")")+1:]
            # print(eng)
            if valType != "Internal":
                ret += WordProcessor.external_word(eng, valType)
            else:
                ret += WordProcessor.internal_word(eng)
            # process flags
            flags = word[word.find("<")+1:word.find(">")].split(",")
            # print(flags)
            ret += WordProcessor.process_word_flags(flags)
        except SyntaxError as e:
            raise SyntaxError("Word #{}" + ",{}: ".format(word) + e.msg)
        # print(ret)
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

    @staticmethod
    def internal_word(word: str) -> uint:
        ret = uint(0)
        if not word.isalpha():
            raise SyntaxError("Cannot contain numbers in word.")
        elif ' ' in word:
            raise SyntaxError("cannot contain whitespace.")
        if WordProcessor.lex.eng_contains(word):
            ret += WordProcessor.lex.english_to_cant(word)
        else:
            ret += WordProcessor.lex.eng_add(word)
        return ret

    @staticmethod
    def external_word(word, val_type) -> uint:
        type_switch = {"int": WordProcessor.process_int_type,
                       "float": WordProcessor.process_float_type,
                       "rbg": WordProcessor.process_rbg_type}
        return type_switch[val_type](word)

    @staticmethod
    def process_int_type(word: str) -> uint:
        ret = uint(int(word))
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
    def word_error_processing(word):
        missingParenType = re.compile(".*\([^\(\)]*\).*")
        matchingParens = [re.compile("[^\(]*\)"),
                          re.compile("\([^\(]*")]
        if missingParenType.search(word):  # missing type value
            raise SyntaxError("Must have type in Parens.")
        if word.find("(") or word.find(")"):  # mismatched parentheses.
            for opt in matchingParens:
                if opt.match(word):
                    raise SyntaxError("Mismatched Parentheses.")

        trailingCharacters = re.compile(".*<[^<]*>.+")
        if trailingCharacters.match(word):  # Trailing Characters
            raise SyntaxError("Trailing Characters after '>'.")

        mismatchingAngles = [re.compile("[^<]*>.*"),
                             re.compile(".*<[^>]*")]
        for opt in mismatchingAngles:  # mismatched angle brackets
            print(opt.fullmatch(word))
            if opt.fullmatch(word):
                raise SyntaxError("Mismatched angle brackets.")
        # no grammar string
        flags = word[word.find("<"):word.find(">")]
        for flag in flags:
            if flag not in WC.GRAMMAR_TOKENS:
                raise SyntaxError("Has no grammar token.")
        raise SyntaxError("Uncertain Syntax Error, double check values.")

    @staticmethod
    def valid_word_prefix(word):
        return word in WC.WORD_TYPES


if __name__ == "__main__":
    print("greet<ver,!>")
    WC.print_word_bin(WordProcessor.process_word("greet<ver,!>"))
    print("speaker<sub,!>")
    WC.print_word_bin(WordProcessor.process_word("speaker<sub,!>"))
    print("(int)123<sub,!,?>")
    intword = WordProcessor.process_word("(int)123<sub,!,?>")
    WC.print_word_bin(intword)

    try:
        WC.print_word_bin(WordProcessor.process_word("spea123<sub,!>"))
    except SyntaxError as E:
        print(E.msg)

    try:
        WordProcessor.process_word("()123<sub,pre>")
    except SyntaxError as E:
        print(E.msg)

    try:
        WordProcessor.process_word("(in)123<sub,pre>")
    except SyntaxError as E:
        print(E.msg)

    try:
        WordProcessor.process_word("(int123<sub,pre>")
    except SyntaxError as E:
        print(E.msg)

    try:
        WordProcessor.process_word("123<sub,pre")
    except SyntaxError as E:
        print(E.msg)

    try:
        WordProcessor.process_word("123sub,pre>")
    except SyntaxError as E:
        print(E.msg)

    try:
        WordProcessor.process_word("123<sub,pre>1")
    except SyntaxError as E:
        print(E.msg)

    try:
        WordProcessor.process_word("123<sub,pre,fut>")
    except SyntaxError as E:
        print(E.msg)

    try:
        WordProcessor.process_word("123<pre,fut>")
    except SyntaxError as E:
        print(E.msg)

    WordProcessor.lex.save()
