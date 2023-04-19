import pyttsx3


se = pyttsx3.init()
n = 1


def main():
    se.setProperty('rate', 125)
    playVoices()


def playVoices():
    voiceChoice = 0

    v = se.getProperty('voices')

    print(v)

    for i in range(len(v)):
        se.setProperty('voice', v[i].id)
        se.say("This is voice" + str(i + 1))
        se.runAndWait()

    try:
        voiceChoice = int(input("Please choose a voice! Input 1-" + str(len(v)) + "\n"))
        se.setProperty('voice', v[voiceChoice - 1].id)
        se.say("You chose voice " + str(voiceChoice))
    except:
        se.setProperty('voice', v[0].id)
        se.say("Invalid input. Defaulted to voice 1")
    finally:
        se.runAndWait()
    

    numBottles()


def numBottles():
    global n

    try:
        n = int(input("Enter number of bottles:\n"))
    except:
        n = 3

    bottlesRecursive(n)


def sayBottles(numberOfBottles):
    i = numberOfBottles
    while(i > 0):
        se.say(str(i) + "bottles of beer on the wall " + str(i) + \
            " bottles of beer. Take one down and pass it around " + \
            str(i - 1) + " bottles of beer on the wall" )
        se.runAndWait()
        i -= 1

def bottlesRecursive(numberOfBottles):
    if (numberOfBottles < 1):
        return

    se.say(str(numberOfBottles) + "bottles of beer on the wall " + str(numberOfBottles) + \
        " bottles of beer. Take one down and pass it around " + \
        str(numberOfBottles - 1) + " bottles of beer on the wall")

    se.runAndWait()
    rate = se.getProperty('rate')
    se.setProperty('rate', rate - 2)
    bottlesRecursive(numberOfBottles - 1)






main()