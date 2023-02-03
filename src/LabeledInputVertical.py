from PyQt6.QtWidgets import QVBoxLayout, QWidget
from LabeledInputInput import LabeledInputInput
from LabeledInputLabel import LabeledInputLabel


class LabeledInputVertical(QWidget):
    
    __layout: QVBoxLayout
    label: LabeledInputLabel
    input_: LabeledInputInput 
    
    def __init__(self, title:str):
        super().__init__()
        self.__instantiations(title)
        self.__layout = QVBoxLayout(self)
        self.__set_appearance()
        self.__add_widgets()
        return
    
    def __instantiations(self, title:str)-> None:
        self.label = LabeledInputLabel(title)
        self.input_ = LabeledInputInput() 
        return
    
    def __set_appearance(self):
        self.setFixedSize(50, 40)
        self.__layout.setSpacing(0)
        self.__layout.setContentsMargins(0, 0, 0, 0)
        return    
    
    def __add_widgets(self):
        self.__layout.addWidget(self.label)
        self.__layout.addWidget(self.input_)