def divisible5(n):
    if(n%5==0):
        return True
    return False
a=[1,2,5,65,77,85,4455,6565,777,885]

f=list(filter(divisible5,a))   
print(f)