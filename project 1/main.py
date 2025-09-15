import random

# Dictionary for mapping
youDict = {"s": 1, "w": -1, "g": 0}
revDict = {1: "Snake", -1: "Water", 0: "Gun"}

# User input
youstr = input("Enter your choice (s for Snake, w for Water, g for Gun): ").lower()
you = youDict[youstr]

# Computer choice
compstr = random.choice(["s", "w", "g"])
computer = youDict[compstr]

print(f"\nYou chose: {revDict[you]}")
print(f"Computer chose: {revDict[computer]}")

# Logic
if computer == you:
    print("Match Draw....")

elif (computer == -1 and you == 1) or (computer == 1 and you == 0) or (computer == 0 and you == -1):
    print("You win!!!!")

else:
    print("Computer wins, Try again!!")
