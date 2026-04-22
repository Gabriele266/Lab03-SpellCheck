import flet as ft
from flet import View
import time
import threading
from domain.dictionary import Dictionary
from domain.spellcheck import Spellcheck

from ui.model import Model

class SpellcheckController:                 # handle all changes to view and model
    def __init__(self, view) -> None:
        self._model = Model("white", "linear")
        self._view = view           # WithBanner or View
        self.dictionaries: dict[str, Dictionary] = {}

    def load_dictionaries(self) -> float:
        self.dictionaries = {}
        threads: list[threading.Thread] = []
        tic = time.time()

        # load all available dictionaries with different threads
        for language in self._model.available_languages:
            dictionary = Dictionary(f"{language}.txt", language)
            print(f"Start loading {language}")
            self.dictionaries[language.lower()] = dictionary
            load_tread = threading.Thread(target=dictionary.load)
            threads.append(load_tread)
            load_tread.start()

        for t in threads:
            t.join()
            threads.remove(t)

        toc = time.time()
        return toc-tic

    @property
    def model(self) -> Model:
        return self._model

    @property
    def view(self) -> View:
        return self._view

    def on_button_click(self, event: ft.Event) -> None:
        print(f"HI {event}")

    def on_theme_switch(self, event: ft.Event[ft.Switch]) -> None:
        print(event)

    def on_correct_click(self):
        if self._model.input_text == "":
            self._view.show_dialog(ft.Banner(
                leading = ft.Icon(ft.Icons.ERROR),
                content = "Please set a text to correct. ",
                open=True,
                actions = [
                    ft.TextButton("Dismiss",
                                  on_click=lambda t: self._view.pop_dialog())
                ]
            ))
            return

        dictionary = self.dictionaries[self._model.language_name.lower()]
        s = Spellcheck(self._model.input_text, dictionary)

        result = None
        if self._model.algorithm_name == "linear":
            result = s.spellcheck_linear()
            self._model.set_result(result)
        elif self._model.algorithm_name == "dicotomic":
            result = s.spellcheck_dicotomic()
            self._model.set_result(result)
        else:
            self._model.has_result = False
            raise ValueError(f"Unrecognized algorithm name: {self._model.algorithm_name}")

        self._view.set_result(f"Correction results. Number of mistakes: {result.total_mistakes} \nComplete list: {result.wrong_words.__str__()}")

    def on_algorithm_select(self, e: ft.Event[ft.Dropdown]) -> None:
        self._model.algorithm_name = e.data

    def on_language_select(self, e: ft.Event[ft.Dropdown]) -> None:
        self._model.language_name = e.data

    # Riceve in data il testo intero attuale
    def on_text_input_change(self, event: ft.Event[ft.TextField]) -> None:
        self._model.input_text = event.data