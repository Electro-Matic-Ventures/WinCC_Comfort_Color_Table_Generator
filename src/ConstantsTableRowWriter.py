class ConstantsTableRowWriter:

    def __init__(self):
        return
    
    def make_name(
        self, 
        flash_state: str, 
        background_color_name: str, 
        background_color_intensity, 
        foreground_color_name: str, 
        foreground_color_intensity: str)-> str:
        name = ''
        if flash_state != '':
            name += f'{flash_state}'
            name += '_'
        name += f'{background_color_name.upper()}{background_color_intensity + 1}'
        name += '_'
        name += f'{foreground_color_name.upper()}{foreground_color_intensity + 1}'
        return name
    
    def write(self, name: str, table: str, data_type: str, value: str, comment: str)-> str:
        _name = self.__write_cell(name)
        _table = self.__write_cell(table)
        _data_type = self.__write_cell(data_type)
        _value = self.__write_cell(value)
        _comment = self.__write_cell(value)
        return f'{_name}{_table}{_data_type}{_value}{_comment}\n'

    def __write_cell(self, value: str)-> str:
        return f'{value}\t'