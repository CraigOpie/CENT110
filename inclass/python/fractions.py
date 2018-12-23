#!/usr/bin/env python
"""
CENT 110
Craig Opie
fractions.py

Algorithm
A) Create an Object known as a fraction that contains a numerator and
denominator. 
B) This object should know how to add, subtract, multiply
and divide simmilar objects.

1) Create an object named "fraction".
2) Initilize the object and force the object to contain two integers,
a numerator and denominator.
3) Create a method that will return a string representation of the 
object.
4) Create a method that will add the numerator and common denominator
of two fractions and create a new object of the result.
5) Create a method that will subtract the numerator and common 
denominator of two fractions and create a new object of the result.
6) Create a method that will multiply the numerator and denominator
of two fractions and create a new object of the result.
7) Create a method that will divide the numerator and denominator
of two fractions and create a new object of the result.
8) Create a method that will return the float value of a fraction.
9) Create a method that will inverse the values of a fraction.
10) Allow input from the user to provide fraction values and 
mathmatical functions.
11) Display the normal representation of the math statement for the 
user to review and provide the answer for the mathmatical function
performed.

"""

class fraction(object):
    """
    Number represented as a fraction.
    """
    def __init__(self, num, denom):
        """
        Numerator and denominators must be integers.
        """
        assert type(num) == int and type(denom) == int
        self.num = num
        self.denom = denom
    def __str__(self):
        """
        Print the human way of representing a fraction.
        """
        return str(self.num) + "/" + str(self.denom)
    def __add__(self, other):
        """
        Returns a fraction representing the two inputs added together.
        """
        top = self.num * other.denom + self.denom * other.num
        bottom = self.denom * other.denom
        return fraction(top, bottom)
    def __sub__(self, other):
        """
        Returns a fraction representing the two inputs subtracted from each other.
        """
        top = self.num * other.denom - self.denom * other.num
        bottom = self.denom * other.denom
        return fraction(top, bottom)
    def __multiply__(self, other):
        """
        Returns a fraction representing the multiplication of the two inputs.
        """
        top = self.num * other.num
        bottom = self.denom * other.denom
        return fraction(top, bottom)
    def __divide__(self, other):
        """
        Returns a fraction representing the division of the two inputs.
        """
        top = self.num * other.denom
        bottom = self.denom * other.num
        return fraction(top, bottom)
    def __float__(self):
        """
        Returns a float value of the fraction,
        """
        return self.num / self.denom
    def __inverse__(self):
        """
        Returns a new fraction representing the inverse of the input.
        """
        return fraction(self.denom, self.num)
    def __simplify__(self):
        """ 
        Finds the common factor and simplifies the fraction.
        """
        top = self.num
        bottom = self.denom
        factor = bottom
        while bottom >= factor:
            if bottom % factor == 0:
                if top % factor == 0:
                    top = int(top/factor)
                    bottom = int(bottom/factor)
                    if bottom == 1:
                        print(top)
                        break
                    else:
                        return fraction(top, bottom)
                    continue
            else:
                factor = factor - 1

# Collect input from the user for our class.
a = int(input("Enter numerator: "))
b = int(input("Enter denominator: "))
f = fraction(a, b)

# Must be +, -, *, /, float or inverse.
c = input("Enter function (+, -, *, /, float, inverse, or simplify: ")

# Performs the function as specified by the user above.
if c == "inverse":
    z = fraction.__inverse__(f)
    print(z)
elif c == "float":
    z = fraction.__float__(f)
    print(z)
elif c == "simplify":
	z = fraction.__simplify__(f)
	print(z)
else:
    # Allows for user input of a second fraction.
    d = int(input("Enter numerator: "))
    e = int(input("Enter denominator: "))
    g = fraction(d, e)

    # Provides feedback on the user's inputs.
    print("\nYou entered: \n"+"\n"," "+str(f),"\n"+c,str(g)+"\n"+"----------")

    if c == "+":
        z = fraction.__add__(f, g)
        print(" "+str(z),"\n")

    if c == "-":
        z = fraction.__sub__(f, g)
        print(" "+str(z),"\n")

    if c == "*":
        z = fraction.__multiply__(f, g)
        print(" "+str(z),"\n")

    if c == "/":
        z = fraction.__divide__(f, g)
        print(" "+str(z),"\n")
