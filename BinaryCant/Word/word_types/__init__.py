from BinaryCant.Word.word_types import const, floating_point, integer, rbga

word_types = [const.flag, floating_point.flag, integer.flag, rbga.flag]

to_word_processors = {const.flag: const.process_bin,
                      floating_point.flag: floating_point.process_bin,
                      integer.flag: integer.process_bin,
                      rbga.flag: rbga.process_bin}

to_bin_processors = {const.flag: const.process_word,
                      floating_point.flag: floating_point.process_word,
                      integer.flag: integer.process_word,
                      rbga.flag: rbga.process_word}

types_regex = ''

for flag in word_types:
    types_regex += flag + '|'
types_regex = types_regex[:-1]
