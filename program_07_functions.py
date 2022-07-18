# a = int(input("enter the first number: "))
# b = int(input("enter the second number: "))
# c = int(input("enter the third number: "))

def largest_number(a,b,c):
    if (a>b and a>c):
        return a
    elif(b>c and b>c):
        return b
    else:
        return c

m = largest_number(3,4,5)
print(f"the largest number is {m}")
