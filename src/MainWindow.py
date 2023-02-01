from PyQt6.QtWidgets import QMainWindow


class MainWidow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WinCC Comofort Appearance Animation Configurator")
        self.setFixedSize(400, 300)  # width x height