from Employee import *
from Manager import *
from CSV import *
from manager_fun import  *

def cli():
    while True:
        try:
            file_name = input("Enter file name: ")
            manager = EmployeeManager(file_name)
            break
        except:
            print("Invalid file name")

    while True:
        print("Welcome to Employee Management")
        print("1. Add Employee")
        print("2. List all employees")
        print("3. Show an employee")
        print("4. Remove an employee")
        print("5. Update information about an employee")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            manager.add_employee()
            print("\n")
        elif choice == "2":
            manager.display_all_employees()
            print("\n")
        elif choice == "3":
            manager.display_specific_employee()
            print("\n")
        elif choice == "4":
            manager.remove_employee()
            print("\n")
        elif choice == "5":
            manager.update_employee()
        elif choice == "6":
            print("Exiting CLI. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

cli()
