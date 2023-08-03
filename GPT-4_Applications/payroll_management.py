import tkinter as tk
from tkinter import ttk

class EmployeePayrollManagement:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Payroll Management")

        # List to store employee details (name, salary, designation)
        self.employee_list = []

        # Create labels and entry widgets to input employee details
        self.lbl_name = tk.Label(root, text="Name:")
        self.lbl_name.grid(row=0, column=0, padx=5, pady=5)
        self.ent_name = tk.Entry(root)
        self.ent_name.grid(row=0, column=1, padx=5, pady=5)

        self.lbl_salary = tk.Label(root, text="Salary:")
        self.lbl_salary.grid(row=1, column=0, padx=5, pady=5)
        self.ent_salary = tk.Entry(root)
        self.ent_salary.grid(row=1, column=1, padx=5, pady=5)

        self.lbl_designation = tk.Label(root, text="Designation:")
        self.lbl_designation.grid(row=2, column=0, padx=5, pady=5)
        self.ent_designation = tk.Entry(root)
        self.ent_designation.grid(row=2, column=1, padx=5, pady=5)

        # Add Employee button
        self.btn_add_employee = tk.Button(root, text="Add Employee", command=self.add_employee)
        self.btn_add_employee.grid(row=3, column=0, columnspan=2, padx=5, pady=10)

        # Output button
        self.btn_output = tk.Button(root, text="Output", command=self.show_table)
        self.btn_output.grid(row=4, column=0, columnspan=2, padx=5, pady=10)

    def add_employee(self):
        name = self.ent_name.get()
        salary = self.ent_salary.get()
        designation = self.ent_designation.get()

        # Validate input
        if name and salary and designation:
            self.employee_list.append((name, salary, designation))
            self.ent_name.delete(0, tk.END)
            self.ent_salary.delete(0, tk.END)
            self.ent_designation.delete(0, tk.END)
            print("Employee added successfully.")
        else:
            print("Please enter all details.")

    def show_table(self):
        # Create a new window to display the table
        output_window = tk.Toplevel(self.root)
        output_window.title("Employee Payroll Table")

        # Create a treeview widget to display data in a table
        table = ttk.Treeview(output_window, columns=("Name", "Salary", "Designation"))
        table.heading("#1", text="Name")
        table.heading("#2", text="Salary")
        table.heading("#3", text="Designation")
        table.grid(row=0, column=0, padx=5, pady=5)

        # Insert data into the table
        for i, (name, salary, designation) in enumerate(self.employee_list, start=1):
            table.insert("", "end", text=str(i), values=(name, salary, designation))

if __name__ == "__main__":
    root = tk.Tk()
    employee_payroll = EmployeePayrollManagement(root)
    root.mainloop() #ㅂㅇ