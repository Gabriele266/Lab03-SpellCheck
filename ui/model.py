import os
from domain.dictionary import Dictionary

class Model:        # application status
    def __init__(self, theme: str, algorithm_name: str):
        self.theme = theme
        self.algorithm_name = algorithm_name
        self.input_text = ""
        self.result_text = ""
        self.has_result = False
        self.__available_languages: list[str] = self.__load_available_languages__()

    @staticmethod
    def __load_available_languages__() -> list[str]:
        files = os.listdir(Dictionary.__DICT_BASE_PATH__)
        r = list(map(lambda x: x.replace(".txt", ""), files))
        return r

    def set_input_text(self, t: str):
        self.input_text = t

    @property
    def available_languages(self):
        return self.__available_languages

    def set_result_text(self, t: str):
        self.has_result = True
        self.result_text = t
    
