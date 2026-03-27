import flet as ft

from ui.model import Model

class SpellcheckController:                 # handle all changes to view and model
    def __init__(self, view: ft.View):
        self.model = Model("white", "linear")
        self.view = view

    def on_button_click(self, event: ft.Event) -> None:
        print(f"HI {event}")