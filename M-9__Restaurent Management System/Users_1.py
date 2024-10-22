# Admin
# Customer
# Employee

from abc import ABC

class User(ABC):
    def __init__(self, name, phone, email, address):
        self.name=name
        self.phone=phone
        self.email=email
        self.address=address

class Employee(User):
    def __init__(self, name, phone, email, address, age, designation, salary):
        super().__init__(name, phone, email, address)
        self.age=age
        self.designation=designation
        self.salary=salary

class Admin(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.employees = []  #like a database of employees

    def add_employee(self, name, phone, email, address, age, designation, salary):

        #created a object of "Employee" class.
        employee = Employee( name, phone, email, address, age, designation, salary)

        self.employees.append(employee)
        print(f'{employee.name} is added.')

    def view_employee(self):
        print("Employees list : ")

        for emp in self.employees:
            print(emp.name, emp.phone, emp.email, emp.address, emp.age, emp.designation, emp.salary)
            
ad=Admin("Soumik", 1521758831, "soumik.hasan.smk@gmail.com", "Rangpur")
ad.add_employee("Sagor", 17612786, "sagor@gmail.com", "Dhaka", 24, "shape", 12000 )
ad.view_employee()