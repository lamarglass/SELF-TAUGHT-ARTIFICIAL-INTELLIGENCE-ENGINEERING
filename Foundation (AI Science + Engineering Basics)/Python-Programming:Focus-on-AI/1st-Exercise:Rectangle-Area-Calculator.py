# 1st-Exercise: Rectangle-Area-Calcultor

# Formular: Area = (Lenght * Widht)

######################################################################
# Documented-By-Lamar
from name_art import print_name

print_name() 

#######################################################################

name = str(input("Hello there, Welcome to Lamar's area calculator, to procees please enter your name: "))

print(f"Nice to meet you {name}, please share the measuments respectively.")

the_lenght = float(input("The lenght please: "))
the_widht = float(input("And the width: "))
unit = (input("Ow..and the unit ofcourse,is it centimetres, metres...: "))

area = the_lenght * the_widht
print("...PROCESSING....")

print(f"Dear {name}, your Area is: {area}{unit}^2.")
print("THANK YOU FOR USING MY CALCULATOR - Lamar")
