# Learning:String-Methods:name.rfind.py

# Strings = a series of texts: "Lamar is Great", "Lamar"
# rfind = to find a desired character in a string, reverse find
######################################################################
# Documented-By-Lamar
from name_art import print_name

print_name() 

#######################################################################

name = str(input("Enter your full name: "))
find =str(input("What would you like to reverse-find in your name?: "))

result = name.rfind(f"{find}")

print(result)
