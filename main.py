import random


print("Welcome to Python CLI Scissors Paper Rock")

humanScore = 0
cpuScore= 0

print("Current Score: Human: " , str(humanScore) , " : " , str(cpuScore) , " :CPU")
print()
choice = input("Choose Scissors (s), Paper (p) or Rock (r): ")

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