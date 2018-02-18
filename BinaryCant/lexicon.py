"""
A file for the lexicon of binary cant. It will allow for translation.
"""

from numpy import uint64 as uint


class Lexicon:
    def __init__(self, file):
        self.lexCant = {}  # Cant to english
        self.lexEng = {}  # english to Cant
        if not file:
            return
        with open(file, 'r') as f:
            for line in f.readlines():
                key, word = line.split(',')
                self.lexCant[uint(int(key))] = word
                self.lexEng[word] = uint(int(key))
        return

    def cant_to_english(self, word):
        return self.lexCant[word]

    def english_to_cant(self, word):
        return self.lexEng[word]

    def save(self, file: str):
        with open(file, 'w') as f:
            for key, value in self.lexCant.items():
                f.write(str(key)+','+value)
        return

    def load_default(self):
        with open('lexCanticon_default.csv') as f:
            for line in f.readlines():
                key, word = line.split(',')
                self.lexCant[uint(int(key))] = word
                self.lexEng[word] = uint(int(key))


if __name__ == '__main__':  # Load 'default' file and save it to the lex file.
    default = Lexicon('')
    default.load_default()
