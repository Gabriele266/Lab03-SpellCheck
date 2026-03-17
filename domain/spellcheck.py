from domain.dictionary import RichWord, Dictionary


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
        """Sanitize the input text"""
        chars = "\\\n\t`*_{}[]()>#+-.!$%^;,=_~?!"

        for c in chars:
            text_cp = text_cp.replace(c, "")

        return text_cp

    def spellcheck(self) -> list[RichWord]:
        # 1 pulizia del testo in input da segni di punteggiatura, a capo
        sanitized = self.sanitize_input()

        # scorrimento delle parole una ad una e controllo della correttezza
        words_list = sanitized.split(" ")
        print(f"Processing text with {len(words_list)} words")

        correction = []
        for word in words_list:
            correction.append(RichWord(word, self._dictionary.is_correct(word)))

        return correction