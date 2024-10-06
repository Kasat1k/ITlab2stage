
import pickle
from tkinter import  messagebox , filedialog
from tablesOperations import update_tables_list

def load_database(self):
        filename = filedialog.askopenfilename(filetypes=[("Database files", "*.db")])
        if filename:
            with open(filename, 'rb') as f:
                self.db = pickle.load(f)
            messagebox.showinfo("Завантаження бази даних", "Базу даних завантажено успішно.")
            update_tables_list(self)

def save_database(self):
    filename = filedialog.asksaveasfilename(defaultextension=".db", filetypes=[("Database files", "*.db")])
    if filename:
        with open(filename, 'wb') as f:
            pickle.dump(self.db, f)
        messagebox.showinfo("Збереження бази даних", "Базу даних збережено успішно.")
