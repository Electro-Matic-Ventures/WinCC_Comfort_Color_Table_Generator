import csv
from pandas import DataFrame, read_csv
from io import StringIO


class Writer:
    
    def __init__(self):
        return
    
    def save_color_table(self, path:str, color_table:str)-> None:
        df = read_csv(
            filepath_or_buffer = StringIO(color_table),
            delimiter = "\t",
            index_col = False,
            header = None
        )
        df.to_excel(
            excel_writer = f'{path}/color_table.xlsx',
            header = False,
            index = False    
            )
        return
    
    def save_constants_table(self, path:str, constants_table:str)-> None:
        df = read_csv(
            filepath_or_buffer = StringIO(constants_table), 
            delimiter = "\t",
            index_col = False,
            header = None
        )
        df.to_excel(
            excel_writer = f'{path}/constants_table.xlsx',
            header = False,
            index = False    
        )
        return