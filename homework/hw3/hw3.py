#!/usr/bin/env python
"""
Name: 		Craig Opie
Class:		CENT 110
Assignment:	hw3.py
Date:		25 September 2018

Algorithm:
Python program that asks the user about their pets and their ages and
embeds that information into a HTML table. The program will then
generate an HTML file called pets.html that will contain the user
entered information in the form of a table.

1) Creates a file named "pets.html" and allows it to be referenced using
the variable 'doc'.
2) Opens the 'doc' and writes the HTML header and initial table content:
<html>
    <head>
        <title>Howework 3 - Pets.html</title>
    </head>
    <body>
		<table border="1">
			<tr>
				<th>Pet name</th>
				<th>Age</th>
			</tr>
3) Create the 'loop_active' variable for the while loop boolean condition.
4) Create a while loop that allows input from the user to submit a pet name.
The pet name is then stripped of all white space and lowercased to allow for
standardized formatting used for comparisons in the variable 'name'.  If the
user types "done" the loop will stop.  The user will be able to submit the
pet's age and all white space will be stripped and the age will be stored in
the variable 'age'.  Then the loop opens the 'doc' and writes the HTML table
data using the 'name' and 'age' variables:
            <tr>
                <td>'name'</td>
                <td>'age'</td>
            </tr>
5) Opens the 'doc' and writes the HTML closing tags:
		</table>
	</body>
</html>
6) Closes the 'doc' to complete writing all content to the file.
7) Outputs a comment to inform the user that the file has been successfully
generated.
"""

# Creates a file named "pets.html" and allows it to be referenced using
# the variable 'doc'.
doc = open("pets.html", "w")

# Adds content to the file created.
doc.write("""
<html>
    <head>
        <title>Howework 3 - Pets.html</title>
    </head>
    <body>
		<table border="1">
			<tr>
				<th>Pet name</th>
				<th>Age</th>
			</tr>""")

# Takes input from the user and adds the content to a table.
loop_active = True
while loop_active == True:
    name = input("Enter name of pet: ").strip().lower()
    if name == "done":
        loop_active = False
    else:
        age = input("Enter age: ").strip()
        doc.write("""
            <tr>
                <td>"""+name+"""</td>
                <td>"""+age+"""</td>
            </tr>""")

# Closes out the remaining html tags to complete the file.
doc.write("""
        </table>
    </body>
</html>""")

# Closes the file after all information has been written.
doc.close()

# Informs the user that there was no errors and the file is created.
print("Your file has been generated.\n")
