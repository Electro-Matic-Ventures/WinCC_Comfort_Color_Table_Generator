from Color import Color


class ConstantsTableRowWriter:

    def __init__(self):
        return
    
    def make_name(
        self, 
        flash_state: bool, 
        background: Color, 
        foreground: Color
    ):
        name = ''
        if flash_state:
            name += 'FLASH_'
        name += f'{background.name.upper()}'
        name += '_'
        name += f'{foreground.name.upper()}'
        return name
    
    def write(self, name: str, table: str, data_type: str, value: str, comment: str)-> str:
        return f'{name}\t{table}\t{data_type}\t{value}\t{comment}\n'