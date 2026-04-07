#Prompt the user to enter the coordinates of two points in a 2D plane (x1, y1) and (x2, y2)
import math

# Input
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# Processing
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Output
print("The distance between the two points is:", distance)