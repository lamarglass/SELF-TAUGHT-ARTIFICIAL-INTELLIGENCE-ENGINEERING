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
is_sunny = bool(input("Is it rainy outside? (True or False): "))

if temperature >= 28 and is_sunny:
    print("It is Hot outside: 🔥")
    print("It is sunny: ☀️")
elif temperature <= 0 and is_sunny:
    print("It is cold outside: ❄️")   
    print("It is sunny: ☀️") 
elif temperature < 28 and temperature > 0 and is_sunny:
    print("It is Warm outside: 🫩")  
    print("It is sunny: ☀️")  
elif temperature >= 28 and not is_sunny:
    print("It is Hot outside: 🔥")
    print("It is cloudy: ☁️")
elif temperature <= 0 and not is_sunny:
    print("It is cold outside: ❄️")   
    print("It is cloudy: ☁️") 
elif temperature < 28 and temperature > 0 and not is_sunny:
    print("It is Warm outside: 🫩")  
    print("It is cloudy: ☁️")   
else:
    print("🍺")       