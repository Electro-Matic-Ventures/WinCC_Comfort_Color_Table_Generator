from ColorData import ColorData


class AreaData:
    
    white: ColorData
    black: ColorData
    red: ColorData
    yellow: ColorData
    green: ColorData
    teal: ColorData
    blue: ColorData
    purple: ColorData
    
    def __init__(self):
        self.white = ColorData()
        self.black = ColorData()
        self.red = ColorData()
        self.yellow = ColorData()
        self.green = ColorData()
        self.teal = ColorData()
        self.blue = ColorData()
        self.purple = ColorData()
        return
    
    def set_property(self, key:str, value:ColorData)-> None:
        self.__dict__[key] = value
        return