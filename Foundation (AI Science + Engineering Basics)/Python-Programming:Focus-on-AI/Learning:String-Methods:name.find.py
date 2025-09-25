# Learning:String-Methods:name.find.py

# Strings = a series of texts: "Lamar is Great", "Lamar"
# find = to find a desired character in a string
######################################################################
# Documented-By-Lamar
from name_art import print_name

print_name() 

#######################################################################

name = str(input("Enter your full name: "))
find =str(input("What would you like to find in your name?: "))

result = name.find(f"{find}")

print(result)
