from PyQt6.QtWidgets import QCheckBox


class SingelColor(QCheckBox):
    
    def __init__(self, title:str):
        super().__init__()
        self.setText(title)