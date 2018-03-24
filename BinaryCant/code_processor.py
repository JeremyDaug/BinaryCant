from numpy import uint64 as uint
from BinaryCant.word_processor import WordProcessor
from BinaryCant.Word.word_const import print_word_bin
from typing import List


class CodeProcessor:
    @staticmethod
    def from_cant_file(file_name: str) -> List[uint]:
        with open(file_name, 'r') as file:
            data = file.read()
        print(data)
        ret = WordProcessor.compile(data)
        return ret

    @staticmethod
    def compile_cant_to_file(input_file: str, output_file: str):
        data = CodeProcessor.from_cant_file(input_file)

    @staticmethod
    def read_from_binary(file_name):
        with open(file_name, 'rb') as file:
            data = file.read()
        print(data)


if __name__ == "__main__":
    CodeProcessor.compile_cant_to_file("test_cant.can", "test_cant.bin")
