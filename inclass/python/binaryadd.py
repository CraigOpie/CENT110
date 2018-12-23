"""
Craig Opie
CENT110

This program adds two, two digit binary numbers and displays the sum for the user.
This is accomplished by: 
	1) Receiving the information from the user.
	2) Generate the sum of the two least significant bits.
	3) Generate the carry of the two least significant bits.
	4) Gererate the sum of the two most significant bits and the carry.
	5) Generate the carry of the sum of the two most significant bits and previous carry.
	6) Display the final values reading from left to right, MSB to LSB.
"""
	
print("This program is a full adder designed to add two, two digit binary numbers.")
a1=int(input("Enter the most significant bit of the first number: "))
a0=int(input("Enter the least significant bit of the first number: "))
b1=int(input("Enter the most significant bit of the second number: "))
b0=int(input("Enter the least significant bit of the second number: "))

y0=((~a0 & b0) or (a0 & ~b0))
carry=(a0 & b0)
y1=(~((~a1 & b1) or (a1 & ~b1)) & carry) or (((~a1 & b1) or (a1 & ~b1)) & ~carry)
y2=((((~a1 & b1) or (a1 & ~b1)) & carry)|(a1 & b1))

print("Your sum is: "+str(y2)+str(y1)+str(y0))
