# Learning:String-Methods:.count

# Strings = a series of texts: "Lamar is Great", "Lamar"
######################################################################
# Documented-By-Lamar
from name_art import print_name

print_name() 

#######################################################################

phone_number = input("Enter your phone number: ")

count = str(input("What would you like to count among the numbers: "))

result = phone_number.count(count)

print(result)