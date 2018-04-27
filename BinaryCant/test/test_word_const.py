import unittest
import BinaryCant.Word.word_const as wc


# FlagCategories is confirmed to work, tests to come.
class TestWordConst(unittest.TestCase):

    def test_BeAbleToFindWordFlag(self):
        for flag, value in wc.Flag_Values.items():
            print(flag, value)
            self.assertEqual(wc.Flag_Values[flag], value)
        return
