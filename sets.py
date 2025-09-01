# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.   

thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)

# Once a set is created, you cannot change its items, but you can add new items.

thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)
print("banana" not in thisset)

# ===========================================
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

# ============================================
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

# =============================================
# To remove an item in a set, use the remove(), or the discard() method.
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")    #Note: If the item to remove does not exist, remove() will raise an error. where discard not

print(thisset)

# ================================================
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")
x = thisset.pop()  # removes a random item
thisset.clear()  # Empties the set
del thisset  # Deletes the set completely

print(thisset)

# ===============================================

# Join Sets
# There are several ways to join two or more sets in Python.

# The union() and update() methods joins all items from both sets.

# The intersection() method keeps ONLY the duplicates.

# The difference() method keeps the items from the first set that are not in the other set(s).

# The symmetric_difference() method keeps all items EXCEPT the duplicates.

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2) # joins both sets
print(set3)

set3 = set1 | set2  # joins both sets
print(set3)

set1.update(set2)   
print(set1)

set3 = set1.intersection(set2)  # keeps only the duplicates
print(set3)

set3 = set1 & set2  # keeps only the duplicates
print(set3)

set1.intersection_update(set2)  # keeps only the duplicates
print(set1)

set3 = set1.difference(set2)    # keeps the items from the first set that are not in the other set(s).
print(set3)

set3 = set1 - set2  # keeps the items from the first set that are not in the other set(s).
print(set3)

set1.difference_update(set2)  # keeps the items from the first set that are not in the other set(s).
print(set1)

set3 = set1.symmetric_difference(set2)  # keeps all items EXCEPT the duplicates.
print(set3)

set3 = set1 ^ set2  # keeps all items EXCEPT the duplicates.
print(set3)

set1.symmetric_difference_update(set2)  # keeps all items EXCEPT the duplicates.
print(set1)

# ================================================
# Set Methods
# Python has a set of built-in methods that you can use on sets.
# Method	Description
# add()	Adds an element to the set  
# clear()	Removes all the elements from the set
# copy()	Returns a copy of the set
# difference()	Returns a set containing the difference between two or more sets
# difference_update()	Removes the items in this set that are also included in another,
# discard()	Removes the specified item
# intersection()	Returns a set, that is the intersection of two other sets
# intersection_update()	Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	Returns whether two sets have a intersection or not
# issubset()	Returns whether another set contains this set or not
# issuperset()	Returns whether this set contains another set or not
# pop()	Removes an element from the set
# remove()	Removes the specified element
# symmetric_difference()	Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	inserts the symmetric differences from this set and another
# union()	Returns a set containing the union of sets
# update()	Update the set with the union of this set and others
# ================================================================


