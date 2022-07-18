class Employee:
    company = "sopra steria"

    def showDetails(self):
        print('this is an employee')

class Programmer(Employee):
    language = 'python'

    def getLang(self):
        print(f"the language of an employee is: {self.language}")

e = Employee()
p = Programmer()

e.showDetails()
p.showDetails()