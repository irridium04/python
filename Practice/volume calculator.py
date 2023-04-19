# Collin Shook
# 9-8-2022
# Volumes of shapes

import math

def main():
    print("------ Volume Of Cylinder ------\n")

    r = float(input("enter radius:\n"))
    h = float(input("enter height:\n"))

    v = calcVolCyl(r, h)

    print(f"The volume of a cylinder with radius {r} and height {h} is {v}\n")

    calcVolCone()

    print("\n\nGoodbye\n\n")
    

def calcVolCyl(r, h):
    v = round(math.pi * h * (r ** 2), 2)
    return v


def calcVolCone():
    print("------ Volume Of Cone ------\n")
    r = float(input("enter base radius:\n"))
    h = float(input("enter height:\n"))
    v = round((math.pi * h * (r ** 2)) / 3.0, 2)
    print(f"The volume of a cone with a base radius {r} and height {h} is {v}\n")


main()