class Employee:
    company = 'sopra steria'
    def getSalary(self):
        print(f"Salary of employee working in {self.company} is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning sir")

obj = Employee()
obj.salary = 10000
obj.getSalary()
obj.greet()