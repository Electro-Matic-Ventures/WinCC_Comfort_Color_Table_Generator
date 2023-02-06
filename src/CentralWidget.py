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
    
    def __init__(self):
        super().__init__()
        self.__instantiations()
        self.__add_widgets()
        self.__set_appearance()
        return
    
    def __instantiations(self)-> None:
        self.__layout = QGridLayout(self)
        self.background = AreaPanel("Background")
        self.foreground = AreaPanel("Foreground")
        self.output_path = OutputPath()
        self.generate_button = GenerateButton()
        self.spacer = QWidget()
        return
    
    def __add_widgets(self)-> None:
        self.__layout.addWidget(self.background, 1, 1, 1, 1)
        self.__layout.addWidget(self.spacer, 1, 2, 1, 1)
        self.__layout.addWidget(self.foreground, 1, 3, 1, 1)
        self.__layout.addWidget(self.output_path, 2, 1, 1, 3)
        self.__layout.addWidget(self.generate_button, 3, 1, 1, 3)
        return
    
    def __set_appearance(self)-> None:
        #self.setFixedSize(w, h)
        self.setStyleSheet(self.__generate_style_sheet())
        self.__layout.setSpacing(10)
        return
    
    def __generate_style_sheet(self)-> str:
        return '''
            CentralWidget {
                background-color: #222831;
            }
        '''