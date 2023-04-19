# Collin Shook
# 10/11/2022
# Assignment 4


import sys, time, random


bookList = []

List1 = ['artless', 'bawdy', 'beslubbering', 'bootless', 'churlish',
         'cockered', 'clouted', 'craven', 'currish', 'dankish', 'dissembling',
         'droning', 'errant', 'fawning', 'fobbing', 'froward', 'frothy',
         'gleeking', 'goatish', 'gorbellied', 'impertinent', 'infectious',
         'jarring', 'loggerheaded', 'lumpish', 'mammering', 'mangled',
         'mewling', 'paunchy', 'pribbling', 'puking', 'puny', 'qualling',
         'rank', 'reeky', 'roguish', 'ruttish', 'saucy', 'spleeny',
         'spongy', 'surly', 'tottering', 'unmuzzled', 'vain',
         'venomed', 'villainous', 'warped', 'wayward', 'weedy', 'yeasty']


List2 = ['base-court', 'bat-fowling', 'beef-witted', 'beetle-headed',
         'boil-brained', 'clapper-clawed', 'clay-brained', 'common-kissing',
         'crook-pated', 'dismal-dreaming', 'dizzy-eyed', 'doghearted',
         'dread-bolted', 'earth-vexing', 'elf-skinned', 'fat-kidneyed',
         'fen-sucked', 'flap-mouthed', 'fly-bitten', 'folly-fallen',
         'fool-born', 'full-gorged', 'guts-griping', 'half-faced',
         'hasty-witted', 'hedge-born', 'hell-hated', 'idle-headed',
         'ill-breeding', 'ill-nurtured', 'knotty-pated', 'milk-livered',
         'motley-minded', 'onion-eyed', 'plume-plucked', 'pottle-deep',
         'pox-marked', 'reeling-ripe', 'rough-hewn', 'rude-growing',
         'rump-fed', 'shard-borne', 'sheep-biting', 'spur-galled',
         'swag-bellied', 'tardy-gaited', 'tickle-brained',
         'toad-spotted', 'unchin-snouted', 'weather-bitten']


List3 = ['apple-john', 'baggage', 'barnacle', 'bladder', 'boar-pig',
         'bugbear', 'bum-bailey', 'canker-blossom', 'clack-dish', 'clotpole',
         'coxcomb', 'codpiece', 'death-token', 'dewberry', 'flap-dragon',
         'flax-wench', 'flirt-gill', 'foot-licker', 'fustilarian', 'giglet',
         'gudgeon', 'haggard', 'harpy', 'hedge-pig', 'horn-beast',
         'hugger-mugger', 'joithead', 'lewdster', 'lout', 'maggot-pie',
         'malt-worm', 'mammet', 'measle', 'minnow', 'miscreant', 'moldwarp',
         'mumble-news', 'nut-hook', 'pigeon-egg', 'pignut', 'puttock',
         'pumpion', 'ratsbane', 'scut', 'skainsmate', 'strumpet', 'varlot',
         'vassal', 'whey-face', 'wagtail']



def main():
    shouldContinue = "y"
    while(shouldContinue == "y"):
        menu()
        shouldContinue = input("Enter 'y' to run again or enter to end!\n").lower()
    print("\nGoodbye!")


def menu():
    choice = "0"
    while(choice != "1" and choice != "2"):
        choice = input("Press '1' to manage books or '2' to run the Shakespearean insult generator!\n")
        if (choice != "1" and choice != "2"):
            print("Invalid input!")
        
        elif(choice == "1"):
            BookMenu()
        else:
            InsultMenu()


def BookMenu():
    choice = 1
    while(True):
        print("""\n------------ Bookkeeping Menu ------------

1. Add books to end of list.
2. Delete a book by name.
3. Delete a book by position in book list.
4. Insert books anywhere in list.
5. Clear the list.
6. Print the list horizontally.
7. Sort the books by title.
8. Main Menu

-------------------------------------------""")

        time.sleep(1)

        invalidInput = True
        while (invalidInput):
            try:
                choice = int(input("Enter 1-8 to choose an option!\n"))
                if(choice < 1 or choice > 8):
                    invalidInput = True
                else:
                    invalidInput = False
            except:
                invalidInput = True

        if(choice == 1):
            AddItemsToEnd(bookList)
        elif (choice == 2):
            DeleteByName()
        elif (choice == 3):
            DeleteByPos(bookList)
        elif (choice == 4):
            InsertInList()
        elif (choice == 5):
            ClearList()
        elif (choice == 6):
            PrintHorizontally()
        elif (choice == 7):
            SortList()
        else:
            break

        time.sleep(1)
        


def DisplayList(aList):
    print("\n-------- List --------\n")
    
    index = 1
    for item in aList:
        print(f"{index}. {item}")
        index += 1

    print()

    time.sleep(1)


def AddItemsToEnd(aList):
    DisplayList(aList)

    title = input("Please enter an item to add to the end of the list!\n")

    aList.append(title)

    DisplayList(aList)


def DeleteByName():
    if (len(bookList) == 0):
        print("Book list is empty. Please add books to use this function.")
    else:
        validInput = False
        while(not validInput):
            DisplayList(bookList)

            titleToDelete = input("Enter name of book to delete!\n")

            try:
                bookList.remove(titleToDelete)
                validInput = True
            except:
                print("That title is not in your list!\n")
                validInput = False

        DisplayList(bookList)

    
