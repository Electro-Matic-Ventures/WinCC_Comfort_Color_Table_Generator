from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QIcon


class MainWidow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WinCC Comofort Appearance Animation Configurator")
        self.setFixedSize(400, 300)  # width x height
        self.setWindowIcon(QIcon('icon.png'))