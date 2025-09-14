num=int(input("Enter any no.:"))

for i in range(2,num):
    if(num%i)==0:
        print("No. is not prime")
        break

else:
    print("NO.is prime")

