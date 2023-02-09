from PyQt6.QtWidgets import QGroupBox, QVBoxLayout
from ColorPanel import ColorPanel


class AreaPanel(QGroupBox):
    
    __layout: QVBoxLayout
    white: ColorPanel
    black: ColorPanel
    red: ColorPanel
    yellow: ColorPanel
    green: ColorPanel
    teal: ColorPanel
    blue: ColorPanel
    purple: ColorPanel
    
    def __init__(self, title:str, style_sheet:str):
        super().__init__(title)
        self.__instantiations(style_sheet)
        self.__layout = QVBoxLayout(self)
        self.__add_widgets()
        self.__set_appearance(style_sheet=style_sheet)
        return
    
    def __instantiations(self, style_sheet:str)-> None:
        self.white = ColorPanel(title="White", style_sheet=style_sheet)
        self.black = ColorPanel("Black", style_sheet=style_sheet)
        self.red = ColorPanel("Red", style_sheet=style_sheet)
        self.yellow = ColorPanel("Yellow", style_sheet=style_sheet)
        self.green = ColorPanel("Green", style_sheet=style_sheet)
        self.teal = ColorPanel("Teal", style_sheet=style_sheet)
        self.blue = ColorPanel("Blue", style_sheet=style_sheet)
        self.purple = ColorPanel("Purple", style_sheet=style_sheet) 
        return
    
    def __add_widgets(self)-> None:
        self.__layout.addWidget(self.white)
        self.__layout.addWidget(self.black)
        self.__layout.addWidget(self.red)
        self.__layout.addWidget(self.yellow)
        self.__layout.addWidget(self.green)
        self.__layout.addWidget(self.teal)
        self.__layout.addWidget(self.blue)
        self.__layout.addWidget(self.purple)
        return
    
    def __set_appearance(self, style_sheet:str)-> None:
        self.__layout.setContentsMargins(10, 15, 10, 10)
        self.setFixedSize(275, 750)
        self.setStyleSheet(style_sheet)
        return