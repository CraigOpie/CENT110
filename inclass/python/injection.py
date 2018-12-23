"""
Craig Opie
CENT110
injection.py

This code will demonstrate how to inject bad code into our interpreter
must be run with python 2.7 or older.
"""

import random

rnum = str(random.randint(1,11))
print("Choose a number between 1 and 10.")

while True:
    res = input("Guess a number: ")
    if res == rnum:
        print("Congrats, You win!")
        break
    else:
        continue
