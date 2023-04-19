#calculate circumfrence of a circle

import math

def getRadius(): #requests input for radius
    radius = input("Enter circle radius:\n")
    try: #checks if the input is a valid number
        radius = float(radius)
    except: #recalls function if it is not
        print("Invalid Radius Given!\n")
        getRadius()

    calculateCircumfrence(radius)


def calculateCircumfrence(radius): #calculates circumfrence
    circum = radius * math.pi * 2
    circum = round(circum, 2) #rounds off circumfrecnce to two decimal places
    print("Circumfrence = " + str(circum))
    print("\nbye")


getRadius()