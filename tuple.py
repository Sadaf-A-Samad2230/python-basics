# Tuple - is the list of constant values


tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

tuple1 = ("abc", 34, True, 40, "male")

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

# ========================================
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

# ========================================
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

# ========================================
thistuple = ("apple", "banana", "cherry")
