#!/usr/bin/env python
"""
Name:   Craig Opie
Class:  CENT110
File:   project1.py

Algorithm:
1)  Add support for PySide and PySide2:
    a. Import required modules from PySide.
    b. Port the PySide.QtGui as QtWidgets to support the code written in PySide2.
    c. If PySide is not installed:
    d. Import required modules from PySide2.
2)  Import the sys module.
3)  Create a class(object) named MyGui using the properties of the object from PySide, QMainWindow.
4)  Define the function '__init__' (standard library) for initiation of the object importing any properties of the object itself (from here on referenced as self).
    a. Setup the Main Dialog Box 'self' properties:
        1.  Execute the initiation of the object QMainWindow from PySide.
        2.  Create a new instance of the object 'QTextEdit' in self and name it 'text'.
        3.  Make it so that 'text' is read only.
        4.  Make 'text' fill the dialog box as the central widget.
        5.  Make the Main Dialog Box (self) 250x250 pixels away from the upper left corner of the screen and 700x400 pixels large.
        6.  Make the title in the uppermost portion of 'self' read "Craig Opie - Project 1".
        7.  Create 'self' as a Dialog Box and make it visible.
    b. Establish 'self' wide variables (simular to Public for other languages).
        1.  'allPriceList' as a list for all prices.
        2.  'appPriceList' as a list for appetizer prices.
        3.  'entreePriceList' as a list for entree prices.
        4.  'dessertPriceList' as a list for dessert prices.
        5.  'otherPriceList' as a list for all other items' prices.
        6.  'data_' as a string containing the xml header information and formatting.
        7.  'closingData' as a string for the closing information that will be added after content.
        8.  'finalData' as a string for combining the 'data_' and 'closingData' strings.
        9.  'itemList' as a string that will be split into a list of items.
        10. 'splitData' as a string from the user input that will be split.
        11. 'foodBox' as a string that will contain the text from the widget 'foodBox'.
        12. 'typeBox' as a string that will contain the text from the widget 'typeBox'.
        13. 'typeBoxString' as a string that will contain the properly formatted information in 'typeBox' used for comparison operations.
        14. 'priceBox' as a float that will contain the value from the widget 'priceBox'.
        15. 'max_price' as a float that will contain the highest price of all the items.
        16. 'min_price' as a float that will contain the lowest price of all the items.
5)  Define a function called 'initMenu' for 'self' that will create a menu bar on Main Dialog Box.
    a.  Create a new instance of the object 'menuBar' from PySide.
    b.  Create a new instance of a 'menuBar' function called 'addMenu' where we define 'file'.
    c.  Add the following items to the 'file' in 'menuBar':
        1.  Create a new selectable object named 'addItem' which displays "Add Item".
        2.  If 'addItem' is selected perform the function 'addItem' in 'self'.
        3.  Display the object 'addItem' in the 'menuBar' under 'file'.
        4.  Create a new selectable object named 'save_' which displays "Save".
        5.  If 'addItem' is selected perform the function 'saveFile' in 'self'.
        6.  Display the object 'save_' in the 'menuBar' under 'file'.
        7.  Create a new selectable object named 'open_' which displays "Open".
        8.  If 'addItem' is selected perform the function 'openFile' in 'self'.
        9.  Display the object 'open_' in the 'menuBar' under 'file'.
        10. Create a new selectable object named 'quit_' which displays "Quit".
        11. If 'addItem' is selected perform the function 'quitFile' in 'self'.
        12. Display the object 'quit_' in the 'menuBar' under 'file'.
6)  Define a function called 'saveFile' for 'self' that will allow the user to save the information in 'text' to a plain text file format.
    a.  Appends user input into a string with pre-selected split identifiers to sort into prepare the data to be split.
        1.  Split 'splitData' anywhere "\n" is present and append line to 'itemList'.
        2.  For eachline in 'itemList':
            i.  Split 'itemList' anywhere "|" is present and append items to a list named 'items'.
            ii. Append str("\n    <item>") to 'data_'.
            iii.Append str("\n        <name>'items[0]'</name>") to 'data_'.
            iv. Append str("\n        <foodType>'items[1]'</foodType") to 'data_'.
            v.  Append str("\n        <price>'items[2]'</price>") to 'data_'.
            vi. Append str("\n    </item>") to 'data_'.
    b.  Append the closing tags and final mxl data to 'closingData'.
        1.  Append str("\n    <overallAvg>'overallAvg'</overallAvg>") to 'closingData'.
        2.  Append str("\n    <appAvg>'appAvg'</appAvg>") to 'closingData'.
        3.  Append str("\n    <entreeAvg>'entreeAvg'</entreeAvg>") to 'closingData'.
        4.  Append str("\n    <dessertAvg>'dessertAvg'</dessertAvg>") to 'closingData'.
        5.  Append str("\n    <otherAvg>'otherAvg'</otherAvg>") to 'closingData'.
        6.  Append str("\n    <priceRange>")
        7.  Append str("\n        <maximum>'max_price'</maximum>") to 'closingData'.
        8.  Append str("\n        <minimum>'min_price'</minimum>") to 'closingData'.
        9.  Append str("\n    </priceRange>") to 'closingData'.
        10. Append str("\n</menu>") to 'closingData'.
    c.  Concatenate 'startData' + 'userData' + 'closingData' and assign to 'finalData'.
    d.  Open a save file dialog box and allow the user to select location and name for the file.
    e.  If the user specifies a filename:
        1.  Create a new document with write abilities and assign it to the variable 'outfile'.
        2.  Create a new variable 'contents' and assign the text stored in 'text'.
        3.  Write the value of 'contents' to 'outfile'.
        4.  Close 'outfile'.
7)  Define a function called 'openFile' for 'self' that will allow the user to open the information in a plain text file and display in 'text'.
    a.  Open an open file dialog box and allow the user to select location and name for the file.
    b.  If the user specifies a filename:
        1.  Open the document with read abilities and assign it to the variable 'infile'.
        2.  Create a new variable 'contents' and assign the text stored in 'infile'.
        3.  Write the value of 'contents' to 'text'.
        4.  Close 'infile'.
8)  Define a function called 'addFile' for 'self' that will open a Child Dialog Box for the user to enter values to be stored in an xml file.
    a.  Setup the Child Dialog Box properties.
        1.  Create a new instance of QDialog for 'self' named 'myDialog'.
        2.  Set 'myDialog' title to display "Enter Data".
        3.  Set 'myDialog' to open 350x350 pixels away from the top left corner of the screen and 400x200 pixels large.
        4.  Create a new instance of 'QGridLayout' named 'layout'.
        5.  Set 'myDialog' to use 'layout'.
    b.  Create a first row of widgets for user input.
        1.  Create a label named 'labelFood' that contains the text "Enter Food".
        2.  Place 'labelFood' in the first column on the first row.
        3.  Create a text box named 'foodBox' that allows the user to input text.
        4.  Place 'foodBox' in the second column on the first row.
        5.  Assign 'foodBox' text to the 'self' variable 'foodBox'.
    c.  Create a second row of widgets for user input.
        1.  Create a label named 'labelType' that contains the text "Enter Type".
        2.  Place 'labelType' in the first column on the second row.
        3.  Create a text box named 'typeBox' that allows the user to input text.
        4.  Place 'typeBox' in the second column on the first row.
        5.  Assign 'typeBox' text to the 'self' variable 'typeBox'.
    d.  Create a third row of widgets for user input.
        1.  Create a label named 'labelPrice' that contains the text "Enter Price".
        2.  Place 'labelPrice' in the first column on the third row.
        3.  Create a text box named 'priceBox' that allows the user to input text.
        4.  Place 'priceBox' in the second column on the third row.
        5.  Assign 'priceBox' text to the 'self' variable 'priceBox'.
    e.  Creates a third column for buttons that are styled for the user.
        1.  Create an instance of 'QDialogButtonBox' named 'buttons'.
        2.  Set the orientation of 'buttons' to be vertical.
        3.  Create a button with the text "Add" and assign it the role of accepted.
        4.  Create a button with the text "Cancel" and assign it the role of reject.
        5.  Connect the rejected role to the close function.
        6.  Connect the accepted role to the 'appendList' function of 'self'.
        7.  Change the button layout to be centered vertically and horizontally, spanned over the three rows.
    f.  Execute the above code and create the Child Dialog Box to see.
9)  Define a function called 'appendList' for 'self' that will take the information from the user input append it to a string, split the string into a list, add items from the list to a string in xml format, and set the Main Dialog Box 'text' to be a new xml string.
    a.  If there are previous entries from the user:
        1.  Compare 'priceBox' and 'max_price' and store the larger amount in 'max_price'.
        2.  Compare 'priceBox' and 'min_price' and store the smaller amount in 'min_price'.
    b.  If there aren't any previous entries from the user:
        1.  Store the value in 'priceBox' in 'max_price'.
        2.  Store the value in 'priceBox' in 'min_price'.
    c.  Sort item prices based off type of food and store the values in the associated list.
        1.  Append the value in 'priceBox' to the list 'allPriceList'.
        2.  Convert the value in 'typeBox' to lowercase and remove whitespace in the front and back of the value and store the new value in 'typeBoxString'.
        3.  If typeBoxString == "appetizer":
            i.  Append the value in 'priceBox' into the list 'appPriceList' as a float.
        4.  Elif typeBoxString == "entree":
            i.  Append the value in 'priceBox' into the list 'entreePriceList' as a float.
        5.  Elif typeBoxString == "dessert":
            i.  Append the value in 'priceBox' into the list 'dessertPriceList' as a float.
        6.  Else:
            i.  Append the value in 'priceBox' into the list 'otherPriceList' as a float.
    d.  Prevent averaged values from dividing by zero and causing a math error:
        1.  If there are values in 'allPriceList':
            i.  'overallAvg' = the sum of values in 'allPriceList' divided by the number of values in 'allPriceList'.
        2.  If there aren't values in 'allPriceList':
            i.  'overallAvg' = the sum of values in 'allPriceList' divided by 1.00.
        3.  If there are values in 'appPriceList':
            i.  'appAvg' = the sum of values in 'appPriceList' divided by the number of values in 'appPriceList'.
        4.  If there aren't values in 'appPriceList':
            i.  'appAvg' = the sum of values in 'appPriceList' divided by 1.00.
        5.  If there are values in 'entreePriceList':
            i.  'entreeAvg' = the sum of values in 'entreePriceList' divided by the number of values in 'entreePriceList'.
        6.  If there aren't values in 'entreePriceList':
            i.  'entreeAvg' = the sum of values in 'entreePriceList' divided by 1.00.
        7.  If there are values in 'dessertPriceList':
            i.  'dessertAvg' = the sum of values in 'dessertPriceList' divided by the number of values in 'dessertPriceList'.
        8.  If there aren't values in 'dessertPriceList':
            i.  'dessertAvg' = the sum of values in 'dessertPriceList' divided by 1.00.
        9.  If there are values in 'otherPriceList':
            i.  'otherAvg' = the sum of values in 'otherPriceList' divided by the number of values in 'otherPriceList'.
        10. If there aren't values in 'otherPriceList':
            i.  'otherAvg' = the sum of values in 'otherPriceList' divided by 1.00.
    e.  Appends user input into a string with selected split identifiers to sort into lists:
        1.  Appends 'foodBox' value concatenated with "|" to 'splitData'.
        2.  Appends 'typeBox' value concatenated with "|" to 'splitData'.
        3.  Appends 'priceBox' value concatenated with "\n" to 'splitData'.
    f.  Assign 'text' = 'splitData' to display xml in Main Dialog Box.
    g.  Close the Child Dialog Box after Main Dialog Box is ready.
10) Define a function called 'closeFile' for 'self' that will exit the application.
    a.  Close 'self'.
11) Create a new instance of 'QApplication' with "sys.argv" properties named 'app'.
12) Create a new instance of 'MyGui' named 'mygui'.
13) Run PySide and only exit PySide upon closing 'mygui'.
"""

