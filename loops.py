# Python has two primitive loop commands:

# while loops
# for loops

i = 1
while i < 6:
  print(i)
  i += 1

# ===============================================
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

# ===============================================
# for loops
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

# ===============================================
for x in "banana":
  print(x)

# ===============================================
# break statement
fruits = ["apple", "banana", "cherry"]

for x in fruits:
  print(x)
  if x == "banana":
    break
  
# ===============================================
# continue statement    
fruits = ["apple", "banana", "cherry"]  
for x in fruits:
  if x == "banana":
    continue
  print(x)

# ===============================================
# range() function
for x in range(6):
  print(x)

# ===============================================
for x in range(2, 6):
  print(x)

# ===============================================
for x in range(2, 30, 3):
  print(x)

# ===============================================
# else in for loop  
for x in range(6):
  print(x)
else:
  print("Finally finished!")
