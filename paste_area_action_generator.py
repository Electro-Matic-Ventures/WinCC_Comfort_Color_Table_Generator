def enable_string(area:str, colors:list)-> str:
    output = f'\tdef __paste_to_{area}_enable(self, value:bool)-> None:\n'
    for color in colors:
        output += f'\t\tself.widget.{area}.{color}.color_enable.setChecked(value)\n'
    output += '\t\treturn\n\n'
    return output

def other_strings(area:str, colors:list, control:str)-> str:
    output = f'\tdef __paste_to_{area}_{control}(self, value:bool)-> None:\n'
    output += '\t\tvalue_ = str(value)\n'
    for color in colors:
        output += f'\t\tself.widget.{area}.{color}.color_{control}.input_.setText(value_)\n'
    output += '\t\treturn\n\n'
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
        if control == "enable":
            output += enable_string(area, colors)
            continue
        output += other_strings(area, colors, control)
        
with open("output.txt", "w") as file_:
    file_.write(output)
