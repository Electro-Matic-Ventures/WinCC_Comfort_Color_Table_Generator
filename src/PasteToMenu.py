from PyQt6.QtWidgets import QMenu 
from PyQt6.QtGui import QAction


class PasteToMenu(QMenu):
    
    paste_to_all: QAction
    paste_to_area: QAction
    
    def __init__(self):
        super().__init__()
        self.__add_actions()
        return

    def __add_actions(self):
        self.paste_to_all = self.addAction("Paste To All")
        self.paste_to_area = self.addAction("Paste To Area")
        return