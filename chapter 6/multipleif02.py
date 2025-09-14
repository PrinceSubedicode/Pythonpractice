x=int(input("Enter Your age:"))

if(x%2==0):
    print("x is even ")
   # end of first if statement  
if x > 20:
    print("x is greater than 20")
elif x > 10:   # <-- this is like "else if"
    print("x is greater than 10 but less than or equal to 20")
else:
    print("x is 10 or less")


    # end of 2nd if statement
    # multile if statement can be used  