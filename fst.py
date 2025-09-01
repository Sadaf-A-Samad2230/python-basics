print("Hello Python")
# Python Comments
"""
It is a multi-line comment
"""

#Python variables

"""
Python has the following data types built-in by default, in these categories:

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""


x = 5
y = "John"
print(x)
print(y)
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
print(type(x))
print(type(y))
print(type(10.5))
print(type(True))
print(type(3+5j))
print(type(None))
print(type([1, 2, 3]))
print(type((1, 2, 3)))
print(type({"name": "John", "age": 30}))
print(type({1, 2, 3}))
print(type(range(5)))
print(type(b"Hello"))
print(type(bytearray(5)))

#Python allows you to extract the values into variables

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)