# from Colors import Black, Blue, Green, Teal, Red, Purple, Yellow, White
# from CreateTables import CreateTables
# from pandas import read_csv, DataFrame
# from io import StringIO


# bg_colors = [Black(), Blue(), Green(), Teal(), Red(), Purple(), Yellow(), White()]
# fg_colors = [Black(), Blue(), Green(), Teal(), Red(), Purple(), Yellow(), White()]
# color_max = 255
# color_min = 100
# intensity_steps = 3

# tables = CreateTables(bg_colors, fg_colors, color_max, color_min, intensity_steps)

# df = read_csv(StringIO(tables.constants_table), "\t", index_col=False)
# df.to_excel("constants_table.xlsx")

# df = read_csv(StringIO(tables.color_table), "\t", index_col=False)
# df.to_excel("color_table.xlsx")


from PyQt6.QtWidgets import QApplication
from MainWindow import MainWindow
import sys


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()    