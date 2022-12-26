#  OOP

class Employee:
    def __init__(self, name, salary): #constructor
        self.name = name
        self.salary = salary
    def showData(self):
        print('{0} earns {1}'.format(self.name, self.salary))
    def updateData(self, salary):
        self.salary = salary
        print("Your updated salary is : "+str(salary))
        
class Manager(Employee):
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department
    def showData(self):
        print('{0} earns {1} and works in {2}'.format(self.name, self.salary, self.department))

John = Employee("john", 60000.00)
print(type(John))
print(John)
John.showData()

Jane = Manager("jane", 60000.00, "Support")
Jane.showData()
Jane.updateData(75000.00)
