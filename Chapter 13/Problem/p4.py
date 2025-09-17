from functools import reduce
a=[1,2,5,65,77,85,4455,6565,777,885]

def greater(a,b):
    if(a>b):
        return a
    return b

print(reduce(greater,a))