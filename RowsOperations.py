
from tkinter import  messagebox , simpledialog
from tablesOperations import update_tables_list

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