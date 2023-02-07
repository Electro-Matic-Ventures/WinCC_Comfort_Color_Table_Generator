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
actions = [
    ["enabled", "is_checked()"],
    ["min_", "min_value()"],
    ["max_", "max_value()"],
    ["steps", "steps_value()"]   
]

output = ''
for area in areas:
    for color in colors:
        for action in actions:
            data_action = action[0]
            widget_action = action[1]
            action_label = data_action
            if action_label == "min_":
                action_label = action_label[:-1]
            if action_label =="max_":
                action_label = action_label[:-1]
            output += f'''  
    def __{area}_{color}_{action_label}_action(self)-> None:
        self.data.{area}.{color}.{data_action} = self.widget.{area}.{color}.{widget_action}
        return\n'''
        
            
with open('output.txt', 'w') as file_:
    file_.write(output)