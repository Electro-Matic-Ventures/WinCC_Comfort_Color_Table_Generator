from Color import Color


class ColorTableRowWriter:

    def __init__(self):
        return

    def write(self, range_: int, background: Color, foreground: Color, flash: str)-> str:
        _range = self.__write_range_cell(range_)
        _background = self.__write_color_cell(background)
        _foreground = self.__write_color_cell(foreground)
        _flash = self.__write_flashing_cell(flash)
        return f'{_range}\t{_background}\t{_foreground}\t{_flash}\n'

    def __write_range_cell(self, value: int)-> str:
        return f'{value}'

    def __write_color_cell(self, color: Color)-> str:
        return f'{color.red};{color.green};{color.blue}'

    def __write_flashing_cell(self, value: str)-> str:
        return f'{value}'