import tkinter as tk
from tkinter import  messagebox, Toplevel, Label, Button, messagebox,  Listbox, END

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
def show_intersect_dialog(self):
        intersect_window = Toplevel(self.master)
        intersect_window.title("Виберіть таблиці для перетину")

        label = Label(intersect_window, text="Виберіть дві таблиці для перетину:")
        label.pack(pady=10)

        intersect_listbox = Listbox(intersect_window, selectmode='multiple', height=10, width=50)
        for table_name in self.db.tables.keys():
            intersect_listbox.insert(END, table_name)
        intersect_listbox.pack(pady=10)

        intersect_button = Button(intersect_window, text="Перетнути", command=lambda: intersect_tables(self, intersect_listbox, intersect_window))
        intersect_button.pack(pady=10)
