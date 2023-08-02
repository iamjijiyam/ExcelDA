import tkinter as tk
from tkinter import filedialog
import pandas as pd

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])
    if file_path:
        df = pd.read_excel(file_path)
        display_data(df)

def display_data(dataframe):
    # Clear previous contents from the text widget
    text.delete(1.0, tk.END)

    # Display the data in the text widget
    text.insert(tk.END, dataframe.to_string())

# Create the main application window
root = tk.Tk()
root.title("Excel Data Viewer")
root.geometry("800x500")

# Create the menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create the "File" menu with an "Open" option
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Exit", command=root.quit)

# Create a text widget to display the Excel data
text = tk.Text(root, wrap=tk.WORD)
text.pack(expand=True, fill="both")

# Start the Tkinter event loop
root.mainloop()

