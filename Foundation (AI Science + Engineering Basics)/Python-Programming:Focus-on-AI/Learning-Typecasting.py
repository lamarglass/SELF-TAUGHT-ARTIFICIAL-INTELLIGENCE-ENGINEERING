# Learning-Typecasting

# Typecasting = The process of converting a variable from one data type to another: str(), int(), float(), bool().

######################################################################
# Documented-By-Lamar
from name_art import print_name

print_name() 

######################################################################

name = "Lamar"
age = 23
gpa = 4.1

print(type(name))
print(type(age))
print(type(gpa))

# Lets type cast it the variables:
gpa = int(gpa)
age = float(age)

print(type(gpa))
print(type(age))

print(gpa)
print(age)
