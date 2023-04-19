# Collin Shook
# Assignment 2
# 9-8-2022

def main():
    # Q1
    print("\n-------- Greeting Message --------\n")

    greet()


    # Q2
    print("\n-------- Calculate Area Of A Triangle --------\n")
    print("-------- A --------\n")

    b = float(input("Please enter base length:\n"))
    h = float(input("Please enter height:\n"))
    a = AreaOfTriangle_a(b, h)

    print(f"A triangle with base length {b} and height {h} has an area of {a}.")

    print("\n-------- B --------\n")

    b = float(input("Please enter base length:\n"))
    h = float(input("Please enter height:\n"))
    AreaOfTriangle_b(b, h)

    print("-------- C --------\n")

    a = AreaOfTriangle_c()

    print(f"The triangle has an area of {a}.")

    print("-------- D --------\n")

    AreaOfTriangle_d()


    # Q3
    print("\n-------- Miles Per Hour To Knots --------\n")

    mph = float(input("Please enter speed in mph:\n"))
    knt = MphToKnt(mph)
    print(f"{mph} mph is {knt} knts")


    # Q4
    print("\n-------- Knots To Miles Per Hour --------\n")

    knt = float(input("Please enter speed in knts:\n"))
    mph = KntToMph(knt)
    print(f"{knt} knts is {mph} mph")


    # Q5
    print("\n-------- Average Of Three Numbers --------\n")

    a = float(input("Enter first number:\n"))
    b = float(input("Enter second number:\n"))
    c = float(input("Enter third number:\n"))

    d = AvgThreeNums(a, b, c)

    print(f"The average of {a}, {b}, and {c} is {d}.")


    # Q6
    print("\n-------- Calculate Gross Income --------\n")

    CalcGrossIncome()


    # Q7
    print("\n-------- Fahrenheit To Celsius --------\n")

    fToC()


    # Q8
    print("\n-------- Celsius To Fahrenheit --------\n")

    cToF()


    print("\n\nGoodbye\n\n")


def greet():
    
    fn = input("Please enter first name:\n")
    ln = input("Please enter last name:\n")
    city = input("Please enter your city name:\n")

    greetMsg = f"Hello {fn} {ln} from {city}!"

    print(greetMsg)


def AreaOfTriangle_a(b, h):
    a = .5 * b * h
    return round(a, 2)


def AreaOfTriangle_b(b , h):
    a = round(.5 * b * h, 2)
    print(f"A triangle with base length {b} and height {h} has an area of {a}.")


def AreaOfTriangle_c():
    b = float(input("Please enter base length:\n"))
    h = float(input("Please enter height:\n"))
    a = .5 * b * h
    return round(a, 2)


def AreaOfTriangle_d():
    b = float(input("Please enter base length:\n"))
    h = float(input("Please enter height:\n"))
    a = round(.5 * b * h, 2)
    print(f"A triangle with base length {b} and height {h} has an area of {a}.")


def MphToKnt(mph):
    return round(mph * 1.1, 2)


def KntToMph(knt):
    return round(knt / 1.1, 2)

def AvgThreeNums(a, b ,c):
    return round((a + b + c) / 3.0, 2)


def CalcGrossIncome():
    salary = int(input("Please enter your monthly salary as a whole number.\n"))
    months = float(input("Please enter number of months"))
    grossInc = round(salary * months, 2)
    print(f"${salary}/month for {months} months equals a gross income of ${grossInc}.")


def fToC():
    f = float(input("Please enter a temperature in farenheit:\n"))

    c = round((f - 32) * (5.0 / 9.0), 2)

    print(f"{f}°F is {c}°C.")


def cToF():
    c = float(input("Please enter a temperature in celsius:\n"))

    f = round(c * (9.0 / 5.0) + 32, 2)

    print(f"{c}°C is {f}°F.")
    

main()