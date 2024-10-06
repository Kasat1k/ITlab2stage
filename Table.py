
class Table:
    def __init__(self, name, schema):
        self.name = name
        self.schema = schema
        self.rows = []

    def add_row(self, data):
        if self.schema.validate(data):
            self.rows.append(data)
            return "Row added successfully."
        else:
            return "Invalid data. Row not added."

    def display_rows(self):
        return self.rows

    def edit_row(self, index, new_data):
        if index < len(self.rows) and self.schema.validate(new_data):
            self.rows[index] = new_data
            return f"Row {index} updated successfully."
        else:
            return "Invalid data or index. Row not updated."