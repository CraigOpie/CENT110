#!/usr/bin/env python
"""
Name: 		Craig Opie
Class:		CENT 110
Assignment:	exam1quest9.py
Date:		27 September 2018

Algorithm:
Program that prompts the user for some input and prints html output to 
the screen.  The output that is produced depends on whether or not the 
institution is a two year or four year one.

1) Ask the user for the institution name and assign it to variable 
'name'.  'name' will be all uppercase characters.
2) Ask the user for the type of institution and assign it to variable
'term'.  'term will be stripped of whitespace in front and at the end
and then lowercase characters for later comparison.
3) Ask the user for the number of programs offered and assign it to 
variable 'num'. 
4) Assign a variable 'css' to identify the style class that will be used
based on the 'term'.  Value should be lowercase and stripped of all 
white space.  Allow a few inputs that would make sense and dress up the
'term'  variable to a more professional look.
5) Print the HTML output using the variables entered by the user with a 
css class being specified by the 'term':
<html>
	<head>
		<style>
			.twoyear
			{
				text-decoration: underline;
				color: teal;
			}
			.fouryear
			{
				color: brown;
				border: thin solid black;
			}
		</style>
	</head>
	<body>
	<h1 class='css'>'name'</h1>
	<p class='css'>'term'</p>
	<p class='css'>Number of programs: 'num'</p>
	</body>
</html>
"""

# Collect inputs from the user for user in the HTML output.
name = input("Enter the name of institution: ").strip().upper()
term = input("Enter the type of institution (Two Year/Four Year): ").strip()\
.lower()
num = input("Enter the number of programs offered: ").strip()

# Takes the 'term' and converts it to a usable value for the css class.
if term == "two year" or term == "2 year" or term == "2":
	css = str('"twoyear"')
	term = "Two Year"
elif term == "four year" or term == "4 year" or term == "4":
	css = str('"fouryear"')
	term = "Four Year"
	
# Specify the HTML output to print on the screen.
print("""<html>
	<head>
		<style>
			.twoyear
			{
				text-decoration: underline;
				color: teal;
			}
			.fouryear
			{
				color: brown;
				border: thin solid black;
			}
		</style>
	</head>
	<body>
	<h1 class="""+css+""">"""+name+"""</h1>
	<p class="""+css+""">"""+term+"""</p>
	<p class="""+css+""">Number of programs: """+num+"""</p>
	</body>
</html>""")
