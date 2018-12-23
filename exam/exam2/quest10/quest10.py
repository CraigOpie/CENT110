#!/usr/bin/env python
"""
Name: 	Craig Opie
Class:	CENT110
File:	quest10.py
Algorithm:
1)  Open the source file to get the information from and assign to 'infile'.
2)  Create a list of all of the lines of 'infile' and store in 'data'.
3)  Close 'infile' because it doesn't need to be used again.
4)  Create a list to store all of the divers names, 'names'.
5)  Create a list to store all of the divers averages, 'average'.
6)  Create a variable to store the name of the winner, 'winner'.
7)  Loop through eachline in 'data':
	a.  Create a variable 'sum_' to store scores for a total.
	b.  Strip the "\n" from 'eachline' and split the information into strings
	based where ever there is a ",".
	c.  Add the first index value to 'names'.
	d.  Loop through the index of 'eachline' from 1 to the end:
		i.  Total up the sum of the values.
	e.  Find the average of each diver by dividing the 'sum_' with the number
	of dives, convert to a two decimal format and store in 'avg'.
	f.  Append 'avg' to the list 'average'.
8)  Loop through each person in 'names' using the index:
	a.  Print each persons name and associated score to the screen.
9)  Create a variable for the highest score and assign the first value in 'average'.
10) Loop through the values in 'averages' using the index:
	a.  Compare each value to the 'highest' to see if it larger:
		1.  If the value is larger: 
			i.  store the value in 'highest'.
			ii. Store the name in 'winner'.
11) Print the winner is 'winner' with a score of 'highest' to the screen.
"""

# Open the data file, load the values, and close the data file
infile = open("divingscores.txt", "r")
data = infile.readlines()
infile.close()

# Create required lists and variables
names = []
average = []
winner = ""

# Create a list of the names of each diver and a list of the averages for each diver 
for eachline in data:
	sum_ = 0
	eachline = eachline.strip().split(",")
	names.append(eachline[0])
	for i in range(1,len(eachline)):
		sum_ += float(eachline[i])
	avg = ("%.2f"%(sum_/(len(eachline)-1)))
	average.append(avg)

# Print each divers name and score to the screen
for person in range(len(names)):
	print(names[person]+" has a score of "+average[person])

# Find the overall winner based on the highest average
highest = average[0]
for value in range(1,len(average)):
	if average[value] > highest:
		highest = average[value]
		winner = names[value]

# Print the name of the overall winner and their score
print("The winner is "+winner+" with a score of "+highest)
