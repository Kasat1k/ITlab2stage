from Table import Table
class Database:
    def __init__(self):
        self.tables = {}

    def create_table(self, name, schema):
        if name not in self.tables:
            self.tables[name] = Table(name, schema)
            return f"Table '{name}' created."
        else:
            return f"Table '{name}' already exists."

    def get_table(self, name):
        return self.tables.get(name, None)

    def delete_table(self, name):
        if name in self.tables:
            del self.tables[name]
            return f"Table '{name}' deleted."
        else:
            return f"Table '{name}' does not exist."
    def intersect_tables(self, table1_name, table2_name):
        if table1_name in self.tables and table2_name in self.tables:
            table1 = self.tables[table1_name]
            table2 = self.tables[table2_name]
            intersected_rows = [row for row in table1.rows if row in table2.rows]
            return intersected_rows
        else:
            return None  # Or raise an error, depending on how you want to handle it
