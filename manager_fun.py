from validators import email
from Employee import Employee

def add_employee(list_employees):
    new_employee = {}
# check id validity
    id_checklist = [employee.ID for employee in list_employees]
    while True:
        try :
            id = int(input("Enter employee ID: "))
            if id in id_checklist:
                print("The ID entered is already taken")
            else:
                new_employee["ID"] = id
                break
        except:
            print('only numeric IDs are allowed')

# ID is valid so we make empty name value and validate first and last name
    name_sequence = ["first", "last"]
    new_employee["Name"] = ""
    for i in name_sequence:
        while True:
            name = input(f"Enter employee {i} name: ")
            if name.isalpha():
                name = name.capitalize()
                new_employee["Name"] += name
                if i == "first":
                    new_employee["Name"] += " "

                break
            else :
                print("Use only letters")

# validating and adding employee position
    positions = ["AI Engineer","Data Scientist",
                 "Machine Learning Engineer",
                 "Research Scientist","AI Product Manager",
                 "AI Ethics and Policy Specialist",
                 "AI Trainer"]
    print(f"Allowed Positions:{positions}")
    while True:
        position = input("Enter position :")
        if position in positions:
            new_employee["Position"] = position
            break
        else:
            print("The position entered is not allowed")

# validating and adding Salary
    while True:
        try:
            salary = int(input("Enter salary: "))
            new_employee["Salary"] = salary
            break
        except:
            print("please enter only numeric values")

# email validation and adding
    while True:
        email_address = input("Enter email: ")
        try:
            if email(email_address):
                new_employee["Email"] = email_address
                break
            else:
                print("please enter only valid email address")
        except:
            print("please enter only valid email address")

# convert new_employee dic to object to ease adding it to csv
    employee = Employee(ID=new_employee["ID"],
                        Name=new_employee['Name'],
                        Position=new_employee['Position'],
                        Salary=new_employee['Salary'],
                        Email=new_employee['Email'], )
    list_employees.append(employee)

def remove_employee(list_employees):
    id_checklist = [employee.ID for employee in list_employees]
    while True:
        try:
            id = int(input("Enter the ID of the employee to be removed: "))
            if id in id_checklist:
                list_employees.pop(id_checklist.index(id))
                break
            else:
                print(f"Employee {id} does not exist")

        except ValueError:
            print('Only numeric IDs are allowed')

def update_field(list_employees):
    id_checklist = [employee.ID for employee in list_employees]
    while True:
        try:
            id = int(input("Enter the ID of the employee: "))
            if id in id_checklist:
                employee = next(emp for emp in list_employees if emp.ID == id)
                field = input("Enter the name of the field to update: ").capitalize()
                if field == "Name":
                    name_sequence = ["first", "last"]
                    new_name = {"Name": ""}
                    for i in name_sequence:
                        while True:
                            name_part = input(f"Enter employee {i} name: ")
                            if name_part.isalpha():
                                name_part = name_part.capitalize()
                                new_name["Name"] += name_part
                                if i == "first":
                                    new_name["Name"] += " "
                                break
                            else:
                                print("Use only letters")
                    employee.update_information(new_name)

                elif  field == "Position":
                    new_position = {}
                    positions = ["AI Engineer", "Data Scientist",
                                 "Machine Learning Engineer",
                                 "Research Scientist", "AI Product Manager",
                                 "AI Ethics and Policy Specialist",
                                 "AI Trainer"]
                    print(f"Allowed Positions:{positions}")
                    while True:
                        position = input("Enter position :")
                        if position in positions:
                            new_position["Position"] = position
                            break
                        else:
                            print("The position entered is not allowed")
                    employee.update_information(new_position)

                elif field == "Salary":
                    new_salary = {}
                    while True:
                        try:
                            salary = int(input("Enter salary: "))
                            new_salary["Salary"] = salary
                            break
                        except ValueError:  # Catch specific exceptions
                            print("Please enter only numeric values.")
                    employee.update_information(new_salary)

                elif field == "Email":
                    new_email = {}
                    while True:
                        email_address = input("Enter email: ")
                        try:
                            if email(email_address):
                                new_email["Email"] = email_address
                                break
                            else:
                                print("please enter only valid email address")
                        except:
                            print("please enter only valid email address")
                    employee.update_information(new_email)

                else:
                    print("There is no field with that name")
                break
            else:
                print(f"Employee {id} does not exist")
        except ValueError:
            print('Only numeric IDs are allowed')






