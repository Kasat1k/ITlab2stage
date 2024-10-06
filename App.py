import tkinter as tk
from intersection import show_intersect_dialog

from Database import *
from Save_Load_Database import *
from RowsOperations import *
from tablesOperations import *
class App:
    def __init__(self, master):
        self.master = master
        self.db = Database()
        self.table = None

        master.title("Система Управління Базами Даних")

        # Використовуємо grid() для розміщення елементів у сітці
        self.label = tk.Label(master, text="Введіть назву таблиці:")
        self.label.grid(row=0, column=0, padx=10, pady=5)

        self.table_name_entry = tk.Entry(master)
        self.table_name_entry.grid(row=0, column=1, padx=10, pady=5)

        self.create_table_button = tk.Button(master, text="Створити таблицю", command=lambda: create_table(self))
        self.create_table_button.grid(row=1, column=0, padx=10, pady=5)

        self.add_row_button = tk.Button(master, text="Додати рядок", command=lambda:add_row(self))
        self.add_row_button.grid(row=1, column=1, padx=10, pady=5)

        self.edit_row_button = tk.Button(master, text="Редагувати рядок", command=lambda:edit_row(self))
        self.edit_row_button.grid(row=2, column=0, padx=10, pady=5)

        self.delete_table_button = tk.Button(master, text="Видалити таблицю", command=lambda: delete_table(self))
        self.delete_table_button.grid(row=2, column=1, padx=10, pady=5)

        self.save_db_button = tk.Button(master, text="Зберегти базу даних", command=lambda: save_database(self))
        self.save_db_button.grid(row=3, column=0, padx=10, pady=5)

        self.load_db_button = tk.Button(master, text="Завантажити базу даних", command=lambda: load_database(self))
        self.load_db_button.grid(row=3, column=1, padx=10, pady=5)

        self.show_table_button = tk.Button(master, text="Показати таблицю", command=lambda: show_table(self))
        self.show_table_button.grid(row=4, column=0, padx=10, pady=5)

        self.intersect_tables_button = tk.Button(master, text="Перетин таблиць", command=lambda: show_intersect_dialog(self))
        self.intersect_tables_button.grid(row=4, column=1, padx=10, pady=5)
        # Список таблиць і текстове поле
        self.tables_list_label = tk.Label(master, text="Доступні таблиці:")
        self.tables_list_label.grid(row=5, column=0, padx=10, pady=5)

        self.tables_listbox = tk.Listbox(master, height=10, width=50)
        self.tables_listbox.bind('<<ListboxSelect>>', self.on_table_select)
        self.tables_listbox.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

        self.text = tk.Text(master, height=10, width=50)
        self.text.grid(row=7, column=0, columnspan=2, padx=10, pady=5)
        

        update_tables_list(self)
    def on_table_select(self, event):
        selection = self.tables_listbox.curselection()
        if selection:
            self.table = self.db.get_table(self.tables_listbox.get(selection[0]))
