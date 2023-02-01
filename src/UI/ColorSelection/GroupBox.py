from PyQt6.QtWidgets import QGroupBox


class ColorListSelectLabel(QGroupBox):
    
    def __init__(self, text:str):
        super().__init__()
        self.setText(text)
        self.setFixedSize(100, 205)  # width x height