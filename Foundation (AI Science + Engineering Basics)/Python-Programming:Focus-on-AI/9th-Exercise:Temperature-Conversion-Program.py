# 9th-Exercise: Temperature-Conversion-Program.

# A basic converter for temperatures.
# Celsius → Fahrenheit formula: (C × 9/5) + 32
# Fahrenheit → Celsius formula: (F − 32) × 5/9

######################################################################
# Documented-By-Lamar
from name_art import print_name

print_name() 

#######################################################################

unit = input("Is the temperature in Celsius or Fahrenheit? (C or F): ").strip().upper()
temp = float(input("Enter the temperature: "))

if unit == "C":
    converted = round((temp * 9/5) + 32, 2)
    print(f"{temp}°C is {converted}°F")

elif unit == "F":
    converted = round((temp - 32) * 5/9, 2)
    print(f"{temp}°F is {converted}°C")

else:
    print(f"{unit} is an invalid unit of measurement.")
