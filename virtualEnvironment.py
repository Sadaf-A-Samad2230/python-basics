# A virtual environment in Python is an isolated environment on your computer, where you can run and test your Python projects.

# It allows you to manage project-specific dependencies without interfering with other projects or the original Python installation.

# Think of a virtual environment as a separate container for each Python project. Each container:

# Has its own Python interpreter
# Has its own set of installed packages
# Is isolated from other virtual environments
# Can have different versions of the same package
# Using virtual environments is important because:

# It prevents package version conflicts between projects
# Makes projects more portable and reproducible
# Keeps your system Python installation clean
# Allows testing with different Python versions
# Creating a Virtual Environment
# Python has the built-in venv module for creating virtual environments.

# To create a virtual environment on your computer, open the command prompt, and navigate to the folder where you want to create your project, then type this command:


# ExampleGet your own Python Server
# Run this command to create a virtual environment named myfirstproject:
# ============================
# Windows
# C:\Users\Your Name> python -m venv myfirstproject
# ============================
# This will set up a virtual environment, and create a folder named "myfirstproject" with subfolders and files, like this:


# Result
# The file/folder structure will look like this:

# myfirstproject
#   Include
#   Lib
#   Scripts
#   .gitignore
#   pyvenv.cfg


# =======================================================
# Activating the Virtual Environment
# =======================================================
# Before you can use the virtual environment, you need to activate it.    
# To activate the virtual environment, use the following command:
# Windows
# -----------------------------
# C:\Users\Your Name> myfirstproject\Scripts\activate
# ------------------------------

# Result
# After activation, your command prompt will change to show the name of the activated environment, like this:
# (myfirstproject) C:\Users\Your Name>

# =======================================================
# Install Packages
# Once your virtual environment is activated, you can install packages in it, using pip.

# We will install a package called 'cowsay':
# # --------------------------------
# Example
# Install 'cowsay' in the virtual environment:
# --------------------------------
# Windows
# (myfirstproject) C:\Users\Your Name> pip install cowsay

# --------------------------------
# Result
# --------------------------------
# The package will be installed in the virtual environment, and you can use it in your Python scripts.


# =====================================================
# Example
# Insert two lines in test.py:

# test.py
import cowsay

cowsay.cow("Good Mooooorning!")


# =====================================================
# Deactivate the virtual environment:

# Windows
# (myfirstproject) C:\Users\Your Name> deactivate

# =====================================================

# Delete Virtual Environment
# Another nice thing about working with a virtual environment is that when you, for some reason want to delete it, there are no other projects depend on it, and only the modules and files in the specified virtual environment are deleted.

# To delete a virtual environment, you can simply delete its folder with all its content. Either directly in the file system, or use the command line interface like this:

# Example
# Delete myfirstproject from the command line interface:
# -------------------------------------------------
# Windows
# C:\Users\Your Name> rmdir /s /q myfirstproject