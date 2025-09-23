# Learning:Conditional-Expressions

# Conditional expressions = a one-line shortcut for the if-else-statement(ternary   operator) 
#                           Print or assign one of the values based on a condition
#                           X if condition else Y

######################################################################
# Documented-By-Lamar
from name_art import print_name

print_name() 

#######################################################################

number = int(input("Please neter a number: "))

print(f"It is a positive number: (+{number})" if number > 0 else f"It is a Negative number: ({number})")

