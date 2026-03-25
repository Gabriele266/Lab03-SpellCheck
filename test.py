import unittest

from domain.dictionary import Dictionary
from domain.spellcheck import Spellcheck, SpellcheckResult


class MyTestCase(unittest.TestCase):
    __TEST_DICTIONARY__ = Dictionary.from_words([
        "ciao",
        "sono",
        "pizza",
        "mucca",
        "pecora",
        "pippo"
    ])

    __TEST_DICTIONARY2__ = Dictionary.from_words([
        "ciao",
        "sono",
        "pizza",
        "mucca",
        "pecora",
        "pippo",
        "quercia"
    ])

    def test_sanitizer(self):
        s = Spellcheck("Ciao, io sono Gabriele! \nOggi è un grande giorno? Sono 24 ore che dormo. $", MyTestCase.__TEST_DICTIONARY__)
        sanitized = s.sanitize_input()
        self.assertNotIn(",", sanitized)
        self.assertNotIn("\n", sanitized)
        self.assertNotIn("!", sanitized)
        self.assertNotIn(".", sanitized)
        self.assertNotIn("?", sanitized)

    def test_spellcheck(self):
        text = "ciao io son, pippo pecora 23!"

        correction = Spellcheck(text, MyTestCase.__TEST_DICTIONARY__)
        results: SpellcheckResult = correction.spellcheck_linear()

        self.assertIs(len(results.wrong_words) + len(results.correct_words), 6)
        self.assertIs(results.total_mistakes, 2)
        self.assertNotEqual(results.time_elapsed, 0)

    def test_dicotomic_1(self):
        self.assertTrue(self.__TEST_DICTIONARY__.is_correct_dicotomic("ciao"))
        self.assertFalse(self.__TEST_DICTIONARY__.is_correct_dicotomic("ciao22"))
        self.assertTrue(self.__TEST_DICTIONARY__.is_correct_dicotomic("pizza"))
        self.assertFalse(self.__TEST_DICTIONARY__.is_correct_dicotomic("pizzeria"))
        self.assertTrue(self.__TEST_DICTIONARY__.is_correct_dicotomic("mucca"))
        self.assertFalse(self.__TEST_DICTIONARY__.is_correct_dicotomic("muccheria"))
        self.assertTrue(self.__TEST_DICTIONARY__.is_correct_dicotomic("pecora"))
        self.assertFalse(self.__TEST_DICTIONARY__.is_correct_dicotomic("pecorie"))
        self.assertTrue(self.__TEST_DICTIONARY__.is_correct_dicotomic("pippo"))
        self.assertFalse(self.__TEST_DICTIONARY__.is_correct_dicotomic("roma"))
        self.assertFalse(self.__TEST_DICTIONARY__.is_correct_dicotomic("giovanna"))
        self.assertFalse(self.__TEST_DICTIONARY__.is_correct_dicotomic("al"))
        self.assertFalse(self.__TEST_DICTIONARY__.is_correct_dicotomic("quercia"))

    def test_dicotomic_2(self):
        self.assertTrue(self.__TEST_DICTIONARY2__.is_correct_dicotomic("ciao"))
        self.assertFalse(self.__TEST_DICTIONARY2__.is_correct_dicotomic("ciao22"))
        self.assertTrue(self.__TEST_DICTIONARY2__.is_correct_dicotomic("pizza"))
        self.assertFalse(self.__TEST_DICTIONARY2__.is_correct_dicotomic("pizzeria"))
        self.assertTrue(self.__TEST_DICTIONARY2__.is_correct_dicotomic("mucca"))
        self.assertFalse(self.__TEST_DICTIONARY2__.is_correct_dicotomic("muccheria"))
        self.assertTrue(self.__TEST_DICTIONARY2__.is_correct_dicotomic("pecora"))
        self.assertFalse(self.__TEST_DICTIONARY2__.is_correct_dicotomic("pecorie"))
        self.assertTrue(self.__TEST_DICTIONARY2__.is_correct_dicotomic("pippo"))
        self.assertFalse(self.__TEST_DICTIONARY2__.is_correct_dicotomic("roma"))
        self.assertFalse(self.__TEST_DICTIONARY2__.is_correct_dicotomic("giovanna"))
        self.assertFalse(self.__TEST_DICTIONARY2__.is_correct_dicotomic("al"))
        self.assertTrue(self.__TEST_DICTIONARY2__.is_correct_dicotomic("quercia"))
if __name__ == '__main__':
    unittest.main()
