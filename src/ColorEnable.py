from PyQt6.QtWidgets import QCheckBox


class ColorEnable(QCheckBox):
    
    def __init__(self):
        super().__init__("on")
        self.__set_appearance()
        return
        
    def __set_appearance(self)-> None:
        self.setFixedSize(50, 40)
        self.setStyleSheet(self.__generate_style_sheet())
        return
    
    def __generate_style_sheet(self)-> str:
        return '''
            ColorEnable {
                background-color: #222831;
                color: #EEEEEE;
                font-size: 12pt;
                padding-left: 4px;
                padding-top: 16px;
            }   
        '''