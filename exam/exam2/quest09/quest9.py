#!/usr/bin/env python
"""
Name: 	Craig Opie
Class:	CENT110
File:	quest9.py
Algorithm:
1)  Create a new file named 'reviews.csv' and assign it to 'outfile'.
2)  Ask the user to enter the product name and store in 'product'.
3)  Ask the user to enter the number of reviews and store in 'numReview'.
4)  Write the 'product' to the first line in 'outfile'.
5)  Create an exit condition for the while loop 'num'.
6)  Create a while loop where the loop will continue until the user has 
entered the number of reviews provided 'numReview':
	a.  Ask the user for the review and store in 'review'.
	b.  Ask the user for the rating and store in 'rating'.
	c.  Write the 'review' and 'rating' to 'outfile' separated by "|".
	d.  Increase 'num' by one.
7)  Close 'outfile'.
"""
# Create file named reviews.csv
outfile = open("reviews.csv", "w")

# Have the user provide the product name and number of reviews
product = input("Enter the product: ")
numReview = input("Enter number of reviews: ")

# Write the product name to the csv file
outfile.write(product)

# Create a loop that asks the user for the review and rating then writes
# the information to the csv file
num = 1
while (num <= int(numReview)):
	review = input("Enter review "+str(num)+": ")
	rating = input("Enter rating(out of 5): ")
	outfile.write("\n"+review+"|"+rating)
	num += 1

# Close the csv file
outfile.close()
	
