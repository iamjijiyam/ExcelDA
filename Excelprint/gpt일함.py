import pandas as pd
import tkinter as tk
from tkinter import ttk

def load_excel_and_display(file_path):
    try:
        df = pd.read_excel(file_path)
        return df
    except Exception as e:
        print(f"Error: {e}")
        return None

def display_excel_data_in_window(data):
    window = tk.Tk()
    window.title("Excel Data Viewer")

    tree = ttk.Treeview(window)

    columns = list(data.columns)
    tree["columns"] = columns

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)

    for index, row in data.iterrows():
        tree.insert("", "end", values=tuple(row))

    tree.pack(expand=True, fill="both")

    window.mainloop()

if __name__ == "__main__":
    file_path = "singer.xlsx"  # Replace with your actual file path
    data = load_excel_and_display(file_path)

    if data is not None:
        display_excel_data_in_window(data)
