# Collin Shook
# 9-20-2022
# Assignment 3


import sys, time



def main():
    shouldContinue = "y"
    while (shouldContinue == "y"):
        ans = 0
        while (ans != 1 and ans != 2):
            ans = menu()
        if (ans == 1):  # game
            game()
        else:  # taxes
            taxes()

        shouldContinue = input("Enter 'y' to run again or any other key to quit!\n").lower()

    print("\nbye")


def menu():
    try:
        ans = int(input(
            "Welcome to this program! Enter '1' To play a game or '2' to calculate taxes!\n"))
    except ValueError:
        ans = 0
    return ans


def game():
    print("\n------ Game ------\n")
    time.sleep(1)
    print("You are stranded on top of a mountain with two paths down!")
    time.sleep(3)
    path = 0
    while (path != 1 and path != 2):
        try:
            path = int(input("You can go (1) left, or (2) right. 1/2\n"))
        except:
            path = 0

    if (path == 1):  # chumchum
        print("You walk down the left path...\n")
        
        time.sleep(2)

        print("""Up ahead you see two items. One is ChumChum, an evil poacher 
who is responsible for the extinction of elephants, lions, and pandas.
The other is a parachute.
        """)

        time.sleep(5)

        choice = 0
        while (choice != 1 and choice != 2):
            try:
                choice = int(input("Do you choose to take (1) ChumChum, or (2) the parachute? 1/2\n"))
            except:
                choice = 0

        if(choice == 1):
            print("You take ChumChum!")
        else:
            print("You take the parachute!")
        
        time.sleep(2)

        print("You have approached another fork in the trail!")
        time.sleep(2)
        path = 0
        while (path != 1 and path != 2):
            try:
                path = int(input("You can go (1) left, or (2) right. 1/2\n"))
            except:
                path = 0

        
        if(path == 1): # cannibals
            print("You walk down the left path...\n")
            time.sleep(2)
            print("Oh No! You have run into cannibals!")
            time.sleep(2)
            if(choice == 1): # has chumchum
                print("You remember you have ChumChum and the cannibals found him quite YumYum!")
                time.sleep(1)
                print("You are able to run to safety! You win!")
            else: # has parachute
                print("Your use your parachute to get away...")
                time.sleep(2)
                print("""... until you remembered you were on flat ground. The cannibals caught you 
and took you to a nice hottub with carrots and onions. You lose!
                """)

        else: #cliff
            print("You walk down the right path...\n")
            time.sleep(2)
            print("You have come across a cliff!")
            time.sleep(2)
            if (choice == 1):  # has chumchum
                print("ChumChum has gotten hungry and eaten you! You lose!")
            else:  # has parachute
                print("You ditch ChumChum and parachute to safety! You win!")

    else:
        print("You walk down the right path...\n")

        time.sleep(2)

        print("""Up ahead you see two items. One is a bag of peanuts and the other is a mouse
        """)

        time.sleep(5)

        choice = 0
        while (choice != 1 and choice != 2):
            try:
                choice = int(
                    input("Do you choose to take (1) the peanuts, or (2) the mouse? 1/2\n"))
            except:
                choice = 0

        if (choice == 1):
            print("You take the peanuts!")
        else:
            print("You take the mouse!")

        time.sleep(2)

        print("You have approached another fork in the trail!")
        time.sleep(2)
        path = 0
        while (path != 1 and path != 2):
            try:
                path = int(input("You can go (1) left, or (2) right. 1/2\n"))
            except:
                path = 0

        if (path == 1):  # chimpanzees  
            print("You walk down the left path...\n")
            time.sleep(2)
            print("Oh No! You have ran into a group of mad chimpanzees!")
            time.sleep(2)
            if (choice == 1):  # has peanuts
                print(
                    "You throw your peanuts and run while the chimps are distracted!")
                time.sleep(1)
                print("You are able to run to safety! You win!")
            else:  # has mouse
                print("You show the chimps your mouse!")
                time.sleep(2)
                print("""They hate mice and tear you to pieces! You Lose!
                """)

        else:  # elephants
            print("You walk down the right path...\n")
            time.sleep(2)
            print("You come across a group of elephants!")
            time.sleep(2)
            if (choice == 1): # has peanuts
                print("They see your peanuts and trample you trying to eat them. You lose!")
            else: # has mouse
                print("The elephants are scared of your mouse! They run off and you continue onward to safety! You win!")

    time.sleep(2)




def taxes():
    print("------ Tax Calaculator ------")
    income = float(input("Please enter your annual income\n"))
    rate = 0.0

    if (income <= 9275):
        rate = .1
    elif (income <= 37650):
        rate = .15
    elif (income <= 91150):
        rate = .25
    elif (income <= 190150):
        rate = .28
    elif (income <= 413350):
        rate = .33
    elif (income <= 415050):
        rate = .35
    else:
        rate = .396

    print(f"An annual income of ${income} would yield a tax rate of {round(rate * 100, 2)}% and a net income of ${round(income * (1.0 - rate), 2)}")


main()
