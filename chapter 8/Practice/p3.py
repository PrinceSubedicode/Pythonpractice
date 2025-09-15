
n=int(input("Enter any no:"))
def sum(n):
    if(n==1):
        return 1
    return sum(n-1)+n

print(f"The sum is : {sum(n)}")