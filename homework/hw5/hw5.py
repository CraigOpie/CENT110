#!/usr/bin/env python
"""
Name:   Craig Opie
Class:  CENT110
File:   hw5.py

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
6) Create a variable 'max_price' that will be used to store the maximum
price of any item.
7) Create a variable 'min_price' that will be used to store the minimum
price of any item.
8) Create a list 'entreePrices' to store the prices of all entrees.
9) Create a list 'appPrices' to store the prices of all appitizers.
10) Create a list 'dessertPrices' to store the prices of all desserts.
11) Create a list 'otherPrices' to store the prices of all other items.
12) Create a variable 'loop_condition' that will be used to enter or exit
the loop.
13) Create a loop that performs the following checks:
    a) Accepts input from the user for the name of the item to be added.
    b) If: The user types "done" then the loop stops and the program
    closes the xml file.
    c) Else:
        i)The user continues entering item information such as:
            Type of food 'item_type'.
            Price of food 'item_price'.
        ii) The 'item_price' is then added to the 'total'.
        iii) If 'num' == 0 then this is the first item and:
            1) 'max_price' is set to the 'item_price'.
            2) 'min_price' is set to the 'item_price'.
            Else:
            3) If 'item_price' is more than the 'max_price' then make
            'max_price' = 'item_price'.
            4) If 'item_price' is less than the 'min_price' then make
            'min_price' = 'item_price'.

        iv) If 'item_type' (corrected to lowercase without any spaces)
        == "entree" then append the 'item_price' to the 'entreePrices'
        list.
            Elif 'item_type' (corrected to lowercase without any spaces)
        == "appetizer" then append the 'item_price' to the 'appPrices'
        list.
            Elif 'item_type' (corrected to lowercase without any spaces)
        == "dessert" then append the 'item_price' to the 'dessertPrices'
        list.
            Else append the 'item_price' to the 'otherPrices' list.

        v) The 'num' increments to count how many items are entered.
        vi) The following information is added to the xml file:
            <item>
                <name>'item_name'</name>
                <foodType>'item_type'</name>
                <price>'item_price'</name>
            </item>

14) If the user adds items:
    a) The average is then calculated to two decimals and stored in the
    variables 'overallAvg', 'entreeAvg', 'appAvg', 'dessertAvg', and
    'otherAvg'.
15) If the user doesn't enter any items, then the program sets
'overallAvg', 'entreeAvg', 'appAvg', 'dessertAvg', and 'otherAvg' = 0.00
16) The averages and 'min_price' and 'max_price' are then added to the
xml file with closing tags.  'min_price' and 'max_price' are formatted
to be a float with two decimal places:
    <overallAvg>'overallAvg'</overallAvg>
    <entreeAvg>'entreeAvg'</entreeAvg>
    <appAvg>'appAvg'</appAvg>
    <dessertAvg>'dessertAvg'</dessertAvg>
    <otherAvg>'otherAvg'</otherAvg>
    <priceRange>
        <maximum>'max_price'</maximum>
        <minimum>'min_price'</minimum>
    </priceRange>
</menu>
17) Close and write the xml file and exit the program.
"""

print("This program generates an XML menu based off of user inputs. \
\nType 'done' when entering an item name to exit.")

doc = open("menu.xml", "w")
doc.write("""<?xml version="1.0" ?>

<menu>
    """)

total = 0.00
max_price = 0.00
min_price = 0.00
num = 0
entreePrices = []
appPrices = []
dessertPrices = []
otherPrices = []

loop_condition = True
while loop_condition == True:
    item_name = input("Enter the name of the item: ")
    if item_name.lower().replace(" ","") == "done":
        loop_condition = False
    else:
        item_type = input("Enter the type of food: ")
        item_price = float(input("Enter the price of the item: "))
        total = total + item_price

        if num == 0:
            max_price = item_price
            min_price = item_price
        else:
            if item_price > max_price:
                max_price = item_price
            if item_price < min_price:
                min_price = item_price

        if item_type.lower().replace(" ","") == "entree":
            entreePrices.append(item_price)
        elif item_type.lower().replace(" ","") == "appetizer":
            appPrices.append(item_price)
        elif item_type.lower().replace(" ","") == "dessert":
            dessertPrices.append(item_price)
        else:
            otherPrices.append(item_price)

        num = num + 1
        doc.write("""<item>
        <name>"""+str(item_name)+"""</name>
        <foodType>"""+str(item_type)+"""</foodType>
        <price>"""+str("%.2f" % (item_price))+"""</price>
    </item>
    """)

if num != 0:
    overallAvg = ("%.2f" % (total/num))
    entreeAvg = ("%.2f" % (sum(entreePrices)/len(entreePrices)))
    appAvg = ("%.2f" % (sum(appPrices)/len(appPrices)))
    dessertAvg = ("%.2f" % (sum(dessertPrices)/len(dessertPrices)))
    otherAvg = ("%.2f" % (sum(otherPrices)/len(otherPrices)))
else:
    overallAvg = 0.00
    entreeAvg = 0.00
    appAvg = 0.00
    dessertAvg = 0.00
    otherAvg = 0.00

doc.write("""<overallAvg>"""+str(overallAvg)+"""</overallAvg>
    <entreeAvg>"""+str(entreeAvg)+"""</entreeAvg>
    <appAvg>"""+str(appAvg)+"""</appAvg>
    <dessertAvg>"""+str(dessertAvg)+"""</dessertAvg>
    <otherAvg>"""+str(otherAvg)+"""</otherAvg>
    <priceRange>
        <maximum>"""+str("%.2f" % (max_price))+"""</maximum>
        <minimum>"""+str("%.2f" % (min_price))+"""</minimum>
    </priceRange>
</menu>""")

doc.close()
