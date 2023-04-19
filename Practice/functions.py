# Collin Shook
# 9-6-2022
# functions practice

def main():
    # a = float(input("Enter First Number:\n"))
    # b = float(input("Enter Second Number:\n"))

    # print("\n\n---------- Example A ----------\n")

    # ans = addTwoNums_a(a, b)
    
    # print("The sum is " + str(ans))

    # print("\n\n---------- Example B ----------\n")

    # addTwoNums_b(a, b)

    # print("\n\n---------- Example C ----------\n")

    # ans = addTwoNums_c()
    
    # print("The sum is " + str(ans))

    # print("\n\n---------- Example D ----------\n")

    # addTwoNums_d()

    dogYears = float(input("Enter the age of your dog:\n"))

    humanYears = dogToHumanYears(dogYears)

    print("Your dog is " + str(humanYears) + " in human years")

    print("\n\n\nGoodbye!\n\n\n")




def addTwoNums_a(a, b):
    return a + b


def addTwoNums_b(a, b):
    ans = a + b
    print ("The sum is " + str(ans))


def addTwoNums_c():
    a = float(input("Enter First Number:\n"))
    b = float(input("Enter Second Number:\n"))
    return a + b


def addTwoNums_d():
    a = float(input("Enter First Number:\n"))
    b = float(input("Enter Second Number:\n"))
    ans = a + b
    print ("The sum is " + str(ans))


def dogToHumanYears(dogYears):
    return dogYears * 7


main()