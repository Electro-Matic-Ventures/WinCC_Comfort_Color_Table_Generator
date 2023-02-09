from PyQt6.QtWidgets import QLineEdit


class OutputPathInput(QLineEdit):
    
    def __init__(self, style_sheet:str):
        super().__init__()
        self.__set_appearance(style_sheet=style_sheet)
        return
    
    def __set_appearance(self, style_sheet:str)-> None:
        self.setFixedSize(420, 30)
        self.setStyleSheet(style_sheet)
        return