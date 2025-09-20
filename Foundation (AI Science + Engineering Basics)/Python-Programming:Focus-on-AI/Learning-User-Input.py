# Learning-User-Input

# Input = A function that prompts the user to enter data.
# Returns the entered data as a string.

######################################################################
# Documented-By-Lamar
from name_art import print_name

print_name() 

######################################################################

name = str(input("Hello there, please enter your name: "))
birth_year = int(input("Please share your birth year with me: "))
current_year = int(input("And the current year, i lost track: "))

age = current_year - birth_year


print(f"Hello there {name}, from the data shared, you are {age} years old.")