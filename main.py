import tkinter as tk
from tkinter import simpledialog, messagebox, Toplevel, Label, Entry, Button, simpledialog, messagebox, filedialog, Listbox, END
import pickle

def create_table(self):
        table_name = self.table_name_entry.get()
        if table_name:
            schema = Schema()
            schema.add_field(Field("ID", int))
            schema.add_field(Field("Name", str))
            message = self.db.create_table(table_name, schema)
            messagebox.showinfo("Create Table", message)
            self.table = self.db.get_table(table_name)

def add_row(self):
        if self.table:
            id = simpledialog.askinteger("Input", "Enter ID")
            name = simpledialog.askstring("Input", "Enter Name")
            message = self.table.add_row([id, name])
            messagebox.showinfo("Add Row", message)
        else:
            messagebox.showerror("Error", "No table selected or created yet.")

def show_table(self):
        if self.table:
            rows = self.table.display_rows()
            self.text.delete(1.0, tk.END)
            for row in rows:
                self.text.insert(tk.END, str(row) + '\n')
        else:
            messagebox.showerror("Error", "No table selected or created yet.")

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


# Функції для збереження та завантаження
def save_database(db, filename):
    with open(filename, 'wb') as f:
        pickle.dump(db, f)
    print("Database saved to disk.")

def load_database(filename):
    with open(filename, 'rb') as f:
        db = pickle.load(f)
    print("Database loaded from disk.")
    return db


class Schema:
    def __init__(self):
        self.fields = []

    def add_field(self, field):
        self.fields.append(field)

    def validate(self, data):
        if len(data) != len(self.fields):
            return False
        return all(field.validate(value) for field, value in zip(self.fields, data))

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

class App:
    def __init__(self, master):
        self.master = master
        self.db = Database()
        self.table = None

        master.title("Система Управління Базами Даних")

        self.label = tk.Label(master, text="Введіть назву таблиці:")
        self.label.pack()

        self.table_name_entry = tk.Entry(master)
        self.table_name_entry.pack()

        self.create_table_button = tk.Button(master, text="Створити таблицю з ID та назвою", command=self.create_table)
        self.create_table_button.pack()

        self.add_row_button = tk.Button(master, text="Додати рядок", command=self.add_row)
        self.add_row_button.pack()

        self.edit_row_button = tk.Button(master, text="Редагувати рядок", command=self.edit_row)
        self.edit_row_button.pack()

        self.delete_table_button = tk.Button(master, text="Видалити таблицю", command=self.delete_table)
        self.delete_table_button.pack()

        self.save_db_button = tk.Button(master, text="Зберегти базу даних", command=self.save_database)
        self.save_db_button.pack()

        self.load_db_button = tk.Button(master, text="Завантажити базу даних", command=self.load_database)
        self.load_db_button.pack()

        self.show_table_button = tk.Button(master, text="Показати таблицю", command=self.show_table)
        self.show_table_button.pack()

        self.intersect_tables_button = tk.Button(master, text="Перетин таблиць", command=self.show_intersect_dialog)
        self.intersect_tables_button.pack()

        self.tables_list_label = tk.Label(master, text="Доступні таблиці:")
        self.tables_list_label.pack()

        self.tables_listbox = tk.Listbox(master, height=10, width=50)
        self.tables_listbox.bind('<<ListboxSelect>>', self.on_table_select)
        self.tables_listbox.pack()

        self.text = tk.Text(master, height=10, width=50)
        self.text.pack()

        self.update_tables_list()

    def on_table_select(self, event):
        selection = self.tables_listbox.curselection()
        if selection:
            self.table = self.db.get_table(self.tables_listbox.get(selection[0]))

    def create_table(self):
        table_name = self.table_name_entry.get()
        if table_name:
            schema = Schema()
            schema.add_field(Field("ID", int))
            schema.add_field(Field("Name", str))
            message = self.db.create_table(table_name, schema)
            messagebox.showinfo("Створення таблиці", message)
            self.update_tables_list()

    def add_row(self):
        if self.table:
            id = simpledialog.askinteger("Input", "Введіть ID")
            name = simpledialog.askstring("Input", "Введіть ім'я")
            message = self.table.add_row([id, name])
            messagebox.showinfo("Додавання рядка", message)
        else:
            messagebox.showerror("Помилка", "Таблиця не вибрана.")

    def edit_row(self):
        if self.table:
            self.selected_row_index = simpledialog.askinteger("Input", "Введіть номер рядка для редагування (з нуля)")
            if self.selected_row_index is not None and 0 <= self.selected_row_index < len(self.table.rows):
                id = simpledialog.askinteger("Input", "Введіть новий ID")
                name = simpledialog.askstring("Input", "Введіть нове ім'я")
                message = self.table.edit_row(self.selected_row_index, [id, name])
                messagebox.showinfo("Редагування рядка", message)
            else:
                messagebox.showerror("Помилка", "Неправильний номер рядка.")

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
            self.update_tables_list()
        else:
            messagebox.showerror("Помилка", "Таблиця не вибрана.")

    def save_database(self):
        filename = filedialog.asksaveasfilename(defaultextension=".db", filetypes=[("Database files", "*.db")])
        if filename:
            with open(filename, 'wb') as f:
                pickle.dump(self.db, f)
            messagebox.showinfo("Збереження бази даних", "Базу даних збережено успішно.")

    def load_database(self):
        filename = filedialog.askopenfilename(filetypes=[("Database files", "*.db")])
        if filename:
            with open(filename, 'rb') as f:
                self.db = pickle.load(f)
            messagebox.showinfo("Завантаження бази даних", "Базу даних завантажено успішно.")
            self.update_tables_list()

    def update_tables_list(self):
        self.tables_listbox.delete(0, END)
        for table_name in self.db.tables.keys():
            self.tables_listbox.insert(END, table_name)

    def show_intersect_dialog(self):
        intersect_window = Toplevel(self.master)
        intersect_window.title("Виберіть таблиці для перетину")

        label = Label(intersect_window, text="Виберіть дві таблиці для перетину:")
        label.pack(pady=10)

        intersect_listbox = Listbox(intersect_window, selectmode='multiple', height=10, width=50)
        for table_name in self.db.tables.keys():
            intersect_listbox.insert(END, table_name)
        intersect_listbox.pack(pady=10)

        intersect_button = Button(intersect_window, text="Перетнути", command=lambda: self.intersect_tables(intersect_listbox, intersect_window))
        intersect_button.pack(pady=10)

    def intersect_tables(self, listbox, window):
        selections = listbox.curselection()
        if len(selections) == 2:
            table1_name = listbox.get(selections[0])
            table2_name = listbox.get(selections[1])
            result = self.db.intersect_tables(table1_name, table2_name)
            if result:
                self.text.delete(1.0, tk.END)
                for row in result:
                    self.text.insert(tk.END, f"{row}\n")
                messagebox.showinfo("Результат перетину", "Таблиці успішно перетнуті. Перегляньте результати.")
                window.destroy()
            else:
                messagebox.showerror("Помилка перетину", "Помилка при перетині таблиць.")
        else:
            messagebox.showerror("Помилка вибору", "Будь ласка, виберіть рівно дві таблиці для перетину.")

root = tk.Tk()
app = App(root)
root.mainloop()
