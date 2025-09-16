a= int(input("Enter a :"))
b= int(input("Enter b :"))
try:
    print(a/b)

except ZeroDivisionError as e:
    print("Infinite......")    