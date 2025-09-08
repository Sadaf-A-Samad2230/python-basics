# File Handling
# The key function for working with files in Python is the open() function.

# The open() function takes two parameters; filename, and mode.

# There are four different methods (modes) for opening a file:

# "r" - Read - Default value. Opens a file for reading, error if the file does not exist

# "a" - Append - Opens a file for appending, creates the file if it does not exist

# "w" - Write - Opens a file for writing, creates the file if it does not exist

# "x" - Create - Creates the specified file, returns an error if the file exists

# In addition you can specify if the file should be handled as binary or text mode

# "t" - Text - Default value. Text mode

# "b" - Binary - Binary mode (e.g. images)

# ====================================================
# Example
# Open a file
f = open("demofile.txt")
f = open("demofile.txt", "rt")
# Because "r" for read, and "t" for text are the default values, you do not need to specify them.

# ====================================================
# Read a file
# The read() method reads the entire file, and returns it as a string
f = open("demofile.txt", "r")
print(f.read())
f.close()
# It is a good practice to always close the file when you are done with it.
# You can also use the with keyword when opening a file. Using with is a good practice
# ---------------------------------------------
# because it automatically takes care of closing the file for you when you are done with it.
with open("demofile.txt", "r") as f:
    print(f.read())

# ====================================================
# Read only parts of the file
# By default the read() method returns the whole text, but you can also specify how many characters you want to return:
f = open("demofile.txt", "r")   
print(f.read(5))
# This will return the first 5 characters of the file
f.close()
# ====================================================
# Read one line of the file
f = open("demofile.txt", "r")
print(f.readline())
# This will return one line of the file
f.close()
# ====================================================
# Read two lines of the file
f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())
# This will return the first two lines of the file
f.close()
# ====================================================
# Loop through the file line by line
f = open("demofile.txt", "r")   
for x in f:
    print(x)
# This will print each line one by one
f.close()
# ====================================================
with open("demofile.txt", "a") as f:
  f.write("Now the file has more content!")

#open and read the file after the appending:
with open("demofile.txt") as f:
  print(f.read())
#   ===================================================
# Write to an existing file
# To write to an existing file, you must add a parameter to the open() function:
f = open("demofile.txt", "a")  # Append to an existing file
f.write("Now the file has more content!")
f.close()
# ====================================================
# Open the file "demofile.txt" and overwrite the content:

with open("demofile.txt", "w") as f:
  f.write("Woops! I have deleted the content!")

#open and read the file after the overwriting:
with open("demofile.txt") as f:
  print(f.read())
# ====================================================
# Create a new file
# To create a new file in Python, use the open() method, with one of the following parameters:
f = open("myfile.txt", "x")  # Create a file
f = open("myfile.txt", "w")  # Create a file or overwrite if it exists
# ====================================================
# Write to a file
f = open("myfile.txt", "w")
f.write("Hello! Welcome to my world!")
f.close()
# ====================================================
# Delete a file
import os
os.remove("myfile.txt")
# ====================================================
# Check if file exists, then delete it
import os
if os.path.exists("myfile.txt"):
    os.remove("myfile.txt")
else:
    print("The file does not exist")
# ====================================================
# Create a directory
import os
os.mkdir("myfolder")
# ====================================================
# Remove a directory
import os
os.rmdir("myfolder")
# Note: You can only remove empty folders
# ====================================================
# Check if folder exists, then remove it
import os
if os.path.exists("myfolder"):
    os.rmdir("myfolder")
else:
    print("The folder does not exist")
# Note: You can only remove empty folders
# ====================================================
# Get the list of files in a directory
import os
print(os.listdir())
# Note: You can specify the path to list files in other directories, e.g. os
# .listdir("c:/")  # List files and directories in C:/ drive
# ====================================================
# Get the current working directory
import os
print(os.getcwd())
# ====================================================
# Change the current working directory
import os   
os.chdir("C:/")
# Note: Change the C:/ to the directory you want to switch to
print(os.getcwd())
# ====================================================
# Get the file size
import os
print(os.path.getsize("demofile.txt"))
# ====================================================
# Rename a file
import os
os.rename("demofile.txt", "myfile.txt")
# ====================================================
# Split the file path   
import os
print(os.path.split("C:/Users/Username/demofile.txt"))
# Note: Change the C:/Users/Username/demofile.txt to the file path you want to use
# ====================================================
# Get the file extension
import os
print(os.path.splitext("demofile.txt"))
# ====================================================
# Get the file name
import os   
print(os.path.basename("C:/Users/Username/demofile.txt"))
# Note: Change the C:/Users/Username/demofile.txt to the file path you
# want to use
# ====================================================  
# Get the directory name    
import os
print(os.path.dirname("C:/Users/Username/demofile.txt"))
# Note: Change the C:/Users/Username/demofile.txt to the file path you want to use
# ====================================================
