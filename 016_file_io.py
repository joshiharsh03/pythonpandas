f = open('sample.txt', 'r')
# data = f.read()
data1 = f.read(5)
print(data1)
f.close()


# write in a file
f1 = open('another.txt', 'w')
f1.write("This is a python tutorial for beginners!")
f1.close()

# append in a file
f1 = open('another.txt', 'a')
f1.write("Nice tutorial!")
f1.close()