#!/usr/bin/env python
"""
Name:   Craig Opie
Class:  CENT110
File:   hw9.py

Algorithm:
1)  Import the 'loads' function from the 'json' module.
2)  Take input from the user to specify the filename of the JSON file and store in 'filename'.
3)  Open 'filename' as 'infile':
    A.  Read the data in filename and store as a string in 'contentsIn', then close 'infile'.
4)  Create a new dictionary using 'loads' to process 'contentsIn' and store in 'studentsDict'.
5)  For each key in 'studentsDict':
    A.  Capture the value of key and store in 'titleNode'.
6)  Create a new list using 'studentsDict[titleNode] and store in 'studentsList'.
7)  Create the first line of the XML file and store in 'contentsOut'.
8)  Create the second line of the XML file and add to 'contentsOut'.
9)  Process through each person in 'studentsList':
    A.  Add the '<students>' XML tag to 'contentsOut'.
    B.  Process through each person's dictionary values:
        1.  Add '<'+str(key)+'>'+str(person[key])+'</'+str(key)+'>' to 'contentsOut'.
    C.  Add the '</students>' XML tag to 'contentsOut'.
10) Add the titleNode closing tag to 'contentsOut'.
11) Change the filename from JSON file extension to XML file extension and save to 'filename'.
12) Create 'filename' as 'outfile':
    A.  Write the string 'contentsOut' to 'outfile', then close 'outfile'.

Questions:
1)  In a JSON file, why are arrays (denoted with [ ]) used?
    A.  Arrays in JSON are used to organize a collection of related items (Which could be JSON objects)
2)  What is the advantage of using the key of a dictionary to access a value versus using the index of a list to access a value?
    A.  It is easier to remember and organize using a key name vice an index number value.
    B.  Faster due to hashing in dictionaries vs. sequencing through each index in a list to find the desired value.
3)  What is the disadvantage of using the key of a dictionary to access a value versus using the index of a list to access a value?
    A.  You need to know the values of all the keys.
    B.  The values are not organized in any specific order.
"""
from json import loads

# User specifies a JSON filename for conversion
filename = input("Please enter the JSON filename for conversion to XML: ")

# Open the JSON file, store as string in contents, then close the file
with open(filename, "r") as infile:
    contentsIn = infile.read()

# Load the value of contents into a dictionary
studentsDict = loads(contentsIn)

# Capture the title node for later use
for key in studentsDict:
    titleNode = key

# Create a list by calling the title node from the dictionary
studentsList = studentsDict[titleNode]

# Create the header information for the XML file
contentsOut = '<?xml version"1.0" ?>'
contentsOut += '\n<'+titleNode+'>'

# For each person in the list, create a XML tag displaying the nodes values
for person in studentsList:
    contentsOut += ('\n    <student>')
    for key in person:
        contentsOut += ('\n        <'+str(key)+'>'+str(person[key])+'</'+str(key)+'>')
    contentsOut += ('\n    </student>')

# Add the closing tag to the title node
contentsOut += '\n</'+titleNode+'>'

# Rename the filename extension from json or JSON to xml
filename = filename.replace(".json", ".xml").replace(".JSON", ".xml")

# Create the output XML file using filename, write contentsOut, then close the outfile
with open(filename, "w") as outfile:
    outfile.write(contentsOut)
