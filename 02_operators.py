import logging

# airthmetic operators 
a = 3
b = 4

print("Additon of a and b ", a+b)
print("Subtraction of a and b ", a-b)
print("Multiplication of a and b ", a*b)
print("Division of a and b ", a/b)


# assignment operators 
d = 34
d+= 12
d-= 12
d*=2
d/=2
print(d)


#comparison operators
e = (14>7)
print(e)

f = (14!=7)
print(f)

g = (14==7)
print(g)


# Logical operatots
bool1 = True
bool2 = False
print("The value of bool1 and bool2 ", bool1 and bool2)
print("The value of bool1 or bool2 ", bool1 or bool2)
print("The value of not bool2 ", not bool1)



# c = 5
# d = 0
# try:
#   e = c / d
# except Exception as e:
#   logging.ERROR("Exception occurred")
