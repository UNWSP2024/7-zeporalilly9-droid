# Program #4: Coordinates
# Write a distance function that will take two 3-dimensional coordinates (as input) 
# and will return (as output) the distance between those points in space.  
# The 3-dimensional coordinates must be stored as tuples.

# Now write a mainline that has the user enter the two tuples.  
# The mainline calls the distance function and stores the distance in a variable.  The mainline then displays the distance.  
# Also include exception handling to deal with faulty input.
# The distance between two points (x1,y1,z1) and (x2, y2, z2) is 
#    given by:   sqrt ((x2-x1)^2 + (y2 - y1)^2 + (z1 - z2)^2) 

# Function to calculate distance between two 3D points
# Program #4: Coordinates
# Author: Zepora Lilly
# Date: 10/14/2025
import math

def distance(coord1, coord2):
    x1, y1, z1 = coord1
    x2, y2, z2 = coord2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

def main():
    try:
        coord1_input = input("Enter the first 3D coordinate (x,y,z): ")
        coord1 = tuple(map(float, coord1_input.split()))

        coord2_input = input("Enter the second 3D coordinate (x,y,z): ")
        coord2 = tuple(map(float, coord2_input.split()))

        if len(coord1) != 3 or len(coord2) != 3:
            raise ValueError("Each coordinate must have exactly 3 values.")

        dist = distance(coord1, coord2)
        print(f"The distance between the points is: {dist:.2f}")

    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"Unexpected error: {e}")

main()
