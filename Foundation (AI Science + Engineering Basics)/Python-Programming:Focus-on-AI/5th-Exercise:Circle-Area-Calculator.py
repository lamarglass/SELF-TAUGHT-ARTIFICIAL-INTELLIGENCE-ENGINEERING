# 5th-Exercise: Circle-Area-Calculator

# Formular: Area = PI * radius

######################################################################
# Documented-By-Lamar
from name_art import print_name

print_name() 

#######################################################################

import math

name = str(input("Hello there, please enter your name: "))
radius = float(input(f"NIce to meet you {name}, can i have your radius please: "))
unit = str(input("And the desired unit: "))

area = round(math.pi * pow(radius, 2))
print("...PROCESSING...")

print(f"Dear {name}, your circle's area is {area}{unit}^2")
