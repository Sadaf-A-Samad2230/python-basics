def my_function():
  print("Hello from a function")

my_function()

# =====================================
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

# ====================================
# Arbitrary Arguments, *args is used to pass a variable number of arguments to a function.
# Note that the name *args is just a convention. You can use any name, but the asterisk is required.
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

# ====================================
# Keyword Arguments
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# ====================================
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

# ====================================
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)

# =====================Lambda Functions==================
# A lambda function is a small anonymous function.

# A lambda function can take any number of arguments, but can only have one expression.

x = lambda a : a + 10
print(x(5))

# ================================================
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))