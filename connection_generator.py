areas = [
    "background",
    "foreground"
]

colors = [
    "white",
    "black",
    "red",
    "yellow",
    "green",
    "teal",
    "blue",
    "purple"
]
output = ''

for area in areas:
    for color in colors:
        output += f'''
    def __connect_{area}_{color}_actions(self)-> None:
        self.widget.{area}.{color}.color_enable.stateChanged.connect(self.__{area}_{color}_enabled_action)
        self.widget.{area}.{color}.color_min.input_.textChanged.connect(self.__{area}_{color}_min_action)
        self.widget.{area}.{color}.color_max.input_.textChanged.connect(self.__{area}_{color}_max_action)
        self.widget.{area}.{color}.color_steps.input_.textChanged.connect(self.__{area}_{color}_steps_action)
        return
        '''
        
with open("output.txt", "w") as file_:
    file_.write(output)