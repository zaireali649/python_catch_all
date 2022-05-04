# script to calculate surface area of cylinder

# Import Libraries
import math
import random

# function for calculating surface area of cylinder
# (2 * math.pi * radius * height) + (2 * math.pi * radius ** 2)
def surface_area_cylinder(radius, height):
    SA = (2 * math.pi * radius * height) + (2 * math.pi * radius ** 2)
    return SA

# print tests
print(abs(surface_area_cylinder(1, 1) - 12.57) < .01 )
print(abs(surface_area_cylinder(5, 15) - 628.32) < .01 )

# input values
r = float(input("Enter radius: "))
h = float(input("Enter height: "))

# print sa
print(surface_area_cylinder(r, h))

# random values
r2 = float(random.uniform(0, 15))
h2 = float(random.uniform(0, 15))

# print sa
print("radius: ", r2)
print("height: ", h2)
print(surface_area_cylinder(r2, h2))
