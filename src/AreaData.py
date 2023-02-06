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
    
    def __init__(
        self,
        white:ColorData=ColorData(),
        black:ColorData=ColorData(),
        red:ColorData=ColorData(),
        yellow:ColorData=ColorData(),
        green:ColorData=ColorData(),
        teal:ColorData=ColorData(),
        blue:ColorData=ColorData(),
        purple:ColorData=ColorData(),
    ):
        self.white = white
        self.black = black
        self.red = red
        self.yellow = yellow
        self.green = green
        self.teal = teal
        self.blue = blue
        self.purple = purple
        return
    
    def set_property(self, key:str, value:ColorData)-> None:
        self.__dict__[key] = value
        return