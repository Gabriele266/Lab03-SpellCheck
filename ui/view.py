import flet as ft
from flet import View

from ui.spellcheckcontroller import SpellcheckController


@ft.control
class HomePage(View):
    def __init__(self):
        self.controller = SpellcheckController(self)
        super().__init__()

    def init(self):
        self.route = "/"
        self.appbar = ft.AppBar(
                title=ft.Text("Spellcheck Application"),
                leading=ft.Icon(ft.Icons.SPELLCHECK),
            )
        self.controls = [
            ft.Text("Hello"),
            ft.Button(
                content="My button",
                on_click=self.controller.on_button_click,
            )
        ]