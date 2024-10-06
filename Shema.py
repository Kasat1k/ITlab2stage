class Schema:
    def __init__(self):
        self.fields = []

    def add_field(self, field):
        self.fields.append(field)

    def validate(self, data):
        if len(data) != len(self.fields):
            return False
        return all(field.validate(value) for field, value in zip(self.fields, data))