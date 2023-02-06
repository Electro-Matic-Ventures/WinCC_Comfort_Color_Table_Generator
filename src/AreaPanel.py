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
    
    def __init__(self, title:str):
        super().__init__(title)
        self.__instantiations()
        self.__layout = QVBoxLayout(self)
        self.__add_widgets()
        self.__set_appearance()
        return
    
    def __instantiations(self)-> None:
        self.white = ColorPanel("White")
        self.black = ColorPanel("Black")
        self.red = ColorPanel("Red")
        self.yellow = ColorPanel("Yellow")
        self.green = ColorPanel("Green")
        self.teal = ColorPanel("Teal")
        self.blue = ColorPanel("Blue")
        self.purple = ColorPanel("Purple") 
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
    
    def __set_appearance(self)-> None:
        self.__layout.setContentsMargins(10, 15, 10, 10)
        self.setFixedSize(275, 750)
        self.setStyleSheet(self.__generate_style_sheet())
        return
    
    def __generate_style_sheet(self)-> str:
        return '''
            AreaPanel {
                background-color: #222831;
                color: #EEEEEE;
                font-size: 20pt;
                border: 2px solid #FFD369;
                margin-top: 10px;
            }
            AreaPanel::title {
                left: 10px;
                bottom: 20px;
            }
        '''