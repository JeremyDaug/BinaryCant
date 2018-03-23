"""
A file for the lexicon of binary cant. It will allow for translation.
"""

from numpy import uint64 as uint
import random as rand
import BinaryCant.Word.word_const as WC

rand.seed()


class Lexicon:
    def __init__(self, file):
        self.lexCant = {}  # Cant to english
        self.lexEng = {}  # english to Cant
        if not file:
            return
        with open(file, 'r') as f:
            for line in f.readlines():
                key, word = line.split(',')
                key = uint(int(key))
                word = word.strip()
                self.lexCant[key] = word
                self.lexEng[word] = key
        return

    def cant_to_english(self, word):
        return self.lexCant.get(word, None)

    def english_to_cant(self, word):
        return self.lexEng.get(word, None)

    def save(self, file: str = "lexCant_default.csv"):
        with open(file, 'w') as f:
            for key, value in self.lexCant.items():
                f.write(str(key)+','+value+'\n')
        return

    def load_default(self):
        with open('lexCant_default.csv') as f:
            for line in f.readlines():
                key, word = line.split(',')
                key, word = line.split(',')
                key = uint(int(key))
                self.lexCant[uint(int(key))] = word
                self.lexEng[word] = uint(int(key))

    def eng_contains(self, word):
        return word in self.lexEng

    def cant_contains(self, word):
        return word in self.lexCant

    def eng_add(self, word: str) -> uint:
        val = rand.randint(0, WC.INT_EXT_MASK)
        while val in self.lexCant:  # find an open value.
            val += 1
        self.lexCant[uint(val)] = word
        self.lexEng[word] = uint(val)
        return uint(val)


if __name__ == '__main__':  # Load 'default' file and save it to the lex file.
    default = Lexicon('')
    default.load_default()
