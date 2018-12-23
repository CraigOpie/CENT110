#!/usr/bin/env python
"""
Name: 	Craig Opie
Class:	CENT110
File: 	hw4.py

Algorithm:
Program that takes input from the user repeatedly and generates a file 
output that is formatted as an XML file.

1) Inform the user the purpose of and how to use the program.  This is 
the part that tells them how to exit the program properly. The line is 
more than 79 characters so I continue the code on the next line using 
'\' without any characters or whitespace following it. For simplicity, I 
also start a new line in the program.
2) Open a new document 'doc' that creates an xml file.
3) Add the header information to the xml file and then start off the 
tags that will not be looped using propper formatting.
4) Create a variable 'total' that is a float and will be used to sum all
of the items price 'item_price' during the loop.
5) Create a variable 'num' that is an integer and will be used to keep 
track of the number of items entered by the user.
6) Create a variable 'loop_condition' that will be used to enter or exit
the loop.
7) Create a loop that performs the following checks:
	a) Accepts input from the user for the name of the item to be added.
	b) If: The user types "done" then the loop stops and the program 
	closes the xml file.
	c) Else: 
		i)The user continues entering item information such as:
			Type of food 'item_type'.
			Price of food 'item_price'.
		ii) The 'item_price' is then added to the 'total'.
		iii) The 'num' increments to count how many items are entered.
		iv) The following information is added to the xml file:
			<item>
				<name>'item_name'</name>
				<foodType>'item_type'</name>
				<price>'item_price'</name>
			</item>
			
8) If the user doesn't enter any items, then the program closes the xml
file without writing anymore information.
9) If the user adds items:
	a) The average is then calculated to two decimals and stored in the 
	variable 'average'.
	b) The average is then added to the xml file and closing tag:
		<averagePrice>'average'</averagePrice>
	</menu>
	
10) Close and write the xml file and exit the program.
		
		
"""

print("This program generates an XML menu based off of user inputs. \
\nType 'done' when entering an item name to exit.")

doc = open("menu.xml", "w")
doc.write("""<?xml version="1.0" ?>

<menu>
	""")

total = 0.00
num = 0

loop_condition = True
while loop_condition == True:
	item_name = input("Enter the name of the item: ")
	if item_name.lower().replace(" ","") == "done":
		loop_condition = False
	else:
		item_type = input("Enter the type of food: ")
		item_price = float(input("Enter the price of the item: "))
		total = total + item_price
		num = num + 1
		doc.write("""<item>
		<name>"""+str(item_name)+"""</name>
		<foodType>"""+str(item_type)+"""</foodType>
		<price>"""+str(item_price)+"""</price>
	</item>
	""")

if num != 0:
	average = ("%.2f" % (total/num))
else:
	average = 0.00
	
doc.write("""<averagePrice>"""+str(average)+"""</averagePrice>
</menu>""")

doc.close()
	
