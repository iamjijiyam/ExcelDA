import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import pandas as pd

def import_csv():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if file_path:
        df = pd.read_csv(file_path)
        display_data(df)

def display_data(data_frame):
    for widget in frame.winfo_children():
        widget.destroy()

    table = ttk.Treeview(frame, columns=list(data_frame.columns), show="headings")
    for column in data_frame.columns:
        table.heading(column, text=column)
    table.pack()

    for index, row in data_frame.iterrows():
        table.insert("", "end", values=list(row))

def add_salary():
    selected_item = table.selection()
    if selected_item:
        salary = salary_entry.get()
        if salary.isdigit():
            selected_index = table.index(selected_item)
            table.set(selected_item, "#2", salary)
        else:
            # Handle invalid input (non-numeric salary)
            pass

root = tk.Tk()
root.title("Payroll Management Program")

frame = ttk.Frame(root)
frame.pack(pady=10)

import_button = ttk.Button(frame, text="Import CSV", command=import_csv)
import_button.pack(side=tk.LEFT, padx=5)

filedialog = filedialog

table = ttk.Treeview(frame)
table.pack()

salary_entry = ttk.Entry(root)
salary_entry.pack(pady=10)

add_salary_button = ttk.Button(root, text="Add Salary", command=add_salary)
add_salary_button.pack()

root.mainloop()
