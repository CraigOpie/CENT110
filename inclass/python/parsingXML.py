#!/usr/bin/env python
"""
Names:	Team Awesome (Craig Opie)
Class: 	CENT110
File:	hw8.py

Algorithm:
"""
from bs4 import BeautifulSoup as bs
from json import dumps

def makeNameTags(name, major):
	print(name+"\n"+major)

with open("students.xml") as infile:
	contents = infile.read()
	
soup = bs(contents, "xml")
students = soup.find_all("student")

studentsDict = {}
studentsList = []
for person in students:
	student = {}
	name = person.find("name").get_text()
	major = person.find("major").get_text()
	student["name"] = name
	student["major"] = major
	studentsList.append(student)
	
studentsDict["students"] = studentsList

with open("students.json", "w") as outfile:
	outfile.write(dumps(studentsDict, indent=4, separators=(","," : "), sort_keys=True))
