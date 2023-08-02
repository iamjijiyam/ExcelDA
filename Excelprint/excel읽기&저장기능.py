import tkinter as tk
from tkinter import filedialog
import pandas as pd
import io  # Add this import for StringIO

# Global variable to store the data
data_to_save = ""

# Function to open an Excel file
def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    if file_path:
        try:
            df = pd.read_excel(file_path)
            text_box.delete("1.0", tk.END)
            text_box.insert(tk.END, df.to_string())
        except Exception as e:
            text_box.delete("1.0", tk.END)
            text_box.insert(tk.END, f"Error: {str(e)}")

# Function to save the current data to a CSV file
def save_to_csv():
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if file_path:
        try:
            df = pd.read_csv(io.StringIO(data_to_save))  # Use io.StringIO here
            df.to_csv(file_path, index=False)
            text_box.delete("1.0", tk.END)
            text_box.insert(tk.END, "Data saved to CSV successfully!")
        except Exception as e:
            text_box.delete("1.0", tk.END)
            text_box.insert(tk.END, f"Error: {str(e)}")

# Function to display the data output window
def data_output_window():
    global data_to_save
    data_to_save = text_box.get("1.0", tk.END)

    output_window = tk.Toplevel()
    output_window.title("Data Output")
    output_window.geometry("500x500")

    output_text_box = tk.Text(output_window, wrap="word")
    output_text_box.pack(expand=True, fill="both")
    output_text_box.insert(tk.END, data_to_save)

    save_button = tk.Button(output_window, text="Save as CSV", command=save_to_csv)
    save_button.pack(pady=10)

# Function to create the option window
def option_window():
    option_window = tk.Toplevel()
    option_window.title("Options")
    option_window.geometry("200x100")

    save_button = tk.Button(option_window, text="Save and Exit", command=data_output_window)
    save_button.pack(pady=10)

# Create the main application window
root = tk.Tk()
root.title("Excel Reader")
root.geometry("500x500")

# Create a text box to display the Excel data
text_box = tk.Text(root, wrap="word")
text_box.pack(expand=True, fill="both")

# Create the menu bar
menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Exit", command=root.quit)

option_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Options", menu=option_menu)
option_menu.add_command(label="Save and Exit", command=option_window)

root.config(menu=menu_bar)
root.mainloop()