def DeleteByPos(aList):
    if (len(aList) == 0):
        print("List is empty. Please add books to use this function.")
    else:
        validInput = False
        while (not validInput):
            DisplayList(aList)

            try:
                indexToDelete = int(input(f"Enter a position to delete. 1-{len(aList)}!\n"))
                if(indexToDelete < 1 or indexToDelete > len(aList)):
                    print("Invalid input!")
                    validInput = False
                else:
                    validInput = True
                    del aList[indexToDelete - 1]
            except:
                print("Invalid input!")
                validInput = False

        DisplayList(aList)

def InsertInList():
    if (len(bookList) == 0):
        print("Book list is empty. Please add books to use this function.")
    else:
        validInput = False
        while (not validInput):
            DisplayList(bookList)

            try:
                indexToInsert = int(input(f"Enter a position to insert to. 1-{len(bookList)}!\n"))
                title = input(f"Please enter a title for position {indexToInsert}!\n")

                if (indexToInsert < 1 or indexToInsert > len(bookList)):
                    print("Invalid input!")
                    validInput = False
                else:
                    validInput = True
                    bookList.insert(indexToInsert - 1, title)
                    
            except:
                print("Invalid input!")
                validInput = False

        DisplayList(bookList)



def ClearList():
    if (len(bookList) == 0):
        print("Book list is empty. Please add books to use this function.")
    else:
        shouldDelete = input("""⚠️ ARE YOU SURE YOU WANT TO CLEAR YOUR LIST? ⚠️
        
Type in 'clear' all lowercase to clear list. Enter to cancel.
        """)

        if(shouldDelete == "clear"):
            bookList.clear()


def PrintHorizontally():
    if (len(bookList) == 0):
        print("Book list is empty. Please add books to use this function.")
    else:
        print("\n-------- Book List --------\n")

        index = 1
        for item in bookList:
            sys.stdout.write(f"{index}. {item}, ")
            index += 1

        print()

        time.sleep(1)


def SortList():
    if (len(bookList) == 0):
        print("Book list is empty. Please add books to use this function.")
    else:
        bookList.sort()

        DisplayList(bookList)


def InsultMenu():
    choice = 1
    while (True):
        print("""\n------------ Shakespearean Insult Generator ------------

1. Random Insult.
2. Custom Insult.
3. Insult list editor.
4. Main Menu.

------------------------------------------------------------""")

        time.sleep(1)

        invalidInput = True
        while (invalidInput):
            try:
                choice = int(input("Enter 1-4 to choose an option!\n"))
                if (choice < 1 or choice > 4):
                    invalidInput = True
                else:
                    invalidInput = False
            except:
                invalidInput = True

        if (choice == 1):
            RandomInsult()
        elif (choice == 2):
            CustomInsult()
        elif (choice == 3):
            InsultEditor()
        else:
            break

        time.sleep(1)


def RandomInsult():
    index1 = random.randint(0, len(List1))
    index2 = random.randint(0, len(List2))
    index3 = random.randint(0, len(List3))

    print(f"Thou is a {List1[index1]} {List2[index2]} {List3[index3]}!")


def CustomInsult():
    print("Custom Insult Generator!")

    invalidInput = True
    while (invalidInput):
        try:
            DisplayList(List1)
            choice1 = int(input(f"Enter 1-{len(List1)} to choose an option!\n"))
            if (choice1 < 1 or choice1 > len(List1)):
                invalidInput = True
            else:
                try:
                    DisplayList(List2)
                    choice2 = int(input(f"Enter 1-{len(List2)} to choose an option!\n"))
                    if (choice2 < 1 or choice2 > len(List2)):
                        invalidInput = True
                    else:
                        try:
                            DisplayList(List3)
                            choice3 = int(input(f"Enter 1-{len(List3)} to choose an option!\n"))
                            if (choice3 < 1 or choice3 > len(List3)):
                                invalidInput = True
                            else:
                                invalidInput = False
                        except:
                            invalidInput = True
                except:
                    invalidInput = True
        except:
            invalidInput = True

    
    print(f"Thou is a {List1[choice1 - 1]} {List2[choice2 - 1]} {List3[choice3 - 1]}!")


def InsultEditor():
    print("Insult editor!")
    invalidInput = True
    while (invalidInput):
        try:
            print("\n------- FIRST LIST -------\n")
            DisplayList(List1)
            print("\n------- SECOND LIST -------\n")
            DisplayList(List2)
            print("\n------- THIRD LIST -------\n")
            DisplayList(List3)

            listChoice = int(input("Enter 1-3 to choose a list to edit!\n"))
            if (listChoice < 1 or listChoice > 3):
                invalidInput = True
            else:
                invalidInput = False
        except:
            invalidInput = True

    invalidInput = True
    while (invalidInput):
        try:
            choice = int(input("Enter 1 to delete an item or 2 to add one!\n"))
            if (choice < 1 or choice > 2):
                invalidInput = True
            else:
                invalidInput = False
        except:
            invalidInput = True

    if(choice == 1):
        if(listChoice == 1):
            DeleteByPos(List1)
        elif(listChoice == 2):
            DeleteByPos(List2)
        elif(listChoice == 3):
            DeleteByPos(List3)
    else:
        if(listChoice == 1):
            AddItemsToEnd(List1)
        elif(listChoice == 2):
            AddItemsToEnd(List2)
        elif(listChoice == 3):
            AddItemsToEnd(List3)
    


main()