import random

print("Choices: 1 for Snake, 2 for Water, 3 for Gun")

you = int(input("Enter your choice (1/2/3): "))
comp = random.randint(1,3)

print("You chose:", you)
print("Computer chose:", comp)

if you == comp:
    print("Draw!")
elif (you == 1 and comp == 2) or (you == 2 and comp == 3) or (you == 3 and comp == 1):
    print("You Win!")
else:
    print("Computer Wins!")
