from PyQt6.QtWidgets import QPushButton


class GenerateButton(QPushButton):
    
    def __init__(self, style_sheet:str):
        super().__init__(text="GENERATE")
        self.__set_appearance(style_sheet=style_sheet)
        return
    
    def __set_appearance(self, style_sheet:str)-> None:
        self.setFixedSize(570, 50)
        self.setStyleSheet(style_sheet)
        return