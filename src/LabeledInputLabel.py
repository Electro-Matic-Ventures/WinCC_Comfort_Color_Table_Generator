from PyQt6.QtWidgets import QLabel
from PyQt6.QtCore import Qt


class LabeledInputLabel(QLabel):
    
    def __init__(self, title:str, style_sheet:str):
        super().__init__(title)
        self.__set_appearance(style_sheet=style_sheet)
        return
        
    def __set_appearance(self, style_sheet:str)-> None:
        self.setFixedSize(50, 20)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setStyleSheet(style_sheet)
        return