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


if __name__ == '__main__':
    unittest.main()
