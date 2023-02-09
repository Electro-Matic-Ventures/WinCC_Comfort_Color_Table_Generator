from PyQt6.QtWidgets import QCheckBox
from PasteToMenu import PasteToMenu

class ColorEnable(QCheckBox):
    
    context_menu: PasteToMenu
    
    def __init__(self, style_sheet:str):
        super().__init__("on")
        t: QCheckBox
        self.context_menu = PasteToMenu()
        self.__set_appearance(style_sheet=style_sheet)
        return
    
    def contextMenuEvent(self, event):
        self.context_menu.exec(event.globalPos())
        return
        
    def __set_appearance(self, style_sheet:str)-> None:
        self.setFixedSize(50, 40)
        self.setStyleSheet(style_sheet)
        return