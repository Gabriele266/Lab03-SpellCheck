import os
from domain.dictionary import Dictionary
from domain.spellcheck import SpellcheckResult


class Model:        # application status
    def __init__(self, theme: str, algorithm_name: str):
        self.theme = theme
        self.algorithm_name = algorithm_name
        self.input_text = ""
        self.result: SpellcheckResult | None = None
        self.has_result = False
        self.language_name: str = "italian"
        self.__available_languages: list[str] = self.__load_available_languages__()

    @staticmethod
    def __load_available_languages__() -> list[str]:
        files = os.listdir(Dictionary.__DICT_BASE_PATH__)
        r = list(map(lambda x: x.replace(".txt", "").replace("/", ""), files))
        return r

    def set_input_text(self, t: str):
        self.input_text = t

    @property
    def available_languages(self):
        return self.__available_languages

    def set_result(self, r: SpellcheckResult):
        self.has_result = True
        self.result = r
    
