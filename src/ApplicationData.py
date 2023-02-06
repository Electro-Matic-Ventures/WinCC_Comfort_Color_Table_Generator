from AreaData import AreaData
from PathData import PathData


class ApplicationData:
    
    background: AreaData
    foreground: AreaData
    path: PathData
    
    def __init__(
        self,
        background:AreaData=AreaData(),
        foreground:AreaData=AreaData(),
        path:PathData=PathData()
    ):
        self.background = background
        self.foreground = foreground
        self.path = path
        return
    
    def set_property(self, key, value)-> None:
        self.__dict__[key] = value
        return
    
    
t = ApplicationData()
stop_here = True