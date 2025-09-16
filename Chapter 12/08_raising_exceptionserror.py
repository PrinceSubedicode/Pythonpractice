a=int(input("Enter a number:"))
b=int(input("Enter another number:"))

if(b==0):
    raise ZeroDivisionError("Hey, our program is not mean to divide by zero!!!")

else:
    print(f"division of {a} by {b} is:{a/b}")