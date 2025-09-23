# Learning:Logical-Operators

# Logical Operators = Evaluate multiple conditions (or, and, not)
#                     or - at least one condition must be TRue
#                    and - both conditions must be true
#                    not - invert the condition (not False, not True)

######################################################################
# Documented-By-Lamar
from name_art import print_name

print_name() 

#######################################################################

temperature = int(input("Please enter the temperature: "))
is_raining = bool(input("Is it rainy outside? (True or False): "))

if temperature > 25 or temperature < 0 or is_raining:
    print("The out door even is canceled.")
else:
    print("The outdoor event is still scheduled")    