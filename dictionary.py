# Dictionary
# Dictionaries are used to store data values in key:value pairs.

# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

# Dictionaries are written with curly brackets, and have keys and values:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

print(thisdict["brand"])

# ======================================
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

# ==========================================
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

# ======================================
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]   # Returns the value of the "model" key

x = thisdict.get("model")   # Returns the value of the "model" key
print(x)

x = thisdict.keys()  # Returns a list of all the keys in the dictionary

# ===================================
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change

x = thisdict.values()  # Returns a list of all the values in the dictionary
print(x)

# =====================================
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

# ==================================
# Update the "year" of the car by using the update() method:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

# The pop() method removes the item with the specified key name:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

thisdict.popitem()  # removes the last inserted item
print(thisdict)

del thisdict["model"]   # removes the item with the specified key name
print(thisdict)

thisdict.clear()   # removes all the elements from the dictionary
print(thisdict)

del thisdict   # deletes the dictionary completely
# print(thisdict)  # this will raise an error because the dictionary no longer exists

# ====================================
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
for x in thisdict:
    print(x)   # prints all the keys
for x in thisdict:
    print(thisdict[x])   # prints all the values
for x in thisdict.values():
    print(x)   # prints all the values
for x in thisdict.keys():
    print(x)   # prints all the keys
for x, y in thisdict.items():
    print(x, y)   # prints all the key-value pairs

# ====================================
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
mydict = thisdict.copy()   # creates a copy of the dictionary
print(mydict)

mydict = dict(thisdict)   # creates a copy of the dictionary
print(mydict)

# ====================================
# Create three dictionaries, then create one dictionary that will contain the other three dictionaries:

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily["child2"]["name"])

# ====================================

for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])