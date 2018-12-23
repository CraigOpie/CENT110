#!/usr/bin/env python
"""
Name: 		Craig Opie
Class:		CENT 110
Assignment:	exam1quest8.py
Date:		27 September 2018

Algorithm:
Ask the user to pick items from a menu and display the price.  There are
three options - cheese burger, vegetable curry, and fried rice.
If the user selects cheese burger, the program asks a second question if
they want a combo.  
	The burger alone is $3.99.
	The combo price is $2.50 more.
Elif the user selects vegetable curry, the program asks a second
question if they want a side.
	The curry alone is $6.99.
	The side price is $2.00 more.
Elif the user selects fried rice. 
	The price is $5.99.
Else the user does not select any of the three options the program gives
up and the user pays nothing.

"""

# Text explaining to the user how to use the program.
print("""Pick an item from the menu to display the price.
1. cheese burger
2. vegetable curry
3. fried rice
""")

# String variable used to determine the users selection.
user_choice = input("Please enter your choice (number): ").strip()

# For cheese burger, the user is allowed to choose to have a combo.
if user_choice == "1":
	cost = 3.99
	side = input("Do you want a combo with it? (yes/no): ").strip().lower()
	if side == "yes" or side == "y":
		cost = cost + 2.50
	print("Please pay $"+str(cost)+".\n")

# For curry, the user is allowed to choose to have a side.
elif user_choice == "2":
	cost = 6.99
	side = input("Do you want a side? (yes/no): ").strip().lower()
	if side == "yes" or side == "y":
		cost = cost + 2.00
	print("Please pay $"+str(cost)+".\n")

# For fried rice, there are no other options.
elif user_choice == "3":
	print("Please pay $5.99.\n")

# For any other input we let the user know there was an issue.
else:
	print("We don't have what you want.\n")
