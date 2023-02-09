class IntValidationResult:
    
    fixed_value: int
    is_valid: bool
    
    def __init__(self, fixed_value:str, is_valid:bool):
        self.fixed_value = fixed_value
        self.is_valid = is_valid