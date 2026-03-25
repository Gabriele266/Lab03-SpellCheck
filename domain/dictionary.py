from dataclasses import dataclass
import math

class Dictionary:
    __DICT_BASE_PATH__ = "resources"

    def __init__(self, filename: str, language: str, terms=None):
        if terms is None:
            terms = []

        terms.sort()
        self._terms: list[str] = terms                 # using a list because the order matters
        self.filename: str = filename
        self._language: str = language

    def load(self, _a=None, _b=None):
        if self.filename is None:
            raise ValueError("No filename provided")

        f = open(f"{Dictionary.__DICT_BASE_PATH__}\\{self.filename}", "r", encoding="utf-8")

        line = f.readline()
        while line:
            self._terms.append(line.strip().replace("\n", ""))
            line = f.readline()

        f.close()

    def is_correct(self, word: str) -> bool:
        if word.isnumeric():
            return True

        return word.lower() in self._terms

    def is_correct_dicotomic(self, word: str) -> bool:
        if word.isnumeric():
            return True

        n = len(self._terms)
        a = 0       # left pointer to search zone
        b = n - 1   # right pointer to search zone
        p = math.floor(math.fabs(b - a) / 2) + a        # pointer to current element to inspect
        p_new = p

        while a >= 0 and n > b >= p and p >= a:
            if self._terms[p] == word:
                return True

            if self._terms[p] > word:                       # go left
                b = p - 1
                p_new = math.floor(math.fabs(b - a) / 2) + a
                if p_new == p:
                    return False

                p = p_new

            if self._terms[p] < word:
                a = p + 1
                p_new = math.floor(math.fabs(b - a) / 2) + a
                if p_new == p:
                    return False

                p = p_new

        return False


    @classmethod
    def from_words(cls, words: list[str]):
        return cls("", "", words)

    def __str__(self):
        return f"{self._language} dictionary with {len(self._terms)} terms"

@dataclass(frozen=True)
class RichWord:
    word: str
    correct: bool

    def __str__(self):
        if self.correct:
            return f"""{self.word} -> correct"""
        else:
            return f"""{self.word} -> not correct"""