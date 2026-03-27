from flet import View

from ui.model import Model


class SpellcheckController:                 # handle all changes to view and model
    def __init__(self, model: Model, view: View):
        self.model = model
        self.view = view