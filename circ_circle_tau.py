#!/usr/bin/env python3
# Created By: Volodymyr Kryzhanovskyi
# Date: 03/03/2025
# It calculates the circumference of circle using tau
import constants

def main():
    radius = float(input("Enter the radius of a circle:"))
    #Gets radius of a circle from the user
    circumference = constants.TAU * radius
    #Calculate the circumference
    print("Circumference = {} cm".format(circumference))
#Display the circumference.
if __name__ == "__main__":
    main()