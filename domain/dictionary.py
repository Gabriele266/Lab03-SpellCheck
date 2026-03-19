from dataclasses import dataclass

class Dictionary:
    __DICT_BASE_PATH__ = "resources"

    def __init__(self, filename: str, language: str, terms=None):
        if terms is None:
            terms = []

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