a=int(input("Enter 1st no:"))
b=int(input("Enter 2nd no:"))
c=int(input("Enter 3rd no:"))

def greatest(a, b, c):
    if(a>b and a>c):
        print("a is greatest")

    elif(b>a and b>c):
        print("b is greatest") 

    else:
        print("c is greatest")    


greatest(a,b,c)        

