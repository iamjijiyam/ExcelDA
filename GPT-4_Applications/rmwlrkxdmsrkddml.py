import tkinter as tk
from tkinter import ttk

class EmployeePayrollManagement:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Payroll Management")

        # List to store employee details (name, salary, designation)
        self.employee_list = []

        # Create labels and entry widgets to input employee details
        # ... (unchanged code)

        # Add Employee button
        # ... (unchanged code)

        # Output button
        self.btn_output = tk.Button(root, text="Output", command=self.show_table)
        self.btn_output.grid(row=4, column=0, columnspan=2, padx=5, pady=10)

        # Create a treeview widget to display data in a table
        self.table = ttk.Treeview(root, columns=("Name", "Salary", "Designation"))
        self.table.heading("#1", text="Name")
        self.table.heading("#2", text="Salary")
        self.table.heading("#3", text="Designation")
        self.table.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

    # ... (unchanged code for add_employee and calculate_average_salary methods)

    def calculate_total_salary(self):
        total_salary = sum(int(salary) for _, salary, _ in self.employee_list)
        return total_salary

    def show_table(self):
        # Clear the table before displaying new data
        for row in self.table.get_children():
            self.table.delete(row)

        # Calculate average and total salary
        average_salary = self.calculate_average_salary()
        total_salary = self.calculate_total_salary()

        # Insert data into the table
        for i, (name, salary, designation) in enumerate(self.employee_list, start=1):
            self.table.insert("", "end", text=str(i), values=(name, salary, designation))

        # Insert the average salary row
        self.table.insert("", "end", text="Average Salary", values=("", f"{average_salary:.2f}", ""))

        # Insert the total salary row
        self.table.insert("", "end", text="Total Salary", values=("", f"{total_salary:.2f}", ""))

if __name__ == "__main__":
    root = tk.Tk()
    employee_payroll = EmployeePayrollManagement(root)
    root.mainloop()

