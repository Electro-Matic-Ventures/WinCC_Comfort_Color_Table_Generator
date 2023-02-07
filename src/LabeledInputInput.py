from PyQt6.QtWidgets import QLineEdit
from PyQt6.QtCore import Qt


class LabeledInputInput(QLineEdit):
    
    def __init__(self):
        super().__init__()
        self.__set_appearance()
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