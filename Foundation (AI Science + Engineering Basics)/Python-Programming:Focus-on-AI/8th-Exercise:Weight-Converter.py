# 8th-Exercise: Weight-Converter

# A basic convertor for weights.

######################################################################
# Documented-By-Lamar
from name_art import print_name

print_name() 

#######################################################################

import math

weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (KG or LBS): ")

if unit == "KG":
    weight = round(weight * 2.205, 2)
elif unit == "LBS":
    weight = round(weight / 2.205, 2)
else:
    print(f"Your unit:'{unit}' is invalid.")

print(f"Your weight is: {weight}{unit}")   

