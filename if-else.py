a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#   ===================Short Hand If===================
if a > b: print("a is greater than b")
#   ===================Short Hand If...Else===================
print("A") if a > b else print("B")

print("A") if a > b else print("=") if a == b else print("B")


# ====================And===================
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

# ====================Pass===================
if b > a:
  pass  # if statement cannot be empty, use pass to avoid error

