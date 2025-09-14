num=int(input("Enter any no.for multiplication table:"))

for i in range(1,11):
    a=i*num
    print(f"{num}*{i}={a}")
    i+=1
    