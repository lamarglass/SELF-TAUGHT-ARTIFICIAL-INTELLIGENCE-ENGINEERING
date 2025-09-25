# Learning:String-Methods:name.capitalize.py

# Strings = a series of texts: "Lamar is Great", "Lamar"
# capitalize = to capitalize the string
######################################################################
# Documented-By-Lamar
from name_art import print_name

print_name() 

#######################################################################

name = input("Enter your full name: ")

choice = input("Would you like your name to be capitalized? (YES or NO): ").strip().lower()

# one-line if assignment
name = name.capitalize() if choice in ("yes", "y") else name

print(f"Your capitalized name is: {name}")
