# 4th-Exercise: Circumference-Calculator

# Formular: Circumference = 2 * PI * Radius

######################################################################
# Documented-By-Lamar
#from name_art import print_name

#print_name() 

#######################################################################

import math

print("Hello there, thank you for choosing Lamar's Calculator.")

name = str(input("Before we start please share your name with me: "))

print(f"Nice to meet you {name} :)")
print("To get your circle's circumference, i will only need..")

radius = float(input("Your circle's radius: "))
unit = str(input("And our unit of choice: "))

circumference = round(2 * math.pi * radius, 2)

print("...PROCESSING...")
print(f"Dear {name}, your circle's circumference is: {circumference}{unit}^2")
