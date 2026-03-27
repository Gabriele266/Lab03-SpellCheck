import flet as ft
from flet import View

from ui.model import Model

class SpellcheckController:                 # handle all changes to view and model
    def __init__(self, view: ft.View):
        self._model = Model("white", "linear")
        self._view = view

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
        pass

    def on_text_input_change(self, event: ft.Event[ft.TextField]) -> None:
        print(event)