class Employee:
    company = 'sopra steria'

    def __init__(self, name, salary, subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("Employee is created!")

    def getDetails(self):
        print(f"The name of employee is {self.name}")
        print(f"The salary of employee is {self.salary}")
        print(f"The subunit of the employee is {self.subunit}")


obj = Employee("harsh", 100, "Youtube")
obj.getDetails()
