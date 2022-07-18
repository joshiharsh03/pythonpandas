# program1: create a class programmer and get details of the programmer
# class Programmer:
#     company = "sopra steria"
#     def __init__(self, name, employeeCode):
#         self.name = name
#         self.employeeCode = employeeCode

#     def getInfo(self):
#         print(f"The name of the employee is {self.name} and the employee code is {self.employeeCode} ")

# harsh = Programmer("harsh", "701489")
# priya = Programmer("priya", "701456")
# harsh.getInfo()
# priya.getInfo()


# program2: create a class to find square , squareroot and cube of a number
# class Calculator:
#     def __init__(self, number):
#         self.number = number

#     def square(self):
#         print(f"the square of a {self.number} is: {self.number **2}")

#     def cube(self):
#         print(f"the cube of a {self.number} is : {self.number **3}")

#     def squareRoot(self):
#         print(f"then squareroot of a {self.number} is: {self.number ** 0.5}")

# obj = Calculator(3)
# obj.square()
# obj.cube()
# obj.squareRoot()


#Program3: create a class train and check the status
class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print("****************")
        print(f"the name of a train is: {self.name}")
        print(f"the seats available in the train is: {self.seats}")
        print("****************")
    
    def getfareInfo(self):
        print(f"the price of the ticket is: {self.fare}")

    def bookTicket(self):
        if(self.seats>0):
            print(f"Your ticket has been booked! Your seat number is: {self.seats}")
            self.seats = self.seats-1
        else:
            print("Sorry This train is full! No tickets available")

intercity = Train("Intercity Express: 1405", 90, 300)
intercity.getStatus()
intercity.bookTicket()
intercity.getStatus()
intercity.getfareInfo()