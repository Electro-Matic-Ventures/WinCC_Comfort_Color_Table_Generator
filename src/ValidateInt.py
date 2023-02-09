from IntValidationResult import IntValidationResult


class ValidateInt:
    
    def __init__(self):
        return
    
    def is_valid(self, value:int, min_:int, max_:int)-> IntValidationResult:
        if value < min_:
            return IntValidationResult(min_, False)
        if value > max_:
            return IntValidationResult(max_, False)
        return IntValidationResult(value, True)
        