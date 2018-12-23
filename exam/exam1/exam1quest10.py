#!/usr/bin/env python
"""
Name: 		Craig Opie
Class:		CENT 110
Assignment:	exam1quest9.py
Date:		27 September 2018

Algorithm:
Program asks the user for thier name and hobbies.  The program then 
generates a HTML file called "AboutMe.html" containing the data entered
by the user.  It will continue to ask the user for their hobbies until 
the user enters "quit".  

1) Create an HTML document that is named "AboutMe.html"
2) Get the user's name as an input and store for use in the HTML file.
3) Write the opening information for the HTML file (that will not be
looped):
<html>
	<body>
		<h1>"""+name+"""</h1>
		<h2>Hobbies</h2>
		<ul>
4) Create a variable 'loop_condition' to start the loop.
5) While the loop is running:
	Ask the user to enter a hobby.
	If the user types "quit":
		Set the loop_condition to "stop" and exit the program.
	Else:
		Write to the HTML document using the 'hobby' input as a list 
		item.
6) Write the closing information for the HTML file:
		</ul>
	</body>
</html>
7) Close the HTML document and exit the program.
"""

# Creates an HTML document and assigns it to 'doc'
doc = open("AboutMe.html", "w")

# Create a variable for the user to input their name.
name = input("Enter the name of the person: ").title().strip()

# Create the opening non-looping information for the HTML file.
doc.write("""<html>
	<body>
		<h1>"""+name+"""</h1>
		<h2>Hobbies</h2>
		<ul>
			""")

# Create a variable for loop condition and start a loop.
loop_condition = "run"
while loop_condition == "run":
	# Allow the user to enter a new hobby which will be added to the HTML file
	# as a new list item, or type quit to exit the loop and program.
	hobby = input("Enter a hobby or 'quit' to stop: ")
	if hobby == "quit":
		loop_condition = "stop"
	else:
		doc.write("<li>"+hobby+"</li>")

# Create the closing non-looping informaiton for the THML file.
doc.write("""
		</ul>
	</body>
</html>""")

# Close the HTML file and save all changes.
doc.close()
