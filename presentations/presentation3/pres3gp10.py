#!/usr/bin/env python
"""
Name: 		Craig Opie
Class:		CENT 110
Assignment:	pres3gp10.py
Date:		20 September 2018

Algorithm:
The program asks the user to input three numbers.  The program will 
write to a file named "numbers.txt" each of the numbers on a separate 
line.  Then, the last line of the file contains the sum of all three 
numbers.

1) Describe the program to the user using a print function.
2) Create three float type 'variables' that takes input from the user.
3) Create a 'variable_result' that sums the three float variables.
4) Create a 'file_content' variable that contains the string content of 
the output file displaying the three user provided numbers, each on 
their own line, with a summation sign and line to make the result easier
to read.  The last line contains the result of adding the three 
variables together.
5) Create a document named "numbers.txt"
6) Add the information stored in the 'file_content' variable to the 
document body.  
7) Close the document 
8) Inform the user that you have completed creating the file.
"""

# Lets the user know how to use the program.
print("\nThis program takes three numbers, provided by you, and writes the \n\
values to a text document named 'numbers.txt'.  Each number will be on a \n\
separate line.  The last line conatains the sum of all three numbers.\n")

# Number values that will be used inside the generated document.
variable_1 = float(input("Please enter the first number: "))
variable_2 = float(input("Please enter the second number: "))
variable_3 = float(input("Please enter the third number: "))
variable_result = (variable_1 + variable_2 + variable_3)

# Sets the design format for the generated document.
file_content = str("""
    """+str(variable_1)+"""
    """+str(variable_2)+"""
    """+str(variable_3)+"""
+ _______
    """+str(variable_result))

# Creates the document using the variables and format as specified above.
doc = open("numbers.txt", "w")
doc.write(file_content)
doc.close()

# Informs the user that the file was created with no issues.
print("\nYour file has been generated.")
