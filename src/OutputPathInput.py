from PyQt6.QtWidgets import QLineEdit


class OutputPathInput(QLineEdit):
    
    def __init__(self):
        super().__init__()
        self.__set_appearance()
        return
    
    def __set_appearance(self)-> None:
        self.setFixedSize(420, 30)
        self.setStyleSheet(self.__generate_style_sheet())
        return
    
    def __generate_style_sheet(self)-> str:
        return '''
            OutputPathInput {
                background-color: #EEEEEE;
                border: 2px solid #FFD369;
                border-radius: 4px;
                color: #393E46;
                font-size: 10pt;
                font-weight: bold;
            }
        '''