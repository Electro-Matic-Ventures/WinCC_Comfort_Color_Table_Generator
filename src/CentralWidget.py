from PyQt6.QtWidgets import QGridLayout, QWidget
from AreaPanel import AreaPanel
from OutputPath import OutputPath
from GenerateButton import GenerateButton


class CentralWidget(QWidget):
    
    __layout: QGridLayout
    background: AreaPanel
    foreground: AreaPanel
    output_path: OutputPath
    generate_button: GenerateButton
    __spacer: QWidget
    
    def __init__(self, style_sheet:str):
        super().__init__()
        self.__instantiations(style_sheet=style_sheet)
        self.__add_widgets()
        self.__set_appearance(style_sheet=style_sheet)
        return
    
    def __instantiations(self, style_sheet:str)-> None:
        self.__layout = QGridLayout(self)
        self.background = AreaPanel(title="Background", style_sheet=style_sheet)
        self.foreground = AreaPanel("Foreground", style_sheet=style_sheet)
        self.output_path = OutputPath(style_sheet=style_sheet)
        self.generate_button = GenerateButton(style_sheet=style_sheet)
        self.spacer = QWidget()
        return
    
    def __add_widgets(self)-> None:
        self.__layout.addWidget(self.background, 1, 1, 1, 1)
        self.__layout.addWidget(self.spacer, 1, 2, 1, 1)
        self.__layout.addWidget(self.foreground, 1, 3, 1, 1)
        self.__layout.addWidget(self.output_path, 2, 1, 1, 3)
        self.__layout.addWidget(self.generate_button, 3, 1, 1, 3)
        return
    
    def __set_appearance(self, style_sheet:str)-> None:
        #self.setFixedSize(w, h)
        self.setStyleSheet(style_sheet)
        self.__layout.setSpacing(10)
        return