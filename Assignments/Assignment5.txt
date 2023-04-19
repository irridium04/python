# Collin Shook
# 10-6-2022
# Loops

import sys, random

def main():
    ans = "y"
    while (ans == "y"):
        menu()
        ans = input("Enter 'y' to continue. Enter any other key to quit!\n")

    print("\nbye")

def menu(): 
    validChoice = False
    while (not validChoice):
        print("""
Please choose a question to run:
1. Reversed Word
2. Numbers divisible by 3
3. Good letters
4. Calender Shift
5. Triangles
6. Guess a random number
   
        """)

        choice =  input("Enter a choice 1-6!\n")
        if(choice == "1"):
            validChoice = True
            Q1()
        elif(choice == "2"):
            validChoice = True
            Q2()
        elif (choice == "3"):
            validChoice = True
            Q3()
        elif (choice == "4"):
            validChoice = True
            Q4()
        elif(choice == "5"):
            validChoice = True
            Q5()
        elif (choice == "6"):
            validChoice = True
            Q6()
        else:
            validChoice = False
            print("Not a valid choice!\n")



def Q1():
    print("\n------ Reversed Word ------\n")
    word = input("Please enter a word to be reversed!")
    reversedWord = ""
    for i in range(len(word), 0, -1):
        reversedWord += word[i - 1]
        
    print(reversedWord
    )


def Q2():
    print("\n------ Divisible by 3 ------\n")
    for i in range(1, 101):
        if(i % 3 == 0):
            print(i)


def Q3():
    print("\n------ Good Letters ------\n")
    word = input("Enter a string of characters!\n")

    goodChars = 0
    badChars = 0

    for char in word:
        asciiValue = ord(char)

        if((asciiValue >= 65 and asciiValue < 91) or (asciiValue >= 97 and asciiValue < 123)):
            goodChars += 1
        else:
            badChars += 1

    print(f'The string "{word}" contains {goodChars} good characters and {badChars} bad characters!')


def Q4():
    print("\n------ Calender Shift ------\n")
    shiftAmount = -1
    while(shiftAmount < 0 or shiftAmount > 6):
        try:
            shiftAmount = int(input("Enter in an amount to shift the calender by! 0-6\n"))
        except:
            print("invalid input!")
            shiftAmount = -1

    calenderList = []

    days = ["S", "M", "T" , "W", "Th", "F", "S"]

    for day in days:
        calenderList.append(day)

    for i in range(shiftAmount):
        calenderList.append("")

    for i in range(31):
        calenderList.append(str(i + 1))

    index = 0
    for item in calenderList:
        itemLength = len(item)
        spaces = 4 - itemLength
        lineToWrite = (" " * spaces) + item
        if(index % 7 == 0):
            print()
        
        sys.stdout.write(lineToWrite)
        index += 1
    
    print("\n")
    

def Q5():
    print("\n------ Triangles ------\n")

    rows = 10
    cols = 10

    print("\n--- a ---\n")
    for i in range(rows):
        print("⭐" * (i + 1))

    print("\n--- b ---\n")
    for i in range(rows, -1 , -1):
        print("⭐" * (i + 1))

    print("\n--- c ---\n")
    for i in range(rows):
        spaces = "  " * i
        stars = "⭐" * (cols - i)
        print(spaces + stars)

    print("\n--- d ---\n")
    for i in range(rows, -1, -1):
        spaces = "  " * i
        stars = "⭐" * (cols - i)
        print(spaces + stars)

    print("\n--- e ---\n")
    for i in range(rows, 0, -2):
        spaces = (rows - i) * " "
        stars = "⭐" * i
        print(spaces + stars + spaces)

    for i in range(2, rows + 1, 2):
        spaces = (rows - i) * " "
        stars = "⭐" * i
        print(spaces + stars + spaces)

    
def Q6():
    print("\n------ Guess a random number ------\n")
    userGuess = 0
    numberToGuess = random.randint(1, 100)
    tries = 0

    while(userGuess != numberToGuess):
        validGuess = False
        while(not validGuess):
            try:
                userGuess = int(input(f"Guess the number between 1 - 100! Tries: {tries}!\n"))
            except:
                print("Invalid input")
                validGuess = False

            if(userGuess > 0 and userGuess <= 100):
                validGuess = True
            else:
                print("Not betweeen 1 and 100!")
                validGuess = False
        
        if(userGuess != numberToGuess):
            print(f"{userGuess} was not the number!")
            tries += 1
        else:
            print(f"Congradulations! {userGuess} was the number! You solved it in {tries + 1} tries!")


main()