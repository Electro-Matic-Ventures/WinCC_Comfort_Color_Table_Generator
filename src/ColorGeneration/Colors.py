from Color import Color


class Black(Color):

    def __init__(self):
        self.red = 0
        self.green = 0
        self.blue = 0
        self.name = "black"


class Blue(Color):

    def __init__(self):
        self.red = 0
        self.green = 0
        self.blue = 1
        self.name = "blue"


class Green(Color):

    def __init__(self):
        self.red = 0
        self.green = 1
        self.blue = 0
        self.name = "green"


class Teal(Color):

    def __init__(self):
        self.red = 0
        self.green = 1
        self.blue = 1
        self.name = "teal"


class Red(Color):

    def __init__(self):
        self.red = 1
        self.green = 0
        self.blue = 0
        self.name = "red"


class Purple(Color):

    def __init__(self):
        self.red = 1
        self.green = 0
        self.blue = 1
        self.name = "purple"


class Yellow(Color):

    def __init__(self):
        self.red = 1
        self.green = 1
        self.blue = 0
        self.name = "yellow"

    
class White(Color):

    def __init__(self):
        self.red = 1
        self.green = 1
        self.blue = 1
        self.name = "white"