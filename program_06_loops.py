# write a program to print multiplication
# num = int(input("enter the number: "))
# for i in range(1,11):
#     print(str(num) + "X" + str(i) + "=" + str(num*i))

# program 2
# list = ["Harsh", "Sachin", "Sohan", "Sachin"]
# for name in list:
#     if name.startswith("S"):
#         print("Hello " + name)

# program 3; factoriaL
# num = int(input('enter the number: '))
# fact = 1;
# for i in range(1, num+1):
#     fact = fact*i;
# print(f"The factorial of a {num} is {fact}");


# print star pattern
# n = int(input('enter the number: '))
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print("* ", end="")
#     print()

# star pattern
n = int(input('enter the number: '))
for i in range(1, n+1):
    for j in range(n-1, i+1):
        print(end=" ")
    for k in range(1, i+1):
        print("*" , end="")
    print()