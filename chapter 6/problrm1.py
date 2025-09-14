a=int(input("enter a number:"))
b=int(input("enter a number:"))
c=int(input("enter a number:"))
d=int(input("enter a number:"))

if(a>b and a>c and a>d):
    print("a is greatest")
 
elif(b>a and b>c and b>d):
    print("b is greatest")

elif(c>b and c>a and c>d):
    print("c is greatest")    

else:
    print("d is greatest")