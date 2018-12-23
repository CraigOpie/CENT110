#!/usr/bin/env python
"""
Name:   Craig Opie
Class:  CENT110
File:   hw11.py

Algorithm:
1)  Import loads from the json module.
2)  Create a function that will accept a list input 'grades' of integers 
	or floats and calculate the average, then return the average as a 
	string to two decimal places.
	A.  Assign 'grades' to sum(grades) divided by len(grades) to achieve the
		average.
	B.  return 'grades' as a string formatted to two decimal places.
3)  Take input from the user to specify the filename of the JSON file to
	be processed and store in 'filename'.
4)  Open the JSON file as 'infile':
	A.  Assign the contents of 'infile' to 'contentsIn' and close 'infile'.
5)  Load the 'contentsIn' using the json loads function and assign to 
	'studentsDict'.
6)  Assign the list of students in 'studentsDict' to 'studentsList'.
7)  For each 'person' in 'studentsList':
	A.  print the person's name, homework average using the function 
		makeAverage(), and exam average using the same function.

Question:
1)  With respect to dealing with these scores in a python program, give 
	two reasons why JSON files are better than CSV files?  
	A.  First, we are loading the information in as a list for each
		person so we don't have to create the list using a 2D list.
	B.  We can call the information by using the key without having to 
		know or remember the index value of the list.
"""
from json import loads

def makeAverage(grades):
	"""
		Input must be a list of integers or floats.
		Returns the calculated averages as strings to two decimal places.
	"""
	grades = sum(grades)/len(grades)
	return("%.2f" % grades)
	
# User specifies a JSON filename
filename = input("Enter name of JSON file to process: ")

# Open the JSON file, store as string in contents, then close the file
with open(filename, "r") as infile:
    contentsIn = infile.read()

# Load the value of contents into a dictionary
studentsDict = loads(contentsIn)

# Load the first key in the dictionary and store as a list
studentsList = studentsDict['students']

# Print each persons name with hw average and exam average
for person in studentsList:
	print(person["name"]+", hw average: "+makeAverage(person["hwscores"])\
	+", exam average: "+makeAverage(person["exams"]))
