# Learning-If-Statements.py

# if = Do some code IF some condition is True
#      Else do something else

######################################################################
# Documented-By-Lamar
from name_art import print_name

print_name() 

#######################################################################

name = str(input("Hello there, please enter your name: "))
age = int(input(f"Nice to meet you {name}, please share our age: "))

if age >= 1000:
    print(f"{name}, you must be a demigod")
elif age == 100:  
    print(f"Did ou live to see your great grand kids. {name}?") 
elif age >= 18:
    print(f"Good news {name}, you are and adult!")    
elif age < 0:
    print(f"I am sure you are not born yet, {name}.")    
else:
    print(f"You must be have an age")     

    