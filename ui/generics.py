from abc import ABC

import flet as ft

"""
Represents a generic component that has the capability of handling a banner"""
class WithBanner(ABC):
    def __init__(self, page: ft.Page) -> None:
        self._page = page

    def show_dialog(self, banner: ft.Banner):
        print("Show banner")
        self._page.show_dialog(banner)

    def pop_dialog(self):
        self._page.pop_dialog()