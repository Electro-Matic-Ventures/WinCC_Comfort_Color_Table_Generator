from PyQt6.QtGui import QIntValidator, QValidator
import re

class IntValidator(QIntValidator):
    
    def validate(self, value:str, pos:int):
        pattern = '[^0-9]+'
        value = re.sub(pattern, "", value)
        if value == '':
            return self.State.Intermediate, value, pos
        if int(value) < self.bottom():
            return self.State.Invalid, value, pos
        if int(value) > self.top():
            return self.State.Invalid, value, pos
        return self.State.Acceptable, value, pos