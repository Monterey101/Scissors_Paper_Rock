import random

#Welcome Page
print("Welcome to Python CLI Scissors Paper Rock")

#Playing Status
playing = True

#Current Human and CPU scores
humanScore = 0
cpuScore= 0

#CPU player
def cpuChoice():
    choice = random.choice([1, 2, 3])
    if choice == 1:
        return "s"
    elif choice == 2:
        return "p"
    elif choice == 3:
        return "r"
    else:
        return ""

#Checks if the user entered a valid choice
def checkValidChoice(choice:str):
    if choice == "s" or choice == "p" or choice == "r":
        return True
    else:
        return False

#Playing interface
while playing == True:
    playerChoice = input("Choose Scissors (s), Paper (p) or Rock (r): ")
    computerChoice = cpuChoice()
    
    #Checks if the user entered a valid choice
    if checkValidChoice(playerChoice):
        
        #Finding who won the match
        if playerChoice == computerChoice:
            print("Draw!")
        elif playerChoice == "s" and computerChoice == "p":
            humanScore += 1
            print("You won!")
        elif playerChoice == "p" and computerChoice == "r":
            humanScore += 1
            print("You won!")
        elif playerChoice == "r" and computerChoice == "s":
            humanScore += 1
            print("You won!")
        else:
            cpuScore += 1
            print("The Computer won!")
        print()
        print("Current Score: Human: " , str(humanScore) , " : " , str(cpuScore) , " :CPU")
        print()
    
    #End loop if user wishes to exit
    elif playerChoice == "e":
        playing = False
        print("Thanks for playing!")
        print("Final Score: Human: " , str(humanScore) , " : " , str(cpuScore) , " :CPU")
    
    #Ask user to re-enter if they enter an invalid choice
    else:
        print("You did not enter a valid choice, try again! (enter 'e' to exit)")
