class Writer:
    
    def __init__(self):
        return
    
    def save_color_table(self, path:str, color_table:str)-> None:
        with open(f'{path}/color_table.csv', "w") as file_:
            file_.write(color_table)
        return
    
    def save_constants_table(self, path:str, constants_table:str)-> None:
        with open(f'{path}/constants_table.csv', "w") as file_:
            file_.write(constants_table)
        returng