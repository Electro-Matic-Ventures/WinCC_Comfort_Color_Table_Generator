from PyQt6.QtWidgets import QGroupBox 
from PyQt6.QtWidgets import QHBoxLayout
from ColorEnable import ColorEnable
from LabeledInputVertical import LabeledInputVertical


class ColorPanel(QGroupBox):
    
    __layout: QHBoxLayout
    color_enable: ColorEnable
    color_min: LabeledInputVertical
    color_max: LabeledInputVertical
    color_steps: LabeledInputVertical
    
    def __init__(self, title:str):
        super().__init__(title)
        self.__instantiations()
        self.__layout = QHBoxLayout(self)
        self.__add_widgets()
        self.__set_appearance()
        return
    
    def __instantiations(self)-> None:
        self.color_enable = ColorEnable()
        self.color_min = LabeledInputVertical("min")
        self.color_max  = LabeledInputVertical("max")
        self.color_steps = LabeledInputVertical("steps")
        return
        
    def __add_widgets(self)-> None:
        self.__layout.addWidget(self.color_enable)
        self.__layout.addWidget(self.color_min)
        self.__layout.addWidget(self.color_max)
        self.__layout.addWidget(self.color_steps)
        return
    
    def __set_appearance(self)-> None:
        self.__layout.setContentsMargins(10, 10, 10, 10)
        self.__layout.setSpacing(10)
        self.setFixedSize(250, 80)
        self.setStyleSheet(self.__generate_style_sheet())
        return
    
    def __generate_style_sheet(self)-> str:
        return '''
            ColorPanel {
                background-color: #222831;
                color: #EEEEEE;
                font-size: 14pt;
                border: 2px solid #FFD369;
                margin-top: 15px;
            }
            ColorPanel::title {
                left: 6px;
                bottom: 15px;
            }
        '''
    
    def is_checked(self)-> bool:
        return self.color_enable.isChecked()
    
    def min_value(self)-> int:
        return int(self.color_min.input_.text())
    
    def max_value(self)-> int:
        return int(self.color_max.input_.text())
    
    def steps_value(self)-> int:
        return int(self.color_steps.input_.text())