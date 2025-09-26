# Learning:String-Methods:name.isalpha.py

# Strings = a series of texts: "Lamar is Great", "Lamar"
# alpha = to check is the string is only alphabetic.
######################################################################
# Documented-By-Lamar
from name_art import print_name

print_name() 

#######################################################################

name = input("Enter your full name: ")

result = name.isalpha()

print(f"I have processed your name and the alphabetic verification came out: {result}")
