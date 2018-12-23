#!/usr/bin/env python
"""
Name: 	Craig Opie
Class:	CENT110
File:	hw7.py
Algorithm:
1)  Open the source file "gymnastics.txt" as read only and assign to 'infile'.
2)  Load all data from 'infile' and store in 'data' as a line separated list.
3)  Close 'infile'.
4)  Create future required variables:
    a.  'averages' as a list.
    b.  'columnlist' as a list.
    c.  'rowlist' as a list.
    d.  'judges' as a list.
5)  Extract the number values from 'data' for 'eachline' and store in 'rowlist':
    a.  Create a list named 'scores'.
    b.  Format 'eachline' and split by "," and store back in 'eachline'.
    c.  For 'score' in 'eachline' restrict the loop by index for 1 through the end of list.
        1.  Append 'score' to 'scores'.
    d.  Append 'scores' to 'rowlist'.
6)  Convert the rowlist into a column list:
    a.  Create a variable 'index' to store the index number of the rowlist.
    b.  While 'index' < or = one more than the number of items in 'rowlist':
        1.  Create a temporary list named 'scores'.
        2.  For 'eachperson' in 'rowlist':
            i.  Append the value in 'eachperson' to 'scores'.
        3.  Append 'scores' to 'columnlist'.
        4.  Incrament 'index'.
        5.  Build a list of 'judges' by appending "Judge " concatenated with 'index'.
7)  Average all of the scores in 'columnlist' and store in 'averages':
    a.  For every 'score' in 'columnlist':
        1.  Create a variable 'sum_' to add all scores for each judge.
        2.  Create a variable 'avg' to store the average of all scores by the judge.
        3.  For each 'value' in 'score':
            i.  Add the value to 'sum_'.
        4.  Divide 'sum_' by the entries in 'score' and store in 'avg'.
        5.  Append the value 'avg' to 'averages'.
8)  For each indexed 'value' in 'averages':
    a.  Print "Average score given by "+judges[value]+" is "+averages[value] to the screen.
"""
# Open source data file and load information into 'data', then close the source data file.
infile = open("gymnastics.txt", "r")
data = infile.readlines()
infile.close()

# Create required variables
averages = []
columnlist = []
rowlist = []
judges = []

# Extract the number data from 'data' and store in 'rowlist'.
for eachline in data:
    scores = []
    eachline = eachline.strip().title().split(",")
    for score in range(1,len(eachline)):
        scores.append(eachline[score])
    rowlist.append(scores)

# Convert number data from row list to column lists and store in 'columnlist'
index = 0
while index <= (len(rowlist)+1):
    scores = []
    for eachperson in rowlist:
        scores.append(eachperson[index])
    columnlist.append(scores)
    index += 1

    # Identify the judges based off number.
    judges.append("Judge "+str(index))

# Average all of the scores in each column list and store in 'averages'
for score in columnlist:
    sum_ = 0
    avg = 0
    for value in score:
        sum_ += int(value)
    avg = str(sum_/len(scores))
    averages.append(avg)

# Print the corresponding Judge name with their respective average scores given.
for value in range(len(averages)):
    print("Average score given by "+judges[value]+" is "+averages[value])
