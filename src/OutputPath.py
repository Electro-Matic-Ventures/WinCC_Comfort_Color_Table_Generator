from PyQt6.QtWidgets import QGroupBox, QHBoxLayout
from OutputPathBrowse import OutputPathBrowse
from OutputPathInput import OutputPathInput


class OutputPath(QGroupBox):
    
    __layout: QHBoxLayout
    input_: OutputPathInput
    browse: OutputPathBrowse
    
    def __init__(self, style_sheet:str):
        super().__init__("Select output path...")
        self.__instantiations(style_sheet=style_sheet)
        self.__add_widgets()
        self.__set_appearance(style_sheet=style_sheet)
        self.setLayout(self.__layout)
        return
    
    def __instantiations(self, style_sheet:str)-> None:
        self.__layout = QHBoxLayout(self)
        self.input_ = OutputPathInput(style_sheet=style_sheet)
        self.browse = OutputPathBrowse(style_sheet=style_sheet)
        return
    
    def __add_widgets(self)-> None:
        self.__layout.addWidget(self.input_)
        self.__layout.addWidget(self.browse)
        return
    
    def __set_appearance(self, style_sheet:str)-> None:
        self.__layout.setContentsMargins(10, 10, 10, 10)
        self.__layout.setSpacing(10)
        self.setFixedSize(570, 85)
        self.setStyleSheet(style_sheet)
        return