
class Model:        # application status
    def __init__(self, theme: str, algorithm_name: str):
        self.theme = theme
        self.algorithm_name = algorithm_name
        self.input_text = ""
        self.result_text = ""
        self.has_result = False

    def set_input_text(self, t: str):
        self.input_text = t

    def set_result_text(self, t: str):
        self.has_result = True
        self.result_text = t
    
