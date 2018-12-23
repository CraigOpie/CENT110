#!/usr/bin/env python
"""
CENT 110
Craig Opie
hw2.py

Task:
A)  Gathers user input to create a simple HTML document. The
program should prompt for the user's name, major, and last programming
course taken.
B)  Generate a HTML output as shown below:
<html> 
  <head> 
    <link rel="stylesheet" type="text/css" href="hw2.css" /> 
  </head> 
  <body> 
    <p class="name">Craig Opie</p> 
    <p class="major">CENT</p> 
    <p class="last_prog_course">C</p> 
  </body> 
</html>

1. Import os and webbrowser modules for deleting previous files and
opening new files in a browser.
2. Provide a method for the users to input their name, major, and last
programming course taken.
3. Use the user provided input to generate content for the new HTML
file
4. Generate the content for the CSS file
5. Remove previous files prior to saving to prevent errors
6. Generate the HTML file
7. Generate the CSS file
8. Launch the newly made file in the default browser

"""
# Import modules for deleting previous files and opening new files
import os 
import webbrowser

# Provides data to populate the web page
name = input("Please enter your name: ").title()
major = input("Please enter your major: ").upper()
lastProgCourse = input("Please enter your last programming course taken: ").title()

# Provides content for the file that will be generated later
contentsHTML = str("""
<html> 
  <head> 
    <link rel="stylesheet" type="text/css" href="hw2.css" /> 
  </head> 
  <body> 
    <p class="name">"""+name+"""</p> 
    <p class="major">"""+major+"""</p> 
    <p class="last_prog_course">"""+lastProgCourse+"""</p> 
  </body> 
</html>
""")

# Provides content for the CSS file that will be generated later
contentsCSS = str("""
p.name {
    font-size: 140%;
    color: red;
}
p.major {
    font-size: 120%;
    color: blue;
}
p.last_prog_course {
    font-size: 120%;
    font-style: italic;
    color: green;
}
""")

# Prevents error code by removing any existing files with old content
if os.path.exists("hw2.html"):
    os.remove("hw2.html")
if os.path.exists("hw2.css"):
    os.remove("hw2.css")

# Creates HTML file using previous content
doc = open("hw2.html", "a")
doc.write(contentsHTML)
doc.close()

# Creates CSS file using previous content
doc = open("hw2.css", "a")
doc.write(contentsCSS)
doc.close()

# Launches new HTML file in default web browser
webbrowser.open("file://" + os.path.realpath("hw2.html"))
