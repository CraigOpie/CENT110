#!/usr/bin/env python
"""
Name:   Craig Opie
Class:  CENT110
File:   quest11.py
Algorithm:
1)  Opent the file "parks.csv" and assign it to 'infile'.
2)  Read all lines of the document and assign to 'data'.
3)  Close the source file 'infile'.
4)  Create a new file named "parks.html" and assign to 'outfile'.
5)  Write the initial html heading information:
<!DOCTYPE html>
<html>
    <head>
        <title>parks.py</title>
    </head>
    <body>
        <table border="1">
6)  Create a variable to allow use of just the first line of the 'data' file.
7)  Loop through 'eachline' of 'data':
	a.  If this is the first line of 'data':
		1.  Strip, title, and split using "," and assign to 'head'.
		2.  Write the table row tag to 'outfile'.
		3.  For each 'value' in 'head':
			i.  Write the column header information to 'outfile'.
		4.  Write the table row closing tag to 'outfile'.
		5.  Change 'row' to false so that the file only gets one table head.
	b.  Else:
		1.  Strip, title, and split using "," and assign to 'eachline'.
		2.  Write the table row tag to 'outfile'.
		3.  For each 'value' in 'eachline':
			i.  Write the column data information to 'outfile'.
		4.  Write the table row closing tag to 'outfile'.
8)  Write the closing html information:
     </table>
    </body>
</html>
9)  Close 'outfile'
"""
# Open the source file and load information into 'data' as a list, then 
# Close the source file
infile = open("parks.csv", "r")
data = infile.readlines()
infile.close()

# Open the outfile and write the initial html heading information
outfile = open("parks.html", "w")
outfile.write("""<!DOCTYPE html>
<html>
    <head>
        <title>parks.py</title>
    </head>
    <body>
        <table border="1">""")

# Create the html table data from 'data'
row = True
for eachline in data:
    if row == True:
        # Load the first line as column header information
        head = eachline.strip().title().split(",")
        outfile.write('\n           <tr>')
        for value in head:
            outfile.write('\n               <th>'+value+'</th>')
        outfile.write('\n           </tr>')
        # Set the 'row' variable to false to prevent creating new headers
        row = False
    else:
		# Load the remaining lines as column data information
        eachline = eachline.strip().title().split(",")
        outfile.write('\n           <tr>')
        for value in eachline:
            outfile.write('\n               <td>'+value+'</td>')
        outfile.write('\n           </tr>')

# Write the closing tag information to the html file
outfile.write("""\n     </table>
    </body>
</html>""")

# Close the 'outfile' for further use
outfile.close()
