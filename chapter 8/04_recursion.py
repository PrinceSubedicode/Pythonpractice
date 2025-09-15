def fact(n):
    if(n==1 or n==0):
        return 1
    return n*fact(n-1)

n=int(input("Enter any no. to find factorial:"))
print(f"The factorial of {n} is: {fact(n)}")