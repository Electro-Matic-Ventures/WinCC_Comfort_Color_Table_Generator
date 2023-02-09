from PyQt6.QtWidgets import QGroupBox 
from PyQt6.QtWidgets import QHBoxLayout
from ColorEnable import ColorEnable
from LabeledInputVertical import LabeledInputVertical

class ColorPanel(QGroupBox):
    
    __layout: QHBoxLayout
    color_enable: ColorEnable
    color_min: LabeledInputVertical
    color_max: LabeledInputVertical
    color_steps: LabeledInputVertical  # LabeledInputVertical
    
    def __init__(self, title:str, style_sheet:str):
        super().__init__(title)
        self.__instantiations(style_sheet=style_sheet)
        self.__layout = QHBoxLayout(self)
        self.__add_widgets()
        self.__set_appearance(style_sheet=style_sheet)
        return
    
    def __instantiations(self, style_sheet:str)-> None:
        self.color_enable = ColorEnable(style_sheet=style_sheet)
        self.color_min = LabeledInputVertical(title="min", style_sheet=style_sheet)
        self.color_min.input_.set_validator(0, 255)
        self.color_max  = LabeledInputVertical(title="max", style_sheet=style_sheet)
        self.color_max.input_.set_validator(0, 255)
        self.color_steps = LabeledInputVertical(title="steps", style_sheet=style_sheet)  
        self.color_steps.input_.set_validator(1, 16)
        return
        
    def __add_widgets(self)-> None:
        self.__layout.addWidget(self.color_enable)
        self.__layout.addWidget(self.color_min)
        self.__layout.addWidget(self.color_max)
        self.__layout.addWidget(self.color_steps)
        return
    
    def __set_appearance(self, style_sheet:str)-> None:
        self.__layout.setContentsMargins(10, 10, 10, 10)
        self.__layout.setSpacing(10)
        self.setFixedSize(250, 80)
        self.setStyleSheet(style_sheet)
        return
    
    def is_checked(self)-> bool:
        return self.color_enable.isChecked()
    
    def min_value(self)-> int:
        return int(self.color_min.input_.text())
    
    def max_value(self)-> int:
        return int(self.color_max.input_.text())
    
    def steps_value(self)-> int:
        return int(self.color_steps.input_.text())