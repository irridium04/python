import sys, random


board = ["1","2","3","4","5","6","7","8","9"]
turns = 0
playerWins = 0
computerWins = 0
draws = 0

def main():
    global board

    shouldPlayAgain = "y"
    while (shouldPlayAgain == "y"):
        print(f"""
       Game Stats:

User Wins :       {playerWins}
Computer Wins :   {computerWins}
Draws :           {draws}
Total Games :     {playerWins + computerWins + draws}
        """)

        board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        Logic()

        shouldPlayAgain = input("Enter 'y' to play again! Enter any other key to quit!\n").lower()


    print(f"""
    Final Game Stats:

User Wins :       {playerWins}
Computer Wins :   {computerWins}
Draws :           {draws}
Total Games :     {playerWins + computerWins + draws}


End Of Program
        """)



def Logic():
    global turns
    global board
    global playerWins
    global computerWins
    global draws


    turns = 0
    winner = ""

    while (turns < 9):
        if (turns % 2 == 0):
            UserTurn()
        else:
            ComputerTurn()

        # test for win
        if (turns >= 5):  # can't win on less than 3 moves from user
            didWin = False

            if (board[0] == board[1] == board[2]):
                didWin = True
                winner = board[0]
            elif (board[3] == board[4] == board[5]):
                didWin = True
                winner = board[3]
            elif (board[6] == board[7] == board[8]):
                didWin = True
                winner = board[6]
            elif (board[0] == board[3] == board[6]):
                didWin = True
                winner = board[0]
            elif (board[1] == board[4] == board[7]):
                didWin = True
                winner = board[1]
            elif (board[2] == board[5] == board[8]):
                didWin = True
                winner = board[2]
            elif (board[0] == board[4] == board[8]):
                didWin = True
                winner = board[0]
            elif (board[2] == board[4] == board[6]):
                didWin = True
                winner = board[2]
            else:
                didWin = False
                winner = ""

            if (didWin):
                break

    if (winner == "O"):
        print("You Lose!")
        computerWins += 1
    elif (winner == "X"):
        print("You Win!")
        playerWins += 1
    else:
        print("Draw!")
        draws += 1
    
                

def DisplayBoard():
    print("\nBoard")

    for y in range(3):
        for x in range(3):
            index = (y * 3) + x
            sys.stdout.write(board[index].ljust(3))

        print()

    print()


def UserTurn():
    global turns
    global board

    print("User Turn\n")
    DisplayBoard()

    validInput = False

    while (not validInput):
        try:
            choice = int(input("Choose a square to play!\n"))

            try:
                int(board[choice - 1])
                if(choice < 1 or choice > 9):
                    print("Not A Valid Square!")
                else:
                    validInput = True
                    
            except:
                print("Square has already been played!")

        except:
            print("Not A Valid Square!")


    board[choice - 1] = "X"

    DisplayBoard()

    turns += 1

def ComputerTurn():
    global turns
    global board

    print("Computer Turn\n")


    validChoice = False

    while (not validChoice):

        choice = random.randint(0,8)

        try:
            int(board[choice])
            validChoice = True
        except:
            validChoice = False

        

    board[choice] = "O"

    DisplayBoard()

    turns += 1


main()