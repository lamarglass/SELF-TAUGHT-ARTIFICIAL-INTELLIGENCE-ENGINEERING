# 1st-Exercise: Shopping Cart Program

######################################################################
# Documented-By-Lamar
from name_art import print_name

print_name() 

#######################################################################

print("Welcome to Lamar's shopping cart program")

name = str(input("For the best experience, please share your name: "))

print(f"Lovely to meet you {name} :)")

item = str(input("What item would you like to buy today?: "))
price = float(input(f"I see..and what is the price of this {item}?: "))
quantity = int(input("And what quantity would you like?: "))
currency = str(input(f"Also, what currency would you use to by your {item}?: "))

total_cost = price * quantity
print("...PROCESSING...")

# so 200 steaks going for CHF:2.00 each, that will be a total of: CHF:400.0
print(f"Alright, so {quantity} {item}/s going for {currency}:{price} each, that will be a total of: {currency}:{total_cost} ")

print(f"Thank you for using this program {name},enjoy your shopping :)")