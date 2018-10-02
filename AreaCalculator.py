"""
This script calculates area of shape that is selected by user.
And prints out calculations.
"""

print("Program is running...")

option = input("Enter C for Circle or T for Triangle: ")

if option == "C" or option == "c":
    radius = float(input("Enter desirable radius: "))
    pi = 3.14159
    area = pi ** radius
    print("area of circle is {}".format(area))
elif option == "T" or option == "t":
    base = float(input("Enter a base: "))
    height = float(input("Enter a height: "))
    area = (base * height) * .5
    print("area of triangle is {}".format(area))
else:
    print("Invalid shape. Try again")

print("Finishing the program...")