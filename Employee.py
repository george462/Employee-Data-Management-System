class Employee:
    def __init__(self, ID, Name, Position, Salary, Email):
        self.ID = int(ID)
        self.Name = Name
        self.Position = Position
        self.Salary = int(Salary)
        self.Email = Email

    def display_employee(self):
        return f"|ID: {self.ID} |Name: {self.Name} |Position: {self.Position} |Salary: {self.Salary} |Email: {self.Email}|"

    def update_information(self,s):
        for key, value in s.items():
            if hasattr(self, key):
                setattr(self, key, value)

