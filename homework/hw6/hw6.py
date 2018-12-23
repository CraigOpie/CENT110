#!/usr/bin/env python
"""
Name:   Craig Opie
Class:  CENT110
File:   hw6.py

Algorithm:
1)  Ask the user for the filename for the CSV file that is to be processed to XML and store in 'filename'.
2)  Accepts a filename without ".csv" extension:
    a.  Removes ".csv" from 'filename' if it has the extension.
    b.  Adds ".csv" from 'filename' to ensure the program loads the ".csv" file.
3)  Open the CSV file using 'filename' as read only and assign to 'infile'.
4)  Read all lines of CSV file and assign to 'data'.
5)  Replace CSV with XML in 'filename'.
6)  Create a new file using 'filename' and assign to 'outfile'.
7)  Write <?xml version="1.0" ?> to 'outfile'.
8)  Write <data> to 'outfile'.
10) Create a variable 'row' that will identify when the first line is being read.
11) For 'eachline' in 'data':
    a.  If 'row' is "1" then input the row as columns:
        1.  Clean up 'eachline' and remove the prefix for the CSV file (Microsoft Excel).
        2.  Assign the first line 'eachline' values to 'head' as a list separated by ','.
        3.  Set 'row' = 0 so no other line is assigned to 'head'.
    b.  Else:
        1.  Cleanup 'eachline' and split into a list by ','.
        2.  If data is for a male:
            i.  Subtract 1 inch from height.
            ii. Add 10 pounds to weight.
        3.  Write <subject> to 'outfile'.
        4.  For 'value' in 'head' (must use range(len(head)) to work correctly)
            i.  Write <'head[value]'><'eachline[value]'</'head[value]'> to 'outfile'.
        5.  Write </subject> to 'outfile'.
12) Write the closing tag </data> to 'outfile'.
13) Close 'outfile'.
14) Close 'infile'.
"""

# Ask the user to enter the name of the file to be processed
filename = input("Please enter the filename of the CSV file that is to be processed to XML: ")

# Allows the user to enter the filename with or without file type extension
filename = filename.replace(".csv","").strip()
filename = str(filename+".csv")

# Open the CSV file and load the lines of data
infile = open(filename, "r")
data = infile.readlines()

# Create a file named data.xml and write the file header information
filename = filename.replace(".csv",".xml")
outfile = open(filename, "w")
outfile.write('<?xml version="1.0" ?>')
outfile.write('\n<data>')

# Load the lines of data from the CSV file to populate the XML data
row = True
for eachline in data:
    if row == True:
        # Load the first line as column header information
        head = eachline.replace("\ufeff","").strip().lower().split(",")
        row = False
    else:
        eachline = eachline.strip().title().split(",")
        # Assume males under reported their weight by 10lbs and over reported their height by 1".
        if str(eachline[1]) == "M":
            eachline[2] = str(float(eachline[2]) - 1)
            eachline[3] = str(float(eachline[3]) + 10)
        # Write the information to the XML file using proper formatting
        outfile.write('\n    <subject>')
        for value in range(len(head)):
            outfile.write('\n        <'+head[value]+'>'+eachline[value]+'</'+head[value]+'>')
        outfile.write('\n    </subject>')

# Include the final closing tag for the XML file
outfile.write('\n</data>')

# Close both files
outfile.close()
infile.close()
