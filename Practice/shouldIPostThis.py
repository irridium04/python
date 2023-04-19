# Collin Shook
# 9-15-2022
# Should I Post This


def main():
    shouldContinue = "y"

    while(shouldContinue == "y"):
        logic()
        shouldContinue = input("Enter 'y' to continue. Press any other key to quit!")

    
def logic():
    isClothed = None
    hasExplicitives = None
    isIllegal = None
    isPartying = None
    
    print("\n\n------ Should I post this? ------\n")
    isImg = askIfImg()
    if(isImg):
        isClothed = askIfClothed()
    else:
        hasExplicitives = askIfHasExplicitives()
    
    if(isClothed == False or hasExplicitives):
        print("🛑 Stop - Do Not Post It! 🛑")
        return
    
    if(isImg):
        isIllegal = askIfIllegal()
    else:
        isPartying = askIfPartying()

    if(isIllegal or isPartying):
        print("🛑 Stop - Do Not Post It! 🛑")
        return
    else:
        print("✅ It is OK to post! ✅")
        



def askIfImg():
    ans = input("Is your post 1. An Image, or 2. Text? Answer 1 or 2!\n")

    if(ans != "1" and ans != "2"):
        print("That wasn't a choice!\n")
        askIfImg()
    elif (ans == "1"):
        return True
    else:
        return False

def askIfClothed():
    ans = input("Is everyone in your image fully clothed? y/n\n").lower()

    if(ans != "y" and ans != "n"):
        print("That wasn't a choice!\n")
        askIfClothed()
    elif (ans == "y"):
        return True
    else:
        return False

def askIfHasExplicitives():
    ans = input("Does your text contain explicitives? y/n\n").lower()

    if(ans != "y" and ans != "n"):
        print("That wasn't a choice!\n")
        askIfHasExplicitives()
    elif (ans == "y"):
        return True
    else:
        return False

def askIfIllegal():
    ans = input("Does your image show illegal activity? y/n\n").lower()

    if(ans != "y" and ans != "n"):
        print("That wasn't a choice!\n")
        askIfIllegal()
    elif (ans == "y"):
        return True
    else:
        return False

def askIfPartying():
    ans = input("Have you been partying? y/n\n").lower()

    if(ans != "y" and ans != "n"):
        print("That wasn't a choice!\n")
        askIfIllegal()
    elif (ans == "y"):
        return True
    else:
        return False

main()