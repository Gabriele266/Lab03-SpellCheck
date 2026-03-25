import time

from domain.dictionary import RichWord, Dictionary
from dataclasses import dataclass

@dataclass(frozen=True)
class SpellcheckResult:
    wrong_words: list[RichWord]
    correct_words: list[RichWord]
    total_mistakes: int
    time_elapsed: float

    def __str__(self):
        return f"""time_elapsed: {self.time_elapsed} s, \ntotal_mistakes: {self.total_mistakes}, \nwrong_words: {self.wrong_words}"""

class Spellcheck:
    def __init__(self, input_text: str, dictionary: Dictionary):
        self._input_text = input_text
        self._dictionary = dictionary

    @property
    def input_text(self):
        return self._input_text

    @property
    def dictionary(self):
        return self._dictionary

    def sanitize_input(self) -> str:
        text_cp = str(self._input_text)         # working copy
        text_cp = text_cp.lower()
        """Sanitize the input text"""
        chars = "\\\n\t`*_{}[]()>#+-.!$%^;,=_~?!'"

        for c in chars:
            text_cp = text_cp.replace(c, "")

        return text_cp

    def spellcheck_linear(self) -> SpellcheckResult:
        """Perform spellcheck using linear search alghorithm"""
        t1 = time.time()
        # 1 pulizia del testo in input da segni di punteggiatura, a capo
        sanitized = self.sanitize_input()

        # scorrimento delle parole una ad una e controllo della correttezza
        words_list = sanitized.split(" ")

        wrong_words = []
        correct_words = []
        wrong = 0
        for word in words_list:
            r = RichWord(word, self._dictionary.is_correct(word))
            if r.correct:
                correct_words.append(r)
            else:
                wrong_words.append(r)
                wrong += 1

        t2 = time.time()
        return SpellcheckResult(wrong_words=wrong_words, correct_words=correct_words, total_mistakes=wrong, time_elapsed=t2 - t1)

    def spellcheck_dicotomic(self) -> SpellcheckResult:
        """Perform spellcheck using dicotmic search alghorithm"""
        t1 = time.time()
        # 1 pulizia del testo in input da segni di punteggiatura, a capo
        sanitized = self.sanitize_input()

        # scorrimento delle parole una ad una e controllo della correttezza
        words_list = sanitized.split(" ")

        wrong_words = []
        correct_words = []
        wrong = 0
        for word in words_list:
            r = RichWord(word, self._dictionary.is_correct_dicotomic(word))
            if r.correct:
                correct_words.append(r)
            else:
                wrong_words.append(r)
                wrong += 1

        t2 = time.time()
        return SpellcheckResult(wrong_words=wrong_words, correct_words=correct_words, total_mistakes=wrong,
                                time_elapsed=t2 - t1)
