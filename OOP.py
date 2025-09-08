class Person:
  def __init__(self, name, age):    # constructor
    self.name = name
    self.age = age

  def __str__(self):    # toString method
    return f"{self.name}({self.age})"
  
  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)     # create object

print(p1)
p1.myfunc()                  # call method

# ===============================
# Delete the age property from the p1 object:
del p1.age

# Delete the p1 object:
del p1

# =========================================
class Person:
  pass               # empty class definition