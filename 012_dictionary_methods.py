myDict = {
    "name": "harsh",
    "age": 28,
    "marks": [1,2,3],
    "anotherDict": {'harsh': '28'},
    1 : 2
}

# Dictionary methods
print(myDict.keys())
print(list(myDict.keys())) # print the list of keys
print(myDict.values()) # print the values of dictionary
print(myDict.items()) # print the (key, value) of the dictionary
print(myDict)
updateDict = {
    "name": "harsh joshi", # also update existing values of keys
    "role": "software engineer",
    "relationship": "single"
}
myDict.update(updateDict) # update the dictionary by adding key-value pairs from updateDict 
print(myDict)

# difference between .get and [] syntax in dictionaries
print(myDict.get("harshhhhh")) # return none as harshhhhh is not present in dictionary
print(myDict["harshhhhh"]) # throws an error as harshhhhh is not present in dictionary
