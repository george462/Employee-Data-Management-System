from Employee import Employee
from CSV import read_csv,save2csv
from manager_fun import add_employee, remove_employee, update_field

class EmployeeManager:
    def __init__(self, file_name):
        self.file_name = file_name
        self.list_employees = read_csv(self.file_name)

    def display_all_employees(self):
        print("\n")
        for employee in self.list_employees: # display every employee in the list
            print(employee.display_employee())
        print("")

    def display_specific_employee(self):
        id = int(input("Enter employee id: "))
        for employee in self.list_employees:
            if employee.ID == id:
                print(employee.display_employee())

    def add_employee(self):
        add_employee(self.list_employees)
        save2csv(self.file_name, self.list_employees)
        print("Employee added successfully")

    def remove_employee(self):
        if len(self.list_employees) > 1:
            remove_employee(self.list_employees)
            save2csv(self.file_name, self.list_employees)
            print("Employee removed successfully")
        else:
            print("There is only one employee , So the process will not be done")

    def update_employee(self):
        update_field(self.list_employees)
        save2csv(self.file_name, self.list_employees)

