from numpy import uint64 as uint
from numpy import ndarray
import numpy
from BinaryCant.word_processor import WordProcessor
from BinaryCant.word_processor import print_list_bin, print_list_hex
from typing import List
from PIL import Image, ImageDraw
from math import sqrt, ceil


class CodeProcessor:
    @staticmethod
    def from_cant_file(file_name: str) -> ndarray:
        with open(file_name, 'r') as file:
            data = file.read()
        print(data)
        ret = WordProcessor.compile(data, True)
        # Send to Cant Processor
        return ret

    @staticmethod
    def compile_cant_to_file(input_file: str, output_file: str):
        data = CodeProcessor.from_cant_file(input_file)
        print(data)
        # do additional checks and work here (send to the cant processor).
        CodeProcessor.output_to_file(data, output_file)

    @staticmethod
    def output_to_file(data: ndarray, output_file: str):
        numpy.save(output_file, data)


    @staticmethod
    def make_file_size(val: int) -> int:
        ret = ceil(sqrt(val))
        return int(ret)

    @staticmethod
    def read_from_bin(file_name):
        data = numpy.load(file_name)
        print("----------")
        print(data)


if __name__ == "__main__":
    print(CodeProcessor.compile_cant_to_file("test_cant.can", "test_cant"))
    CodeProcessor.read_from_bin("test_cant.npy")
