# Learning:String-Methods:name.isdigit.py

# Strings = a series of texts: "Lamar is Great", "Lamar"
# isdigit = to check is the string has a number or numbers.
######################################################################
# Documented-By-Lamar
from name_art import print_name

print_name() 

#######################################################################

name = input("Enter your full name: ")

result = name.isdigit()

print(f"I have checked your name and the digit verification is: {result}.")