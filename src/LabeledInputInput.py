from PyQt6.QtWidgets import QLineEdit
from PyQt6.QtCore import Qt, QRegularExpression
from PyQt6.QtGui import QIntValidator
from IntValidator import IntValidator 
from PasteToMenu import PasteToMenu


class LabeledInputInput(QLineEdit):
    
    context_menu: PasteToMenu
    
    def __init__(self, style_sheet:str):
        super().__init__()
        self.context_menu = PasteToMenu()
        self.__set_appearance(style_sheet)
        return
    
    def contextMenuEvent(self, event):
        self.context_menu.exec(event.globalPos())
        return
    
    def __set_appearance(self, style_sheet:str)-> None:
        self.setFixedSize(50, 20)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setStyleSheet(style_sheet)
        return
    
    def set_validator(self, min_:int, max_:int)-> None:
        validator = IntValidator(min_, max_)
        self.setValidator(validator)
        return