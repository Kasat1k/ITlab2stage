import tkinter as tk
from tkinter import  messagebox, END
from Shema import Schema
from Field import Field

def create_table(self):
        table_name = self.table_name_entry.get()
        if table_name:
            schema = Schema()
            schema.add_field(Field("ID", int))
            schema.add_field(Field("Name", str))
            message = self.db.create_table(table_name, schema)
            messagebox.showinfo("Створення таблиці", message)
            update_tables_list(self)

def show_table(self):
        if self.table:
            rows = self.table.display_rows()
            self.text.delete(1.0, tk.END)
            for i, row in enumerate(rows):
                self.text.insert(tk.END, f"Рядок {i}: {row}\n")
        else:
            messagebox.showerror("Помилка", "Таблиця не вибрана.")

def delete_table(self):
        if self.table:
            table_name = self.table.name
            self.db.delete_table(table_name)
            self.table = None
            messagebox.showinfo("Видалення таблиці", f"Таблиця '{table_name}' видалена.")
            update_tables_list(self)
        else:
            messagebox.showerror("Помилка", "Таблиця не вибрана.")

def update_tables_list(self):
        self.tables_listbox.delete(0, END)
        for table_name in self.db.tables.keys():
            self.tables_listbox.insert(END, table_name)
