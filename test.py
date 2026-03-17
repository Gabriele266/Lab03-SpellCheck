import unittest

from domain.dictionary import Dictionary
from domain.spellcheck import Spellcheck


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
        text = "ciao io son, pippo pecora!"

        correction = Spellcheck(text, MyTestCase.__TEST_DICTIONARY__)
        results = correction.spellcheck()

        self.assertIs(len(results), 5)
        self.assertFalse(results[1].correct)
        self.assertFalse(results[2].correct)
        self.assertTrue(results[3].correct)


if __name__ == '__main__':
    unittest.main()
