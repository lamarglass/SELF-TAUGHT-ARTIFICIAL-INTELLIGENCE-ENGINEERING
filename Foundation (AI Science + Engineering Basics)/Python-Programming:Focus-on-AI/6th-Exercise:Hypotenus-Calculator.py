# 6th-Exercise: Hypotenuse-Calculator

# Formular: Side-C = sqrt(A^2 + B^2)

######################################################################
# Documented-By-Lamar
from name_art import print_name

print_name() 

#######################################################################
import math

name = str(input("Please enter your name: "))
print(f"Nice to meat you {name}. To find your hypotenuse please enter the following")

side_a = float(input("Please enter the measurement of side A: "))
side_b = float(input("PLease enter the measurement of side B: "))
unit = str(input("And the unit <cm,metres>:"))

hypotenuse = round(math.sqrt(pow(side_a, 2) + pow(side_b, 2)), 2)

print(f"The hypotenuse to your triangle is: {hypotenuse}{unit}^2.")