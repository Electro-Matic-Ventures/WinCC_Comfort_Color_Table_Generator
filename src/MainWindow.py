from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QIcon
from AreaPanel import AreaPanel

class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WinCC Comofort Color Table Generator")
        self.setWindowIcon(QIcon('icon.png'))
        w = AreaPanel("Background")
        self.setContentsMargins(20,20,20,20)
        x = '''
            MainWindow {
                background-color: #222831;
            }
        '''
        self.setStyleSheet(x)
        self.setCentralWidget(w)
        