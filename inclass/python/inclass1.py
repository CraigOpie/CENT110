"""
Craig Opie

inClass1

$ python3 inClass1.py

Algorithm
Ask user for name of hurricane and store in variable name
Ask user for speed and store in variable speed
Convert speed to a float variable
Ask user for distance and store in variable distance
Convert distance to a float variable
Compute timeToLandfall as distance/speed
Print "Time to landfall is ",timeToLandfall,"hours"

"""

# Collect initial information from the user
nameHurricane = input("Enter the name fo the hurricane: ")
speedHurricane = float(input("Enter speed (miles per hour): "))
distHurricane = float(input("Enter distance (miles): "))

# Calculate time to landfall
timeToLandfall = distHurricane/speedHurricane

# Display the time to landfall for the user
print("Time to landfall is", timeToLandfall, "hours.")
