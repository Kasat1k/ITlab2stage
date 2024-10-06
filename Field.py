class Field:
    def __init__(self, name, datatype):
        self.name = name
        self.datatype = datatype

    def validate(self, data):
        if self.datatype == str and len(data) == 1:  # Char type
            return True
        elif self.datatype == str:  # String type
            return isinstance(data, str)
        elif self.datatype == int:  # Integer type
            try:
                int(data)
                return True
            except ValueError:
                return False
        elif self.datatype == float:  # Real type
            try:
                float(data)
                return True
            except ValueError:
                return False
        else:
            return False