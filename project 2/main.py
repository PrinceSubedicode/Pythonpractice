import random
n=random.randint(1,100)
a=-1
guesses=1
while(a!=n):
    a=int(input("Guess a Number:"))

    if(a>n):
        print("Lower Number Please:")
        guesses+=1

    elif(a<n):
        print("Higher Number Please")
        guesses+=1

print(f"You have Guessed the Number {n} Correctly in {guesses} attempt.")

