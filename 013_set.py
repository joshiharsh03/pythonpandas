# important: This syntax will create an empty dictionary and not an empty set
a = {}
print(type(a))

# An empty set will be created using below syntax
b = set()
print(type(b))

# Methods of Set
b.add(3) # adding values to the set
b.add(4)
b.add(7)
b.add((8,9,2)) # we can add tuple to sets
# b.add({4:2}) # we cannot add lists and dictionaries to sets because lists and dictionaries are unhashable. we can change the content of lists and dictionaries
print(b)

# print length of set
print(len(b))

# remove a particular element from set
b.remove(4)
print(b)