# Import from PySide or PySide2 (QtWidgets)
try:
    from PySide import QtGui, QtCore
    import PySide.QtGui as QtWidgets
except ImportError:
    from PySide2 import QtGui, QtCore, QtWidgets
import sys

# Creates the Main Dialog Box as an Object (Class)
class MyGui(QtWidgets.QMainWindow):
    """ Main Dialog Box that allow reading plain text files """
    def __init__(self):
        """ Initiallizes the Main Dialog Box and establishes object variables """
        # Setup the Main Dialog Box properties
        QtWidgets.QMainWindow.__init__(self)
        self.initMenu()
        self.text = QtWidgets.QTextEdit()
        self.text.setReadOnly(True)
        self.setCentralWidget(self.text)
        self.setGeometry(250,250,700,400)
        self.setWindowTitle("Craig Opie - Project 1")
        self.show()

        # Establish Object wide variables
        self.allPriceList = []
        self.appPriceList = []
        self.entreePriceList = []
        self.dessertPriceList = []
        self.otherPriceList = []
        self.startData = str('<?xml version="1.0" ?>\n\n<menu>')
        self.userData = ""
        self.closingData = ""
        self.finalData = ""
        self.itemList = ""
        self.splitData = ""
        self.foodBox = ""
        self.typeBox = ""
        self.typeBoxString = ""
        self.overallAvg = 0.00
        self.appAvg = 0.00
        self.entreeAvg = 0.00
        self.dessertAvg = 0.00
        self.otherAvg = 0.00
        self.priceBox = 0.00
        self.max_price = 0.00
        self.min_price = 0.00

    def initMenu(self):
        """ Creates the Main Dialog Box menu items """
        menubar = self.menuBar()
        fileMenu = menubar.addMenu("File")

        # Opens a new Dialog for user input into pre-determined fields
        addItem = QtWidgets.QAction("Add Item", self)
        addItem.triggered.connect(self.addItem)
        fileMenu.addAction(addItem)

        # Opens a save Dialog for the user to save the displayed information
        save_ = QtWidgets.QAction("Save", self)
        save_.triggered.connect(self.saveFile)
        fileMenu.addAction(save_)

        # Opens a load Dialog for the user to load a plain text file to be displayed
        open_ = QtWidgets.QAction("Open", self)
        open_.triggered.connect(self.openFile)
        fileMenu.addAction(open_)

        # Allows the user to quit the application
        quit_ = QtWidgets.QAction("Quit", self)
        quit_.triggered.connect(self.closeFile)
        fileMenu.addAction(quit_)

    def saveFile(self):
        """ Saves information displayed in the Main Dialog Box to an xml format """
        # Sorts the user input into lists and appends xml data to a string for the Main Dialog Box
        self.itemList = self.splitData.strip().split("\n")
        for eachline in self.itemList:
            items = eachline.split("|")
            self.userData += str("\n    <item>")
            self.userData += str("\n        <name>"+items[0]+"</name>")
            self.userData += str("\n        <foodType>"+items[1]+"</foodType>")
            self.userData += str("\n        <price>"+items[2]+"</price>")
            self.userData += str("\n    </item>")

        # Appends closing and final xml data to a string that is to be combined with the previous
        # String xml data
        self.closingData = str("\n    <overallAvg>"+str("%.2f" % (self.overallAvg))+"</overallAvg>")
        self.closingData += str("\n    <appAvg>"+str("%.2f" % (self.appAvg))+"</appAvg>")
        self.closingData += str("\n    <entreeAvg>"+str("%.2f" % (self.entreeAvg))+"</entreeAvg>")
        self.closingData += str("\n    <dessertAvg>"+str("%.2f" % (self.dessertAvg))+"</dessertAvg>")
        self.closingData += str("\n    <otherAvg>"+str("%.2f" % (self.otherAvg))+"</otherAvg>")
        self.closingData += str("\n    <priceRange>")
        self.closingData += str("\n        <maximum>"+str("%.2f" % (self.max_price))+"</maximum>")
        self.closingData += str("\n        <minimum>"+str("%.2f" % (self.min_price))+"</minimum>")
        self.closingData += str("\n    </priceRange>")
        self.closingData += str("\n</menu>")

        # Creates a final string of xml data to be displayed in the Main Dialog Box
        self.finalData = str(self.startData) + str(self.userData) + str(self.closingData)

        # Opens a Dialog Box for the user to select name and location of file to save 'finalData'
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save File",".")
        if (filename != ""):
            outfile = open(filename, "w")
            contents = self.finalData
            outfile.write(contents)
            outfile.close()

    def openFile(self):
        """ Opens a plain text file to display in the Main Dialog Box """
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open File",".")
        if (filename != ""):
            infile = open(filename, "r")
            contents = infile.read()
            infile.close()
            self.text.setText(contents)

    def addItem(self):
        """ Creates a Child Dialog Box with user input fields to display in the Main Dialog Box """
        # Setup the Child Dialog Box properties
        self.myDialog = QtWidgets.QDialog(self)
        self.myDialog.setWindowTitle("Enter Data")
        self.setGeometry(350,350,400,200)
        layout = QtWidgets.QGridLayout()
        self.myDialog.setLayout(layout)

        # Create the first row of widgets for user input
        labelFood = QtWidgets.QLabel("Enter Food")
        layout.addWidget(labelFood,0,0)
        foodBox = QtWidgets.QLineEdit()
        layout.addWidget(foodBox,0,1)
        self.foodBox = foodBox

        # Create the second row of widgets for user input
        labelType = QtWidgets.QLabel("Enter Type")
        layout.addWidget(labelType,1,0)
        typeBox = QtWidgets.QLineEdit()
        layout.addWidget(typeBox,1,1)
        self.typeBox = typeBox

        # Create the third row of widgets for user input
        labelPrice = QtWidgets.QLabel("Enter Price")
        layout.addWidget(labelPrice,2,0)
        priceBox = QtWidgets.QLineEdit()
        layout.addWidget(priceBox,2,1)
        self.priceBox = priceBox

        # Creates a third column for buttons that are styled and allows user control
        buttons = QtWidgets.QDialogButtonBox()
        buttons.setOrientation(QtCore.Qt.Vertical)
        buttons.addButton("Add",QtWidgets.QDialogButtonBox.AcceptRole)
        buttons.addButton("Cancel",QtWidgets.QDialogButtonBox.RejectRole)
        # Exits the Child Dialog Box without saving/appending information to the Main Dialog Box
        self.myDialog.connect(buttons,QtCore.SIGNAL("rejected()"),self.myDialog.close)
        # Exits the Child Dialog Box but saves/appends information to the Main Dialog Box
        self.myDialog.connect(buttons,QtCore.SIGNAL("accepted()"),self.appendList)
        layout.addWidget(buttons,0,2,3,1,QtCore.Qt.AlignCenter)

        # Executes the above code to create the Child Dialog Box
        self.myDialog.exec_()

    def appendList(self):
        """ Updates lists and variables from the user input to display in the Main Dialog Box """
        # If there are no previous entries the Max and Min values are set to equal the first entry
        # Otherwise, the item price entered is compared to see if it is the new Max or Min
        if len(self.allPriceList) != 0:
            if float(self.priceBox.text().strip()) > self.max_price:
                self.max_price = float(self.priceBox.text().strip())
            if float(self.priceBox.text().strip()) < self.min_price:
                self.min_price = float(self.priceBox.text().strip())
        else:
            self.max_price = float(self.priceBox.text().strip())
            self.min_price = float(self.priceBox.text().strip())

        # Sorts item price based off type of food and stores in a list for statistics
        self.allPriceList.append(float(self.priceBox.text().strip()))
        self.typeBoxString = self.typeBox.text().lower().strip()
        if str(self.typeBoxString) == "appetizer":
            self.appPriceList.append(float(self.priceBox.text().strip()))
        elif str(self.typeBoxString) == "entree":
            self.entreePriceList.append(float(self.priceBox.text().strip()))
        elif str(self.typeBoxString) == "dessert":
            self.dessertPriceList.append(float(self.priceBox.text().strip()))
        else:
            self.otherPriceList.append(float(self.priceBox.text().strip()))

        # Prevents averaged values from dividing by zero and causing an error
        if len(self.allPriceList) > 0:
            self.overallAvg = (sum(self.allPriceList)/len(self.allPriceList))
        else:
            self.overallAvg = (sum(self.allPriceList)/1.00)
        if len(self.appPriceList) > 0:
            self.appAvg = (sum(self.appPriceList)/len(self.appPriceList))
        else:
            self.appAvg = (sum(self.appPriceList)/1.00)
        if len(self.entreePriceList) > 0:
            self.entreeAvg = (sum(self.entreePriceList)/len(self.entreePriceList))
        else:
            self.entreeAvg = (sum(self.entreePriceList)/1.00)
        if len(self.dessertPriceList) > 0:
            self.dessertAvg = (sum(self.dessertPriceList)/len(self.dessertPriceList))
        else:
            self.dessertAvg = (sum(self.dessertPriceList)/1.00)
        if len(self.otherPriceList) > 0:
            self.otherAvg = (sum(self.otherPriceList)/len(self.otherPriceList))
        else:
            self.otherAvg = (sum(self.otherPriceList)/1.00)

        # Appends user input into a string with selected split identifiers to sort into lists
        self.splitData += str(self.foodBox.text().title().strip() + "|")
        self.splitData += str(self.typeBox.text().title().strip() + "|")
        self.splitData += str("%.2f" % (float(self.priceBox.text().strip())) + "\n")

        # Sets the value of the Main Dialog Box
        self.text.setText(self.splitData)

        # Closes the Child Dialog after the Main Dialog Box is displaying the updated data.
        self.myDialog.done(0)

    def closeFile(self):
        self.done(0)

# Specifies the variable that references Qt module data
app = QtWidgets.QApplication(sys.argv)

# Creates an instance of the MyGui Class/Object
mygui = MyGui()

# Executes the above code to create the Main Dialog Box
sys.exit(app.exec_())
