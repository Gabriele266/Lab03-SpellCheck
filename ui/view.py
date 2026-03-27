import flet as ft
from flet import View

@ft.control
class HomePage(View):
    def init(self):
        self.route = "/"
        self.appbar = ft.AppBar(
                title=ft.Text("Spellcheck Application"),
                leading=ft.Icon(ft.Icons.SPELLCHECK),
            )
        self.controls = [
            ft.Text("Hello")
        ]