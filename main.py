# This program calculates your age in the year 2050.
# Input:  Your current age, follwed by current year.
# Output: Your current age followed by your age in 2050.
# Variables are 'myCurrentAge', and 'currentYear'.

myCurrentAge = int(input ("Please put your current age "))

currentYear = int(input ("Please put your current year "))

myNewAge = myCurrentAge + (2050 - currentYear)

print("My Current Age is " + str(myCurrentAge))
print("I will be " + str(myNewAge) + " in 2050.")
