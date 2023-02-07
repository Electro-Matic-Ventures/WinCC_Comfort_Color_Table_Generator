from PyQt6.QtWidgets import QLineEdit
from PyQt6.QtCore import Qt, QRegularExpression
from PyQt6.QtGui import QRegularExpressionValidator
from PasteToMenu import PasteToMenu


class LabeledInputInput(QLineEdit):
    
    context_menu: PasteToMenu
    
    def __init__(self):
        super().__init__()
        self.context_menu = PasteToMenu()
        self.__set_appearance()
        self.__set_validator()
        return
    
    def contextMenuEvent(self, event):
        self.context_menu.exec(event.globalPos())
        return
    
    def __set_appearance(self)-> None:
        self.setFixedSize(50, 20)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setStyleSheet(self.__generate_style_sheet())
        return
    
    def __generate_style_sheet(self)-> str:
        return '''        
            LabeledInputInput {
                background-color: #EEEEEE;
                border: 2px solid #FFD369;
                color: #393E46;
                font-size: 10pt;
                font-weight: bold;
            }
        ''' 
    
    def __set_validator(self)-> None:
        pattern = '[0-9]+'
        regex = QRegularExpression(pattern)
        validator = QRegularExpressionValidator(regex)
        self.setValidator(validator)
        return