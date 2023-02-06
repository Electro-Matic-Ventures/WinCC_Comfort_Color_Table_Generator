class ColorData:
    
    enabled: bool
    min_: int
    max_: int
    steps: int
    
    def __init__(
        self, 
        enabled:bool=False, 
        min_:int=0, 
        max_:int=0, 
        steps:int=0
    ):
        self.enabled = enabled
        self.min_ = min_
        self.max_ = max_
        self.steps = steps
        return
    
    def set_property(self, key:str, value):
        self.__dict__[key] = value
        return