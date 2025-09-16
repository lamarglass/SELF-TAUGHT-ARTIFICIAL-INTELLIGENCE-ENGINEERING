# Documented-By-Lamar
from name_art import print_name

print_name() 

# Boolean = A boolean is either true or false.

print("Are you a student?")
is_student = str(input("Reply with <Yes/Y> for YES or <No/N> for NO:  "))

# Trying if statements from what i learned earlier.
if is_student == "Yes" or "Y":
    is_student = True
    print("Ow nice..lucky programmer you are:)")
elif is_student == "No" or "N":
    is_student = False  
    print("So you chose the hard way, guess i am not alone, i respect that :)")  
else:
    print("That was an invalid choise.")    