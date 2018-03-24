from numpy import uint64 as uint
import re
from BinaryCant.WordProcessor import WordProcessor


MAJOR_SYNTAX_ERROR = "Error: Syntax after word {} is invalid be sure it is in " \
                   "([type])[word]<[flags]> or [word]<[flags]> format."


class CodeProcessor:
    @staticmethod
    def read_text(words):
        # strip newlines and tabs for safety reasons.
        words = words.replace("\n", "")
        words = words.replace("\t", "")
        # do regex to find a word.
        regex = re.compile("((\(?[^\(\)\<\>]*\)?)? *[a-zA-Z0-9]+ *\<([a-zA-Z0-9, ])+\>)+?\s*")
        word_num = 0
        while words:
            word_match = regex.match(words)
            # print(word_match)
            if not word_match:
                raise SyntaxError(
                    MAJOR_SYNTAX_ERROR
                    .format(word_num)
                )
            curr_word = words[word_match.start():word_match.end()]
            # print(curr_word)
            words = words[word_match.end():]
            # process word_match
            try:
                res = WordProcessor.process_word(curr_word)
            except SyntaxError as E:
                raise SyntaxError(E.msg.format(word_num))
            # final step
            word_num += 1


if __name__ == "__main__":
    try:
        CodeProcessor.read_text("(int stuffA < sub >\n()stuffB <ver, pas> stuffC <obj, fut, 0>")
    except SyntaxError as E:
        print(E.msg)
    except AttributeError as E:
        print(E.args)
    try:
        CodeProcessor.read_text("stuffA")
    except SyntaxError as E:
        print(E.msg)
    except AttributeError as E:
        print(E.args)
