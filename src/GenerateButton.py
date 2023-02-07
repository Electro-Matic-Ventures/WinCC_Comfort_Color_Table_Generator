from PyQt6.QtWidgets import QPushButton


class GenerateButton(QPushButton):
    
    def __init__(self):
        super().__init__(text="GENERATE")
        self.__set_appearance()
        return
    
    def __set_appearance(self)-> None:
        self.setFixedSize(570, 50)
        self.setStyleSheet(self.__generate_style_sheet())
        return
    
    def __generate_style_sheet(self)-> str:
        return '''
            GenerateButton {
                background-color: #393E46;
                color: #EEEEEE;
                border: 2px solid #FFD369;
                border-radius: 4px;
                font-size: 24px;
                font-weight: bold;
            }
        '''