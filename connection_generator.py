def write_connect(area:str, color:str)-> str:
    output = f'''
    def __connect_{area}_{color}_actions(self)-> None:
        # ENABLE
        self.widget.{area}.{color}.color_enable.stateChanged.connect(self.__{area}_{color}_enabled_action)
        self.widget.{area}.{color}.color_enable.context_menu.paste_to_all.triggered.connect(self.__paste_{area}_{color}_enable_to_all)
        self.widget.{area}.{color}.color_enable.context_menu.paste_to_area.triggered.connect(self.__paste_{area}_{color}_enable_to_area)
        # MIN
        self.widget.{area}.{color}.color_min.input_.textChanged.connect(self.__{area}_{color}_min_action)
        self.widget.{area}.{color}.color_min.input_.context_menu.paste_to_all.triggered.connect(self.__paste_{area}_{color}_min_to_all)
        self.widget.{area}.{color}.color_min.input_.context_menu.paste_to_area.triggered.connect(self.__paste_{area}_{color}_min_to_area)
        # MAX
        self.widget.{area}.{color}.color_max.input_.textChanged.connect(self.__{area}_{color}_max_action)
        self.widget.{area}.{color}.color_max.input_.context_menu.paste_to_all.triggered.connect(self.__paste_{area}_{color}_max_to_all)
        self.widget.{area}.{color}.color_max.input_.context_menu.paste_to_area.triggered.connect(self.__paste_{area}_{color}_max_to_area)
        # STEPS
        self.widget.{area}.{color}.color_steps.input_.textChanged.connect(self.__{area}_{color}_steps_action)
        self.widget.{area}.{color}.color_steps.input_.context_menu.paste_to_all.triggered.connect(self.__paste_{area}_{color}_steps_to_all)
        self.widget.{area}.{color}.color_steps.input_.context_menu.paste_to_area.triggered.connect(self.__paste_{area}_{color}_steps_to_area)
        return
    '''
    return output

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
        output += write_connect(area, color)
        
with open("output.txt", "w") as file_:
    file_.write(output)