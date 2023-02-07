from PyQt6.QtWidgets import QCheckBox
from PasteToMenu import PasteToMenu

class ColorEnable(QCheckBox):
    
    context_menu: PasteToMenu
    
    def __init__(self):
        super().__init__("on")
        t: QCheckBox
        self.context_menu = PasteToMenu()
        self.__set_appearance()
        return
    
    def contextMenuEvent(self, event):
        self.context_menu.exec(event.globalPos())
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