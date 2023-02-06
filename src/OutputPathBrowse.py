from PyQt6.QtWidgets import QPushButton 


class OutputPathBrowse(QPushButton):
    
    def __init__(self):
        super().__init__(text="BROWSE")
        self.__set_appearance()
        return
    
    def __set_appearance(self)-> None:
        self.setFixedSize(100, 30)
        self.setStyleSheet(self.__generate_style_sheet())
        return
    
    def __generate_style_sheet(self)-> str:
        return '''
            OutputPathBrowse {
                background-color: #393E46;
                color: #EEEEEE;
                font-size: 10px;
                font-weight: bold;
                border: 2px solid #FFD369;
                border-radius: 4px;
            }
        '''