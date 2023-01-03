import random

def displayInstructions():
    print("Enter 0 to select Rock\nEnter 1 to select Paper\nEnter 2 to select Scissors\nEnter 3 to select Lizard\nEnter 4 to select Spock")

def getUserChoice():
    userChoice = int(input("Enter the number associated with your selection: "))
    return userChoice

def generateComputerChoice():
    computerChoice = random.randint(0, 4)
    return computerChoice

def determineWinner(userWins, computerWins):
    userChoice = getUserChoice()
    computerChoice = generateComputerChoice()
    if userChoice == 0 and computerChoice == 2:
        userWins += 1
        return userWins, computerWins
    elif computerChoice == 0 and userChoice == 2:
        computerWins += 1
        return userWins, computerWins
    elif userChoice == 1 and computerChoice == 4:
        userWins += 1
        return userWins, computerWins
    elif computerChoice == 1 and userChoice == 4:
        computerWins += 1
        return userWins, computerWins
    elif userChoice == 2 and computerChoice == 1 or 3:
        userWins += 1
        return userWins, computerWins
    elif computerChoice == 2 and userChoice == 1 or 3:
        computerWins += 1
        return userWins, computerWins
    elif userChoice == 3 and computerChoice == 4 or 1:
        userWins += 1
        return userWins, computerWins
    elif computerChoice == 3 and userChoice == 4 or 1:
        computerWins += 1
        return userWins, computerWins
    elif userChoice == 4 and computerChoice == 2 or 0:
        userWins += 1
        return userWins, computerWins
    elif computerChoice == 4 and userChoice == 2 or 0:
        computerWins += 1
        return userWins, computerWins
    else:
        print("**ERROR**")
    
def trackScores(userWins, computerWins):
    print(f"Current Score:\nYou have {userWins} wins\nThe computer has {computerWins}")

def determineChampion(userWins, computerWins):
    if userWins == 3:
        winner = "The winner is the user!"
        return winner
    elif computerWins == 3:
        winner = "The computer is the winner!"
        return winner
    else:
        print("ERROR")

def outputResults(winner):
    print(winner)

def main():
    userWins = 0
    computerWins = 0
    while (userWins != 3) and (computerWins != 3):
        displayInstructions()
        userWins, computerWins = determineWinner(userWins, computerWins)
        trackScores(userWins, computerWins)
    winner = determineChampion(userWins, computerWins)
    outputResults(winner)

if __name__ == "__main__":
    main()