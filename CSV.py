import csv
from Employee import Employee

def read_csv(file_name):
    with open(file_name) as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        list_employees = []
        for emp in csv_reader:
            employee = Employee(ID=emp['ID'],
                                Name=emp['Name'],
                                Position=emp['Position'],
                                Salary=emp['Salary'],
                                Email=emp['Email'])
            list_employees.append(employee)
    return list_employees

def save2csv(file_name,list_employees):
    added_list = []
    for employee in list_employees:
        employee = employee.__dict__
        added_list.append(employee)
    keys = added_list[0].keys()
    with open(file_name, 'w', newline='') as csv_file:
        dict_writer = csv.DictWriter(csv_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(added_list)