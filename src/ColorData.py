class ColorData:
    
    enabled: bool
    min_: int
    max_: int
    steps: int
    
    def __init__(self):
        self.enabled = False
        self.min_ = 0
        self.max_ = 0
        self.steps = 0
        return
    
    def set_property(self, key:str, value):
        self.__dict__[key] = value
        return