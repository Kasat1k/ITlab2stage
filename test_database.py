import unittest
from main import Database, Table, Schema, Field

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.db = Database()
        self.schema = Schema()
        self.schema.add_field(Field("ID", int))
        self.schema.add_field(Field("Name", str))

    def test_create_table(self):
        message = self.db.create_table("Users", self.schema)
        self.assertIn("created", message)
        self.assertTrue("Users" in self.db.tables)

    def test_add_row(self):
        self.db.create_table("Users", self.schema)
        result = self.db.get_table("Users").add_row([1, "John Doe"])
        self.assertIn("successfully", result)

    def test_intersect_tables(self):
        self.db.create_table("Users", self.schema)
        self.db.create_table("Admins", self.schema)
        self.db.get_table("Users").add_row([1, "John Doe"])
        self.db.get_table("Users").add_row([2, "Jane Doe"])
        self.db.get_table("Admins").add_row([1, "John Doe"])
        intersected_rows = self.db.intersect_tables("Users", "Admins")
        self.assertEqual(len(intersected_rows), 1)
        self.assertEqual(intersected_rows[0], [1, "John Doe"])

if __name__ == '__main__':
    unittest.main()
