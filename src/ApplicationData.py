from AreaData import AreaData
from PathData import PathData


class ApplicationData:
    
    background: AreaData
    foreground: AreaData
    path: PathData
    
    def __init__(self):
        self.background = AreaData()
        self.foreground = AreaData()
        self.path = PathData()
        return
    
    def set_property(self, key, value)-> None:
        self.__dict__[key] = value
        return
    
