#!/usr/bin/env python
"""
Name:       Craig Opie
Class:      CENT 110
Assignment: inclass3.py
Date:       18 Sep 2018

Algorithm:
Allow user to enter a choice between going to the zoo or to the beach 
and stores in variable 'location' which is explicitly stripped of 
white space and forced to be lower case.

If 'location' is "zoo": 
	Then the program asks whether they have an annual pass and stores in
	variable 'patron' which is explicitly stripped of white space and 
	forced to be lower case.
	
	If 'patron' is "yes":
		Print "You already paid, go ahead."
	Else:
		Ask user for the number of adults.  The value is explicitly 
		stored as an int and then multiplied by 8 before being stored in
		the variable 'adultTicketCost'.
		Ask user for the number of children.  The value is explicitly
		stored as an int and then multiplied by 4 before being stored in
		the variable 'childTicketCost'.
		The total ticket cost is then calculated by adding the values of
		'adultTicketCost' and 'childTicketCost'.  The value is then 
		formated as a float value to two decimal places and stored in 
		the variable 'totalCost'.
		Print "Please pay $"+'totalCost'.
Else if 'location' is "beach":
	Print "Your cost is $0, good choice."
Else:
	Print "Please enter a valid input."
	
Print "Goodbye!"
"""

# Collects where the user would like to visit.
location = input("Would you like to go to the Zoo or the Beach?: ").lower()\
.strip()
if location == "zoo":
    # Determine whether the user will have to pay anything for entry.
    patron = input("Do you have the annual pass (yes/no)?: ").lower().strip()
    if patron == "yes":
        print("You already paid, go ahead.")
    # Determines the overall cost and informs the user.
    elif patron == "no":
        adultTicketCost = int(input("Enter the number of adults: ")) * 8
        childTicketCost = int(input("Enter the number of children: ")) * 4
        totalCost = str(format((adultTicketCost + childTicketCost), '.2f'))
        print("Please pay $"+totalCost)
    else:
        print("Please enter a valid input.")
elif location == "beach":
    print("Your cost is $0, good choice.")
else:
    print("Please enter a valid input.")
print("Goodbye!")
