marks= int(input("Enter Your Marks: "))

if(marks<=100 and marks >=90):
    print("You acheive grade A+")

elif(marks<=90 and marks >=80):
    print("You acheive grade A")
elif(marks<=80 and marks >=70):
    print("You acheive grade B+")
elif(marks<=70 and marks >=60):
    print("You acheive grade B")

else:
    print("You are fail")
