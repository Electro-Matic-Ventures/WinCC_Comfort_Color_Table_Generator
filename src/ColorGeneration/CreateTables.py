from Color import Color
from Colors import Black, Blue, Green, Teal, Red, Purple, Yellow, White
from ColorCalculator import ColorCalculator
from ColorTableRowWriter import ColorTableRowWriter
from ConstantsTableRowWriter import ConstantsTableRowWriter


class CreateTables:

    __color_max: int
    __color_min: int
    __intensity_steps: int
    __background_colors: list
    __foreground_colors: list
    __color_table_row_writer: ColorTableRowWriter
    __constants_table_row_writer: ConstantsTableRowWriter
    __color_calculator: ColorCalculator
    __value: int
    __color_table: str
    constants_table: str
    __combinations: list
    
    def __init__(self, background_colors: list, foreground_colors: list, color_max: int, color_min: int, intensity_steps: int):
        self.__color_max = color_max
        self.__color_min = color_min
        self.__intensity_steps = intensity_steps
        self.__background_colors = background_colors
        self.__foreground_colors = foreground_colors
        self.__color_table_row_writer = ColorTableRowWriter()
        self.__constants_table_row_writer = ConstantsTableRowWriter()
        self.__color_calculator = ColorCalculator(color_max, color_min, intensity_steps)
        self.__value = 0
        self.color_table = 'Range\tBackground color\tForeground color\tFlashing\n'
        self.constants_table = 'Name\tPath\tData Type\tValue\tComment\n'
        self.__combinations = []
        self.__generate_rows(False)
        self.__generate_rows(True)
        return
                        
    def __generate_rows(self, flash: bool)-> None:
        if flash:
            self.__value = -1
        else:
            self.__value = 1
        # non-flashing loop
        for background in self.__background_colors:
            for bg_intensity_step in range(self.__intensity_steps):
                # black only needs one intensity level
                if background.name == 'black' and bg_intensity_step >= 1:
                    continue
                for foreground in self.__foreground_colors:
                    for fg_intensity_step in range(self.__intensity_steps):
                        # black only needs one intensity level
                        if foreground.name == 'black' and fg_intensity_step >= 1:
                            continue
                        # don't need color on color rows (i.e. red back ground with red foreground)
                        if background == foreground: 
                            continue
                        # check if combination has been generated 
                        bg_name = f'{background.name}{bg_intensity_step}'
                        fg_name = f'{foreground.name}{fg_intensity_step}'
                        if flash and self.__combination_exists(bg_name, fg_name):
                            continue
                        # generate row
                        self.__generate_row(
                            background,
                            bg_intensity_step,
                            foreground,
                            fg_intensity_step,
                            flash
                        )
                        # decrement value
                        if flash:
                            self.__value -= 1
                        else:
                            self.__value += 1
        return
        
    def __combination_exists(self, bg_name: str, fg_name: str)-> bool:
        combination = bg_name + fg_name
        if combination in self.__combinations:
            return True
        combination = fg_name + bg_name
        if combination in self.__combinations:
            return True
        self.__combinations.append(combination)
        return False                

    def __generate_row(self, bg: Color, bg_intensity_step: int, fg: Color, fg_intensity_step: int, flash: bool)-> None:
        # calculate colors
        bg_calculated = self.__calculate_color(bg, bg_intensity_step)
        fg_calculated = self.__calculate_color(fg, fg_intensity_step)
        # generate color table row
        self.color_table += self.__generate_color_table_row(
            self.__value,
            bg_calculated,
            fg_calculated,
            flash
        )
        # generate constants table row
        self.constants_table += self.__generate_constants_table_row(
            bg_calculated, 
            bg_intensity_step, 
            fg_calculated, 
            fg_intensity_step, 
            self.__value,
            flash
        )
        return

    def __calculate_color(self, color: Color, intensity_step: int)-> Color:
        if color.name == 'black': # black doens't need the calculator because it only has one intensity level
            return Black()
        return self.__color_calculator.calculate(color, intensity_step + 1)

    def __generate_color_table_row(self, value: int, bg_calculated: Color, fg_calculated: Color, flash: bool)-> str:
        _flash = "No"
        if flash:
            _flash = "Yes"
        return self.__color_table_row_writer.write(
            value, 
            bg_calculated, 
            fg_calculated, 
            _flash
        )

    def __generate_constants_table_row(
        self, 
        bg: Color, 
        bg_intensity_step: int, 
        fg: Color, 
        fg_intensity_step: int, 
        value: int, 
        flash: bool)-> str:
        _flash = ""
        if flash:
            _flash = "FLASH"
        name = self.__constants_table_row_writer.make_name(
            _flash, 
            bg.name, 
            bg_intensity_step, 
            fg.name, 
            fg_intensity_step
        )
        return self.__constants_table_row_writer.write(
            name,
            "Colors", 
            "Int", 
            value,
            ""
        )
                    