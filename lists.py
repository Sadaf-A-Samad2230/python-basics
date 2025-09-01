# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

# =============================================
# Lists are used to store multiple items in a single variable.
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)


# List items are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list1 = ["abc", 34, True, 40, "male"]

thislist = list(("apple", "banana", "cherry")) # list constructor
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

# ==================================================
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:     # checking if "apple" is present in the list
  print("Yes, 'apple' is in the fruits list")

# =====================================
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant" # changing the value of the second item
print(thislist)

# ==============================
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]  #changing the range of item values
print(thislist)

# ===============================================
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")    # inserting an item at the specified index
print(thislist)

# =====================================
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")   #append list add new item in the end
print(thislist)

# =========================================
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)       # add items from another list use extend
print(thislist)

# =========================================
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")       #remove List item by value
print(thislist)

# =========================================
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)     #remove List item by index
print(thislist)

# ==========================================
thislist = ["apple", "banana", "cherry"]
del thislist[0]     #remove List item by index using del keyword
print(thislist)

# =========================================
thislist = ["apple", "banana", "cherry"]
del thislist        # it can also delete the list completely

# =========================================
thislist = ["apple", "banana", "cherry"]
thislist.clear()    #clear the list content
print(thislist)

# ============================================
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

# ============================================
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

# ============================================
thislist = ["apple", "banana", "cherry"]
for index, value in enumerate(thislist):
  print(index, value)

# ============================================
thislist = ["apple", "banana", "cherry"]
thislist.sort()     #sort the list alphabetically
print(thislist)

# ============================================
thislist = [100, 50, 65, 82, 23]
thislist.sort()     #sort the list numerically
print(thislist)

# ============================================
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()     #sort the list case sensitive
print(thislist)

# ============================================
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)   #sort the list ignoring case sensitivity
print(thislist)

# ============================================
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)     #sort the list in descending order
print(thislist)

# ============================================
thislist = ["apple", "banana", "cherry"]
newlist = thislist.copy()     #copy the list
print(newlist)

# ============================================
thislist = ["apple", "banana", "cherry"]
newlist = list(thislist)      #copy the list using list() method
print(newlist)

# =====================List Comprehension=======================
# newlist = [expression for item in iterable if condition == True]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

# --------------------------------
newlist = [x for x in fruits if x != "apple"]
newlist = [x if x != "banana" else "orange" for x in fruits]

# ===============================================
# List Methods
# -------------------------------
# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list