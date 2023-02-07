from PyQt6.QtWidgets import QLabel
from PyQt6.QtCore import Qt


class LabeledInputLabel(QLabel):
    
    def __init__(self, title:str):
        super().__init__(title)
        self.__set_appearance()
        return
        
    def __set_appearance(self)-> None:
        self.setFixedSize(50, 20)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setStyleSheet(self.__generate_style_sheet())
        return
    
    def __generate_style_sheet(self)-> str:
        return '''
            LabeledInputLabel {
                background-color: #222831;
                color: #EEEEEE;
                font-size: 10pt;
            }        
        '''