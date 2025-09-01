# we can use 3 double qutes or 3 single quotes for multi-line strings
# Note: in the result, the line breaks are inserted at the same position as in the code.

my_string = """Hello, World!
This is a multi-line string.
It can span multiple lines."""

print(my_string)
another_string = '''This is another way
to create a multi-line string.
It also spans multiple lines.'''
print(another_string)

# we can use single or double quotes for single-line strings
single_line_string1 = "Hello, World!"
single_line_string2 = 'Hello, World!'
print(single_line_string1)
print(single_line_string2)

# we can loop through the characters in a string
for x in "banana":
  print(x)

# we can check the length of a string using len() function
print(len("Hello, World!"))

# we can check if a substring exists in a string using 'in' keyword
txt = "The best things in life are free!"
print("free" in txt)

# we can use 'not in' to check if a substring does not exist in a string
txt = "The best things in life are free!"
print("expensive" not in txt)

# we can use 'if' statement to check for a substring in a string
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

# we can use slicing to get a substring from a string
b = "Hello, World!"
print(b[2:5])  # prints 'llo'

# we can use negative indexing to slice a string from the end
b = "Hello, World!"
print(b[-5:-2])  # prints 'orl'

# we can use various string methods to manipulate strings
a = " Hello, World! "
print(a.strip())  # removes whitespace from the beginning and end   

print(a.lower())  # converts to lowercase
print(a.upper())  # converts to uppercase
print(a.replace("H", "J"))  # replaces 'H' with 'J'
print(a.split(","))  # splits the string into a list at each comma  
print(a.split(" "))  # splits the string into a list at each space
print(a.split("o"))  # splits the string into a list at each 'o'

age = 36
txt = f"My name is John, I am {age}"
print(txt)  # using f-string for formatting

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)  # formats price to 2 decimal places


    # ============================

    # Method	Description
    # ---------------------------------------------------
    # capitalize()	Converts the first character to upper case
    # casefold()	Converts string into lower case
    # center()	Returns a centered string
    # count()	Returns the number of times a specified value occurs in a string
    # encode()	Returns an encoded version of the string
    # endswith()	Returns true if the string ends with the specified value
    # expandtabs()	Sets the tab size of the string
    # find()	Searches the string for a specified value and returns the position of where it was found
    # format()	Formats specified values in a string
    # format_map()	Formats specified values in a string
    # index()	Searches the string for a specified value and returns the position of where it was found
    # isalnum()	Returns True if all characters in the string are alphanumeric
    # isalpha()	Returns True if all characters in the string are in the alphabet
    # isascii()	Returns True if all characters in the string are ascii characters
    # isdecimal()	Returns True if all characters in the string are decimals
    # isdigit()	Returns True if all characters in the string are digits
    # isidentifier()	Returns True if the string is an identifier
    # islower()	Returns True if all characters in the string are lower case
    # isnumeric()	Returns True if all characters in the string are numeric
    # isprintable()	Returns True if all characters in the string are printable
    # isspace()	Returns True if all characters in the string are whitespaces
    # istitle()	Returns True if the string follows the rules of a title
    # isupper()	Returns True if all characters in the string are upper case
    # join()	Joins the elements of an iterable to the end of the string
    # ljust()	Returns a left justified version of the string
    # lower()	Converts a string into lower case
    # lstrip()	Returns a left trim version of the string
    # maketrans()	Returns a translation table to be used in translations
    # partition()	Returns a tuple where the string is parted into three parts
    # replace()	Returns a string where a specified value is replaced with a specified value
    # rfind()	Searches the string for a specified value and returns the last position of where it was found
    # rindex()	Searches the string for a specified value and returns the last position of where it was found
    # rjust()	Returns a right justified version of the string
    # rpartition()	Returns a tuple where the string is parted into three parts
    # rsplit()	Splits the string at the specified separator, and returns a list
    # rstrip()	Returns a right trim version of the string
    # split()	Splits the string at the specified separator, and returns a list
    # splitlines()	Splits the string at line breaks and returns a list
    # startswith()	Returns true if the string starts with the specified value
    # strip()	Returns a trimmed version of the string
    # swapcase()	Swaps cases, lower case becomes upper case and vice versa
    # title()	Converts the first character of each word to upper case
    # translate()	Returns a translated string
    # upper()	Converts a string into upper case
    # zfill()	Fills the string with a specified number of 0 values at the beginning
    # ============================