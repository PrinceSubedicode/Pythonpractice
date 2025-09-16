try:
    a=int(input("Hey,Enter an integer:"))
    print(a)

except Exception as e:
    print(e)    

finally:
    print("finally Block is always executed... ")    