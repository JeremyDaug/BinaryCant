from numpy import uint64 as uint
from numpy import ndarray
import numpy
from typing import List
from BinaryCant.Word import word as W
from BinaryCant.Word import word_const as WC
import queue


class CantProcessor:

    @staticmethod
    def read(data: ndarray, length=-1):
        print("new read ---------------------")
        print(data)
        words = queue.deque(data.tolist())
        memory = []
        for word in range(len(data)):
            if length == 0:
                break
            length -= 1
            if W.external_pointer_flag(data[word]):
                print("Is external pointer yah!")
            elif W.sentence_meta_flag(data[word]):
                print("Is Sentence start ya!")
                word_count = W.word_count(data[word])
                CantProcessor.read(data[word+1:])
            else:  # is a word in the sentence.
                print("Is word ya!")


if __name__ == "__main__":
    import BinaryCant.word_processor
    temp = [WC.EXTERNAL_POINTER_TRUE_FLAG]
    CantProcessor.read(numpy.asarray(temp, uint))
    temp = [WC.SENT_META_TRUE_FLAG]
    CantProcessor.read(numpy.asarray(temp, uint))
    temp = [WC.SENT_META_FALSE_FLAG]
    CantProcessor.read(numpy.asarray(temp, uint))
