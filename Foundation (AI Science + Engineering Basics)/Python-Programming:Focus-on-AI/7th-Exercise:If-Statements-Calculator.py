# 7th-Exercise-If-Statements-Calculator

# A basic calculator usinG if statements.

######################################################################
# Documented-By-Lamar
from name_art import print_name

print_name() 

#######################################################################

import math

name = str(input("Hello there, please enter your name: "))
number_1 = float(input(f"I will need the first number: "))
operator = str(input("What operator will you use? (/, *, +, -,): "))
number_2 = float(input("And the last number: "))

if operator == "+":
    answer = round(number_1 + number_2, 3)
    print(f"Answer: {number_1} {operator} {number_2} = {answer}.")
elif operator == "-":
    answer = round(number_1 - number_2, 3)
    print(f"Answer: {number_1} {operator} {number_2} = {answer}.")
elif operator == "*":
    answer = round(number_1 * number_2, 3)
    print(f"Answer: {number_1} {operator} {number_2} = {answer}.")    
elif operator == "/":
    answer = round(number_1 / number_2, 3)
    print(f"Answer: {number_1} {operator} {number_2} = {answer}.") 
else:
    print(f"Sorry {name}, i am not familiar with this '{operator}' operator.")          