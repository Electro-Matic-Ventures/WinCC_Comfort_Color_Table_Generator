from Color import Color
from math import ceil


class ColorCalculator:

    __intensity_step: int
    __offset: int

    def __init__(self, color_max: int, color_min: int, intensity_steps: int):
        self.__intensity_step = self.__calculate_intensity_step(color_max, color_min, intensity_steps)
        self.__offset = color_min
        return
    
    def calculate(self, color: Color, step: int)-> Color:
        _color = self.__color_deep_copy(color)
        _color.red *= self.__calculate_intensity(step)
        _color.green *= self.__calculate_intensity(step)
        _color.blue *= self.__calculate_intensity(step)
        _color.name += f'_{step}'
        return _color

    def __color_deep_copy(self, color: Color)-> Color:
        _color = Color()
        _color.red = color.red
        _color.blue = color.blue
        _color.green = color.green
        _color.name = color.name
        return _color

    def __calculate_intensity(self, step: int)-> int:
        value = self.__intensity_step * step + self.__offset
        if value > 255:
            value = 255
        return value

    def __calculate_intensity_step(self, color_max: int, color_min: int, intensity_steps: int)-> int:
        return int(ceil((color_max - color_min)/ intensity_steps))