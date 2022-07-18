class Employee:
    company = "sopra steria"
    salary = 100
    location = 'delhi'

    @classmethod
    def chanageSalary(cls, sal):
        cls.salary = sal

e = Employee()
print(e.salary)

e.chanageSalary(455)
print(e.salary)