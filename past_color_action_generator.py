def enable_to_all(area:str, color:str)-> str:
    output = f'''
    def __paste_{area}_{color}_enable_to_all(self)-> None:
        value = self.widget.{area}.{color}.color_enable.isChecked()
        self.__paste_to_all_enable(value)
        return
    '''   
    return output

def enable_to_area(area:str, color:str)-> str:
    output = f'''
    def __paste_{area}_{color}_enable_to_area(self)-> None:
        value = self.widget.{area}.{color}.color_enable.isChecked()
        self.__paste_to_{area}_enable(value)
        return
    '''
    return output

def other_to_all(control:str, area:str, color:str)-> str:
    output = f'''
    def __paste_{area}_{color}_{control}_to_all(self)-> None:
        value = int(self.widget.{area}.{color}.color_{control}.input_.text())
        self.__paste_to_all_{control}(value)
        return
    '''
    return output

def other_to_area(control:str, area:str, color:str)-> str:
    output = f'''
    def __paste_{area}_{color}_{control}_to_area(self)-> None:
        value = int(self.widget.{area}.{color}.color_{control}.input_.text())
        self.__paste_to_{area}_{control}(value)
        return
    '''
    return output

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
controls = [
    "enable",
    "min",
    "max",
    "steps"
]
areas = [
    "background",
    "foreground"
]

output = ''
for area in areas:
    for control in controls:
        for color in colors:
            if control == "enable":
                output += enable_to_all(area, color)
                output += enable_to_area(area, color)
                continue
            output += other_to_all(control, area, color)
            output += other_to_area(control, area, color)
with open("output.txt", "w") as file_:
    file_.write(output)            
