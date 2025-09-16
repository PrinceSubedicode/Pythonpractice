n=int(input("Enter an Number:"))

table = [n*i for i in range(1,11)]

with open("table.txt","a") as f:
    f.write(f"Table of {n} is : {str(table)}\n")