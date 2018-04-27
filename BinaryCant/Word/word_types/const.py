from numpy import uint64 as uint
import random as rand
import atexit


rand.seed()
const_file = 'const.csv'

flag = 'const'
word_to_bin = dict()
bin_to_word = dict()


def load_constants():
    with open(const_file, 'r') as file:
        for line in file.readlines():
            word, value = line.split(',')
            value = uint(int(value))
            word_to_bin[word] = value
            bin_to_word[value] = word


def save_constants():
    with open(const_file, 'w') as file:
        for word, val in word_to_bin.items():
            file.write(str(word)+','+str(val)+'\n')


def process_word(word: str) -> uint:
    if word in word_to_bin:
        return word_to_bin[word]
    else:
        temp = rand.randint(0, 2**32-1)
        while temp in bin_to_word:
            temp += 1
        word_to_bin[word] = temp
        bin_to_word[temp] = word
        return temp


def process_bin(val: uint) -> str:
    if val in bin_to_word:
        return bin_to_word[val]
    else:
        temp = 0
        undef = 'undef'
        while undef in word_to_bin:
            temp += 1
            undef = 'undef' + str(temp)
        bin_to_word[val] = undef
        word_to_bin[undef] = val
    return bin_to_word[val]


atexit.register(save_constants)
