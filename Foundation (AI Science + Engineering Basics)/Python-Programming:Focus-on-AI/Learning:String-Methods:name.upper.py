# Learning:String-Methods:name.upper.py

# Strings = a series of texts: "Lamar is Great", "Lamar"
# upper = to make every string uppercased.
######################################################################
# Documented-By-Lamar
from name_art import print_name

print_name() 

#######################################################################

name = input("Enter your full name: ")

choice = input("Would you like your name to be upper-cased? (YES or NO): ").strip().lower()

# one-line if assignment
name = name.upper() if choice in ("yes", "y") else name

print(f"Your choice name is: {name}")
