from ApplicationData import ApplicationData
from Color import Color
from Colors import White, Black, Red, Yellow, Green, Teal, Blue, Purple
from ColorCalculator import ColorCalculator
from ColorData import ColorData
from ColorTableRowWriter import ColorTableRowWriter
from ConstantsTableRowWriter import ConstantsTableRowWriter


class Generate:
    
    row_number: int
    color_table: str
    constants_table: str
    visited: list  
    
    def __init__(self):
        self.row_number = 0
        self.color_table = ''
        self.constants_table = ''
        self.visited = []
        return  
        
    def generate(self, data:ApplicationData)-> None:
        if data is None:
            return
        bg_data: ColorData
        fg_data: ColorData
        for bg_name in data.background.__dict__:
            bg_data = data.background.__dict__[bg_name]
            if not bg_data.enabled:
                continue
            for fg_name in data.foreground.__dict__:
                fg_data = data.foreground.__dict__[fg_name]
                if not fg_data.enabled:
                    continue
                if bg_name == fg_name:
                    continue                 
                if not self.__in_visited(bg_name, fg_name):
                    self.__write_rows_to_tables(bg_data, bg_name, fg_data, fg_name, True)
                self.__add_to_visited(bg_name, fg_name)
                self.__write_rows_to_tables(bg_data, bg_name, fg_data, fg_name, False)
        return
    
    def __in_visited(self, bg:str, fg:str)-> bool:
        return f'{bg}{fg}' in self.visited
    
    def __write_rows_to_tables(self, bg:ColorData, bg_name:str, fg:ColorData, fg_name:str, flash:bool)-> None:
        color_writer = ColorTableRowWriter()
        constants_writer = ConstantsTableRowWriter()
        bg_calculator = ColorCalculator(bg.max_, bg.min_, bg.steps)
        fg_calculator = ColorCalculator(fg.max_, fg.min_, fg.steps)
        for bg_i in range(bg.steps):
            if bg_name == "black" and bg_i >= 1:
                continue
            for fg_i in range(fg.steps):
                if fg_name == "black" and fg_i >= 1:
                    continue
                bg_color = bg_calculator.calculate(self.__color_str_to_obj(bg_name), bg_i + 1)
                fg_color = fg_calculator.calculate(self.__color_str_to_obj(fg_name), fg_i + 1)
                self.color_table += color_writer.write(
                    self.row_number, 
                    bg_color, 
                    fg_color, 
                    flash
                )
                self.constants_table += constants_writer.write(
                    constants_writer.make_name(flash, bg_color, fg_color), 
                    "Colors", 
                    "DInt", 
                    self.row_number, 
                    ""
                )
                self.row_number += 1
        return
    
    def __add_to_visited(self, bg:str, fg:str)-> None:
        flags = self.__create_visited_flags(bg, fg)
        self.visited.append(flags[0])
        self.visited.append(flags[1])
        return
    
    def __create_visited_flags(self, bg:str, fg:str)-> tuple:
        return f'{bg}{fg}', f'{fg}{bg}'
    
    def __color_str_to_obj(self, color_name:str)-> Color:
        if color_name == 'white':
            return White()
        if color_name == 'black':
            return Black()
        if color_name == 'red':
            return Red()
        if color_name == 'yellow':
            return Yellow()
        if color_name == 'green':
            return Green()
        if color_name == 'teal':
            return Teal()
        if color_name == 'blue':
            return Blue()
        if color_name == 'purple':
            return Purple()
        return Color()