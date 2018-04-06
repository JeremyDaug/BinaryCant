"""
The fire for the structure of binary cant.

Started 13-Feb-2018.
"""

import BinaryCant.Word.word_const as WC
from BinaryCant.lexicon import Lexicon
from numpy import uint64 as uint
from numpy import ndarray
import numpy
import re
from typing import List

MAJOR_SYNTAX_ERROR = "Error: Invalid Syntax Word:{}, {}"


class WordProcessor:
    """
    A class that translates code into
    """
    lex = Lexicon('lexCant_default.csv')

    @staticmethod
    def compile(words: str, save: bool) -> ndarray:
        ret = []
        # strip newlines and tabs for safety reasons.
        words = words.replace("\n", "")
        words = words.replace("\t", "")
        # do regex to find a word.
        sent_regex = re.compile("\<[a-zA-Z0-9 ,]*\>")
        word_regex = re.compile("((\(?[^\(\)\<\>]*\)?)? *[a-zA-Z0-9]+ *\<([a-zA-Z0-9, \!\?])+\>)+?\s*")
        sent_end = re.compile("\<\!\>")
        word_num = 0
        while words:
            words = words.strip()
            word_match = word_regex.match(words)
            sent_match = sent_regex.match(words)
            # sent_end_match = sent_end.match(words)
            # print(word_match)
            if word_match:
                curr_word = words[word_match.start():word_match.end()]
                # print(curr_word)
                words = words[word_match.end():]  # snip current word.
                # process word_match
                res = 0
                try:
                    res = WordProcessor.process_word(curr_word)
                except SyntaxError as E:
                    raise SyntaxError(E.msg.format(word_num))
                ret.append(uint(res))  # put into list to process in the Cant Processor.
            elif sent_match:
                # get current word.
                curr_word = words[sent_match.start():sent_match.end()]
                # snip current word from string.
                words = words[sent_match.end():]
                res = 0
                try:
                    res = WordProcessor.process_sent_meta(curr_word)
                except SyntaxError as E:
                    raise SyntaxError(E.msg.format(word_num))
                ret.append(uint(res))  # put into the list.
            else:
                raise SyntaxError(
                    MAJOR_SYNTAX_ERROR
                    .format(word_num,
                            words.split("\n")[0])
                )
            # final step
            word_num += 1
        if save:
            WordProcessor.lex.save()
        return numpy.asarray(ret, uint)

    @staticmethod
    def process_sent_meta(word: str) -> uint:
        # it is sentence meta
        ret = WC.SENT_META_TRUE_FLAG
        # strip of whitespace
        word = word.replace(" ", "")
        # get flags
        flags = word[1:-1]
        flags = flags.split(",")
        existing_flags = set()
        try:
            # go through the flags
            for flag in flags:
                if flag in WC.STATEMENT_TOKENS:
                    if "SentType" in existing_flags:
                        raise SyntaxError("{}: Too many Sentence Type flags."
                                          .format(word))
                    existing_flags.add("SentType")
                    ret += WC.STATEMENT_TOKENS[flag]
                elif flag in WC.QUERY_TOKENS:
                    if "SentType" in existing_flags:
                        raise SyntaxError("{}: Too many Sentence Type flags."
                                          .format(word))
                    existing_flags.add("SentType")
                    ret += WC.QUERY_TOKENS[flag]
                elif flag in WC.A_AFF_TOKENS:
                    if "Aff" in existing_flags:
                        raise SyntaxError("{}: Too many Affection flags."
                                          .format(word))
                    existing_flags.add("Aff")
                    ret += WC.A_AFF_TOKENS[flag]
                elif flag in WC.E_EVID_TOKENS:
                    if "Evid" in existing_flags:
                        raise SyntaxError("{}: Too many Evidentiality flags."
                                          .format(word))
                    existing_flags.add("Evid")
                    ret += WC.E_EVID_TOKENS[flag]
                elif flag.isdigit():
                    if "Num" in existing_flags:
                        raise SyntaxError("{}: Too many Evidentiality flags."
                                          .format(word))
                    existing_flags.add("Num")
                    num = uint(int(flag))
                    if num > 2**51-1:
                        raise SyntaxError("{}: Word count too high."
                                          .format(word))
                    else:
                        ret += uint(int(flag))
                else:
                    raise SyntaxError("{}: {} is not a valid flag."
                                      .format(word, flag))
            # ensure flags are there
            if "SentType" not in existing_flags:
                raise SyntaxError("{}: Must have a Sentence Type flag."
                                  .format(word))
            elif "Num" not in existing_flags:
                raise SyntaxError("{}: Must contain word count in the word."
                                  .format(word))
        except SyntaxError as E:
            raise SyntaxError("Word #{},"+E.msg)
        return ret

    @staticmethod
    def process_word(word: str) -> uint:
        try:
            # strip whitespace
            word = word.replace(" ", "")
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


def print_list_bin(vals):
    for val in vals:
        WC.print_word_bin(val)


def print_list_hex(vals):
    for val in vals:
        WC.print_word_hex(val)


if __name__ == "__main__":
    # word processor
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

    print("compile tests-----------------------------------------------")
    # compile tests
    vals = WordProcessor.compile("< SA, 3> (int) 123 < sub >\nstuffB <ver, pas> stuffC <obj, fut, 0>")
    print(vals)
    print_list_bin(vals)
    try:
        WordProcessor.compile("(int stuffA < sub >\n()stuffB <ver, pas> stuffC <obj, fut, 0>")
    except SyntaxError as E:
        print(E.msg)
    except AttributeError as E:
        print(E.args)
    try:
        WordProcessor.compile("stuffA")
    except SyntaxError as E:
        print(E.msg)
    except AttributeError as E:
        print(E.args)
    try:
        WordProcessor.compile("<SA, 3")
    except SyntaxError as E:
        print(E.msg)
    except AttributeError as E:
        print(E.args)
    try:
        WordProcessor.compile("SA, 3>")
    except SyntaxError as E:
        print(E.msg)
    except AttributeError as E:
        print(E.args)
