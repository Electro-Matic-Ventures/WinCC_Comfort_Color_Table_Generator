from ApplicationData import ApplicationData
from Color import Color
from Colors import White, Black, Red, Yellow, Green, Teal, Blue, Purple
from ColorCalculator import ColorCalculator
from ColorData import ColorData

class Generate:
    
    table = []
    
    def __init__(self):
        return  
    
    def generate(self, data:ApplicationData)-> None:
        if data is None:
            return
        self.__calculate(data)
        return
        
    def __calculate(self, data:ApplicationData)-> None:
        value: ColorData
        for key in data.background.__dict__:
            value = data.background.__dict__[key]
            if not value.enabled:
                continue
            self.__append_color_rows(key, value)    
        return
        
    def __append_color_rows(self, color_name:str, channel:ColorData)-> Color:
        calculator = ColorCalculator(channel.max_, channel.min_, channel.steps)
        color = self.__color_str_to_obj(color_name, channel)
        for i in range(channel.steps):
            self.table.append(calculator.calculate(color, i+1))
        return
    
    def __color_str_to_obj(self, color_name:str, channel:ColorData)-> Color:
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