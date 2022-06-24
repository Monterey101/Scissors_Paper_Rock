import random

#Welcome Page
print("Welcome to Python CLI Scissors Paper Rock")

#Current Human and CPU scores
humanScore = 0
cpuScore= 0

#Playing interface
print("Current Score: Human: " , str(humanScore) , " : " , str(cpuScore) , " :CPU")
print()
choice = input("Choose Scissors (s), Paper (p) or Rock (r): ")

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