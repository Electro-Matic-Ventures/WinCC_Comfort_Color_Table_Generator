from PyQt6.QtWidgets import QGroupBox, QHBoxLayout
from OutputPathBrowse import OutputPathBrowse
from OutputPathInput import OutputPathInput


class OutputPath(QGroupBox):
    
    __layout: QHBoxLayout
    input_: OutputPathInput
    browse: OutputPathBrowse
    
    def __init__(self):
        super().__init__("Select output path...")
        self.__instantiations()
        self.__add_widgets()
        self.__set_appearance()
        self.setLayout(self.__layout)
        return
    
    def __instantiations(self)-> None:
        self.__layout = QHBoxLayout(self)
        self.input_ = OutputPathInput()
        self.browse = OutputPathBrowse()
        return
    
    def __add_widgets(self)-> None:
        self.__layout.addWidget(self.input_)
        self.__layout.addWidget(self.browse)
        return
    
    def __set_appearance(self)-> None:
        self.__layout.setContentsMargins(10, 10, 10, 10)
        self.__layout.setSpacing(10)
        self.setFixedSize(570, 85)
        self.setStyleSheet(self.__generate_style_sheet())
        return
    
    def __generate_style_sheet(self)-> str:
        return '''
            OutputPath {
                background-color: #222831;
                color: #EEEEEE;
                font-size: 14pt;
                border: 2px solid #FFD369;
                margin-top: 15px;
            }
            OutputPath::title {
                left: 6px;
                bottom: 15px;
            }
        '''   