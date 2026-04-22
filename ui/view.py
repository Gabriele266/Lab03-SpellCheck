import flet as ft
from flet import View

from ui.generics import WithBanner
from ui.spellcheckcontroller import SpellcheckController
from domain.spellcheck import AvailableAlgorithms

@ft.control
class HomePage(View, WithBanner):
    def __init__(self, page: ft.Page) -> None:
        self.__result_input = None
        self.controller = SpellcheckController(self)
        super().__init__()
        WithBanner.__init__(self, page)

    def init(self):
        langs = self.controller.model.available_languages

        self.route = "/"
        self.__result_input = ft.TextField(label = "", width = 300, height = 200)
        self.appbar = ft.AppBar(
                title=ft.Text("Spellcheck Application by Gabry - TDP 2026", color=ft.Colors.BLUE),
                leading=ft.Icon(ft.Icons.SPELLCHECK),
            actions=[
                ft.Switch(label="Dark theme",
                          value=False,
                          on_change=self.controller.on_theme_switch)
            ],
            actions_padding=ft.Padding.all(20)
            )

        self.controls = [
            ft.Dropdown(
                width=300,
                value=langs[0],
                options=HomePage.__map_languages__(langs),
                label="Select language",
                on_select=self.controller.on_language_select
            ),
            ft.Dropdown(
                width=400,
                value=AvailableAlgorithms.LINEAR.value,
                options=list(map(lambda t: ft.DropdownOption(
                    key=t,
                    text=t
                ), AvailableAlgorithms.list())),
                label="Select algorithm",
                on_select=self.controller.on_algorithm_select
            ),
            ft.TextField(
                multiline=True,
                height=600,
                width=900,
                max_lines=10,
                min_lines=10,
                autocorrect=False,
                label="Insert text to correct",
                on_change=self.controller.on_text_input_change,
                counter=ft.Button(
                    content="Correct",
                    on_click=self.controller.on_correct_click
                )
            ),
            self.__result_input
        ]
        print("Start loading dictionaries...")
        r = self.controller.load_dictionaries()
        print(f"Dictionaries loaded in {r} ms")

    def set_result(self, value):
        if self.__result_input is not None:
            self.__result_input.value = value

    @staticmethod
    def __map_languages__(langs: set[str]) -> list[ft.DropdownOption]:
        return list(map(lambda t: ft.DropdownOption(
            key=t,
            text=t
        ), langs))